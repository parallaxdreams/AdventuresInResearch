##
## Adventures in Research (2012-2017)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActSix:
    call setupGameVariables from _call_setupGameVariables_5
    $ name = persistent.playerName
    jump ActSix

label ActSix:

    $ save_name = "Name: %s.\nScene: Act 6." % (name)

    if not persistent.ActSix_unlocked:
       $ persistent.ActSix_unlocked = True

    scene bg blackSolid with fade
    scene bg ActSix with None
    $ renpy.pause(3.0)

    scene bg calendar with fade

    show calendar backing:
        xpos 0
        ypos 0
    
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -7.72
        pause 1.0
        ease 1.00 xpos -8.978
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(4.0)

    scene bg classroom with fade
    $ save_name = "Name: %s.\nScene: Act 6 – Classroom." % (name)
    play music "music/Classroom.ogg"
    show kevin neutral at right
    show jeff neutral at left
    with qdissolve

    sv "You arrive for the final session of Dr. Windham’s class."
    sv "There’s a sense of nervousness in the air as everyone waits for the presentations to begin."

    k "Wow, I can’t believe it’s finally presentation day."

    j "I know, I feel like we’ve been working on this project forever."

    menu:

        jc "I know, I feel like we’ve been working on this project forever.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I can’t believe I’m saying this, but it was kind of interesting to do this research project.":
            k "I agree. I’m glad to finally have it done though."
            jump ActSixContinues

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I’m glad to finally have it done.":
            k "Me too. I can’t believe I’m saying this, but it was kind of interesting to do this research project."
            jump ActSixContinues

label ActSixContinues:
    show jeff concerned
    with qdissolve
    j "Are you two ready? Were you up all night preparing?"

    k "I know I was. All my research was done, I was just putting the finishing touches on my presentation."

    show jeff neutral
    with qdissolve
    j "Me too. I just got so afraid that I would forget everything I wanted to say so I practiced over and over."

    show kevin happy
    with qdissolve
    k "I’m not worried about that, I put most of the stuff I wanted to say on my slides."

    menu:

        kc "I’m not worried about that, I put most of the stuff I wanted to say on my slides.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} You might want to rethink that.":
            show kevin concerned
            with qdissolve
            k "Why?"
            jump slideText

        "{font=SourceSansPro-Bold.ttf}Say:{/font} That’s a good idea.":
            j "Actually, you might want to rethink that, Kevin."
            show kevin concerned
            with qdissolve
            k "Why?"
            jump slideText

