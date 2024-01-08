#STYLES
style wide is text:
        size 35
        xpos 367
        ypos 60

        ymaximum 1000
        textalign 0.0
        xmaximum 1200
        outlines [(2, "#000", 1,1)]

style wideN is text:
        size 35
        xpos 367
        ypos 50

        ymaximum 1000
        textalign 0.0
        xmaximum 1200
        outlines [(2, "#000", 1,1)]

style border is text:
    size 45
    outlines [(2, "#000", 1, 1)]

style white_border is text:
    size 45
    outlines [(2, "#fff", 1, 1)]


define longDiss = Dissolve(4)
define longerDiss = Dissolve(8)
define longFade = Fade(4,0,2)
define longerFade = Fade(6,0,4)


#BACKGROUNDS
image notes = im.Scale("notes.png", 1920, 1080)
image notes closed = im.Scale("notes closed.png", 1920, 1080)
image clinic out = im.Scale("clinic out.png", 1920, 1080)
image clinic desk = im.Scale("clinic desk.png", 1920, 1080)
image clinic room = im.Scale("clinic room.png", 1920, 1080)
image clinic back = im.Scale("clinic back.png", 1920, 1080)
image streets = im.Scale("streets.png", 1920, 1080)
image koya = im.Scale("koya.png", 1920, 1080)
image basement = im.Scale("basement.png", 1920, 1080)
image torakku = im.Scale("torakku.png", 1920, 1080)
image small shrine = im.Scale("small shrine.png", 1920, 1080)
image hinamizawa = im.Scale("hinamizawa.png", 1920, 1080)
image fragment = im.Scale("fragment80.png", 1920, 1080)
image fragment9 = im.Scale("fragment90.png", 1920, 1080)
image satokhome = im.Scale("satokhome.png", 1920, 1080)
image satokhome flashback = im.Scale("satokhome flashback.png", 1920, 1080)
image satokhome sunset = im.Scale("satokhome sunset.png", 1920, 1080)
image crossroad rain = im.Scale("crossroad rain.png", 1920, 1080)
image shrine night = im.Scale("shrine night.png", 1920, 1080)
image red = im.Scale("red.png", 1920, 1080)
image woods1 = im.Scale("woods1.png", 1920, 1080)
image moon = im.Scale("moon.png", 1920, 1080)
image telephone = im.Scale("telephone.png", 1920, 1080)
image classroom = im.Scale("classroom.png", 1920, 1080)
image eyes = im.Scale("eyes.png", 1920, 1080)
image control room = im.Scale("control room.png", 1920, 1080)


#CHARACTERS
define n = Character(None, what_style= "wideN")
define ck = Character("Check", who_color = "#480000", what_style= "wide", who_style = "border")
define la = Character("Larry", who_color = "#fae69f", what_style= "wide", who_style = "border")
define ir = Character("Irie", who_color = "#977b6d", what_style= "wide", who_style = "border")
define tk = Character("Takano", who_color = "#c4b48f", what_style= "wide", who_style = "border")
define witch = Character("???", who_color = "#0000cf", what_style= "wide", who_style = "border")
define bk = Character("Bernkastel", who_color = "#0000cf", what_style= "wide", who_style = "border")
define ter = Character("Terry", who_color = "#0090ca", what_style= "wide", who_style = "border")
define tep = Character("Teppei", what_style = "wide", who_color= "#ffe674", who_style = "border")
define alt = Character("Voce alterata", what_style = "wide", who_color= "#000", who_style = "white_border", what_size = 45, what_font = "static/VT323-Regular.ttf")
define ltk = Character("Lambdadelta", what_style = "wide", who_color= "#000", who_style = "white_border", what_size = 45, what_font = "static/VT323-Regular.ttf")
define true_n = Character(None, what_style = "wide", what_font = "static/Caveat-VariableFont_wght.ttf", what_size = 45)


