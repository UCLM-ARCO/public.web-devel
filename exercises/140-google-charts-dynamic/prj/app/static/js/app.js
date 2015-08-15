// -*- mode: js; coding: utf-8 -*-

var data = null;
var chart = null;

function drawChart() {
    data = new google.visualization.DataTable();
    data.addColumn('number');
    data.addColumn('number');
    data.addColumn({type: 'string', role: 'style'});

    for (var i = 0; i < 100; i++)
        data.addRow([Math.floor(Math.random()*100),
                     Math.floor(Math.random()*100),
		    'color: #3366CC']);

    options = {
        legend: 'none',
        crosshair: { trigger: 'both' }
    };

    var element = document.getElementById('chart-container')
    chart = new google.visualization.ScatterChart(element);
    chart.draw(data, options);
}

s = new WebSocket("ws://" + location.host + "/ws");
s.onmessage = function(event) {
    if (data == null || chart == null)
	return;

    var message = JSON.parse(event.data);
    data.addRow([message.x, message.y, 'color: #DC3912']);
    chart.draw(data, options);
};

google.load("visualization", "1.1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
