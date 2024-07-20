init:
    layeredimage bern:
        group exp:
            attribute yoko:
                "sprites/bk/yoko.png"
            attribute chira default:
                 "sprites/bk/chira.png"
            attribute close:
                "sprites/bk/close.png"

        #talk worried unhappy smile shout
        group mouth:
            attribute a default:
                "sprites/bk/neutral0.png"
            attribute b:
                "sprites/bk/up0.png"
            attribute noflap:
                "sprites/bk/neutral0.png"
            attribute a_talk:
                "bk_neutral_talk"
            attribute b_talk:
                "bk_up_talk"
            attribute noflap_talk:
                "sprites/bk/neutral0.png"

    image bk_neutral_talk:
        "sprites/bk/neutral1.png"
        .2
        "sprites/bk/neutral2.png"
        .2
        repeat

    image bk_up_talk:
        "sprites/bk/up1.png"
        .2
        "sprites/bk/up2.png"
        .2
        repeat