/* -*- mode: js; coding: utf-8 -*- */

EventLogApp.controller("EventLogCtrl", function($scope, $http) {

    $scope.states = [
	{color: "green", text: "Successfull Flight"},
	{color: "orange", text: "Flight has Issues"},
	{color: "red", text: "Complete Failure"},
    ];

    $scope.get_color = function(state) {
	return $scope.states[state].color;
    };

    $scope.error = null;

    $http.get('data/flights.json')
	.success(function(flights) {
	    $scope.flights = flights;
	})
	.error(function() {
	    $scope.error = "Could not load Flights information";
	});
});
