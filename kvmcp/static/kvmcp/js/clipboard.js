$(document).ready(function () {
    $(".clipboard").click(function (event) {
        event.preventDefault();
        var valueNeighbor = $(this).siblings(".password").text();
        CopyToClipboard(valueNeighbor, true, "Пароль скопирован.")
    })
});

function CopyToClipboard(value, showNotification, notificationText) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(value).select();
    document.execCommand("copy");
    $temp.remove();

    if (typeof showNotification === 'undefined') {
        showNotification = true;
    }
    if (typeof notificationText === 'undefined') {
        notificationText = "Скопировать пароль.";
    }

    var notificationTag = $("div.copy-notification");
    if (showNotification && notificationTag.length == 0) {
        notificationTag = $("<div/>", {"class": "copy-notification", text: notificationText});
        $("body").append(notificationTag);

        notificationTag.fadeIn("slow", function () {
            setTimeout(function () {
                notificationTag.fadeOut("slow", function () {
                    notificationTag.remove();
                });
            }, 1000);
        });
    }
}