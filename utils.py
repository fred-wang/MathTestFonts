# Copyright (C) 2016 Igalia S.L.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import fontforge

em = 1000

def create(aName):
    print("Generating %s.otf..." % aName, end="")

    # Create a new font.
    font = fontforge.font()
    font.encoding = "UnicodeFull"
    font.fontname = aName
    font.familyname = aName
    font.fullname = aName

    # License the font under OFL.
    font.copyright = "Copyright (c) 2016 Igalia S.L."
    with open('OFL.txt', 'r') as OFLFile:
        lang = "English (US)"
        font.sfnt_names = (
            (lang, 'Copyright', OFLFile.read()),
            (lang, 'License URL', 'http://scripts.sil.org/OFL'),
            (lang, 'Family', aName),
            (lang, 'SubFamily', 'Regular'),
            (lang, 'Fullname', aName),
            (lang, 'PostScriptName', aName)
        )

    # Create a space character.
    g = font.createChar(ord(" "), "space")
    g.width = em
    return font

def drawRectangle(aGlyph, aWidth, aHeight):
    aGlyph.width = aWidth
    p = aGlyph.glyphPen()
    p.moveTo(0, 0)
    p.lineTo(0, aHeight)
    p.lineTo(aWidth, aHeight)
    p.lineTo(aWidth, 0)
    p.closePath();

def save(aFont):
    # Set ascent/descent metrics.
    # aFont.os2_winascent, aFont.os2_windescent should be the maximum of
    # ascent/descent for all glyphs. Does fontforge compute them automatically?
    aFont.ascent = aFont.hhea_ascent = aFont.os2_typoascent = em
    aFont.descent = aFont.hhea_descent = aFont.os2_typodescent = 0
    aFont.hhea_ascent_add = aFont.hhea_descent_add = 0
    aFont.os2_typoascent_add = aFont.os2_typodescent_add = 0
    aFont.os2_winascent_add = aFont.os2_windescent_add = 0
    aFont.os2_use_typo_metrics = True

    # Generate the font.
    if aFont.validate() == 0:
        print(" done.")
    else:
        print(" validation error!")
        exit(1)
    aFont.generate("%s.otf" % aFont.fontname)
