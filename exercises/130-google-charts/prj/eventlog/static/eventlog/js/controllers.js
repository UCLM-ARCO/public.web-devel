/* -*- mode: js; coding: utf-8 -*- */

EventLogApp.controller(
    "EventLogListCtrl",
    function($rootScope, $scope, $http, $interval, $location) {

    $scope.states = [
	{color: "green", text: "Successfull Flight"},
	{color: "orange", text: "Flight has Issues"},
	{color: "red", text: "Complete Failure"},
    ];

    $scope.get_color = function(state) {
	return $scope.states[state].color;
    };

    $http.get('data/flights.json')
	.success(function(flights) {
	    $rootScope.error = null;
	    $scope.flights = flights;
	})
	.error(function() {
	    $rootScope.error = "Could not load Flights information";
	});

    var s = new WebSocket("ws://" + location.host + "/eventlog/ws");
    s.onerror = function(error) {
	console.error(error);
    };
    s.onmessage = function(event) {
	var flight = JSON.parse(event.data);
	$scope.flights.push(flight);
	$scope.$apply();
    };
});

EventLogApp.controller("EventLogInsertCtrl", function($rootScope, $scope, $http) {

    var uavs = ["Condor I", "Brave", "Wulong"];

    function s4() {
	return Math.floor((1 + Math.random()) * 0x10000)
	    .toString(16).substring(1).toUpperCase();
    };

    function init_values() {
	$scope.uav_name = uavs[Math.floor(Math.random() * uavs.length)];
	$scope.flight_number = s4() + "-" + s4();
    };

    $scope.insert = function() {
	var params = {uav: $scope.uav_name, flight: $scope.flight_number}
	$http.post('/eventlog/insert/', params)
	    .success(function() {
		$scope.insert_ok = true;
	    })
	    .error(function() {
		$rootScope.error = "Could not add new Flight!";
		$scope.insert_ok = false;
	    });

	init_values();
    };

    init_values();
});

EventLogApp.controller("UavCtrl", function($rootScope, $scope, $http, $routeParams) {

    $http.get("uav/" + $routeParams.uavId)
	.success(function(profile) {
	    $scope.uav = profile;
	    compute_fields(profile);

	    google.setOnLoadCallback(draw_charts);
	})
	.error(function() {
	    $rootScope.error = "Could not load UAV Profile";
	});

    var traveled_distances = [];

    function compute_fields(uav) {
	$scope.uav_life = 5;
	$scope.uav_flight_hours = 0;
	$scope.uav_first_flight = "N/A";
	$scope.uav_last_flight = "N/A";
	$scope.uav_distance = 0;
	$scope.uav_flight_status = [0, 0, 0];

	if (!uav.flights)
	    return;

	for (i in uav.flights) {
	    var f = uav.flights[i];
	    $scope.uav_flight_status[f.status]++;

	    if (!f.points.length)
		continue;

	    var p_first = new Date(f.points[0] * 1000);
	    var p_last = new Date(f.points[f.points.length - 1] * 1000);
	    var delta = (p_last - p_first) / 1000 / 60 / 60;

	    $scope.uav_flight_hours += delta;

	    var kms = f.points.length * 0.8;
	    $scope.uav_distance += kms;

	    // remove the 'time' part from date
	    p_first = new Date(p_first.getFullYear(),
			       p_first.getMonth(),
			       p_first.getDate());
	    traveled_distances.push([p_first, kms]);
	}

	var f_first = uav.flights[0];
	var f_last = uav.flights[uav.flights.length - 1];

	if (f_first.points.length) {
	    var first_flight = new Date(f_first.points[0] * 1000);
	    $scope.uav_first_flight = first_flight.toDateString();

	    if (f_last.points.length) {
		var p_first = new Date(f_first.points[0] * 1000);
		var p_last = f_last.points[f_last.points.length -1];
		p_last = new Date(p_last * 1000);

		$scope.uav_life +=  Math.floor(
		    (p_last - p_first) / 1000 / 60 / 60 / 24);
	    }
	}

	if (f_last.points.length) {
	    var last_flight = new Date(f_last.points[0] * 1000);
	    $scope.uav_last_flight = last_flight.toDateString();
	}

	$scope.uav_flight_hours = $scope.uav_flight_hours.toFixed(2);
	$scope.uav_distance = $scope.uav_distance.toFixed(2);

	$scope.flights_ok = $scope.uav_flight_status[0] * 100 / uav.flights.length;
	$scope.flights_issue = $scope.uav_flight_status[1] * 100 / uav.flights.length;
	$scope.flights_fail = $scope.uav_flight_status[2] * 100 / uav.flights.length;

	$scope.fields = [
	    {label: 'Name:', value: uav.name},
	    {label: '# Flights:', value: uav.flights.length},
	    {label: 'Span of Life:', value: $scope.uav_life + " days"},
	    {label: 'Flight Hours:', value: $scope.uav_flight_hours + " h"},
	    {label: 'First Flight:', value: $scope.uav_first_flight},
	    {label: 'Last Flight:', value: $scope.uav_last_flight},
	    {label: 'Distance:', value: $scope.uav_distance + " Km"},
	];

	// try to load charts if google API is ready
	draw_charts();
    };

    function draw_charts() {
	draw_distance_chart();
	draw_usage_chart();
    };

    function draw_distance_chart() {
        var data = new google.visualization.DataTable();
	data.addColumn('date', 'Date of Flight');
	data.addColumn('number', 'Traveled Distance');

	data.addRows(traveled_distances);

	// create dashboard
	var dash_elem = document.getElementById('distance-dashboard');
	var dashboard = new google.visualization.Dashboard(dash_elem);

	// create range filter
	var filter = new google.visualization.ControlWrapper({
	    controlType: 'ChartRangeFilter',
	    containerId: 'distance-filter',
	    options: {
		filterColumnIndex: 0,
	    },
	});

	// create scatter chart
        var chart = new google.visualization.ChartWrapper({
	    chartType: 'ScatterChart',
	    containerId: 'distance-chart',
	    options: {
		colors: ['#3367D6'],
		legend: 'none',
	    },
	});

	dashboard.bind(filter, chart);
	dashboard.draw(data);
    };

    function draw_usage_chart() {
	var data = new google.visualization.DataTable();
	data.addColumn('date', 'Date of Flight');
	data.addColumn('number', 'Traveled Distance');

	data.addRows(traveled_distances);

        var options = {
	    colorAxis: {colors: ["#00914C", "#00914C"]},
	    calendar: {
		cellSize: 13,
	    },
	    legend: 'none',
	};

	var element = document.getElementById('chart-usage');
        var chart = new google.visualization.Calendar(element);
        chart.draw(data, options);
    };
});
