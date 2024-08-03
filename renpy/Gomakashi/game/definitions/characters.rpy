# CHARACTERS
define n = Character(None, what_style= "wideN")

define ck = Character("Check", who_color = "#780000", what_style= "wide", who_style = "border", image="check", callback=functools.partial(lipflap, name="check", mouths=["yep", "nope", "worried", "smile", "shout"]))
define la = Character("Larry", who_color = "#fad861", what_style= "wide", who_style = "border", image="larry", callback=functools.partial(lipflap, name="larry", mouths=["yep", "nope", "worried", "smile"]))
define witch = Character("???", who_color = "#3030df", what_style= "wide", who_style = "border", image="bern", callback=functools.partial(lipflap, name="bern", mouths=["a", "b"]))
define bk = Character("Bernkastel", who_color = "#3030df", what_style= "wide", who_style = "border", image="bern", callback=functools.partial(lipflap, name="bern", mouths=["a", "b", "noflap"]))
define hb = Character("Hanabi", who_color = "#cc4f33", what_style= "wide", who_style = "border", image="hnb", callback=functools.partial(lipflap, name="hnb", mouths=["yep", "yepper", "nope", "nopper", "sneer", "grin", "evilgrin", 'devil']))
define ld = Character("Lambdadelta", who_color = "#ffe674", what_style= "wide", who_style = "border", image="lamb", callback=functools.partial(lipflap, name="lamb", mouths=["yep","cat","mal","scary","smirk","pout","nag","mad", "b_yep"]))
define bent_ld = Character("lambdadelta", who_color = "#ffe674", what_style= "wide", who_style = "border")
define old1 = Character("Vecchio col bastone", who_color = "#999", what_style= "wide", who_style = "border")
define old2 = Character("Vecchio con la barba", who_color = "#999", what_style= "wide", who_style = "border")
define anon = Character("???", who_color = "#999", what_style= "wide", who_style = "border")
define ltk2 = Character("Comandante Lambdadelta", what_style = "wide", who_color= "#000", who_style = "white_border", what_size = 45, what_font = "static/VT323-Regular.ttf", callback=static_voice)


define cr = Character("??¿??¿?", who_color = "#00b83b", what_style= "wide", who_style = "border", image="check", callback=green_flare)
define hd = Character("?¿¿??", who_color = "#f37530", what_style= "wide", who_style = "border", image="check", callback=orange_flare)


#Codec characters
define lac = Character(None, what_style= "codec", window_background="gui/frame_null.png", image="larry", what_size = 45, what_font = "static/VT323-Regular.ttf", callback=functools.partial(lipflap, name="larry", mouths=["yep", "nope", "worried", "smile"]))
define ltk = Character(None, what_style = "codec", window_background="gui/frame_null.png", who_color= "#000", image="static", who_style = "white_border", what_size = 45, what_font = "static/VT323-Regular.ttf", callback=static_voice)



# Novel characters
define lan = Character("", kind=nvl, who_color = "#fad861", what_style= "notes_dialogue", who_style = "border")