#SPRITES
#check
image check1 neutral unhappy = im.Scale("sprites/check1 neutral dissatisfied.png", 681, 1080)
image check1 neutral smile = im.Scale("sprites/check1 neutral smile.png", 681, 1080)
image check1 neutral straight = im.Scale("sprites/check1 neutral straight.png", 681, 1080)
image check1 neutral talk = im.Scale("sprites/check1 neutral talk.png", 681, 1080)
image check1 neutral worried = im.Scale("sprites/check1 neutral worried.png", 681, 1080)

image check1 angry unhappy = im.Scale("sprites/check1 angry dissatisfied.png", 681, 1080)
image check1 angry shout = im.Scale("sprites/check1 angry shout.png", 681, 1080)
image check1 angry smile = im.Scale("sprites/check1 angry smile.png", 681, 1080)
image check1 angry straight = im.Scale("sprites/check1 angry straight.png", 681, 1080)
image check1 angry talk = im.Scale("sprites/check1 angry talk.png", 681, 1080)
image check1 angry worried = im.Scale("sprites/check1 angry worried.png", 681, 1080)

image check1 closed straight = im.Scale("sprites/check1 closed straight.png", 681, 1080)
image check1 closed worried = im.Scale("sprites/check1 closed worried.png", 681, 1080)
image check1 closed talk = im.Scale("sprites/check1 closed talk.png", 681, 1080)
image check1 closed smile = im.Scale("sprites/check1 closed smile.png", 681, 1080)
image check1 closed shout = im.Scale("sprites/check1 closed shout.png", 681, 1080)
image check1 closed unhappy = im.Scale("sprites/check1 closed unhappy.png", 681, 1080)

image check2 neutral worried  = im.Scale("sprites/check2 neutral worried.png", 681, 1080)
image check2 angry unhappy  = im.Scale("sprites/check2 angry dissatisfied.png", 681, 1080)

image check talk1:
    im.Scale("sprites/check1 neutral straight.png", 681, 1080)
    pause 0.2
    im.Scale("sprites/check1 neutral talk.png", 681, 1080)
    pause 0.2
    repeat


#larry
image lar1 evil unhappy    = im.Scale("sprites/lar1 evil dissatisfied.png", 681, 1080)
image lar1 evil pleased    = im.Scale("sprites/lar1 evil pleased.png", 681, 1080)
image lar1 evil shout    = im.Scale("sprites/lar1 evil shout.png", 681, 1080)
image lar1 evil smile    = im.Scale("sprites/lar1 evil smile.png", 681, 1080)
image lar1 evil straight    = im.Scale("sprites/lar1 evil straight.png", 681, 1080)
image lar1 evil talk    = im.Scale("sprites/lar1 evil talk.png", 681, 1080)
image lar1 evil worried    = im.Scale("sprites/lar1 evil worried.png", 681, 1080)

image lar1 closed talk    = im.Scale("sprites/lar1 closed talk.png", 681, 1080)
image lar1 closed straight    = im.Scale("sprites/lar1 closed straight.png", 681, 1080)
image lar1 closed shout    = im.Scale("sprites/lar1 closed shout.png", 681, 1080)
image lar1 closed pleased    = im.Scale("sprites/lar1 closed pleased.png", 681, 1080)
image lar1 closed smile    = im.Scale("sprites/lar1 closed smile.png", 681, 1080)
image lar1 closed unhappy    = im.Scale("sprites/lar1 closed unhappy.png", 681, 1080)
image lar1 closed worried    = im.Scale("sprites/lar1 closed worried.png", 681, 1080)

image lar1 cry pleased    = im.Scale("sprites/lar1 cry pleased.png", 681, 1080)
image lar1 cry smile    = im.Scale("sprites/lar1 cry smile.png", 681, 1080)
image lar1 cry worried    = im.Scale("sprites/lar1 cry worried.png", 681, 1080)
image lar1 cry shout    = im.Scale("sprites/lar1 cry shout.png", 681, 1080)
image lar1 cry talk    = im.Scale("sprites/lar1 cry talk.png", 681, 1080)
image lar1 cry straight    = im.Scale("sprites/lar1 cry straight.png", 681, 1080)
image lar1 cry unhappy    = im.Scale("sprites/lar1 cry dissatisfied.png", 681, 1080)

