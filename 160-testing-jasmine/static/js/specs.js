// -*- mode: makefile; coding: utf-8 -*-

describe("Event Logger", function() {

    // Inject application
    beforeEach(module('LogApp'));

    // Inject controller and get its scope
    var $scope = {};
    beforeEach(inject(function($controller) {
	$controller("LogCtrl", { $scope: $scope });
    }));

    describe("events", function() {

	it("should have no records on init", function() {
	    expect($scope.events.length).toEqual(0);
	});

	it("should have one event when 'record_event' is called", function() {
	    $scope.record_event("This is the event message");
	    expect($scope.events.length).toEqual(1);
	});

	it("recorded events should have the correct fields", function() {
	    var message = "This is the event message";
	    $scope.record_event(message);
	    expect($scope.events[0].text).toEqual(message);
	    expect($scope.events[0].number).toEqual(1);
	});
    });
});
