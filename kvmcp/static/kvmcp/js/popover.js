$(document).ready(function () {
    $('a[data-toggle=popover]').popover({
        trigger: 'hover',
        placement: 'bottom',
        content: function () {
            end = $(this).attr('content');
            var t = timer(end);
            if (end <= Date.now()) {
                clearInterval(si);
                return 'Свободен.';
            }
            if ($(this).hasClass('.'))
            var si = setInterval(timer(end), 1000);
            return t.hours + ':' + t.minutes + ':' + t.seconds;
        }
    });

    function timer(end) {
        var endAccess = end;
        var diff = endAccess - Date.now();
        diff /= 1e3;
        timeLeft = {
            hours: diff / 3600 % 24 |0,
            minutes: diff / 60 % 60 |0,
            seconds: diff / 1 % 60 |0
        };
        return timeLeft;
    }
});