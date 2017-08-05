##
## Adventures in Research (2012-2017)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

label Tutorial:
    
    $ save_name = "Name: %s.\nScene: Tutorial." % (name)

    play ambient "sfx/greenery-ambient.ogg"
    play music "music/Greenery.ogg" fadein 0.8

    tu "Hi [name!q]! Welcome to {font=SourceSansPro-SemiboldItalic.ttf}Adventures in Research!{/font} To advance to the next screen, click the mouse button or press the “Enter” key on the keyboard."
    
    tu "Great! In this game we’ll be exploring the basics of academic research."
    
    tu "You are going to be playing this game in your LIBR 21OO class."

    # For Self-voicing only
    sv "This tutorial will help introduce some of the game’s features."

    tu "Your LIBR 21OO professor will also give you outside assignments, readings, and/or group work."
    tu "This game is meant to supplement the things you are doing in class; it will introduce some concepts and reinforce others."
    
    tu "As you go along in the game you’ll have opportunities to earn achievements and test your knowledge."
    tu "Once you complete one of the game’s six Acts you’ll be given a unique code that will give you access to the next part of the game."
    
    tu "Sometimes, you will have to make choices to progress through the game."
    tu "When you are given dialogue options, use your mouse to click on the most appropriate answer."

    sv "You may use the up and down arrow keys on the keyboard to cycle through each answer. Press “Enter” to confirm your choice."
    tu "Let’s try one now!"
    sv "After the question has been asked, press “Enter” to be able to select from the possible answers."
    tu "Who is UWG’s mascot?"

    menu:

        tuc "Who is UWG’s mascot?{fast}"
        
        "Wolfie the Wolf":
            tu "Correct! Great job."
        
        "Jane the Parrot":
            tu "Sorry, it’s Wolfie."
        
        "Larry the Lion":
            tu "Sorry, it’s Wolfie."
    
    tu "For some of these scenarios, you will have to choose several options until you find the correct answer."
    tu "Be careful! Some incorrect answers could lead to unintended consequences for the game’s characters."
    
    tu "Click the settings icon {image=imgs/ui/settings_icon.png} at the top left corner of the screen to access the game’s settings, save your progress, or quit the game."
    sv "You can also use the up arrow key to access the settings button anytime during the game."
    tu "You can stop and save and resume your progress as often as you need to."
    tu "Note that pressing the “esc” or “escape” key on your keyboard will also bring up the game’s menu."

    tu "You can change the text speed of the game and the volume for sound effects and music from the settings menu."
    sv "To change the speed of the self-voicing for the game’s text, consult the Help file from the settings menu."

    tu "If you need to see part of the screen that’s covered by a menu or this text box, you press “h” on your keyboard."

    tu "Try it now. Press “h” (press it again to show this text box)."

    if not persistent.achievement_tutorial_complete_unlocked:
        $ persistent.achievement_tutorial_complete_unlocked = True
        show achievement tutorialComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"

        tu "You just earned your first Achievement for completing this Tutorial!"

        tu "You’ll get opportunities to earn more Achievements throughout the game, depending on what choices you make and how far you get. Try to collect them all!"

        tu "Note that you can view all of the Achievements you’ve earned so far by visiting the Achievements screen in the game’s menu."

    tu "Also, you can click “Help” from the game’s menu if you need to look up anything covered in this tutorial."
    
    tu "Now you should be all ready to start the game! Happy researching!"

    jump tutorialEnterPassword

label tutorialEnterPassword:
    $player_pass = renpy.input("Please enter the password for Act One and press “Enter”", length=6)
    if player_pass.upper().strip() == actOne_pass:
        stop ambient fadeout 0.8
        stop music fadeout 0.8
        jump ActOne
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump tutorialEnterPassword
    
