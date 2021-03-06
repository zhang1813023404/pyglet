"""Test that rendering of bullet glyphs works.

You should see 5 bullet glyphs rendered in the bottom-left of the window.
"""


import unittest

from pyglet import font

from . import base_text


class TEST_HALIGN(base_text.TextTestBase):
    font_name = ''
    font_size = 60
    text = '\u2022' * 5
