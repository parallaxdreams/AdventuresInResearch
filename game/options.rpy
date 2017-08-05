##
## Adventures in Research (2012-2017)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

##########################################################################

## Alpha Hex Chart
## percent decimal hex
##     0%       0  00
##     5%      12  0c
##    10%      25  19
##    15%      38  26
##    20%      51  33
##    25%      63  3f
##    30%      76  4c
##    35%      89  59
##    40%     102  66
##    45%     114  72
##    50%     127  7f
##    55%     140  8c
##    60%     153  99
##    65%     165  a5
##    70%     178  b2
##    75%     191  bf
##    80%     204  cc
##    85%     216  d8
##    90%     229  e5
##    95%     242  f2
##   100%     255  ff


init -1:
    #Custom Style for Chatterbox
    $ style.create("say_chatterbox", "say_dialogue")

    #Update KeyBindings
    $ config.keymap['rollback'].append('K_LEFT')
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['rollforward'].append('K_RIGHT')
    $ config.keymap['rollforward'].remove('mousedown_5')
    $ config.keymap['game_menu'].remove('mouseup_3')


init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True
    config.console = True

    ## These control the width and height of the screen.

    config.screen_width = 1280
    config.screen_height = 720

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Adventures in Research!"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Adventures in Research"
    config.version = "1.8.2"


    config.thumbnail_width = 375
    config.thumbnail_height = 211


    # Game Icon
    config.window_icon = "Icon.png"
    config.windows_icon = "icon_32x32.png"

    #Autosave Frequency
    config.autosave_frequency = 20

    #Testing Saves
    #config.save_dump = True

    #########################################
    ## Sound Channels

    ## Custom channel for sound effects that don't loop (Achievements, etc.)
    renpy.music.register_channel("sndfx", "sfx", False)

    ## Custom channel for ambient sounds that do loop
    renpy.music.register_channel("ambient", "sfx", loop=True, tight=True)
     
    
    
    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.threeD(
        ## Theme: 3D
        ## Color scheme: Basic Blue
                                    
        ## The color of an idle widget face.
        widget = "#ffffff",

        ## The color of a focused widget face.
        widget_hover = "#fdff4b",

        ## The color of the text in a widget.
        widget_text = "#ffffff",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#fdff4bff",

        ## The color of a disabled widget face. 
        disabled = "#404040",

        ## The color of disabled widget text.
        disabled_text = "#888888",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#000000b2",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#dcebff",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#5a5a5a00",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    # style.window.background = Frame("frame.png", 12, 12)
    style.window.background = "imgs/ui/dialoguebox.png"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 108
    style.window.right_padding = 110
    style.window.top_padding = 0
    style.window.bottom_padding = 0

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 277


    ########################################
    ## Character Name Label font and placement
    
    style.say_label.font = "SourceSansPro-Bold.ttf"
    style.say_label.color = "#1a1a1a"
    style.say_label.bold = False
    style.say_label.size = 32
    style.say_label.xpos = 5
    style.say_label.ypos = 35
    style.say_label.outlines = [(1, "#fce428", 0, 1)]
    
    
    #########################################
    ## Character Dialogue font and placement
    
    style.say_dialogue.font = "SourceSansPro-Semibold.ttf"
    style.say_dialogue.bold = False
    style.say_dialogue.color = "#f0f0f0"
    style.say_dialogue.size = 30
    style.say_dialogue.ypos = 40
    style.say_dialogue.outlines = [(1, "#0d0d0d", 0, 0)]#,(0, "#000000d8", 2, 2)]
    
    style.hyperlink_text.font = "SourceSansPro-Semibold.ttf"
    style.hyperlink_text.bold = False
    style.hyperlink_text.color = "#ff8330"
    style.hyperlink_text.size = 30
    style.hyperlink_text.underline = False
    style.hyperlink_text.hover_underline = True

    style.say_chatterbox.outlines = [(0, "#00000000", 0, 0),(0, "#00000000", 0, 0)]


    #########################################
    ##Non-attributable Generic Text

    style.say_thought.font = "SourceSansPro-Semibold.ttf"
    style.say_thought.bold = False
    style.say_thought.color = "#f0f0f0"
    style.say_thought.size = 30
    style.say_thought.ypos = 90
    style.say_thought.outlines = [(1, "#00000066", 0, 0),(0, "#000000d8", 2, 2)]
   
    ########################################
    ## Text Box Input Style
    
    style.input.font = "SourceSansPro-Bold.ttf"
    style.input.size = 31
    style.input.color = "#f2d927"
    style.input.ypos = 92
    style.input.xpos = 0
    style.input.caret = "inputCaret"
    style.input_window.yalign = 0.0 

    style.text.color = "#f0f0f0"
    style.text.size = 30
    style.text.font = "SourceSansPro-Semibold.ttf"
    style.text.ypos = 90

    #########################################
    ## Menu Choice Button Style
    
    style.menu_window.bottom_margin = 180
    style.menu_window.top_padding = 15
    style.menu_window.bottom_padding = 15
    style.menu_window.left_padding = 146
    style.menu_window.right_padding = 0
    style.menu_window.xmargin = 0
    style.menu_choice_button.xmaximum = 1280
    style.menu_choice_button.xminimum = 1280
    style.menu_window.background = Frame("imgs/ui/menu_frame.png",0,0,tile=True)
    style.menu_choice_button.background = "#00000000"
    style.menu_choice_button.hover_background = "#00000000"
    style.menu_choice_button.ypadding = 8
    style.menu_choice_button.right_padding = 20
    style.menu_choice_button.xmargin = 0
    
    style.menu_choice.xalign = 0.0
    style.menu_choice.line_spacing = 0
    style.menu_choice.text_align = 0.0
    style.menu_choice.rest_indent = 20
    style.menu_choice.font = "SourceSansPro-Semibold.ttf"
    style.menu_choice.outlines = [(1, "#0d0d0d", 0, 0)]
    style.menu_choice.size = 27
    style.menu_choice.color = "#f0f0f0"
    style.menu_choice.hover_color = "#fff200"
    style.menu_choice.hover_outlines = [(1, "#423109", 0, 0)]
    #Trying to add hover bullets
    #style.menu_choice.hover_background = Image("imgs/ui/choice_icon.png",yalign=0.5)


    



    #########################################
    ## Customize appearance of menu buttons that appear in other menu screeens.

    style.pref_frame.background = "#363636"

    style.pref_button_text.font = "SourceSansPro-Semibold.ttf"
    style.pref_button_text.size = 28
    style.pref_button_text.hover_color = "#000000"

    style.pref_button.background = "#000000"
    style.pref_button.hover_background = "#fdff4b"

    style.pref_label_text.font = "SourceSansPro-Semibold.ttf"
    style.pref_label_text.size = 28

    
    style.file_picker_frame.background = "#00000000"

    style.yesno_label_text.font = "SourceSansPro-Bold.ttf"
    style.yesno_label_text.color = "#f0f0f0"
    style.yesno_label_text.size = 32
    style.yesno_label_text.outlines = [(1, "#333333", 0, 0)]
    style.yesno_button.ypadding = 8
    style.yesno_button.xpadding = 50
    style.yesno_button.background = "#00000019"
    style.yesno_button.hover_background = "#00000019"
    style.yesno_button_text.font = "SourceSansPro-Bold.ttf"
    style.yesno_button_text.size = 30
    style.yesno_button_text.outlines = [(1, "#333333", 0, 0)]
    style.yesno_button_text.color = "#f0f0f0"
    style.yesno_button_text.hover_color = "#fff200"
    style.yesno_button_text.hover_outlines = [(1, "#504700", 0, 0)]
    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # style.default.font = "DejaVuSans.ttf"

    ## The default size of text.

    # style.default.size = 22

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/Opener.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "Help.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = fade

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:

    #Custom Location for Saves
    config.savedir = renpy.config.renpy_base + "/saves"
    
    #Default Value For Saves
    #config.save_directory = "LIBR2100 Game-1345493192"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 36

    #########################################
    ## More customizations can go here.
    
    

                         
## This section contains information about how to build your project into 
## distribution files.
init python:

    #use for generating build folder / Delete for Final Release
    import datetime

    show_date = datetime.datetime.now().strftime('%Y%m%d')

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    #build.directory_name = "libr2100game-" + "v" + config.version + "-" + show_date
    build.directory_name = "libr2100game-" + "v" + config.version
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "libr2100game"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('LICENSE.txt', None)
    build.classify('README.txt', None)
    
    ## To archive files, classify them as 'archive'.
    
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ttf', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('fonts/*.txt')
    
