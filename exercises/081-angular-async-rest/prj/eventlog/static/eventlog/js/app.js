/* -*- mode: js; coding: utf-8 -*- */

EventLogApp = angular.module(
    "EventLogApp", ['ngResource'],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);
