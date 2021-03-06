from vanilla.dialogs import *

# copy-paste to fill this list with whatever glyphs fontMake flags as not being interpolatable
glyphsToDelete = ['divide', 'plusminus']

# help(CurrentFont().removeGlyph())

inputFonts = getFile("select masters for var font", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    f = OpenFont(fontPath, showUI=False)
    # # open the fonts, then:
    for glyphName in glyphsToDelete:
        print(glyphName)
        if glyphName in f.glyphOrder:
            f.removeGlyph(glyphName)
    f.save()
    f.close()

