label scene3_0:
    call hide_menu
    stop music fadeout 4

    scene clinic_back with longFade
    play music("audio/higu/lies lies.mp3")
    show larry evil at left
    show check at right
    show larry direct at flip

    ""
    window hide dissolve
    show larry:
        ease 1 center
    show check:
        ease 1 offscreenright

    "start"
    ""
    show larry evil
    ""
    show larry directevil
    ""
    show larry hide_arm tilt with dissolve
    ""
    show larry evil
    ""
    show larry direct

    ""

    jump mid_start

    return