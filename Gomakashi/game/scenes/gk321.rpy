label gk321:
    call hide_menu
    play music "audio/umi/dread of the grave.mp3"
    scene monitor_room
    show hnb evilgrin fury at right onlayer overlayer
    show check angry nope fp at left onlayer overlayer
    show check at flip
    "------------scene 321 Metarivali part 2-------------"
    show vs_screen
    show tsumi_prop:
        zoom 0.3
        xalign 0.5
        yalign 0.0

    show hnb:
        xoffset -450
        yoffset 180
    show check:
        xoffset 280
        yoffset 230
    camera overlayer:
        zoom 2
        xalign 0.5
        yalign 0.5
    play sound "audio/sfx/zbiin.ogg"

    window hide
    pause

    ck "Ti faccio nero!!!!!"
    hb "No you!!!!!!"
    window hide
#     show black onlayer overlayer with Dissolve(1):
#         alpha 0.6


    pause 0.3

    camera:
        xalign 0.5
        yalign 0.0
        easeout_expo 1.5 zoom 3

    camera overlayer:
#         easeout_expo 1.5 yalign -0.4
        easeout_expo 1.5 zoom 6

    pause 1.5

    hide check
    hide hnb

    camera:
        zoom 1
    scene tsumi_frag

    play sound "audio/sfx/doon.mp3" volume 1.5

    stop music fadeout 35
    $renpy.transition(vpunch)
    $renpy.call_screen('welcome_tsumi')

    return