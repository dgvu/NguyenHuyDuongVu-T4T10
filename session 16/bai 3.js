var del = document.getElementsByClassName('delete');
for (i = 0; i < del.length; i++) {
    var btn = del[i];
    btn.addEventListener('click', function(e) {
        var a = e.target;
        var div = a.parentNode;
        div.remove()
    })
}