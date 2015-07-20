/* -*- mode: js; coding: utf-8 -*- */

EventLogApp = angular.module(
    "EventLogApp", ['ngRoute'],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);

EventLogApp.config(function($routeProvider, $httpProvider) {
    var partials = "/static/eventlog/partials/";

    // Needed for Django CSRF system
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // If AJAX requests need to be checked in the backend
    // $httpProvider.defaults.headers
    //        .common['X-Requested-With'] = 'XMLHttpRequest';

    $routeProvider
	.when('/',       {redirectTo: '/list'})
	.when('/list',   {templateUrl: partials + 'list.html'})
	.when('/insert', {templateUrl: partials + 'insert.html'})
    ;
});
