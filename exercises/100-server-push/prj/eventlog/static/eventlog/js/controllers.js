/* -*- mode: js; coding: utf-8 -*- */

EventLogApp.controller("EventLogListCtrl", function($rootScope, $scope, $http, $interval) {

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

    function on_insert(flight) {
	$scope.flights.push(flight);
    }

    function on_remove(flight) {
        for (var i = 0; i < $scope.flights.length; i++) {
	    var f = $scope.flights[i];
	    if (f.number != flight.number)
		continue;

	    $scope.flights.splice(i, 1);
	    break;
	}
    };

    var s = new WebSocket("ws://" + location.host + "/eventlog/ws");
    s.onmessage = function(event) {
	var message = JSON.parse(event.data);

	if (message.action == "insert")
	    on_insert(message.flight);
	else if (message.action == "remove")
	    on_remove(message.flight);

	$scope.$apply();
    };

    $scope.remove = function(flight) {
	$http.post('/eventlog/remove/', {flight: flight.number});
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
	    });

	init_values();
    };

    init_values();

});
