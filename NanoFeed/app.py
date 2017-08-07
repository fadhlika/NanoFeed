from flask import Flask, render_template, request, redirect, url_for
from lxml import html
import feedparser
import html2text
from NanoFeed.models import *

app = Flask(__name__)
app.config.from_object('NanoFeed.config.DevelopmentConfig')

db.init_app(app)

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True

@app.cli.command()
def initdb():
    db.create_all()
    print("Database initialized")

@app.cli.command()
def deletedb():
    channel = Channel.query.delete()
    item = Item.query.delete()
    print(channel, item, 'deleted')

@app.route('/')
def index():
    channels = Channel.query.all()
    items = Item.query.order_by(Item.date.desc()).all()
    return render_template('index.html', channels = channels, items = items)

@app.route('/add/source', methods=['GET','POST'])
def add_source():
    if request.method == 'POST':
        link = request.form['link']
        if link != '':
            d = feedparser.parse(link)
            s = Channel(d['channel']['title'], link)
            db.session.add(s)
            for e in d['items']:
                tree = html.fromstring(e['description'])
                img = tree.xpath('//img')
                try:
                    img = img[0]
                except IndexError:
                    pass
                thumbnail = ''
                try:
                    thumbnail = img.attrib['src']
                except AttributeError:
                    thumbnail = None
                i = Item(e['title'], e['published_parsed'], e['link'], thumbnail, h.handle(e['description']), e['description'], s)
                db.session.add(i)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        channels = Channel.query.all()
        return render_template('add_source.html', channels=channels, location=' ')

@app.route('/item')
def item():
    title = request.args.get('title')
    item = Item.query.filter_by(title=title).first()
    return render_template("item.html", item=item)

@app.route('/channel/<channel_name>')
def filter_channel(channel_name):
    channel = Channel.query.filter_by(name=channel_name).first()
    channels = Channel.query.all()
    items = Item.query.filter_by(channel=channel).all()
    return render_template("index.html", channels=channels, items=items, location=channel_name)

if __name__ == '__main__':
    app.run()