##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

## Screen Configuration file

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        

        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    tag menu

    text "Adventures in Research main menu"

    add "mmSlideShow"

 #Custom Main Menu
    imagemap:
        ground "imgs/ui/title_screen.png" 
        hover "imgs/ui/title_screen_hover.png"
        
        hotspot (0, 547, 255, 98) action Start() alt _("Start game button")
        hotspot (255, 547, 238, 98) action [If(FileCurrentPage()=="auto", FilePage(1)),ShowMenu("load")] alt _("Load game button")
        hotspot (493, 547, 193, 98) action ShowMenu("preferences") alt _("Settings button")
        hotspot (686, 547, 314, 98) action ShowMenu("achievements") alt _("Achievements button")
        hotspot (1000, 547, 137, 98) action Help() alt _("Help button")
        hotspot (1137, 547, 143, 98) action Quit(confirm=False) alt _("Quit game button")
    


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    
    imagemap:
        ground "imgs/ui/nav_buttons_ground.png"
        idle "imgs/ui/nav_buttons_idle.png"
        hover "imgs/ui/nav_buttons_hover.png"
        selected_idle "imgs/ui/nav_buttons_selected.png"
        selected_hover "imgs/ui/nav_buttons_selected.png"
        #insensitive "imgs/ui/nav_buttons_ground.png"
        
        hotspot (0,  605, 130, 84) action Return() alt "Back button"
        hotspot (130, 605, 222, 84) action [If(FileCurrentPage()=="auto", FilePage(1)), ShowMenu("save")] alt _("Save Game button")
        hotspot (353, 605, 225, 84) action [If(FileCurrentPage()=="auto", FilePage(1)), ShowMenu("load")] alt _("Load Game button")
        hotspot (578, 605, 179, 84) action ShowMenu("preferences") alt _("Settings button")
        hotspot (757, 605, 269, 84) action ShowMenu ("achievements") alt _("Achievements button")
        hotspot (1026, 605, 131, 84) action Help() alt _("Help button")
        hotspot (1158, 605, 123, 84) action Quit() alt _("Quit game button")

    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
screen load_save_slot:
    $ file_text = "%s \nSaved on: %s" % (
        FileSaveName(number),
        FileTime(number, empty=_("N/A\nEmpty Save Slot")))
    ## Original File Slot Text Layout
    #$ file_text = "%2s. Saved on: %s\n %s" % (
    #    FileSlotName(number, 3),
    #    FileTime(number, empty=_("N/A\n Empty Save Slot")),
    #    FileSaveName(number))
    add "imgs/ui/save_scrnshot_background.png" xpos 10 ypos 10
    add FileScreenshot(number) xpos 10 ypos 10
    text file_text xpos 10 ypos 221 size 30 font "SourceSansPro-Semibold.ttf" color "#f0f0f0" hover_color "#333333" outlines [(1, "#333333", 0, 0)] hover_outlines [(1, "#fff32a", 0, 0)]
    add "imgs/ui/save_scrnshot_overlay.png" xpos 10 ypos 10


screen save_file_picker:

        imagemap:

            ground "imgs/ui/save_slots_nav_idle.png"
            #idle "imgs/ui/save_slots_nav_idle.png"
            hover "imgs/ui/save_slots_nav_hover.png"
            selected_idle "imgs/ui/save_slots_nav_selected.png"
            selected_hover "imgs/ui/save_slots_nav_selected.png"

            hotspot (47, 43, 329, 54) action FilePage(1)
            hotspot (378, 43, 326, 54) action None


        imagemap:
            ground "imgs/ui/save_slots_idle.png"
            #idle "imgs/ui/save_slots_idle.png"
            hover "imgs/ui/save_slots_hover.png"


            hotspot (47, 99, 395, 477) clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (442, 99, 395, 477) clicked FileAction(2):
                use load_save_slot(number=2)
            hotspot (838, 99, 395, 477) clicked FileAction(3):
                use load_save_slot(number=3)


screen load_file_picker:

#    frame:
#        style "file_picker_frame"

#        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
#        hbox:
#            style_group "file_picker_nav"
            
