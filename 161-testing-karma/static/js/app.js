// -*- mode: makefile; coding: utf-8 -*-

var app = angular.module("LogApp", []);

app.controller("LogCtrl", function($scope) {
    $scope.events = [];

    $scope.record_event = function(message) {
	$scope.events.push({
	    text: message,
	    number: $scope.events.length + 1,
	});
    };
});
