$(document).ready(function () {
    $(".btnChangePswd").click(function () {
        var kvmName = $(this).attr("value");
        $.ajax({
            method: "GET",
            url: "/activate/",
            data:{
                kvm_name: kvmName
            },
            success: function (json) {
                if(json.status == 'error') {
                    handleError(json.status);
                } else {
                    $(".modal-title").append(kvmName.toUpperCase());
                    pswd = $.parseHTML(json.password);
                    $(".pswd-fields").append(pswd);
                    $("#activateModal").modal('show');
                    var start = Date.now();
                    $.post(
                        "/timestamp/",
                        {
                            csrfmiddlewaretoken: getCookie('csrftoken'),
                            timestamp: start,
                            kvm_name: kvmName
                        }
                    )
                }
            },
            error: handleError
        })
    });
    $("#btnPsswdModal").click(function() {
        location.reload();
    });
    $("#modalActivateContainer").on("hidden.bs.modal", function () {
        location.reload();
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function handleError() {
        alert('RDP server not respond.');
    }
});
