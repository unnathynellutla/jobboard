$(function() {
    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

var group = $(".connectedSortable" ).sortable({
        connectWith: '.connectedSortable',
        delay: 500,
        update: function () {
            const arr = [];
            {% for stage in latest_stage_list %}
                var data = $(document.getElementById("{{ stage.stage_title }}")).sortable("serialize", {key:"id"});
                arr.push(data)
            {% endfor %}
            $.ajax({
                        type: "POST",
                        data: JSON.stringify(arr),
                        url: ""
                    });
        },
});
}).disableSelection();