label slideText:

    j "Well all that text on the slide is distracting. Not to mention boring."

    show kevin neutral
    with qdissolve
    k "Let me guess, you got some presentation tips in your LIBR 21OO class."

    show jeff happy
    with qdissolve
    j "What can I say? It was a really helpful experience!"

    show kevin concerned
    with qdissolve
    k "Do you get a fee for promoting that class?"

    j "Knowledge is its own reward, Kevin."

    show kevin neutral
    with qdissolve
    k "Right..."

    show jeff neutral
    with qdissolve
    j "There’s Kana and Christina over there."
    j "If you don’t believe me, you should ask Kana. She’s an artist, she probably has some helpful advice in putting together a nice visual presentation."

    j "Hey Kana! Hey Christina."
    
    show jeff happy at Position(xpos=0.13, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show kevin happy at Position(xpos=0.87, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show christina happy at Position(xpos=0.46, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show kana happy at Position(xpos=0.60, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve
    ka "Hey, Jeff. Are you all ready for the presentation today?"

    show jeff neutral
    with qdissolve
    j "More or less. I was just talking to Kevin about putting presentations together."

    show christina neutral
    with qdissolve
    c "I hope you told him to stay away from PowerPoint Karaoke."

    menu:

        cc "I hope you told him to stay away from PowerPoint Karaoke.{fast}"

        "{font=SourceSansPro-Bold.ttf}Ask:{/font} PowerPoint Karaoke? What is that?":
            j "It’s when you read all of the text right off your PowerPoint slide."
            jump PowerPointKaraoke

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Is that like, reading all the text right off your PowerPoint slide?":
            j "Right."
            jump PowerPointKaraoke

label PowerPointKaraoke:

    show kana neutral 
    with qdissolve
    ka "All that text is too much for your audience to read. Besides, they can’t listen to you and read your slides at the same time."
    ka "The brain just doesn’t work that way. It’s better to stick to images that help the viewer process what you are saying."

    show jeff concerned
    with qdissolve
    j "Not to mention, reading directly from a slide means you will have your back to the audience."

    show kevin confused
    with qdissolve
    k "I guess that makes sense."
    k "I know it’s a lot to ask because we are all about to present, but I don’t suppose you guys would mind looking over my presentation to give me some feedback?"

    show kana happy
    with qdissolve
    ka "I don’t mind at all! We’ve got a little time before our presentations begin."

    show jeff happy
    with qdissolve
    j "Fine with me, it will take my mind off my own presentation!"

    show kevin neutral
    with qdissolve
    k "Here, let me bring up my presentation on my laptop."
    k "Here it is."

    show jeff neutral
    show kana neutral
    with qdissolve
    j "Title page looks good, the title of your research project hints at what your presentation is going to be about."

    ka "I like that you added that image of a video game with a machine gun. It’s a little goofy, but it sets a mood for your presentation."

    show kevin concerned
    with qdissolve
    k "You think it’s goofy? I thought it was pretty epic..."

    show kana happy
    with qdissolve
    ka "Oh! Well, yeah! It is totally epic!"
    show kevin happy
    show kana neutral
    with qdissolve
    ka "Anyway, let’s see what’s on your first slide."

    show kana confused
    with qdissolve
    ka "Yeah, this whole slide is just one big block of text. That’s too much."

    show kevin concerned
    with qdissolve
    k "Can I just split up the text into two or three slides?"

    menu:

        kc "Can I just split up the text into two or three slides?{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} It is still too much to read, even over a few slides.":
            ka "I agree."
            jump moreSlideCritiques

        "{font=SourceSansPro-Bold.ttf}Say:{/font} That might be a good solution!":
            ka "I disagree. It is still too much to read, even over a few slides."
            jump moreSlideCritiques

label moreSlideCritiques:
    show jeff concerned
    with qdissolve
    j "Sorry Kev, I think that you need to take the text from these slides and make some speaking notes."

    show tony neutralright at Position(xpos=0.30, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve
    sv "Tony walks over and joins the group."
    t "Hey guys, how’s it going?"

    show kevin neutral
    show kana neutral
    show jeff neutral
    with qdissolve

    show christina happy
    with qdissolve
    c "Hey Tony. Just helping Kev with his presentation."

    show christina neutral
    with qdissolve
    c "We were talking about taking text off of your PowerPoint and using that text in your speaking notes instead."

    t "That’s a good point. Just be careful not to read all of your notes from the paper. I had a professor who would just read all of his lectures, it was so boring."

    k "I guess that’s true. I don’t imagine I’d get a very good grade if I did that either."

    t "Probably not."
    show tony confusedright
    with qdissolve
    t "If you think about it, just reading something is not really presenting. You aren’t showing that you’ve synthesized anything."

    show kevin concerned
    with qdissolve
    k "I can still have some text on there, though, right?"
    show tony neutralright
    with qdissolve
    j "Yeah. Maybe to quickly sum up a main point?"

    show kevin surprised
    with qdissolve
    k "I’m just freaking out, though—without that information somewhere, I’m worried I’m gonna lose my place."

    menu:

        kc "I’m just freaking out, though—without that information somewhere, I’m worried I’m gonna lose my place.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Well that is where preparation comes in.":
            j "If you know a good amount about your topic, you will not need so many of the textual clues."
            jump yetMoreSlideCritiques

        "{font=SourceSansPro-Bold.ttf}Say:{/font} If you know a good amount about your topic, you won’t need so many of those textual clues.":
            j "Right, preparation can help a lot to make sure you stay on track."
            jump yetMoreSlideCritiques

label yetMoreSlideCritiques:

    j "Also, those bulleted lists you have on several of your slides? Ditch them. They’re keeping your thoughts organized, but that helps you—not your audience."

    show kevin neutral
    with qdissolve
    k "Really?"

    j "Yeah, your audience doesn’t have any context for why those items are in a list."

    show kana happy
    with qdissolve
    ka "Images can help too. They are great ways to engage the audience but they can also keep you organized without cluttering up your slide."

    k "Unless you clutter up your slide with images."

    show kana neutral
    with qdissolve
    ka "Right. Don’t do that either. Choose maybe one image a slide and stick with it."
    ka "Don’t be afraid to have the image take up the whole slide. It’s all about the impact you want it to have on the audience."

    k "Okay, so I’ll take most of this text off."
    k "Anything else?"

    jump reviewingSlidesWithKevin


label reviewingSlidesWithKevin:

    if fonts_are_bad == animations_are_bad == colors_are_bad == True:
        if not persistent.achievement_power_pointers_unlocked:
            $ persistent.achievement_power_pointers_unlocked = True
            show achievement powerPointers:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
            sv "You just unlocked the “Power Pointers” achievement."
        jump NotTooBad

    else:

        menu:

            kc "Anything else?{fast}"

            "{font=SourceSansPro-Bold.ttf}Say:{/font} Make sure your font is consistent throughout, and clear enough to read." if fonts_are_bad == False:
                $ fonts_are_bad = True
                show kevin happy
                with qdissolve
                k "Good point! I’m switching between Times New Roman and Arial, I didn’t even notice."
                show kevin neutral
                with qdissolve
                k "Anything else?"
                jump reviewingSlidesWithKevin

            "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Maybe take those animations away?" if animations_are_bad == False:
                $ animations_are_bad = True
                show kevin concerned
                with qdissolve
                k "Really?"
                show kevin happy
                with qdissolve
                k "I thought that having each slide explode like a firework made it seem exciting!"
                m "It is kinda cheesy, buddy. Sorry."
                show kevin neutral
                with qdissolve
                k "Fair enough."
                k "Anything else?"
                jump reviewingSlidesWithKevin

            "{font=SourceSansPro-Bold.ttf}Say:{/font} I can’t really see that bright yellow text on your white background." if colors_are_bad == False:
                $ colors_are_bad = True
                show kevin surprised
                with qdissolve
                k "Yikes, yeah. I’ll just make that text black."
                m "That’s much better."
                show kevin confused
                with qdissolve
                k "Maybe I should have tried one of the templates."
                show kana concerned
                with qdissolve
                ka "Actually, the templates in PowerPoint aren’t very good."
                show kevin concerned
                with qdissolve
                k "Really?"
                show kana confused
                with qdissolve
                ka "Yeah, the designs of the templates aren’t based on any best practices of how to visually present information."
                show kana neutral
                with qdissolve
                ka "Stick to the basics, like black text on a white background, or white text on a black background."
                k "No color?"
                ka "I’ve been learning about color theory for years—it’s not easy."
                ka "Don’t be afraid to stick to the simpler choices."
                show kana happy
                with qdissolve
                ka "In the end, it’s all about contrast and making the content on your slides easy to read."
                show kevin happy
                with qdissolve
                k "Wow, thanks. I just thought I had to be creative with my slides, or the professor would think I was being lazy."
                show kana neutral
                show kevin neutral
                with qdissolve
                k "Anything else?"
                jump reviewingSlidesWithKevin

            "{font=SourceSansPro-Bold.ttf}Say:{/font} I think that’s it." if fonts_are_bad == True or animations_are_bad == True or colors_are_bad == True:
                jump NotTooBad


label NotTooBad:

    m "Overall it’s really not that bad."

    show kana happy
    with qdissolve
    ka "Right! Those were just some suggestions to make it more engaging."

    j "I’m sure with you presenting it will be entertaining either way."

    show kevin happy
    with qdissolve
    k "I’m going to take that as a compliment!"

    show jeff happy
    with qdissolve
    j "You should!"

    show windham neutrallarge at Position(xpos=0.71, xanchor=0.5, ypos=0.57, yanchor=0.5)
    show kevin neutral
    show kana neutral
    show jeff neutral
    with qdissolve
    dw "Hi class! Go ahead and take your seats, we are gonna get started pretty soon."
    dw "I’ll give you all a second to get your materials together and then we’ll pick the order in which you all will present."

    hide windham
    with qdissolve
    k "Let’s see, changed the font, took the bullets away, deleted all that unneeded text...I think I’m ready to go!"

    show kevin happy
    with qdissolve
    k "Thank you all for your help!"

    show kana happy
    with qdissolve
    ka "No problem."
    ka "You guys want to meet after class for a post presentation coffee?"

    show christina happy
    with qdissolve
    c "Sounds good."

    show jeff happy
    with qdissolve
    j "Sure."

    t "Count me in."

    k "We can celebrate how we all totally rocked this presentation’s face off."

    menu:

        kc "We can celebrate how we all totally rocked this presentation’s face off.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Kevin, don’t ever change.":
            jump WindhamsAnnouncement

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Better than drinking our sorrows away!":
            jump WindhamsAnnouncement

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Here’s hoping...":
            jump WindhamsAnnouncement


label WindhamsAnnouncement:
    hide tony
    hide kevin
    hide kana
    hide christina
    hide jeff
    with qdissolve
    show windham neutral at center
    with qdissolve
    dw "Alright everyone. I’m going to pick names out of this hat to see who goes first."
    show windham happy
    with qdissolve
    dw "You all ready to go?"

    menu:

        dwc "You all ready to go?{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} As we’ll ever be":
            jump pickingTheOrder

        "{font=SourceSansPro-Bold.ttf}Say:{/font} We don’t have much choice, so...I guess.":
            jump pickingTheOrder

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Let’s do this!":
            jump pickingTheOrder

label pickingTheOrder:

    dw "Alright then!"
    dw "Let’s see, the first five to present are..............."
    dw "[name!q], Christina, Alex, Tony, and Terrius."
    dw "Looks like you are up first, [name!q]!"
    hide windham
    with qdissolve

    show tony happyright at center
    with qdissolve
    t "Good luck!"
    hide tony
    with qdissolve

    show christina happy at center
    with qdissolve
    c "Thanks for all your help this semester!"
    c "Break a leg!"
    hide christina
    with qdissolve

    show kana happy at center
    with qdissolve
    ka "You are gonna do great, [name!q]!"
    hide kana
    with qdissolve

    show jeff happy at center
    with qdissolve
    j "You got this!"
    hide jeff
    with qdissolve

    show kevin happy at center
    with qdissolve
    k "As a wise woman once said, “It is a truth universally acknowledged that someone as awesome as you is gonna give a great presentation.”"
    k "Rock it out!"
    hide kevin
    with qdissolve

    if not persistent.achievement_actSix_complete_unlocked:
        $ persistent.achievement_actSix_complete_unlocked = True
        show achievement actSixComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
        sv "You just unlocked the “Act Six Completed” achievement."
    m "Thanks everyone!"
    m "Here goes nothing....."

    sv "You walk to the front of the room to give your presentation."
    sv "You have completed the game."
    stop music fadeout 0.8
    jump EndCredits

label EndCredits:
###Ending Credits Go Here#####
    $config.skipping = None
    $config.rollback_enabled = False
    $_game_menu_screen = None
    scene bg blackSolid with fade
    show endSlideShow
    play music "music/Opener.ogg"
    $ save_name = "Name: %s.\nScene: End Credits." % (name)
    if not persistent.achievement_allActs_complete_unlocked:
        $ persistent.achievement_allActs_complete_unlocked = True
        show achievement allActsComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
    show EndCredits:
        ypos 420
        xalign 0.0
        linear 85 ypos -3250

    $ renpy.pause (89.0, hard=True)
    $ config.rollback_enabled = True
    $_game_menu_screen = "preferences"
    $ renpy.full_restart()
