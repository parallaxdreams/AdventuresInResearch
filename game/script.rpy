##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

## Game script starts with this file

init:

    # Custom Screen Positions
    $ leftedge = Position(xpos=0.10, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ leftmid = Position(xpos=0.25, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ leftthird = Position(xpos=0.33, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ rightthird = Position(xpos=0.66, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ rightmid = Position(xpos=0.75, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ farright = Position(xpos=0.80, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ rightedge = Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
    
    #custom char appearance fx
    $ qdissolve = Dissolve(0.10)

    #Long Dissove for SlideShows
    $ ldissolve = Dissolve(2.0)

    #Long Fade for End Credit Slideshow
    $ lfade = Fade(1.0, 0, 1.0)

    #Custom Transition for Background Wipes
    $ fadewiperight = ImageDissolve("imgs/bg/bg_black_wipe.png", 2.0, reverse=True)

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

## Achievement Pop-ups
image achievement tutorialComplete = "imgs/ui/achievements/acts/achievement_tutorial_complete.png"
image achievement topicTackler = "imgs/ui/achievements/achievement_topic_tackler.png"
image achievement futureReference = "imgs/ui/achievements/achievement_future_reference.png"
image achievement actOneComplete = "imgs/ui/achievements/acts/achievement_actOne_complete.png"
image achievement informationWrangler = "imgs/ui/achievements/achievement_information_wrangler.png"
image achievement actTwoComplete = "imgs/ui/achievements/acts/achievement_actTwo_complete.png"
image achievement appropriateBook = "imgs/ui/achievements/achievement_appropriate_book.png"
image achievement booleanExpert = "imgs/ui/achievements/achievement_boolean_expert.png"
image achievement chattyCathy = "imgs/ui/achievements/achievement_chatty_cathy.png"
image achievement actThreeComplete = "imgs/ui/achievements/acts/achievement_actThree_complete.png"
image achievement honestyPolicy = "imgs/ui/achievements/achievement_honesty_policy.png"
image achievement actFourComplete = "imgs/ui/achievements/acts/achievement_actFour_complete.png"
image achievement criticalThinker = "imgs/ui/achievements/achievement_critical_thinker.png"
image achievement actFiveComplete = "imgs/ui/achievements/acts/achievement_actFive_complete.png"
image achievement powerPointers = "imgs/ui/achievements/achievement_power_pointers.png"
image achievement actSixComplete = "imgs/ui/achievements/acts/achievement_actSix_complete.png"
image achievement allActsComplete = "imgs/ui/achievements/acts/achievement_allActs_complete.png"
image achievement badEnd1 = "imgs/ui/achievements/endings/achievement_bad_end1.png"
image achievement badEnd2 = "imgs/ui/achievements/endings/achievement_bad_end2.png"
image achievement badEnd3 = "imgs/ui/achievements/endings/achievement_bad_end3.png"
image achievement badEnd4 = "imgs/ui/achievements/endings/achievement_bad_end4.png"
image achievement badEnd5 = "imgs/ui/achievements/endings/achievement_bad_end5.png"

## Screenshots
image screenshot bookRecordCN = "imgs/sshots/book_record_cn.png"
image screenshot bookRecordTOC = "imgs/sshots/book_record_toc.png"
image screenshot libraryHome = "imgs/sshots/library_home_pg.png"
image screenshot galileoHome = "imgs/sshots/galileo_home.png"
image screenshot acCompleteHome = "imgs/sshots/acComplete_home.png"
image screenshot acCompleteRecord = "imgs/sshots/acComplete_record.png"

## Backgrounds
image bg classroom = "imgs/bg/bg_classroom.jpg"
image bg fountainDay = "imgs/bg/bg_fountain_day.jpg"
image bg movieSet = "imgs/bg/bg_movie_set.jpg"
image bg movieSetExtras = "imgs/bg/bg_movie_set_extras.jpg"
image bg festival = "imgs/bg/bg_festival.jpg"
image bg genericCampus = "imgs/bg/bg_greenery.jpg"

## Black Background for longer fades
image bg blackSolid = "imgs/bg/bg_black_solid.jpg"

## For Bad Endings
image bg tenYrsLater = Image("imgs/bg/bg_10yrslater.jpg", alt="Ten Years Later...")


#library
image bg libraryPCs = "imgs/bg/bg_library_computers.jpg"
image bg libraryDVDs = "imgs/bg/bg_library_dvds.jpg"
image bg libraryBrowsing = "imgs/bg/bg_library_browsing.jpg"
image bg libraryReference = "imgs/bg/bg_library_reference.jpg"
image bg libraryStacks = "imgs/bg/bg_library_stacks.jpg"
image bg libraryPatio = "imgs/bg/bg_library_patio.jpg"

#bad Endings
image bg officeAttack = "imgs/bg/bg_office_attack.jpg"
image bg zombies = "imgs/bg/bg_zombies.jpg"
image bg bunker = "imgs/bg/bg_bunker.jpg"
image bg sharkDentist = "imgs/bg/bg_shark_dentist.jpg"
image bg moonLandscaper = "imgs/bg/bg_moon_landscaper.jpg"

## Calendar
image bg calendar = "imgs/bg/bg_calendar.png"
image calendar dates = "imgs/ui/calendar_dates.png"
image calendar backing = "imgs/ui/calendar_backing.png"

## Act Titlecards
image bg ActOne = Image("imgs/bg/bg_ActOne.png", alt="Act One: A Case of the Mondays")
image bg ActTwo = Image("imgs/bg/bg_ActTwo.png", alt="Act Two: Pride and Periodicals")
image bg ActThree = Image("imgs/bg/bg_ActThree.png", alt="Act Three: Hollywood is Boolean")
image bg ActFour = Image("imgs/bg/bg_ActFour.png", alt="Act Four: Avoiding Plagiarism")
image bg ActFive = Image("imgs/bg/bg_ActFive.png", alt="Act Five: Climate Change a Palooza")
image bg ActSix = Image("imgs/bg/bg_ActSix.png", alt="Act Six: Presentation Day")

##Boolean Extras Images
image booleanEveryone = "imgs/bool/bool_everyone.png"
image booleanWomen = "imgs/bool/bool_women.png"
image booleanBlueShirt = "imgs/bool/bool_blueShirt.png"
image booleanBlueShirtORskirt = "imgs/bool/bool_blueShirtORskirt.png"
image booleanPants = "imgs/bool/bool_pants.png"
image booleanPantsANDblueShirt = "imgs/bool/bool_pantsANDblueShirt.png"
image booleanWomenNOTpink = "imgs/bool/bool_womenNOTpink.png"
image booleanWomenORmen = "imgs/bool/bool_womenORmen.png"

## Main Menu Slideshow
image mmSlideShow:
    "imgs/bg/bg_greenery.jpg" with ldissolve
    pause 5.0
    "imgs/bg/bg_fountain_day.jpg" with ldissolve
    pause 6.0
    "imgs/bg/bg_library_browsing.jpg" with ldissolve
    pause 6.0
    "imgs/bg/bg_library_reference.jpg" with ldissolve
    pause 6.0
    repeat

##End Credits
image EndCredits = "imgs/EndCredits.png"


##End Credits Slideshow
image endSlideShow:
    alpha 0.8
    pause 4.0
    "imgs/bg/bg_black_solid.jpg" with qdissolve
    "imgs/end/endShow01.jpg" with lfade
    pause 8.0
    "imgs/end/endShow02.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow09.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow04.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow05.jpg" with lfade
    pause 8.0
    "imgs/end/endShow06.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow07.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow08.jpg" with ldissolve
    pause 8.0
    "imgs/end/endShow03.jpg" with lfade
    pause 8.0


## Characters

##Dr. Windham
image windham neutral = "imgs/chars/drw/drw_neutral.png"
image windham neutrallarge = "imgs/chars/drw/drw_neutrallarge.png"
image windham concerned = "imgs/chars/drw/drw_concerned.png"
image windham happy = "imgs/chars/drw/drw_happy.png"
image windham surprised = "imgs/chars/drw/drw_surprised.png"

##Kevin
image kevin neutral = "imgs/chars/kevin/kevin_neutral.png"
image kevin happy = "imgs/chars/kevin/kevin_happy.png"
image kevin concerned = "imgs/chars/kevin/kevin_concerned.png"
image kevin confused = "imgs/chars/kevin/kevin_confused.png"
image kevin surprised = "imgs/chars/kevin/kevin_surprised.png"

##Jeff
image jeff neutral ="imgs/chars/jeff/jeff_neutral.png"
image jeff neutralleft = im.Flip("imgs/chars/jeff/jeff_neutral.png", horizontal=True)
image jeff concerned = "imgs/chars/jeff/jeff_concerned.png"
image jeff concernedleft = im.Flip("imgs/chars/jeff/jeff_concerned.png", horizontal=True)
image jeff happy = "imgs/chars/jeff/jeff_happy.png"
image jeff happyleft = im.Flip("imgs/chars/jeff/jeff_happy.png", horizontal=True)
image jeff confused = "imgs/chars/jeff/jeff_confused.png"
image jeff confusedleft = im.Flip("imgs/chars/jeff/jeff_confused.png", horizontal=True)
image jeff surprised = "imgs/chars/jeff/jeff_surprised.png"
image jeff surprisedleft = im.Flip("imgs/chars/jeff/jeff_surprised.png", horizontal=True)

##Christina
image christina neutral ="imgs/chars/christina/christina_neutral.png"
image christina concerned = "imgs/chars/christina/christina_concerned.png"
image christina confused = "imgs/chars/christina/christina_confused.png"
image christina happy = "imgs/chars/christina/christina_happy.png"
image christina sad = "imgs/chars/christina/christina_sad.png"
image christina surprised = "imgs/chars/christina/christina_surprised.png"

##Kana
image kana neutral = "imgs/chars/kana/kana_neutral.png"
image kana happy = "imgs/chars/kana/kana_happy.png"
image kana concerned = "imgs/chars/kana/kana_concerned.png"
image kana confused = "imgs/chars/kana/kana_confused.png"
image kana surprised = "imgs/chars/kana/kana_surprised.png"

##Stephanie
image stephanie neutral = "imgs/chars/stephanie/stephanie_neutral.png"
image stephanie happy = "imgs/chars/stephanie/stephanie_happy.png"
image stephanie confused = "imgs/chars/stephanie/stephanie_confused.png"
image stephanie concerned = "imgs/chars/stephanie/stephanie_concerned.png"
image stephanie surprised = "imgs/chars/stephanie/stephanie_surprised.png"

##Tony
image tony neutral = im.FactorScale("imgs/chars/tony/tony_neutral.png", 0.985)
image tony neutralright = im.Flip("imgs/chars/tony/tony_neutral.png", horizontal = True)
image tony happy = im.FactorScale("imgs/chars/tony/tony_happy.png", 0.985)
image tony happyright = im.Flip("imgs/chars/tony/tony_happy.png", horizontal = True)
image tony concerned = im.FactorScale("imgs/chars/tony/tony_concerned.png", 0.985)
image tony confused = im.FactorScale("imgs/chars/tony/tony_confused.png", 0.985)
image tony confusedright = im.Flip("imgs/chars/tony/tony_confused.png", horizontal = True)
image tony surprised = im.FactorScale("Imgs/chars/tony/tony_surprised.png", 0.985)

##George Blucas, Director
image georgeblucas = "imgs/chars/director/director.png"
image georgeblucas faceRight = im.Flip("imgs/chars/director/director.png", horizontal=True)



######################################
## Animations

image calendar_alpha:
    "imgs/ui/calendar_whiteout.png"
    xalign 0.0 yalign 0.0 #alpha 0.00
    

image dialogueAdvance = "imgs/ui/dialogueAdvanceSymbol.png"

image inputCaret:
    "imgs/ui/caret.png"
    alpha 1.0
    pause 0.10
    linear 0.5 alpha 0.0
    pause 0.10
    repeat

image biWipe:
    "imgs/bg/bg_black_wipe.png"
    xpos 1281
    ypos 0
    linear 0.25 xpos -640
             
#######################################
## Persistent Variables for Achievements 

$ persistent.achievement_tutorial_complete_unlocked = False
$ persistent.achievement_topic_tackler_unlocked = False
$ persistent.achievement_future_reference_unlocked = False
$ persistent.achievement_actOne_complete_unlocked = False
$ persistent.achievement_information_wrangler_unlocked = False
$ persistent.achievement_actTwo_complete_unlocked = False
$ persistent.achievement_appropriate_book_unlocked = False
$ persistent.achievement_boolean_expert_unlocked = False
$ persistent.achievement_chatty_cathy_unlocked = False
$ persistent.achievement_actThree_complete_unlocked = False
$ persistent.achievement_honesty_policy_unlocked = False
$ persistent.achievement_actFour_complete_unlocked = False
$ persistent.achievement_critical_thinker_unlocked = False
$ persistent.achievement_actFive_complete_unlocked = False
$ persistent.achievement_power_pointers_unlocked = False
$ persistent.achievement_actSix_complete_unlocked = False
$ persistent.achievement_allActs_complete_unlocked = False

$ persistent.achievement_bad_end1_unlocked = False
$ persistent.achievement_bad_end2_unlocked = False
$ persistent.achievement_bad_end3_unlocked = False
$ persistent.achievement_bad_end4_unlocked = False
$ persistent.achievement_bad_end5_unlocked = False


#######################################
## Persistent Variables for Unlocking Acts for Act Selection Screen

$ persistent.ActOne_unlocked = False
$ persistent.ActTwo_unlocked = False
$ persistent.ActThree_unlocked = False
$ persistent.ActFour_unlocked = False
$ persistent.ActFive_unlocked = False
$ persistent.ActSix_unlocked = False


#######################################
## Declare characters used by this game.

#Create variable for player name
$ name = ""

#line below is player character
define m = Character("Me", who_alt="You", color="#000",ctc="dialogueAdvance", ctc_position="nestled", what_alt="say, [text]")
define mt = Character("Me", who_alt="You", color="#000",ctc="dialogueAdvance", ctc_position="nestled", what_alt="think to yourself, [text]")

#supporting characters
define tu = Character('Tutorial', who_alt=" ", ctc="dialogueAdvance", ctc_position="nestled")
define dw = Character('Dr. Windham', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define k = Character('Kevin', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define ka = Character('Kana', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define j = Character('Jeff', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define c = Character('Christina', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define s = Character('Stephanie', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define t = Character('Tony', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define r = Character('Robot Overlord', who_alt="The Robot Overlord", ctc="dialogueAdvance", ctc_position="nestled", what_font="Quantico-Bold.ttf", what_alt="says, [text]")
define d = Character('Director', who_alt="The Director", ctc="dialogueAdvance", ctc_position="nestled", what_alt="shouts, [text]")
define cm = Character('Crew Member', who_alt="A crew member", ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define e = Character('Everyone', ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define l = Character('Chat Librarian', who_alt="The Chat Librarian", ctc="dialogueAdvance", ctc_position="nestled", what_alt="types, [text]")

#used in choices so that self-voicing doesn't speak "[person] says" and instead offers the helpful "Choose a response"
#format is charAbbrev + c (stands for 'choice')
define tuc = Character('Tutorial', ctc="dialogueAdvance", ctc_position="nestled", who_alt="Choose a response")
define dwc = Character('Dr. Windham', ctc="dialogueAdvance", ctc_position="nestled", who_alt="Choose a response")
define kc = Character('Kevin', ctc="dialogueAdvance", ctc_position="nestled", who_alt="Choose a response")
define jc = Character('Jeff', ctc="dialogueAdvance", ctc_position="nestled", who_alt="Choose a response")
define sc = Character('Stephanie', ctc="dialogueAdvance", ctc_position="nestled", who_alt="Choose a response")


#This is the unknown character, before he or she has been introduced
define ul = Character('Librarian', who_alt="The Librarian", ctc="dialogueAdvance", ctc_position="nestled", what_alt="says, [text]")
define un = Character('???', who_alt="unknown speaker", color="#000",ctc="dialogueAdvance", ctc_position="nestled", what_alt="says [text]")

#chatterbox characters and window, text styling
#Kana
define cbkana = Character(None, window_background="imgs/ui/kanachatterbox.png", window_yminimum=249, window_ypos=0.55, window_left_padding=430, window_right_padding=340, window_top_padding=66, what_font="SourceSansPro-Regular.ttf", what_color="#323232", what_size=24, what_style="say_chatterbox", slow=False)
#Kevin
define cbkevin = Character(None, window_background="imgs/ui/kevinchatterbox.png", window_yminimum=249, window_ypos=0.55, window_left_padding=430, window_right_padding=340, window_top_padding=66, what_font="SourceSansPro-Regular.ttf", what_color="#323232", what_size=24, what_style="say_chatterbox", slow=False)
#Player
define cbkme = Character(None, window_background="imgs/ui/playerchatterbox.png", window_yminimum=249, window_ypos=0.55, window_left_padding=430, window_right_padding=340, window_top_padding=66, what_font="SourceSansPro-Regular.ttf", what_color="#323232", what_size=24, what_style="say_chatterbox", slow=False)


#######################################
## The game starts here.
label start:
    
    #initialies all variables for player choices/passwords/etc.
    call setupGameVariables from _call_setupGameVariables_6

    #Set the scene for the Beginning of the Game:
    scene bg genericCampus with fade
    
    #Player enters name here (used by other characters and in menus)
    $ noNameMatch = True
    $ name = renpy.input("Please enter your first name (Example: Sarah) and press “Enter”", length=15)
    $ name = name.strip()
    jump validateName

label validateName:

    if name == "Kevin" or name == "Tony" or name == "Jeff" or name == "Kana" or name == "Stephanie" or name == "Christina":
        $ noNameMatch = False
        "To avoid confusion with another character in the game, please enter a nickname, or your first name and the first letter of your last name."
        $ name = renpy.input("Please enter a nickname, or first name and last initial (Example: Jeff M.) and press “Enter”", length=15)
        $ name = name.strip()
        jump validateName

    elif name == "":

        "You didn’t enter a name. Please try again."

        if noNameMatch == True:
            $ name = renpy.input("Please enter your first name (Example: Sarah) and press “Enter”", length=15)
            $ name = name.strip()
            jump validateName

        if noNameMatch == False:
            $ name = renpy.input("Please enter a nickname, or first name and last initial (Example: Jeff M.) and press “Enter”", length=15)
            $ name = name.strip()
            jump validateName

    else:
        $ persistent.playerName = name
        jump Tutorial


label setupGameVariables:

    stop music fadeout 2.0
    stop ambient fadeout 2.0
    #Make prefs screen default
    $_game_menu_screen = "preferences"
    
    ###################################
    ## Declare all Game variables.
    
    #Act One Refining Research Questions
    $ done_refining = False
    $ societyAttitudes_asked = False
    $ soccerSouth_asked = False
    $ soccerOlympics_asked = False
    $ soccerMedia_asked = False
    
    #Act One Ready Reference Questions
    $ done_ready_ref = False
    $ finding_ref = False
    $ what_stuff_ref = False
    $ checkout_ref = False
    $ easier_ref = False
    
    #Act One WrapUp Questions
    $ researchq_yesno = False
    $ researchq_sowhat = False
    $ researchq_opinion = False
    
    #Act Passwords
    $ actOne_pass = "B3MWFJ"
    $ actTwo_pass = "PY7VCX"
    $ actThree_pass = "S3VR6Z"
    $ actFour_pass = "OU6Q2C"
    $ actFive_pass = "LKIV2H"
    $ actSix_pass = "XZA9YG"

    #Act Two Newspapers Questions
    $ newspapers_choice_one_picked = False
    $ newspapers_choice_two_picked = False
    
    #Act Two Book Comparison Questions
    $ done_comparing = False
    $ books_longer_asked = False
    $ books_published_later_asked = False
    
    #Act Two Wrap Up Questions
    $ done_wrapping_up_ActTwo = False
    $ infocycle_asked = False
    $ different_sources_asked = False
    $ popular_scholarly_asked = False
    $ info_source_differences_asked = False

    #Act Three Catalog Record Questions
    $ author_important_asked = False
    $ date_published_asked = False
    $ similar_items_asked = False
    $ call_number_asked = False

    #Act Three Boolean Quiz
    $ boolean_and_right = False
    $ boolean_or_right = False
    $ boolean_not_right = False

    #Act Three WrapUp Questions
    $ first_chat = True
    $ chat_crap_asked = False
    $ chat_scholarly_asked = False
    $ chat_keywords_asked = False
    $ chat_galileo_asked = False
    $ chat_subjdbase_asked = False
    $ chat_boolean_asked = False

    #Act Four Types of Plagiarism Questions
    $ style_plagiarism_asked = False
    $ idea_plagiarism_asked = False

    #Act Four WrapUp Questions
    $ paraphrase_asked = False
    $ style_plag_asked = False
    $ idea_plag_asked = False
    $ common_know_asked = False
    $ image_ethics_asked = False
    $ intext_citation_asked =False

    #Act Five Memory Jogging
    $ paraphrase_jogged = False
    $ direct_quote_jogged = False

    #Act Five Visit Order
    $ visited_kana = False
    $ visited_christina = False
    
    #Act Five WrapUp Questions
    $ filter_bubbles_asked = False
    $ social_media_lit_asked = False
    $ reading_text_asked = False
    $ integrating_sources_asked = False

    #Act Six PowerPoint Questions
    $ fonts_are_bad = False
    $ animations_are_bad = False
    $ colors_are_bad = False

    return
    