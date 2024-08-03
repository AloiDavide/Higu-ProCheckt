
init:
    image napalm_flip = Transform("sprites/hb/napalm_flip.png", xoffset=-30)

    layeredimage hnb:

        group body:
            attribute defa default:
                "sprites/hb/defa.png"
            attribute objection:
                "hanabi_objection"


        group flippable:
            attribute napalm_left default if_any "defa":
                "sprites/hb/napalm.png"

            attribute napalm_right:
                "napalm_flip"

        group shades:
            attribute shadesUp default:
                "sprites/hb/shades_up.png"
            attribute shadesDown:
                "sprites/hb/shades_down.png"

        group left_arm:
            attribute Lrest default if_any "defa":
                "sprites/hb/rest_sx.png"
            attribute cigar:
                "sprites/hb/cigar.png"

        group right_arm:
            attribute Rrest default if_any "defa":
                "sprites/hb/rest_dx.png"
            attribute fist:
                "sprites/hb/fist.png"
            attribute finger:
                "sprites/hb/finger1.png"
            attribute finger2:
                "sprites/hb/finger2.png"
            attribute taunt:
                "hb_taunt"

        group eyes:
            attribute smug default:
                "sprites/hb/eyes/smug.png"
            attribute smug2:
                "sprites/hb/eyes/smug2.png"
            attribute fury:
                "sprites/hb/eyes/fury.png"
            attribute ohno:
                "sprites/hb/eyes/ohno.png"
            attribute close:
                "sprites/hb/eyes/close.png"



        group mouth:
            attribute yep default:
                "sprites/hb/mouths/yep0.png"
            attribute yepper:
                "sprites/hb/mouths/yep0.png"
            attribute nope:
                "sprites/hb/mouths/nope0.png"
            attribute nopper:
                "sprites/hb/mouths/annoyed0.png"
            attribute sneer:
                "sprites/hb/mouths/sneer0.png"
            attribute grin:
                "sprites/hb/mouths/grin0.png"
            attribute evilgrin:
                "sprites/hb/mouths/grin0.png"
            attribute devil:
                "sprites/hb/mouths/yep3.png"

            attribute yep_talk:
                "hb_yep_talk"
            attribute yepper_talk:
                "hb_yepper_talk"
            attribute nope_talk:
                "hb_nope_talk"
            attribute nopper_talk:
                "hb_nopper_talk"
            attribute sneer_talk:
                "hb_sneer_talk"
            attribute grin_talk:
                "hb_yepper_talk"
            attribute evilgrin_talk:
                "hb_sneer_talk"
            attribute devil_talk:
                "hb_devil_talk"


    image hb_yep_talk:
        "sprites/hb/mouths/yep1.png"
        .2
        "sprites/hb/mouths/yep2.png"
        .2
        repeat

    image hb_yepper_talk:
        "sprites/hb/mouths/yep2.png"
        .2
        "sprites/hb/mouths/yep4.png"
        .2
        repeat

    image hb_nope_talk:
        "sprites/hb/mouths/nope1.png"
        .2
        "sprites/hb/mouths/nope2.png"
        .2
        repeat

    image hb_nopper_talk:
        "sprites/hb/mouths/nope2.png"
        .2
        "sprites/hb/mouths/shout1.png"
        .2
        repeat

    image hb_sneer_talk:
        "sprites/hb/mouths/sneer1.png"
        .2
        "sprites/hb/mouths/sneer2.png"
        .2
        repeat

    image hb_devil_talk:
        "sprites/hb/mouths/sneer1.png"
        .2
        "sprites/hb/mouths/sneer2.png"
        .2
        repeat





    image hb_taunt:
        "sprites/hb/finger2.png"
        .3
        "sprites/hb/finger1.png"
        .3
        repeat 2