image lar1 neutral unhappy    = im.Scale("sprites/lar1 neutral dissatisfied.png", 681, 1080)
image lar1 neutral pleased    = im.Scale("sprites/lar1 neutral pleased.png", 681, 1080)
image lar1 neutral shout    = im.Scale("sprites/lar1 neutral shout.png", 681, 1080)
image lar1 neutral smile    = im.Scale("sprites/lar1 neutral smile.png", 681, 1080)
image lar1 neutral straight    = im.Scale("sprites/lar1 neutral straight.png", 681, 1080)
image lar1 neutral talk    = im.Scale("sprites/lar1 neutral talk.png", 681, 1080)
image lar1 neutral worried    = im.Scale("sprites/lar1 neutral worried.png", 681, 1080)

image lar1 scared unhappy    = im.Scale("sprites/lar1 scared dissatisfied.png", 681, 1080)
image lar1 scared straight    = im.Scale("sprites/lar1 scared straight.png", 681, 1080)
image lar1 scared shout    = im.Scale("sprites/lar1 scared shout.png", 681, 1080)
image lar1 scared talk    = im.Scale("sprites/lar1 scared talk.png", 681, 1080)
image lar1 scared worried    = im.Scale("sprites/lar1 scared worried.png", 681, 1080)
#missing smile and pleased

image lar1 focus talk    = im.Scale("sprites/lar1 focus talk.png", 681, 1080)
image lar1 focus worried    = im.Scale("sprites/lar1 focus worried.png", 681, 1080)
image lar1 focus straight    = im.Scale("sprites/lar1 focus straight.png", 681, 1080)
image lar1 focus smile    = im.Scale("sprites/lar1 focus smile.png", 681, 1080)
image lar1 focus shout    = im.Scale("sprites/lar1 focus shout.png", 681, 1080)
image lar1 focus pleased    = im.Scale("sprites/lar1 focus pleased.png", 681, 1080)
image lar1 focus unhappy    = im.Scale("sprites/lar1 focus unhappy.png", 681, 1080)

image lar2 focus smile    = im.Scale("sprites/lar2 focus smile.png", 681, 1080)
image lar2 focus pleased    = im.Scale("sprites/lar2 focus pleased.png", 681, 1080)
image lar2 neutral talk    = im.Scale("sprites/lar2 neutral talk.png", 681, 1080)



#irie
image irie def0 = im.Scale("sprites/iri2_def1_0.png", 1920, 1080)
image irie def2 = im.Scale("sprites/iri2_def1_2.png", 1920, 1080)
image irie serious0 = im.Scale("sprites/iri2_majime_0.png", 1920, 1080)
image irie serious2 = im.Scale("sprites/iri2_majime_2.png", 1920, 1080)
image irie tilt0 = im.Scale("sprites/iri2_majime2_0.png", 1920, 1080)
image irie tilt2 = im.Scale("sprites/iri2_majime2_2.png", 1920, 1080)
image irie smile0 = im.Scale("sprites/iri2_warai_0.png", 1920, 1080)
image irie smile2 = im.Scale("sprites/iri2_warai_2.png", 1920, 1080)

image irie talk:
    im.Scale("sprites/iri2_def1_0.png", 1920, 1080)
    pause 0.2
    im.Scale("sprites/iri2_def1_2.png", 1920, 1080)
    pause 0.2
    repeat

#takano
image takano def0 = im.Scale("sprites/ta2_def_0.png", 1920, 1080)
image takano def2 = im.Scale("sprites/ta2_def_2.png", 1920, 1080)
image takano smirk0 = im.Scale("sprites/ta2_akuwarai_0.png", 1920, 1080)
image takano smirk2 = im.Scale("sprites/ta2_akuwarai_2.png", 1920, 1080)
image takano smile0 = im.Scale("sprites/ta2_warai_0.png", 1920, 1080)
image takano smile2 = im.Scale("sprites/ta2_warai_2.png", 1920, 1080)