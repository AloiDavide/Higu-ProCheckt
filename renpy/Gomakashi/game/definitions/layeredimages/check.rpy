init:
    layeredimage check:
        group pose:
            attribute plain:
                "sprites/ck/def.png"
            attribute calling:
                "sprites/ck/calling.png"
            attribute sor default:
                "sprites/ck/sorcerer.png"
            attribute objection:
                "check_objection"
            attribute objection:
                "sprites/ck/objection_armless.png"

        group eyes:
            attribute neutral default:
                "sprites/ck/neutral.png"
            attribute angry:
                "sprites/ck/angry.png"
            attribute close:
                "sprites/ck/close.png"
            attribute sus:
                "sprites/ck/sus.png"
            attribute think:
                "sprites/ck/think.png"

        attribute shades if_any ["sor", "objection"] default:
            "sprites/ck/round_shades.png"



        group flippable:
            attribute p if_any ["sor", "objection"]:
                "sprites/ck/hat.png"

            attribute p if_any ["sor", "objection"]:
                "sprites/ck/distinctive.png"

            attribute fp if_any ["sor", "objection"]:
                "sprites/ck/f_hat.png"

            attribute fp if_any "sor":
                "sprites/ck/f_distinctive.png"

            attribute fp if_any "objection":
                "leftdist"

            attribute fp if_any ["plain"]:
                "sprites/ck/f_bkg.png"
            attribute fp if_any ["calling"]:
                "sprites/ck/f_bkg2.png"


        group mouth:
            attribute yep default:
                "sprites/ck/mouths/yep0.png"
            attribute nope:
                "sprites/ck/mouths/nope0.png"
            attribute smile:
                "sprites/ck/mouths/smile2.png"
            attribute worried:
                "sprites/ck/mouths/worried0.png"
            attribute shout:
                "sprites/ck/mouths/worried0.png"

            attribute yep_talk:
                "yep_talk"
            attribute nope_talk:
                "nope_talk"
            attribute smile_talk:
                "smile_talk"
            attribute worried_talk:
                "worried_talk"
            attribute shout_talk:
                "shout_talk"


    image yep_talk:
        "sprites/ck/mouths/yep1.png"
        .2
        "sprites/ck/mouths/yep2.png"
        .2
        repeat

    image nope_talk:
        "sprites/ck/mouths/nope1.png"
        .2
        "sprites/ck/mouths/nope2.png"
        .2
        repeat

    image worried_talk:
        "sprites/ck/mouths/nope1.png"
        .2
        "sprites/ck/mouths/nope2.png"
        .2
        repeat

    image smile_talk:
        "sprites/ck/mouths/yep1.png"
        .2
        "sprites/ck/mouths/yep2.png"
        .2
        repeat

    image shout_talk:
        "sprites/ck/mouths/shout1.png"
        .2
        "sprites/ck/mouths/shout2.png"
        .2
        repeat
