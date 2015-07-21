/* -*- mode: js; coding: utf-8 -*- */

EventLogApp = angular.module(
    "EventLogApp", [],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);
