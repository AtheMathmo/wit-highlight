# README

This is the [highlight](https://github.com/faethonm/highlight) [wit.ai](https://wit.ai) bot logic.

# SETUP

1. Clone this repo.
2. Install the requirements with `pip install -r requirements.txt`. It is a good idea to use a [virtualenv](https://virtualenv.pypa.io/en/stable/) for this step. *(Note: At time of writing pip doesn't have v4.0.0. Download and [install from source](https://github.com/wit-ai/pywit#install))*
3. Get the app token from wit ai, and run the program with `python highlight.py <wit-token>`

# TODO

- Keep the logic in `highlight.py` but move the executable code in a new `debug.py`.
- Integrate actual highlight API.
