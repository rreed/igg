$(function() {
    $("div#accordion div.list-title").click(
        function(){
            var game = $(this).attr('data-id');
            var contentObject = $('#content_'+game);
            
            console.log(game)
            console.log($(this))
            if (!$(this).hasClass('ui-state-active'))
            {
                $(this).addClass('ui-state-active');
                contentObject.load('/games/'+game,function() {
                    contentObject.slideDown('fast');
                    //contentObject.attr('style', 'diplay:block');
                });
            }
            else
            {
                $(this).removeClass('ui-state-active');
                //contentObject.attr('style', 'diplay:none');
                contentObject.slideUp('fast');
            }
        }
    );
});

//tooltips
$(function() {
    console.log('ready')  
    $('.tooltip').tipsy({trigger: 'hover', gravity: 'n',opacity:0.95}); 
    $('#thresholdtooltip').tipsy({trigger: 'hover', gravity: 'n',opacity:0.95}); 
});

// buh?
//    $(function() {
//        if (window.location.hash) {
//            document.getElementById(window.location.hash.substring(1)).click();
//        }
//    });

