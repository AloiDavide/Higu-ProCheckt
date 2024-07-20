init:
    $ renpy.add_layer('overlayer', above='master')
    $ renpy.add_layer('underlayer', below='master')
    $ renpy.add_layer('notes_layer', above='overlayer')
    define masterFade = { "master" : Fade(2,0,2) }