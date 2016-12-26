function getRSSFeedData() {
    $.ajax({
        type: 'GET',
        url: '/RSSFeedData',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
        	console.log("Got RSS Feed data!");
            console.log(response);

        }
    });
}

getRSSFeedData();