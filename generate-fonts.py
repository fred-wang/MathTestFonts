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
from utils import *
import fontforge

################################################################################
f = create("MathTestFontFull")

# MathConstants
f.math.ScriptPercentScaleDown = 87
f.math.ScriptScriptPercentScaleDown = 76
f.math.DelimitedSubFormulaMinHeight = 100
f.math.DisplayOperatorMinHeight = 200
f.math.MathLeading = 300
f.math.AxisHeight = 400
f.math.AccentBaseHeight = 500
f.math.FlattenedAccentBaseHeight = 600
f.math.SubscriptShiftDown = 700
f.math.SubscriptTopMax = 800
f.math.SubscriptBaselineDropMin = 900
f.math.SuperscriptShiftUp = 1100
f.math.SuperscriptShiftUpCramped = 1200
f.math.SuperscriptBottomMin = 1300
f.math.SuperscriptBaselineDropMax = 1400
f.math.SubSuperscriptGapMin = 1500
f.math.SuperscriptBottomMaxWithSubscript = 1600
f.math.SpaceAfterScript = 1700
f.math.UpperLimitGapMin = 1800
f.math.UpperLimitBaselineRiseMin = 1900
f.math.LowerLimitGapMin = 2200
f.math.LowerLimitBaselineDropMin = 2300
f.math.StackTopShiftUp = 2400
f.math.StackTopDisplayStyleShiftUp = 2500
f.math.StackBottomShiftDown = 2600
f.math.StackBottomDisplayStyleShiftDown = 2700
f.math.StackGapMin = 2800
f.math.StackDisplayStyleGapMin = 2900
f.math.StretchStackTopShiftUp = 3000
f.math.StretchStackBottomShiftDown = 3100
f.math.StretchStackGapAboveMin = 3200
f.math.StretchStackGapBelowMin = 3300
f.math.FractionNumeratorShiftUp = 3400
f.math.FractionNumeratorDisplayStyleShiftUp = 3500
f.math.FractionDenominatorShiftDown = 3600
f.math.FractionDenominatorDisplayStyleShiftDown = 3700
f.math.FractionNumeratorGapMin = 3800
f.math.FractionNumeratorDisplayStyleGapMin = 3900
f.math.FractionRuleThickness = 4000
f.math.FractionDenominatorGapMin = 4100
f.math.FractionDenominatorDisplayStyleGapMin = 4200
f.math.SkewedFractionHorizontalGap = 4300
f.math.SkewedFractionVerticalGap = 4400
f.math.OverbarVerticalGap = 4500
f.math.OverbarRuleThickness = 4600
f.math.OverbarExtraAscender = 4700
f.math.UnderbarVerticalGap = 4800
f.math.UnderbarRuleThickness = 4900
f.math.UnderbarExtraDescender = 5000
f.math.RadicalVerticalGap = 5100
f.math.RadicalDisplayStyleVerticalGap = 5200
f.math.RadicalRuleThickness = 5300
f.math.RadicalExtraAscender = 5400
f.math.RadicalKernBeforeDegree = 5500
f.math.RadicalKernAfterDegree = 5600
f.math.RadicalDegreeBottomRaisePercent = 65

# MathGlyphInfo
def italicCorrection(aCodePoint):
    return 111 + (aCodePoint * em) % 349

def topAccentAttachment(aCodePoint):
    return 222 + (aCodePoint * em) % 257

def isExtendedShape(aCodePoint):
    return aCodePoint % 3 == 0

def mathKern(aCodePoint):
    height = 10
    kern = 5
    count = aCodePoint % 11
    t = []
    if count > 0:
        for i in range(0, count):
            height += 5 + aCodePoint % 17
            kern += 7 + aCodePoint % 23
            t.append((height, kern))
    return tuple(t)

for codePoint in range(ord("A"), ord("Z")+1):
    # Create a square glyph
    g = f.createChar(codePoint)
    drawRectangle(g, em, em)

    g.italicCorrection = italicCorrection(codePoint)
    g.topaccent = topAccentAttachment(codePoint)
    g.isExtendedShape = isExtendedShape(codePoint)

    if codePoint % 2 > 0:
      g.mathKern.bottomLeft = mathKern(codePoint)
    if codePoint % 3 > 0:
        g.mathKern.bottomRight = mathKern(codePoint + 13)
    if codePoint % 4 > 0:
        g.mathKern.topLeft = mathKern(codePoint + 73)
    if codePoint % 5 > 0:
        g.mathKern.topRight = mathKern(codePoint + 113)

# MathVariants
f.math.MinConnectorOverlap = 54

horizontalAndVerticalArrows = [
    0x2190, # &LeftArrow;
    0x2191, # &UpArrow;
    0x2192, # &RightArrow;
    0x2193, # &DownArrow;
    0x2194, # &LeftRightArrow;
    0x2195, # &UpDownArrow;
    0x21A4, # &LeftTeeArrow;
    0x21A5, # &UpTeeArrow;
    0x21A6, # &RightTeeArrow;
    0x21A7, # &DownTeeArrow;
    0x21C7, # leftwards paired arrows
    0x21C8, # upwards paired arrows
    0x21C9, # rightwards paired arrows
    0x21CA, # downwards paired arrows
    0x21D0, # &DoubleLeftArrow;
    0x21D1, # &DoubleUpArrow;
    0x21D2, # &DoubleRightArrow;
    0x21D3, # &DoubleDownArrow;
    0x21D4, # &DoubleLeftRightArrow;
    0x21D5, # &DoubleUpDownArrow;
    0x21E6, # leftwards white arrow
    0x21E7, # upwards white arrow
    0x21E8, # rightwards white arrow
    0x21E9 # downwards white arrow
]

for i in range(0, len(horizontalAndVerticalArrows)):
    isHorizontal = (i % 2 == 0)
    codePoint = horizontalAndVerticalArrows[i]

    # Create the base glyph.
    g = f.createChar(codePoint)
    g.italicCorrection = italicCorrection(codePoint)
    drawRectangle(g, em, em)

    # Create size variants.
    count = codePoint % 7
    variants = ""
    length = em + em * (codePoint % 19) / 10

    for j in range(2, 2 + count):
        name = "uni%04X_size%d" % (codePoint, j)
        g = f.createChar(-1, name)
        g.italicCorrection = italicCorrection(codePoint + j)
        length += (1 + j % 3) * em / 4
        size = em / (2 + j % 5)
        if isHorizontal:
            drawRectangle(g, length, size)
        else:
            drawRectangle(g, size, length)
        variants = "%s %s" % (variants, name)

    if isHorizontal:
        f[codePoint].horizontalVariants = variants
    else:
        f[codePoint].verticalVariants = variants

    # Create glyph assembly.
    if codePoint % 5:
        None # TODO

save(f)
################################################################################
