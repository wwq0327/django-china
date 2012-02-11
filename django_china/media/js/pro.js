jQuery('html').ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

jQuery(document).ready(function($) {
        $('#big_nav a').hover(function () {
                $(this).addClass('hover');
        }, function() {
                $(this).removeClass('hover');
        });
});

jQuery(document).ready(function($) {
    $("form.comment").submit(function() {
        var comment = $("#id_comment").val();
        if (!comment || comment.length < 4) {
            alert("回复不能为空或少于4字符！");
            return false;
        }
    });
});