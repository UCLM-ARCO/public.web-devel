// -*- mode: js; coding: utf-8 -*-

MapApp.controller("MapCtrl", function($scope, $sce) {
    $scope.events = [];

    $scope.add_event = function(msg) {
	$scope.events.push({
	    text: $sce.trustAsHtml(msg),
	    number: $scope.events.length + 1,
	});
    };

    var click_times = 0;
    $scope.on_click_plane = function() {
	click_times++;

	$scope.add_event("You clicked <b>" + click_times +
			 "</b> times on a plane, somehow created in the future.");

    };
});
