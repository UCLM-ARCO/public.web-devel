// -*- mode: js; coding: utf-8 -*-

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

    setInterval(insertData, 1000);
}

function insertData() {
    data.addRow([Math.floor(Math.random()*100),
		 Math.floor(Math.random()*100),
		'color: #DC3912']);
    chart.draw(data, options);
}

google.load("visualization", "1.1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
