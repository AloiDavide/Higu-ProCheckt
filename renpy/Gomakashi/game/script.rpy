default preferences.text_cps = 30
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5


#image building = im.Scale("building.png", 1920, 1080)


label start:
    stop music fadeout 2.5
    scene sonozroom with Dissolve(3.5)
    play sound "audio/sfx/glass crack.mp3"
    show frag_overlay

    play music "audio/higu/asagiri.mp3"

    call screen tips

    return

