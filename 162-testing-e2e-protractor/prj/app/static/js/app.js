// -*- mode: js; coding: utf-8 -*-

var app = angular.module("app", [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller("ctrl", function($scope, $http) {

    $http.get('/list/')
	.success(function(items) {
	    console.info(items);
	    $scope.items = items;
	})
	.error(function() {
	    $scope.error = "Could not load TODO list";
	});
});
