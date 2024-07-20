init:
    layeredimage lamb:
        group pose:
            attribute normal default:
                "sprites/ld/normal.png"
            attribute bent:
                 "sprites/ld/bent.png"

        group head:
            attribute defa:
                "sprites/ld/defa.png"
            attribute fury:
                "sprites/ld/fury.png"
            attribute close:
                "sprites/ld/close.png"
            attribute evil:
                "sprites/ld/evil.png"
            attribute frown:
                "sprites/ld/frown.png"
            attribute lookaway:
                "sprites/ld/lookaway.png"
            attribute psycho:
                "sprites/ld/psycho.png"
            attribute smugclose:
                "sprites/ld/smugclose.png"
            attribute surprise:
                "sprites/ld/surprise.png"
            attribute tantrum:
                "sprites/ld/tantrum.png"
            attribute unhappy:
                "sprites/ld/unhappy.png"
            attribute worried:
                "sprites/ld/worried.png"
            attribute b_psycho if_all "bent":
                "sprites/ld/b_psycho.png"
            attribute b_defa if_all "bent":
                "sprites/ld/b_defa.png"

        group mouth:
            attribute yep default:
                "sprites/ld/mouths/yep0.png"
            attribute cat:
                "sprites/ld/mouths/cat0.png"
            attribute mal:
                "sprites/ld/mouths/malicious0.png"
            attribute scary:
                "sprites/ld/mouths/scary0.png"
            attribute smirk:
                "sprites/ld/mouths/smirk0.png"
            attribute pout:
                "sprites/ld/mouths/pout0.png"
            attribute nag:
                "sprites/ld/mouths/pout0.png"
            attribute mad:
                "sprites/ld/mouths/mad0.png"
            attribute b_yep if_all "bent":
                "sprites/ld/mouths/b_yep.png"
            attribute b_yep_talk if_all "bent":
                "sprites/ld/mouths/b_yep.png"
            attribute b_scary if_all "bent":
                "sprites/ld/mouths/b_scary.png"


            attribute yep_talk:
                "ld_yep_talk"
            attribute cat_talk:
                "ld_yep_talk"
            attribute mal_talk:
                "mal_talk"
            attribute scary_talk:
                "scary_talk"
            attribute smirk_talk:
                "mad_talk"
            attribute pout_talk:
                "pout_talk"
            attribute nag_talk:
                "nag_talk"
            attribute mad_talk:
                "mad_talk"


    image ld_yep_talk:
        "sprites/ld/mouths/yep1.png"
        .2
        "sprites/ld/mouths/yep2.png"
        .2
        repeat
    image mal_talk:
        "sprites/ld/mouths/malicious1.png"
        .2
        "sprites/ld/mouths/malicious2.png"
        .2
        repeat
    image scary_talk:
        "sprites/ld/mouths/scary1.png"
        .2
        "sprites/ld/mouths/scary2.png"
        .2
        repeat
    image pout_talk:
        "sprites/ld/mouths/pout1.png"
        .2
        "sprites/ld/mouths/pout2.png"
        .2
        repeat
    image nag_talk:
        "sprites/ld/mouths/nagging1.png"
        .2
        "sprites/ld/mouths/nagging2.png"
        .2
        repeat
    image mad_talk:
        "sprites/ld/mouths/mad1.png"
        .2
        "sprites/ld/mouths/mad2.png"
        .2
        repeat
