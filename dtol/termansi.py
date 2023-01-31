# coding: utf-8

# Copyright (c) 2008-2011 Volvox Development Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>

"""ANSII Color formatting for output in terminal."""

import os


__ALL__ = ['colored', 'cprint']

VERSION = (1, 1, 0)

ATTRIBUTES = {
    'clear': 0,
    'reset': 0,
    'normal': 0,
    'bold': 1,
    'dark': 2,
    'faint': 2,
    'dim': 2,
    'italic': 3,
    'underline': 4,
    'underscore': 4,
    'blink': 5,
    'reverse': 7,
    'concealed': 8
}

COLORS = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'default': 39,
    'bright_black': 90, 'lt_black': 90,
    'bright_red': 91, 'lt_red': 91,
    'bright_green': 92, 'lt_green': 92,
    'bright_yellow': 93, 'lt_yellow': 93,
    'bright_blue': 94, 'lt_blue': 94,
    'bright_magenta': 95, 'lt_magenta': 95,
    'bright_cyan': 96, 'lt_cyan': 96,
    'bright_white': 97, 'lt_white': 97
}

BACKGROUND_COLORS = {
    'bg_black': 40, 'on_black': 40,
    'bg_red': 41, 'on_red': 41,
    'bg_green': 42, 'on_green': 42,
    'bg_yellow': 43, 'on_yellow': 43,
    'bg_blue': 44, 'on_blue': 44,
    'bg_magenta': 45, 'on_magenta': 45,
    'bg_cyan': 46, 'on_cyan': 46,
    'bg_white': 47, 'on_white': 47,
    'bg_bright_grey': 100, 'on_bright_grey': 1000, 'bg_lt_grey': 100, 'on_lt_grey': 100, 'bg_light_grey': 100, 'on_light_grey': 100,
    'bg_bright_red': 101, 'on_bright_red': 101, 'bg_lt_red': 101, 'on_lt_red': 101, 'bg_light_red': 101, 'on_light_red': 101,
    'bg_bright_green': 102, 'on_bright_green': 102, 'bg_lt_green': 102, 'on_lt_green': 102, 'bg_light_green': 102, 'on_light_green': 102,
    'bg_bright_yellow': 103, 'on_bright_yellow': 103, 'bg_lt_yellow': 103, 'on_lt_yellow': 103, 'bg_light_yellow': 103, 'on_light_yellow': 103,
    'bg_bright_blue': 104, 'on_bright_blue': 104, 'bg_lt_blue': 104, 'on_lt_blue': 104, 'bg_light_blue': 104, 'on_light_blue': 104,
    'bg_bright_magenta': 105, 'on_bright_magenta': 105, 'bg_lt_magenta': 105, 'on_lt_magenta': 105, 'bg_light_magenta': 105, 'on_light_magenta': 105,
    'bg_bright_cyan': 106, 'on_bright_cyan': 106, 'bg_lt_cyan': 106, 'on_lt_cyan': 106, 'bg_light_cyan': 106, 'on_light_cyan': 106,
    'bg_bright_white': 107, 'on_bright_white': 107, 'bg_lt_white': 107, 'on_lt_white': 107, 'bg_light_white': 107, 'on_light_white': 107
}


RESET = '\033[0m'


def brighten(color=None):
    return 'bright_' + color if color is not None else None


def colored(text, color=None, on_color=None, attrs=None):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text background colors:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_black', ['blue', 'blink'])
        colored('Hello, World!', 'green')
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (BACKGROUND_COLORS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text


def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    """Print colorize text.

    It accepts arguments of print function.
    """

    print((colored(text, color, on_color, attrs)), **kwargs)
