init:

    def head_tilt_func(img):
        return Transform(Crop((150, 80, 350, 350), img), rotate=-15, align=(0.5,0.5), offset=(-658, -258), transform_anchor=True, rotate_pad=False)

    transform head_tilt:
        crop (150, 80, 350, 350)
        transform_anchor True
        rotate_pad False
        rotate -13
        align (0.5,0.5)
        offset (-655, -250)


    #LARRY
    layeredimage larry:
        group pose:
            attribute defa default:
                "sprites/la/defa.png"
            attribute notes:
                "sprites/la/notes.png"


        group head:
            attribute head_defa default:
                "sprites/la/head.png"
            attribute tilt:
                at head_tilt
                "sprites/la/head.png"

        attribute shades default:
            if_all "tilt" at head_tilt
            "sprites/la/shades.png"

        attribute shades default:
            if_not "tilt"
            "sprites/la/shades.png"

        attribute drop:
            if_all "tilt" at head_tilt
            "sprites/la/drop.png"

        attribute drop:
            if_not "tilt"
            "sprites/la/drop.png"

        group eyes:
            if_all "tilt" at head_tilt
            attribute neutral default:
                "sprites/la/eyes/neutral.png"
            attribute scared:
                "sprites/la/eyes/scared.png"
            attribute close:
                "sprites/la/eyes/close.png"
            attribute cry:
                "sprites/la/eyes/cry.png"
            attribute focus:
                "sprites/la/eyes/focus.png"
            attribute evil:
                "sprites/la/eyes/evil.png"


        group eyes:
            if_not "tilt"
            attribute neutral default:
                "sprites/la/eyes/neutral.png"
            attribute scared:
                "sprites/la/eyes/scared.png"
            attribute close:
                "sprites/la/eyes/close.png"
            attribute cry:
                "sprites/la/eyes/cry.png"
            attribute focus:
                "sprites/la/eyes/focus.png"
            attribute evil:
                "sprites/la/eyes/evil.png"

        group mouth:
            if_all "tilt" at head_tilt
            attribute nope default:
                "sprites/la/mouths/nope0.png"
            attribute smile:
                "sprites/la/mouths/smile0.png"
            attribute yep:
                "sprites/la/mouths/yep0.png"
            attribute worried:
                "sprites/la/mouths/worried0.png"


            attribute nope_talk:
                "lar_nope_talk"
            attribute smile_talk:
                "lar_smile_talk"
            attribute worried_talk:
                "lar_nope_talk"
            attribute yep_talk:
                "lar_smile_talk"

        group mouth:
            if_not "tilt"
            attribute nope:
                "sprites/la/mouths/nope0.png"
            attribute smile:
                "sprites/la/mouths/smile0.png"
            attribute yep:
                "sprites/la/mouths/yep0.png"
            attribute worried:
                "sprites/la/mouths/worried0.png"


            attribute nope_talk:
                "lar_nope_talk"
            attribute smile_talk:
                "lar_smile_talk"
            attribute worried_talk:
                "lar_nope_talk"
            attribute yep_talk:
                "lar_smile_talk"



    image lar_nope_talk:
        "sprites/la/mouths/nope1.png"
        .2
        "sprites/la/mouths/nope2.1.png"
        .2
        repeat

    image lar_smile_talk:
        "sprites/la/mouths/smile1.png"
        .2
        "sprites/la/mouths/smile2.png"
        .2
        repeat