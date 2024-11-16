init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

    transform codec_right:
        xalign 1.0
        xoffset -50
        yoffset 30

    transform codec_left:
        xalign 0.0
        xoffset 50
        yoffset 30

    transform flip:
        xzoom -1

    transform unflip:
        xzoom 1

    transform pointing:
        xoffset -136
        yoffset 60

    transform reset:
        xoffset 0
        yoffset 0

    transform static_left:
        xalign 0.1
        yalign 0.11

    transform static_right:
        xalign 0.9
        yalign 0.11

    image check_objection = Transform("sprites/ck/wright.png", xoffset=-658)
    image hanabi_objection = Transform("sprites/hb/von karma.png", xoffset=-693)
    image leftdist = Transform("sprites/ck/f_distinctive.png", xoffset=70, yoffset=-30)



    define flash = Fade(0.1, 0.0, 0.5, color="#fff")
    define purple_flash = Fade(0.1, 0.0, 0.5, color="#7E3FFF")
    define purple_quick = Fade(0.1, 0.0, 0.1, color="#7E3FFF")


    define longDiss = Dissolve(4)
    define longerDiss = Dissolve(8)
    define longFade = Fade(4,0,2)
    define longerFade = Fade(6,0,4)