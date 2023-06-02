# ShortCutWindow ✂️🖼️

How many times have you had a website that you visit very often, such as a translator like Google Translator or DeepL? Or do you often visit ChatGPT to ask questions on the fly while you are working and studying? 🤔

Going to the browser each time and interrupting what you are doing could be frustrating, especially if you do it often. 🙄

That's why this software was born. Easily create a configuration file (instructions below) and create/place your favorite websites and access them with a shortcut very quickly and effectively!

# Installation

`For now it has been tested on windows, but it might work on linux as well (as soon as I have time to try it I will update it)`

To install it on windows, run these commands:

1. `git clone https://github.com/DanielusG/ShortCutWindow.git`
2. `cd ShortCutWindow`
3. `pip install -r requirements.txt`
4. Configure the `config.json` file (instructions below)
4. Finally, run `python main.py`

# Configuration

To configure it first copy the example configuration:
* `cp config.json.example config.json`

Then open the `config.json` file and edit it to your liking.

## Explanation of various parameters:

```
{
    "link": "Here you have to put the link of the website you want to open",
    "shortcut": [
        "Here you have to put the shortcut you want to use to open the website",
        "Each item in this "shortcut" list is a key to press, so enter all the",
        "keys you want to press to open this site",
        "For example:"
        "ctrl",
        "f1"
    ],
    "geometry": { // This is the position and size of the window
        "x": 0,
        "y": 0,
        "width": 800,
        "height": 600
    },
    "name": "Name of window" // This is the name of the window
}
```

For now, only the following keys have been associated with shortcuts and that you can use in the `shortcut` field of the `config.json` file:
* `ctrl`
* `alt`
* `shift`
* `f1`
* `f2`
* `f3`
* `f4`
* `q`