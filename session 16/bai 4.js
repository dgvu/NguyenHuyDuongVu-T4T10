var a = document.getElementById('song_container')
var f = document.getElementsByClassName('song')
var g = document.getElementsByClassName('title')
var h = document.getElementsByClassName('artist')

console.log(a)
var b = a.children
for (i = 0; i < b.length; i++) {
    var c = b[i];
    if (c = f[i]) {
        console.log(c)
        var k = c.children;
        if (k = g[i]) {
            console.log(k.innerHTML)
        }
        if (k = h[i]) {
            console.log(k.innerHTML)
        }
    }
}

var del = document.getElementsByClassName('delete');
for (i = 0; i < del.length; i++) {
    var btn_del = del[i];
    btn_del.addEventListener('click', function (e) {
        var d = e.target;
        var div = d.parentNode;
        div.remove()
    })
}
var edi = document.getElementsByClassName('edit');
for (i = 0; i < edi.length; i++) {
    var btn_edi = edi[i];
    btn_edi.addEventListener('click', function (e) {
        var ad = e.target;
        console.log("song_id : " + ad.parentElement.getAttribute('song_id'))
    })
}
var mor = document.getElementsByClassName('more');
for (i = 0; i < mor.length; i++) {
    var btn_mo = mor[i];
    btn_mo.addEventListener('click', function (e) {
        var ab = e.target;
        var sibling_ = ab.parentNode;
        var title = sibling_.getElementsByClassName('title')        
        var artist = sibling_.getElementsByClassName('artist')
        console.log("title : " + title[0].innerHTML)
        console.log("artist : " + artist[0].innerHTML)
        console.log("song_id : " + ab.parentElement.getAttribute('song_id'))
    })
}
function addLoader() {
    var div_ = document.createElement('div')
    div_.innerHTML =`<div class="song" song_id="12354">
                        <h4 class="title">Whatever it takes</h4>
                        <h5 class="artist">Imagine Dragons</h5>
                        <button class="delete">Delete</button>
                        <button class="edit">Edit</button>
                        <button class="more">More</button>
                    </div>`
    document.getElementById("song_container").appendChild(div_)
}
