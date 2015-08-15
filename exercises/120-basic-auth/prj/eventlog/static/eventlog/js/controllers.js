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

    var s = new WebSocket("ws://" + location.host + "/eventlog/ws");
    s.onmessage = function(event) {
	var flight = JSON.parse(event.data);
	$scope.flights.push(flight);
	$scope.$apply();
    };

    $scope.logout = function() {
	console.log("logout---");
	$http.get('/accounts/logout/?next=/');
    };

    $scope.$on("$destroy", function() {
	$http.get('/accounts/logout/?next=/');
    });

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
