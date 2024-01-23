# THING INTERNET :0
Internet for THINGS!!!!
Inspired by [Obvious Plant's Goat Internet](https://obviousplant.com/products/a-3-5-inch-floppy-disk-that-unlocks-the-goat-internet?variant=41492628078785)

_Last updated: Jan 09, 2024_

## Development
Basic, simple, static website which serves as a frontend of sorts. Backend is a Flask server that scrapes the user input website and processes the html.

This separation is mainly used to allow finer control over the CSS elements of the faux browser interface. A lot of the scraped websites will require external CSS and eventually some dynamically loaded content. For now it is easier to keep my custom interface separate so things like the headers and stylesheets don't collide.

To view on debug mode (include link to backend), use 

See [thing-internet-backend](https://glitch.com/~thing-internet-backend)
