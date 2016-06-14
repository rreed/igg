document.getElementById('amount').onblur = function() {
    if (this.value && typeof this.value === 'number') {
        updateROI(this.value);
    }
}

function updateROI(amount) {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
            document.getElementById('time-roi').innerHTML = req.responseText;
            document.getElementById('roi').style.display = 'block';
        }
    };
    req.open('GET', '/roi/' + amount, true);
    req.send();
}