#            textbutton _("Previous"):
#                action FilePagePrevious()

#            textbutton _("Auto"):
#                action FilePage("auto")

#            textbutton _("Quick"):
#                action FilePage("quick")

#            for i in range(1, 11):
#                textbutton str(i):
#                    action FilePage(i)
                    
#            textbutton _("Next"):
#                action FilePageNext()

       # $ columns = 2
       # $ rows = 3
        imagemap:

            ground "imgs/ui/load_slots_nav_idle.png"
            hover "imgs/ui/load_slots_nav_hover.png"
            selected_idle "imgs/ui/load_slots_nav_selected.png"
            selected_hover "imgs/ui/load_slots_nav_selected.png"

            hotspot (47, 43, 329, 54) action FilePage(1) alt _("View Saved Games button")
            hotspot (378, 43, 326, 54) action FilePage("auto") alt _("View auto saved games button")
            hotspot (706, 43, 244, 54) action ShowMenu("actSelect") alt _("View Act Selection screen button")
            

        imagemap:
            ground "imgs/ui/save_slots_idle.png"
            #idle "imgs/ui/save_slots_idle.png"
            hover "imgs/ui/save_slots_hover.png"


            hotspot (47, 99, 395, 477) clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (442, 99, 395, 477) clicked FileAction(2):
                use load_save_slot(number=2)
            hotspot (838, 99, 395, 477) clicked FileAction(3):
                use load_save_slot(number=3)
        #    hotspot (642, 100, 591, 157) clicked FileAction(4):
        #        use load_save_slot(number=4)
        #    hotspot (642, 259, 591, 157) clicked FileAction(5):
        #        use load_save_slot(number=5)
        #    hotspot (642, 418, 591, 157) clicked FileAction(6):
        #        use load_save_slot(number=6)
######### Original Save / Load Slots Code Below                
##        # Display a grid of file slots.
##        grid columns rows:
##            transpose True
##            xfill True
##            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
##            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
##                button:
##                    action FileAction(i)
##                    xfill True
##
##                    has hbox

                    # Add the screenshot.
##                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
##                    $ description = "% 2s. %s\n%s" % (
##                        FileSlotName(i, columns * rows),
##                        FileTime(i, empty=_("Empty Slot.")),
##                        FileSaveName(i))

##                    text description

##                    key "save_delete" action FileDelete(i)
                    
                    
screen save:
    # This ensures that any other menu screen is replaced.
    tag menu

    text "Save Game Screen"

    add "imgs/ui/save_background.png" xalign 1.0 yalign 0.0

    #use load_save_slot_nav
    use save_file_picker
    use navigation

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    text "Load Game Screen"

    add "imgs/ui/load_background.png" xalign 1.0 yalign 0.0

    #use load_save_slot_nav
    use load_file_picker
    use navigation

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Act Selection Screen
#
# Screen that allows the user replay/restart a selected Act after it has been unlocked.
#

