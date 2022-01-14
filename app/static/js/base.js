(function () {
    url = window.location.pathname
    if (url == '/' || url == '/recent/'){
        $('#recent').addClass('linking')
    }
    if (url== '/my/gifts/'){
        $('#gifts').addClass('linking')
    }
    if (url == '/my/wish/'){
        $('#wishes').addClass('linking')
    }
    if (url == '/pending/'){
        $('#pending').addClass('linking')
    }
})()