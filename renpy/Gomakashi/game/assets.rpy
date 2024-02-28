init python:
    def head_tilt_func(img):
        return Transform(Crop((150, 80, 350, 350), img), rotate=-15, align=(0.5,0.5), offset=(-658, -258), transform_anchor=True, rotate_pad=False)
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
init:
    transform flip:
        xzoom -1

    transform unflip:
        xzoom 1


    image check_objection = Transform("sprites/ck/wright.png", xoffset=-658)
    image hanabi_objection = Transform("sprites/hb/von karma.png", xoffset=-693)
    image leftdist = Transform("sprites/ck/f_distinctive.png", xoffset=70, yoffset=-30)





    #CHECK


    layeredimage check:
        group pose:
            attribute defa:
                "sprites/ck/def.png"
            attribute sor default:
                "sprites/ck/sorcerer.png"
            attribute objection:
                "check_objection"

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
            attribute p:
                "sprites/ck/hat.png"

            attribute p:
                "sprites/ck/distinctive.png"

            attribute fp:
                "sprites/ck/f_hat.png"

            attribute fp if_any "sor":
                "sprites/ck/f_distinctive.png"
            attribute fp if_any "objection":
                "leftdist"

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





#------------------------------------------------
            #   LARRY
#------------------------------------------------
#attribute tilt:
#                transform_anchor False
#                rotate_pad False
#                anchor (0.5,0.5)
#                #align (0.1, 0.1)

#                rotate -10

#                "sprites/la/border_head.png"

    layeredimage larrys_head:
        always:
            "sprites/la/border_head.png"

        group eyes:
            attribute close:
                "sprites/ck/close.png"
            attribute sus:
                "sprites/ck/sus.png"
            attribute think:
                "sprites/ck/think.png"

        attribute shades default:
            "sprites/la/shades.png"



    #Transform(Crop((150, 80, 350, 350), img), rotate=-15, align=(0.5,0.5), offset=(-658, -258), transform_anchor=True, rotate_pad=False)

    transform head_tilt:
        crop (150, 80, 350, 350)
        transform_anchor True
        rotate_pad False
        rotate -15
        align (0.5,0.5)
        offset (-658, -258)


    #image larrys_tilted_head = head_tilt_func("larrys_head")


    # LARRY
    layeredimage larry:



        group pose:
            attribute defa default:
                "sprites/la/border.png"
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

        group mouth:
            attribute yep :
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







#------------------------------------------------
            #   HANABI
#------------------------------------------------
    layeredimage hnb:

        group body:
            attribute defa default:
                "sprites/hb/defa.png"
            attribute objection:
                "hanabi_objection"


        group flippable:
            attribute unflip default if_any "defa":
                "sprites/hb/napalm.png"

            attribute flip:
                "sprites/hb/napalm_flip.png"

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
            attribute smug2 default:
                "sprites/hb/eyes/smug.png"
            attribute fury:
                "sprites/hb/eyes/fury.png"
            attribute ohno:
                "sprites/hb/eyes/ohno.png"
            attribute close:
                "sprites/hb/eyes/close.png"



        group mouth:
            attribute yep default:
                "sprites/hb/mouths/yep0.png"
            attribute nope:
                "sprites/hb/mouths/nope0.png"
            attribute sneer:
                "sprites/hb/mouths/sneer0.png"
            attribute laugh:
                "sprites/hb/mouths/laugh1.png"
            attribute smirk:
                "sprites/hb/mouths/smirk0.png"

            attribute yep_talk:
                "hb_yep_talk"
            attribute nope_talk:
                "hb_nope_talk"
            attribute sneer_talk:
                "hb_sneer_talk"
            attribute laugh_talk:
                "hb_laugh_talk"
            attribute smirk_talk:
                "hb_yep_talk"


    image hb_yep_talk:
        "sprites/hb/mouths/yep1.png"
        .2
        "sprites/hb/mouths/yep2.png"
        .2
        repeat

    image hb_nope_talk:
        "sprites/hb/mouths/nope1.png"
        .2
        "sprites/hb/mouths/nope2.png"
        .2
        repeat

    image hb_sneer_talk:
        "sprites/hb/mouths/sneer1.png"
        .2
        "sprites/hb/mouths/sneer2.png"
        .2
        repeat

    image hb_laugh_talk:
        "sprites/hb/mouths/laugh1.png"
        .2
        "sprites/hb/mouths/laugh2.png"
        .2
        repeat



    image hb_taunt:
        "sprites/hb/finger2.png"
        .3
        "sprites/hb/finger1.png"
        .3
        repeat 2




    #BERN
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
            attribute a_talk:
                "bk_neutral_talk"
            attribute b_talk:
                "bk_up_talk"

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

    #LAMB
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


