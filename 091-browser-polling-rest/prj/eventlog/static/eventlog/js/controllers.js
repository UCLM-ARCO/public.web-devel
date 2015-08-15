/* -*- mode: js; coding: utf-8 -*- */

EventLogApp.controller("EventLogListCtrl", function($rootScope, $scope, $http, $interval, $resource) {

    $scope.states = [
	{color: "green", text: "Successfull Flight"},
	{color: "orange", text: "Flight has Issues"},
	{color: "red", text: "Complete Failure"},
    ];

    $scope.get_color = function(state) {
	return $scope.states[state].color;
    };

    function refresh() {
	var flight_rs = $resource('/eventlog/api/flight/')
	var flights = flight_rs.query(
	    function() {
		$rootScope.error = null;
		$scope.flights = flights;
	    },
	    function() {
		$rootScope.error = "Could not load Flights information";
	    });
    };

    refresh();
    var timer = $interval(refresh, 1000);

    $scope.$on("$destroy", function() {
	$interval.cancel(timer);
    });
});

EventLogApp.controller("EventLogInsertCtrl", function($rootScope, $scope, $http, $resource) {

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
	var flight_rs = $resource('/eventlog/api/flight/');
	var new_flight = new flight_rs(params);
	new_flight.$save();

	init_values();
    };

    init_values();

});
