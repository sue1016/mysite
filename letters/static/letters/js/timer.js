
function timer() {
    window.setTimeout("timer()", 1000);
    var start = new Date("2018-06-09 22:00:00").getTime();
    var t = new Date().getTime() - start; 
    var h = ~~(t / 1000 / 60 / 60 % 24);
    if (h < 10) {
        h = "0" + h;
    }
    var m = ~~(t / 1000 / 60 % 60);
    if (m < 10) {
        m = "0" + m;
    }
    var s = ~~(t / 1000 % 60);
    if (s < 10) {
        s = "0" + s;
    }
    document.getElementById('d').innerHTML = ~~(t / 1000 / 60 / 60 / 24);
    document.getElementById('h').innerHTML = h;
    document.getElementById('m').innerHTML = m;
    document.getElementById('s').innerHTML = s;
}
timer();
setInterval(timer, 1000);