#CHARACTERS
define n = Character(None, what_style= "wideN")
define ck = Character("Check", who_color = "#480000", what_style= "wide", who_style = "border", image="check", callback=functools.partial(lipflap, name="check", mouths=["yep", "nope", "worried", "smile", "shout"]))
define la = Character("Larry", who_color = "#fad861", what_style= "wide", who_style = "border", image="larry")
define witch = Character("???", who_color = "#0000cf", what_style= "wide", who_style = "border", image="bern", callback=functools.partial(lipflap, name="bern", mouths=["a", "b"]))
define bk = Character("Bernkastel", who_color = "#0000cf", what_style= "wide", who_style = "border", image="bern", callback=functools.partial(lipflap, name="bern", mouths=["a", "b"]))
define hb = Character("Hanabi", dynamic=True, who_color = "#cc4f33", what_style= "wide", who_style = "border", image="hnb", callback=functools.partial(lipflap, name="hnb", mouths=["yep", "nope", "sneer", "smirk", "laugh"]))
define ld = Character("lambdadelta", dynamic=True, who_color = "#ffe674", what_style= "wide", who_style = "border", image="lamb", callback=functools.partial(lipflap, name="lamb", mouths=["yep","cat","mal","scary","smirk","pout","nag","mad", "b_yep"]))
define yw = Character("yellow_witch", dynamic=True, who_color = "#ffe674", what_style= "wide", who_style = "border")
define rika = Character("Rika", who_color = "#0000cf", what_style= "wide", who_style = "border")
define bent_ld = Character("lambdadelta", who_color = "#ffe674", what_style= "wide", who_style = "border")


image chibimion = "sprites/chibimion.png"
image oryou = "sprites/oryou.png"
image ooishi = "sprites/ooishi.png"
image rika defa = "sprites/rika defa.png"
image rika majime = "sprites/rika majime.png"
image rika niya = "sprites/rika niya.png"

#BACKGROUNDS
image black = im.Scale("bg/black.jpg", 1920, 1080)
image red = im.Scale("bg/red.png", 1920, 1080)
image fragplane = im.Scale("bg/fragplane.png", 1920, 1080)
image bern_kekkai = im.Scale("bg/bern kekkai.png", 1920, 1080)
image bern_kekkai_closeup = im.Scale("bg/bern kekkai closeup.png", 1920, 1080)
image vortex = im.Scale("bg/vortex.png", 1920, 1080)
image sky_frag = im.Scale("bg/sky of frag.png", 1924, 1080)
image hinamizawa = im.Scale("bg/hinamizawa.png", 1920, 1080)
image hinamizawa2 = im.Scale("bg/hinamizawa 2.webp", 1920, 1080)
image field = im.Scale("bg/field.png", 1920, 1080)
image sonozroom = im.Scale("bg/sonozroom.png", 1920, 1080)
image sonozakitchen = im.Scale("bg/sonozakitchen.png", 1920, 1080)
image basement = im.Scale("bg/basement.png", 1920, 1080)
image dam = im.Scale("bg/dam.png", 1920, 1080)




#OVERLAYS
image welcome = im.Scale("overlay/welcome.png", 1920, 1080)
image frag_overlay = im.Scale("overlay/frag_overlay70.png", 1920, 1080)
image frag_lines = im.Scale("overlay/frag_overlay0.png", 1920, 1080)
image stop_time = im.Scale("overlay/stop time.png", 1920, 1080)
image table = im.Scale("overlay/table.png", 1920, 1080)
image lawyer_table = im.Scale("overlay/lawyer table.png", 1920, 1080)
image judge_table = im.Scale("overlay/judge table.png", 1920, 1080)
image witness_table = im.Scale("overlay/witness table.png", 1920, 1080)
image debris = im.Scale("overlay/debris.png", 1920, 1080)
image blue_aura = im.Scale("overlay/blue aura.png", 780, 1180)
image yellow_aura = im.Scale("overlay/yellow aura.png", 780, 1180)

#FRAGMENTS
image meakashi_frag = im.Scale("frags/meakashi fragment.png", 1920, 1080)
image meakashi_prop = im.Scale("frags/meakashi fragment alpha.png", 1920, 1080)
image hima_frag = im.Scale("frags/hima fragment.png", 1920, 1080)
image hima_prop = im.Scale("frags/hima fragment alpha.png", 1920, 1080)
image tatari_prop = im.Scale("frags/tatari fragment alpha.png", 1920, 1080)
image wata_frag = im.Scale("frags/wata fragment.png", 1920, 1080)
image wata_prop = im.Scale("frags/wata fragment alpha.png", 1920, 1080)
image oni_frag = im.Scale("frags/oni fragment.png", 1920, 1080)
image oni_prop = im.Scale("frags/oni fragment alpha.png", 1920, 1080)
image check_prop = im.Scale("frags/check fragment alpha.png", 1920, 1080)

image lamb black = im.Scale("sprites/lambda siluett.png", 640, 1080)
image lamb blackB= im.Scale("sprites/lambda siluett B.png", 640, 1080)
