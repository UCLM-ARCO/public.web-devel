// -*- mode: js; coding: utf-8 -*-

app = angular.module(
    "app", [],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);

_ = function(args) { console.info(args); }

window.onload = function() {
    var canvas = $('#canvas').get(0);
    var context = canvas.getContext("2d");
    var paint = false;

    var x_clicks = [];
    var y_clicks = [];
    var drags = [];

    function addClick(x, y, dragging) {
	x_clicks.push(x);
	y_clicks.push(y);
	drags.push(dragging);
    }

    function redraw() {
	context.clearRect(0, 0, context.canvas.width, context.canvas.height);
	context.strokeStyle = "#ffffff";
	context.lineWidth = 2;

	for (var i in x_clicks) {
	    context.beginPath();

	    if (i && drags[i]) {
		context.moveTo(x_clicks[i-1], y_clicks[i-1]);
	    }
	    else {
		context.moveTo(x_clicks[i]-1, y_clicks[i]);
	    }

	    context.lineTo(x_clicks[i], y_clicks[i]);
	    context.closePath();
	    context.stroke();
	}
    }

    $('#canvas').mousedown(function(e) {
	paint = true;
	addClick(e.offsetX, e.offsetY);
	redraw();
    });

    $('#canvas').mousemove(function(e) {
	if (!paint)
	    return;

	addClick(e.offsetX, e.offsetY, true);
	redraw();
    });

    $('#canvas').mouseup(function(e) {
	paint = false;
    });

    window.onresize = function() {
	// 26: margin and padding
	canvas.width = $('#well').width() + 26;
    };

    window.clearCanvas = function() {
	x_clicks.length = [];
	y_clicks = [];
	drags = [];

	redraw();
    }

    // set initial canvas width
    onresize();
}