screen actSelect:

    tag menu

    text "Act Selection Screen"

    add "imgs/ui/actSelect_background.png" xalign 1.0 yalign 0.0

    imagemap:

        ground "imgs/ui/load_slots_nav_idle.png"
        hover "imgs/ui/load_slots_nav_hover.png"
        selected_idle "imgs/ui/load_slots_nav_selected.png"
        selected_hover "imgs/ui/load_slots_nav_selected.png"

        hotspot (47, 43, 329, 54) action [If(FileCurrentPage()=="auto", FilePage(1)), ShowMenu("load")] alt _("View Saved Games button")
        hotspot (378, 43, 326, 54) action [If(FileCurrentPage()==1, FilePage("auto")), ShowMenu("load")] alt _("View auto saved games button")
        hotspot (706, 43, 244, 54) action ShowMenu("actSelect") alt _("View Act Selection screen button")

    imagemap:
        ground "imgs/ui/actSelect_buttons_locked_insensitive.png"
        insensitive "imgs/ui/actSelect_buttons_locked_insensitive.png"
        idle "imgs/ui/actSelect_buttons_unlocked_idle.png"
        hover "imgs/ui/actSelect_buttons_unlocked_hover.png"

        #1st Row
        if persistent.ActOne_unlocked:
            hotspot (45, 99, 396, 238) action Start("restartActOne") alt _("Restart from Act One button")
        if persistent.ActTwo_unlocked:
            hotspot (442, 99, 396, 238) action Start("restartActTwo") alt _("Restart from Act Two button")
        if persistent.ActThree_unlocked:
            hotspot (839, 99, 395, 238) action Start("restartActThree") alt _("Restart from Act Three button")
        #2nd Row
        if persistent.ActFour_unlocked:
            hotspot (45, 338, 396, 238) action Start("restartActFour") alt _("Restart from Act Four button")
        if persistent.ActFive_unlocked:
            hotspot (442, 338, 396, 238) action Start("restartActFive") alt _("Restart from Act Five button")
        if persistent.ActSix_unlocked:
            hotspot (839, 338, 395, 238) action Start("restartActSix") alt _("Restart from Act Six button")

    use navigation


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    text "Settings Screen"

    add "imgs/ui/settings_background.png" xalign 1.0 yalign 0.0

    imagemap:
        ground "imgs/ui/settings_dialog_ground.png"
        idle "imgs/ui/settings_dialog_idle.png"
        hover "imgs/ui/settings_dialog_hover.png"
        selected_hover "imgs/ui/settings_dialog_hover.png"
        selected_idle "imgs/ui/settings_dialog_hover.png"

        hotspot (598, 173, 137, 38) action Preference("display", "window") alt _("Run game in a window button")
        hotspot (785, 173, 165, 38) action Preference("display", "fullscreen") alt _("Run game fullscreen button")

    # Sliders
        bar pos (610, 276, 336, 28) value Preference("Text Speed") style "pref_slider" alt _("Text speed slider")
        bar pos (610, 383, 336, 28) value Preference("Sound Volume") style "pref_slider" alt _("Sound effects volume slider")
        bar pos (610, 499, 336, 28) value Preference("Music Volume") style "pref_slider" alt _("Music volume slider")
        #bar pos (32,243,148,15) value Preference("Voice Volume") style "pref_slider"
        #bar pos (47,308,148,15) value Preference("Auto-Forward", "toggle") style "pref_slider"

    # Include the navigation.
    use navigation

init -2 python:
    style.pref_slider.left_bar = "imgs/ui/bar_full.png" #full
    style.pref_slider.right_bar = "imgs/ui/bar_empty.png" #empty
    style.pref_slider.ymaximum = 28
    style.pref_slider.xmaximum = 336
    style.pref_slider.left_gutter = 6
    style.pref_slider.right_gutter = 6
    style.pref_slider.bar_resizing = False
    style.pref_slider.thumb = "imgs/ui/bar_thumb.png"
    style.pref_slider.thumb_shadow = None
    style.pref_slider.thumb_offset = 5
    style.pref_slider.bar_vertical = False



##############################################################################
# Achievements Nav Buttons
#
# Screen that displays buttons to navigate between achievement pages

screen achievement_nav_buttons:

    imagemap:
        ground "imgs/ui/achievements_navbuttons_disabled.png"
        idle "imgs/ui/achievements_navbuttons_idle.png"
        hover "imgs/ui/achievements_navbuttons_hover.png"

        # activate Previous Button
        if achvt_pg == 2:
            hotspot (37, 451, 90, 90) action [ SetVariable("achvt_pg", 1), ShowMenu("achievements") ] 

        elif achvt_pg == 1:
            hotspot (37, 451, 90, 90) action None

        # activate Next Button
        if achvt_pg == 1:
            hotspot (1154, 451, 90, 90) action [ SetVariable("achvt_pg", 2), ShowMenu("achievements") ] 

        elif achvt_pg == 2:
            hotspot (1154, 451, 90, 90) action None
                

##############################################################################
# Achievements Screen
#
# Screen that shows list of achievements player has earned

