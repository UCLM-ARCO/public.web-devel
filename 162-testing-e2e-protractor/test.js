// -*- mode: js; coding: utf-8 -*-

describe('TODO list', function() {

    it('should add a todo', function() {
	browser.get("http://127.0.0.1:8000");

	var items = element.all(by.repeater("i in items"))
	expect(items.count()).toEqual(0);

	var text = "make more angular tests";
	element(by.css('[name="item"]')).sendKeys(text);
	element(by.css('button')).click();

	var items = element.all(by.repeater("i in items"))
	expect(items.count()).toEqual(1);
	expect(items.get(0).getText()).toEqual(text);
    });

});
