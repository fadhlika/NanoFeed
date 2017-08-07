$(document).ready(function()
{
    var isMobile = window.matchMedia("only screen and (orientation: portrait)");

    $(".item").click(function(){
        var item_title = $(this).find("h4").text();
        $.ajax({
            url: '/item',
            type: 'GET',
            data: {title: item_title},
            success: function(response){
                $(".article").html(response);
            }
        });

        if(isMobile.matches) {
            $(".article-container").css("width", "95%");
        } else {
            $(".article-container").css("width", "75%");
        }
        $(".overlay").css("width", "100%");
        $("body").css("overflow-y", "hidden");
    });

    $(".overlay").click(function(){
        $(".article-container").css("width", "0px");
        $(".overlay").css("width", "0px");
        $("body").css("overflow-y", "auto");
    });

    $("#close-button").click(function(){
        $(".article-container").css("width", "0px");
        $(".overlay").css("width", "0px");
        $("body").css("overflow-y", "auto");
    });
});