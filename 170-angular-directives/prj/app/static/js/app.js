// -*- mode: js; coding: utf-8 -*-

app = angular.module(
    "app", [],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);
