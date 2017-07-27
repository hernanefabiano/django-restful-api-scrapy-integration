
$(document).on("click", "#id_search", function() {
    var search_keyword = $("#id_keyword").val();
    var search_page = window.search + '?q=' + search_keyword;
    $.ajax({
        type: 'GET',
        url: search_page, 
    }).done (function() {
        window.location=search_page; 
    });
})


