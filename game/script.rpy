﻿# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.


label start:
    $ _dismiss_pause = False
    pass

label classroom_jump:
    $ persistent.playthrough = 3 #this forces the mod to start out in ch30_main
    #$ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_intro"
    $ renpy.full_restart(transition=None, label="splashscreen")

#label start:
    #$ delete_all_saves()
    #$ persistent.playthrough = 0
    #$ persistent.anticheat = renpy.random.randint(100000, 999999)
    #$ persistent.autoload = "ch0_main"
    #$ renpy.full_restart(transition=None, label="splashscreen")

label startgame:
    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = False

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Girl 3"
    $ m_name = "Girl 2"
    $ n_name = "Girl 1"
    $ y_name = "???"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.playthrough == 3:
        jump ch30_intro

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
