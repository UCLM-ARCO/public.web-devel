// -*- mode: js; coding: utf-8 -*-

// simple directive (as a html tag)
//    like: <user-heading />

app.directive('welcome', function() {
    return {
	restrict: 'E',
	template: '<h1 class="text-center"><i class="fa fa-fw fa-pencil-square"></i> ' +
	    'Welcome to your blackboard!<h1><hr>',
    };
});

// more complex directive (as an attribute)
//    <div profile-for="leo"></div>

app.directive('profile', function() {

    function link(scope, element, attrs) {
	scope.user = scope.users[attrs.profile];
	$(element).css({
	    'color': 'white',
	    'background-color': scope.user.color,
	});
    };

    return {
	restrict: 'A',
	link: link
    };
});
