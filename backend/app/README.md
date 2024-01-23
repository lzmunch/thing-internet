# THING INTERNET BACKEND

Internet for THINGS!!!!
Frontend [thing-internet](https://glitch.com/~thing-internet) hosts this in an iframe.

Inspired by [Obvious Plant's Goat Internet](https://obviousplant.com/products/a-3-5-inch-floppy-disk-that-unlocks-the-goat-internet?variant=41492628078785)

Currently supports the following things:
* fish
* goat
* worm
* toaster
* internet


## Development
This is a Python Flask webserver.

### Endpoints

| name               | type | args            | function                               |
| ------------------ | ---- | --------------- | -------------------------------------- |
| `/go`              | get  | input_url,thing | Displays processed webpage             |
| `/debug`           | get  | input_url,thing | Displays webpage w/o processing        |
| `/debug-no-header` | get  | input_url,thing | Displays webpage w/o processing & head |

Example:
`/go?thing=fish&input_url=https://www.coolmathgames.com`

### Architecture

On the back-end,

- app starts at `server.py`
- frameworks and packages in `requirements.txt`
- safely store app secrets in `.env`

## Misc


---

Remixed from ['hello-flask' by Gareth](https://glitch.com/~hello-flask)
