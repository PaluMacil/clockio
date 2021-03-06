'use strict';

var clock = {
	DST: false,
	timezone: "EST",
	setTime: function() {
		var clockTime = document.querySelector("#clock .current-time");
		var today = new Date();
		var hours = function(){
			var militaryHours = today.getHours();
			if (militaryHours > 12) {
				militaryHours = militaryHours - 12;
				return ("00" + militaryHours).slice(-2);
			}
			else {
				return ("00" + militaryHours).slice(-2);
			}
		};
		var minutes = ("00" + today.getMinutes()).slice(-2);
		var AMPM = function(){
			if (today.getHours() >= 12) {
				return "PM";
			}
			else {
				return "AM";
			}
		};
		clockTime.innerHTML = hours() + ":" + minutes + " " + AMPM();
	},
	start: function() {
	    console.log('Setting setTime interval.');
		setInterval(clock.setTime, 150);
	},
	alarms: [],
	loadAlarms: function() {
		var alarm = { 1: "6:45 AM" };
		this.alarms.push(alarm);
	}

};

window.onload = function() {
	console.log('Starting clock.');
	clock.start();
	clock.loadAlarms();
	if (clock.alarms.length > 0) {
		//alert( JSON.stringify(clock.alarms) );
	}
};

/* console shim*/
(function () {
    var f = function () {};
    if (!window.console) {
        window.console = {
            log:f, info:f, warn:f, debug:f, error:f
        };
    }
}());