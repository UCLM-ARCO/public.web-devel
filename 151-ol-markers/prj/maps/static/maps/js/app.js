// -*- mode: js; coding: utf-8 -*-

MapApp = angular.module(
    "MapApp", [],
    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);

function add_event(msg) {
    $scope = angular.element("#MapCtrlId").scope();
    $scope.add_event(msg);
    $scope.$apply();
}

function createMap() {
    var map = new ol.Map({
    	target: 'map',
	controls: ol.control.defaults().extend([
	    new ol.control.FullScreen(),
	    new ol.control.OverviewMap(),
	]),
    	layers: [
    	    new ol.layer.Tile({
    		source: new ol.source.TileJSON({
    		    url: "/maps/tile.json",
    		})
    	    }),
	    new ol.layer.Tile({
		source: new ol.source.TileDebug({
		    projection: 'EPSG:3857',
		    tileGrid: ol.tilegrid.createXYZ({maxZoom: 6})
		})
	    }),
    	],
    	view: new ol.View({
    	    center: [0, 0],
    	    zoom: 2
    	})
    });

    map.on('click', function(event) {
	var coord = ol.proj.transform(event.coordinate, 'EPSG:3857', 'EPSG:4326');

	if (-112 < coord[0] && coord[0] < -71 && -42 < coord[1] && coord[1] < -23)
	    add_event("You clicked in the <b>Middle Earth</b>");

	else if (Math.abs(coord[0] - 64.42) < 0.3 && Math.abs(coord[1] - -10.55) < 0.5)
	    add_event("If I were you, I'll <b>not maraud</b> around there...");

	else
	    add_event("You clicked on " + coord[0] + ", " + coord[1])
    });

    var plane = new ol.Overlay({
	position: ol.proj.fromLonLat([-106.3725, 20.208889]),
	positioning: 'center-center',
	element: document.getElementById('plane'),
	stopEvent: false
    });

    map.addOverlay(plane);
};

setTimeout(createMap, 0);
