default preferences.text_cps = 30
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5


#image building = im.Scale("building.png", 1920, 1080)


label start:
#     $ persistent._clear()

    stop music fadeout 4.5
    play sound "audio/sfx/heavy door open.mp3"
    scene sonozroom with Dissolve(3.5)
    pause 1.5


    call hide_menu
    play sound "audio/sfx/heavy door open.mp3"
    scene sonozakitchen with Fade(1.5,0,1.5)
    pause 1.5

    #Remove comments to add third step

    #play sound "audio/sfx/heavy door close.mp3"
    #scene basement with Fade(1,0,1.5)
    #pause 1.5

    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay


    show screen curtains
    show screen tips
    pause 1.5
    play music ["<silence 2.0>", "audio/higu/asagiri.mp3"]
    play sound "<to 2.0>audio/sfx/beam.mp3"
    show screen prism with CropMove(3.0, "wiperight")
    stop sound

    if persistent.first and persistent.second and persistent.third:
        play sound "audio/sfx/secret_unlock.mp3"
        show screen secret with Dissolve(1)

    while True:
        pause


    return

label hide_menu:
    hide screen tips
    hide screen prism
    hide screen curtains
    hide screen secret

    return