screen achievements:

    tag menu

    # set variable for achievements counter
    $ achcount = 0

    # This for Self Voicing this menu screen
    text "Achievements Screen"

    # Self Voicing Support for achievements earned.
    text "You have unlocked the following achievements:"
    if persistent.achievement_tutorial_complete_unlocked:
        text "Tutorial Completed"
        $ achcount = achcount + 1

    if persistent.achievement_topic_tackler_unlocked:
        text "Topic Tackler"
        $ achcount = achcount + 1

    if persistent.achievement_bad_end1_unlocked:
        text "Bad Ending Number One: Robot Apocalypse"
        $ achcount = achcount + 1

    if persistent.achievement_future_reference_unlocked:
        text "For Future Reference"
        $ achcount = achcount + 1

    if persistent.achievement_actOne_complete_unlocked:
        text "Act One Completed"
        $ achcount = achcount + 1

    if persistent.achievement_bad_end2_unlocked:
        text "Bad Ending Number Two: Zombies at the Farm"
        $ achcount = achcount + 1

    if persistent.achievement_information_wrangler_unlocked:
        text "Information Wrangler"
        $ achcount = achcount + 1

    if persistent.achievement_actTwo_complete_unlocked:
        text "Act Two Completed"
        $ achcount = achcount + 1

    if persistent.achievement_appropriate_book_unlocked:
        text "An Appropriate Book"
        $ achcount = achcount + 1

    if persistent.achievement_bad_end3_unlocked:
        text "Bad Ending Number Three: Shark Dental Assistant"
        $ achcount = achcount + 1

    if persistent.achievement_boolean_expert_unlocked:
        text "Boolean Expert"
        $ achcount = achcount + 1

    if persistent.achievement_chatty_cathy_unlocked:
        text "Chatty Cathy"
        $ achcount = achcount + 1

    if persistent.achievement_actThree_complete_unlocked:
        text "Act Three Completed"
        $ achcount = achcount + 1

    if persistent.achievement_bad_end4_unlocked:
        text "Bad Ending Number Four: Moon Landscaper"
        $ achcount = achcount + 1

    if persistent.achievement_honesty_policy_unlocked:
        text "Honesty is the Best Policy"
        $ achcount = achcount + 1

    if persistent.achievement_actFour_complete_unlocked:
        text "Act Four Completed"
        $ achcount = achcount + 1

    if persistent.achievement_bad_end5_unlocked:
        text "Bad Ending Number Five: Hiding in My Bomb Shelter"
        $ achcount = achcount + 1

    if persistent.achievement_critical_thinker_unlocked:
        text "Critical Thinker"
        $ achcount = achcount + 1

    if persistent.achievement_actFive_complete_unlocked:
        text "Act Five Completed"
        $ achcount = achcount + 1

    if persistent.achievement_power_pointers_unlocked:
        text "Power Pointers"
        $ achcount = achcount + 1

    if persistent.achievement_actSix_complete_unlocked:
        text "Act Six Completed"
        $ achcount = achcount + 1

    if persistent.achievement_allActs_complete_unlocked:
        text "All Six Acts Completed"
        $ achcount = achcount + 1

    $ achremain = 22 - achcount

    if achcount > 1:
        text " . You have unlocked [achcount] achievements. [achremain] achievements remain locked."

    if achcount == 1:
        text " . You have unlocked [achcount] achievement. [achremain] achievements remain locked."

    if achcount == 0:
        text " . You have not unlocked any achievements yet. [achremain] achievements remain locked."


    # End Self Voicing of Achievements
    ##############################################################

    add "imgs/ui/achievements_background.png" xalign 1.0 yalign 0.0
    # Include the navigation buttons.
    use achievement_nav_buttons
    use navigation


    #The first page of achievements
    if achvt_pg == 1:
        grid 3 5:

            transpose True
            xalign .50
            yalign .48
            style_group "achievements"
                        
            if persistent.achievement_tutorial_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_tutorial_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_tutorial_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_topic_tackler_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_topic_tackler.png"
                    hover "imgs/ui/achievements/achievement_topic_tackler.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_bad_end1_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/endings/achievement_bad_end1.png"
                    hover "imgs/ui/achievements/endings/achievement_bad_end1.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_future_reference_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_future_reference.png"
                    hover "imgs/ui/achievements/achievement_future_reference.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_actOne_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actOne_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actOne_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_bad_end2_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/endings/achievement_bad_end2.png"
                    hover "imgs/ui/achievements/endings/achievement_bad_end2.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_information_wrangler_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_information_wrangler.png"
                    hover "imgs/ui/achievements/achievement_information_wrangler.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"
            
            if persistent.achievement_actTwo_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actTwo_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actTwo_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_appropriate_book_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_appropriate_book.png"
                    hover "imgs/ui/achievements/achievement_appropriate_book.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_bad_end3_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/endings/achievement_bad_end3.png"
                    hover "imgs/ui/achievements/endings/achievement_bad_end3.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_boolean_expert_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_boolean_expert.png"
                    hover "imgs/ui/achievements/achievement_boolean_expert.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"
            
            if persistent.achievement_chatty_cathy_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_chatty_cathy.png"
                    hover "imgs/ui/achievements/achievement_chatty_cathy.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_actThree_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actThree_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actThree_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_bad_end4_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/endings/achievement_bad_end4.png"
                    hover "imgs/ui/achievements/endings/achievement_bad_end4.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_honesty_policy_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_honesty_policy.png"
                    hover "imgs/ui/achievements/achievement_honesty_policy.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

    #The second page of achievements
    if achvt_pg == 2:
        grid 2 5:
            transpose True
            xalign .239
            yalign .48
            style_group "achievements"

            if persistent.achievement_actFour_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actFour_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actFour_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_bad_end5_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/endings/achievement_bad_end5.png"
                    hover "imgs/ui/achievements/endings/achievement_bad_end5.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_critical_thinker_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_critical_thinker.png"
                    hover "imgs/ui/achievements/achievement_critical_thinker.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_actFive_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actFive_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actFive_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_power_pointers_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/achievement_power_pointers.png"
                    hover "imgs/ui/achievements/achievement_power_pointers.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_actSix_complete_unlocked:
                imagebutton:
                    idle "imgs/ui/achievements/acts/achievement_actSix_complete.png"
                    hover "imgs/ui/achievements/acts/achievement_actSix_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"

            if persistent.achievement_allActs_complete_unlocked:
                    imagebutton:
                        idle "imgs/ui/achievements/acts/achievement_allActs_complete.png"
                        hover "imgs/ui/achievements/acts/achievement_AllActs_complete.png"
            else:
                imagebutton:
                    idle "imgs/ui/achievements/locked/achievement_locked.png"
                    hover "imgs/ui/achievements/locked/achievement_locked.png"
            
            #blank placeholders for grid
            imagebutton:
                    idle "imgs/ui/achievements/achievement_spacer.png"
                    hover "imgs/ui/achievements/achievement_spacer.png"
            imagebutton:
                    idle "imgs/ui/achievements/achievement_spacer.png"
                    hover "imgs/ui/achievements/achievement_spacer.png"
            imagebutton:
                    idle "imgs/ui/achievements/achievement_spacer.png"
                    hover "imgs/ui/achievements/achievement_spacer.png"
        

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    add "imgs/ui/yesno_background.png"
#    window:
#        style "gm_root"

    # "Are you sure you want to quit?\nUnsaved progress will be lost."
    frame:
        style_group "yesno"
        background "#00000000"
        xfill True
        xmargin .05
        yalign .5
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 0.0
        yalign 0.02

        #textbutton _("Quick Save") action QuickSave()
        #textbutton _("Quick Load") action QuickLoad()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Load") action ShowMenu("load")
        # textbutton _("Skip") action Skip()
        # textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Settings") action ShowMenu('preferences')
        imagebutton:
            idle "imgs/ui/settings_icon.png"
            hover "imgs/ui/settings_icon_hover.png"
            action ShowMenu('preferences')
            alt "Game Settings Button"
        
init -2 python:

    # initialize value for achievement page at first run
    achvt_pg = 1

    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.font = "SourceSansPro-Bold.ttf"
    style.quick_button_text.size = 14
    style.quick_button_text.idle_color = "#ddd"
    style.quick_button_text.hover_color = "#fdff4b"
    #style.quick_button_text.selected_idle_color = "#cc08"
    #style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    
