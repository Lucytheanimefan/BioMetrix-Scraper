function getRSSFeedData() {
    $.ajax({
        type: 'GET',
        url: '/RSSFeedData',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Got RSS Feed data!");
            console.log(response);
            populateData(response.result);

        }
    });
}

getRSSFeedData();

function populateData(data) {
    for (var key in data) {
        $("#noti-box").html($("#noti-box").html() + "<h1>" + key + "</h1>");
        for (var i = 0; i < data[key].length; i++) {
            $("#noti-box").html($("#noti-box").html() +"<div class = 'RSSAlert'>"+data[key][i]["title"]+data[key][i]["content"]+"</div><hr>");
        }

    }
}
