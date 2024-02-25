default preferences.text_cps = 30
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5

image building = im.Scale("building.png", 1920, 1080)

image black = im.Scale("black.jpg", 1920, 1080)

define newFade = Fade(1, 0, 2)

label start:
    scene building with newFade

    play music "audio/asagiri.mp3"


    call screen tips




    return

