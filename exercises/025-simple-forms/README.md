
Description
===========

When the user sents the form's data, store it somewhere, and redirect
the user to its profile. In the profile view, render it using the
previous stored data.

Notes
=====

I've used django.shortcuts.redirect, and stored the username as a
global variable inside the views module. When the profile view is
loaded, it renders the previous example template (profile), but
instead of using the data from GET arguments, it take it from the
stored variable.
