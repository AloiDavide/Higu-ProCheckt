default preferences.text_cps = 30
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5


#image building = im.Scale("building.png", 1920, 1080)


label start:
    stop music fadeout 4.5
    play sound "audio/sfx/heavy door open.mp3"
    scene sonozroom with Dissolve(3.5)
    pause 1.5
    play sound "audio/sfx/heavy door open.mp3"
    scene sonozakitchen with Fade(1.5,0,1.5)
    pause 1.5

    #Remove comments to add third step

    #play sound "audio/sfx/heavy door close.mp3"
    #scene basement with Fade(1,0,1.5)
    #pause 1.5

    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay

    play music "audio/higu/asagiri.mp3"

    call screen tips with Dissolve(0.1)

    return

