// -*- mode: js; coding: utf-8 -*-

app.controller("ctrl", function($scope) {
    $scope.users = {
	'leo': {
	    name: "Leonardo",
	    surname: "da Vinci",
	    age: 33,
	    birthdate: new Date(1452, 4, 15),
	    occupation: 'Inventor',
	    color: "#959C71",
	},
    };
});
