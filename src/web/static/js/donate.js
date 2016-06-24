document.getElementById('amount_total').onblur = function() {
    if (this.value && typeof this.value === 'number') {
        updateROI(this.value);
    }
}

document.getElementById('donation_name').onblur = function() {
    document.getElementById('donationPreview').innerHTML = getDonationPreviewText();
}
document.getElementById('amount_total').onblur = function() {
    document.getElementById('donationPreview').innerHTML = getDonationPreviewText();
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

function getDonationPreviewText() {
    var amount = Number(document.getElementById('amount_total').value);
    var name = document.getElementById('donation_name').value;

    if (!amount || isNaN(amount)) {
        amount = Number("0.00");
    }

    if (!name) {
        name = "Anonymous";
    }

    return "$" + amount.toFixed(2) + " donated by " + name;
}
