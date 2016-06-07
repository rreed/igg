window.setInterval(function() {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
            document.getElementById("timer").innerHTML = req.responseText;
        }
    };
    req.open('GET', '/ajax/elapsed', true);
    req.send();
}, 60000);
