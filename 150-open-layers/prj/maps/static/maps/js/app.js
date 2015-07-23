// -*- mode: js; coding: utf-8 -*-

function createMap() {
    var map = new ol.Map({
    	target: 'map',
    	layers: [
    	    new ol.layer.Tile({
    		source: new ol.source.TileJSON({
    		    url: "/maps/tile.json",
    		})
    	    })
    	],
    	view: new ol.View({
    	    center: [0, 0],
    	    zoom: 0
    	})
    });
};

setTimeout(createMap, 0);
