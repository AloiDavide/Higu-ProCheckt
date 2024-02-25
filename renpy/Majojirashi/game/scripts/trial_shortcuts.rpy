#shortcut per i cambi di scena durante il processo

label defence:
    scene def_stand
    show check objection fp angry at flip
    show lawyer_table
    return

label berndef:
    scene def_stand
    show lawyer_table
    show bern behind lawyer_table:
        xalign 0.3
        ypos -100
    return

label prosecution:
    scene pros_stand
    show hnb objection:
        xoffset 800
        yoffset -30
    show lawyer_table at flip
    return

label witness:
    scene witness_stand
    show lamb worried nag:
        xalign 0.5
        ypos -60

    show witness_table
    return

label judge:
    scene judge_stand
    show lamb:
        xalign 0.5
        ypos -100
    show judge_table
    return