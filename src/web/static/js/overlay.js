//I wonder how many things have used this exact function from SO...
Number.prototype.formatMoney = function(c, d, t){
    var n = this,
    c = isNaN(c = Math.abs(c)) ? 2 : c,
    d = d == undefined ? "." : d,
    t = t == undefined ? "," : t,
    s = n < 0 ? "-" : "",
    i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

//bar things

var bar = {
    height: 35, // Height of bar (px)
    pause: 5000, // Linger time on a message
    slide: 4000, // Inter-message transition speed
    appear: 1000, // How quickly does it appear and disappear
    active: false,
    thanksCount: 0,
    thankDonors: function () {
	if (!bar.active && $(".slide").children().length > 0) {
	    bar.active = true;
	    $(".slide").css('left', 'auto');
	    $(".slide_container").slideDown(600, function () {
		$(".slide").delay(bar.pause).slide({
		    duration: bar.appear,
		    delay: bar.pause
		});
	    });
	}
    },

    addDonor: function (nick, amount) {
	if (amount != 0) {
	    $(".slide").append($("<li>").width(this.width).text("$" + Number(amount).toFixed(2) + " donated by " + nick + ", thanks!"));
	} else {
	    $(".slide").append($("<li>").width(this.width).text("Welcome to Indie Games for Good!"));
	}
    }
};


$.fn.slide = function (m) {
    $this = this;
    liwidth = $('>li', $this).width();

    if ($this.css('left') == "auto") {
        $this.css('left', 0);
    }

    bar.thanksCount = $this.children().length;
    if (-1 * parseFloat($this.css('left')) < ($this.children().length - 1) * liwidth) {

        $this.animate({'left': "+=" + (liwidth * -1)},
            m.duration,
            'swing',
            function () { $this.delay(m.delay).slide(m); }
        );
    } else {
        console.log("Done");

        $(".slide_container").delay(m.delay).slideUp(function () {
            $(".slide>li:lt(" + bar.thanksCount + ")").remove();
            bar.active = false;
            bar.thanksCount = 0;
            bar.thankDonors();
        });
    }
    return this;
};

function barprep() {
    bar.width = $(window).width();

    _this = $('.slide');
    _this.height(bar.height)
	.parent().css({
	'overflow': 'hidden',
	'height': bar.height
    }).find('>ul').css({
        width: screen.width * 20
    });

}



//info box things

function updateMarathonInfo() {
    $.getJSON('/ajax/marathoninfo', function(data){
        $('.info_total').html(data.total.formatMoney(2));
        $('.info_nexthourcost').html(Number(data.nexthourcost).formatMoney(2));
        $('.info_nexthour').html(data.hours+1);
        $('.info_hours').html(data.hours);
        $('.info_now_playing').html(data.currentgame);
        $('.info_nextgame').html(data.nextgame);

        setTimeout(function(){updateMarathonInfo(); console.log('updated overlay');}, 60000);
    });
}


function updateClocks() {
    var today=new Date();
    var h=today.getHours();
    if (h > 12){ ampm = "pm";  h -= 12;} else { ampm = "am"; if (h == 12) {ampm = "pm"; }}
    var m=today.getMinutes();
    var s=today.getSeconds();
    m = checkTime(m);
    $('#localtime').html(h+":"+m+ampm);

    $.get('/ajax/elapsed', function(data){
        $('#marathoncounter').html(data);

        setTimeout(function(){updateClocks(); console.log('updated clocks');}, 10000);
    });
}

function checkTime(i) {
    if (i<10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}


$(document).ready(function(){
    updateMarathonInfo();
    updateClocks();
    //startTime();

    bar.width = $(window).width();
    _this = $('.slide');
    _this.height(bar.height)
        .parent().css({
            'overflow': 'hidden',
            'height': bar.height
    }).find('>ul').css({
        width: screen.width * 20
    });

    var pubnub = PUBNUB.init({
    	publish_key   : 'pub-c-376a7bcd-1c5b-49b3-a05a-91d83f1ea2dc',
     	subscribe_key : 'sub-c-ffcf9c0e-4960-11e4-b332-02ee2ddab7fe',
    	ssl : (('https:' == document.location.protocol) ? true : false)
    });
    var pubnub_channel = 'igg';

    pubnub.subscribe({
     	channel: pubnub_channel,
     	message: function(m) {
	    console.log('Message received on ' + pubnub_channel, m);
	    if ('donation' in m) {
                window.bar.addDonor(m['donation']['name'], m['donation']['amount']);
	        window.bar.thankDonors();
	    }
        }
    });



    $('#testdonor').click(function() {
        console.log('tested addDonor');
        window.bar.addDonor('tester', 31.41);
        window.bar.thankDonors();
    })
    window.bar.addDonor('test', 0);
    window.bar.thankDonors();
})

