## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)
    if persistent.playthrough == 0:
        stop music fadeout 2.0
        scene bg club_day
        $ current_text_num = 0
        $ s_hist.text_history.append(test_text_one)
        mc "Test Text Mode"
        if persistent.iphone:
            mc "iPhone Test Text Mode"
        else:
            mc "Android Test Text Mode"

        $ s_name = "Sayori"
        call screen phone(number="+1 (323) 555-5555", sender="Sayori", text_class=test_text_two)
        $ s_hist.text_history.append(test_text_two)
        $ current_text_num = 0
        mc "End solo text mode. Starting group text mode."

        call screen phone(number="Group Chat 1", sender="Sayori, Monika, Natsuki, Yuri", text_class=test_text_three, groupChat=True)
        $ group_hist.append(test_text_three)
        $ current_text_num = 0
        mc "Monologue Monologue."
        call screen phone(number="Group Chat 1", sender="Sayori, Monika, Natsuki, Yuri", text_class=test_text_four, groupChat=True)
        $ group_hist.append(test_text_four)
        $ current_text_num = 0
        mc "End group text mode. Starting custom list."

        $ group_hist_2 = []
        call screen phone(number="Group Chat 2", sender="Sayori, Monika", text_class=test_text_five, hist=group_hist_2, groupChat=True)
        $ group_hist_2.append(test_text_five)
        $ current_text_num = 0
        mc "End custom list. Starting call."
        
        call screen phone_call("Sayori", "Los Santos, LV", "bgm/5.ogg")
        mc "Weird conversation but OK."
        mc "Guess I should end this by now."
        return

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
