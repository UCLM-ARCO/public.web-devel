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

    function refresh() {
	$http.get('data/flights.json')
	    .success(function(flights) {
		$rootScope.error = null;
		$scope.flights = flights;
	    })
	    .error(function() {
		$rootScope.error = "Could not load Flights information";
	    });
    };

    $scope.data_hash = null;
    function check_changes() {
	$http.get('data/hash')
	    .success(function(hash) {
		if ($scope.data_hash == hash)
		    return;

		$scope.data_hash = hash;
		refresh();
	    })
	    .error(function() {
		$rootScope.error = "Could not load Flights information";
	    });
    };

    check_changes();
    var timer = $interval(check_changes, 500);

    $scope.$on("$destroy", function() {
	$interval.cancel(timer);
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
	    });

	init_values();
    };

    init_values();
});
