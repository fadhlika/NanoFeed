from setuptools import setup

setup (
    name='NanoFeed',
    packages=['NanoFeed'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'feedparser',
        'html2text',
        'lxml',
        'rq',
    ],
)