// -*- mode: js; coding: utf-8 -*-

PositionLogApp = angular.module(
    "PositionLogApp", [],
    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);
