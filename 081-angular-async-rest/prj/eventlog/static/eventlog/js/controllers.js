/* -*- mode: js; coding: utf-8 -*- */

EventLogApp.controller("EventLogCtrl", function($scope, $resource) {

    $scope.states = [
	{color: "green", text: "Successfull Flight"},
	{color: "orange", text: "Flight has Issues"},
	{color: "red", text: "Complete Failure"},
    ];

    $scope.get_color = function(state) {
	return $scope.states[state].color;
    };

    $scope.error = null;

    var flight_rs = $resource('/eventlog/api/flight/')
    $scope.flights = flight_rs.query();
});
