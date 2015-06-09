##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActFive:
    call setupGameVariables from _call_setupGameVariables_2
    $ name = persistent.playerName
    jump ActFive

label ActFive:

    $ save_name = "Name: %s.\nScene: Act 5." % (name)

    if not persistent.ActFive_unlocked:
       $ persistent.ActFive_unlocked = True

    scene bg blackSolid with fade
    scene bg ActFive with None
    $ renpy.pause(3.0)

    scene bg calendar with fade

    show calendar backing:
        xpos 0
        ypos 0
    
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -5.225
        pause 1.0
        ease 1.50 xpos -7.72
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(5.8)
    
    scene bg festival with fade
    play ambient "sfx/festival-ambient.ogg" fadein 0.8
    $ save_name = "Name: %s.\nScene: Act 5 – The Festival." % (name)
    show jeff neutral at leftmid
    with qdissolve

    show kevin confused at rightmid
    with qdissolve

    play music "music/Festival.ogg"

    sv "Jeff, Kevin, and you walk over to the Climate Change a Palooza event happening on campus."
    sv "A variety of booths with climate-related themes are set up around the festival."

    k "So this is Climate Change a Palooza, huh?"
    
    show jeff concerned
    with qdissolve
    j "What gave it away? The people in lightbulb costumes? The pictures of polar bears drifting away on ice floes?"
    
    show kevin neutral
    with qdissolve
    k "Actually it was the big sign that said “Climate Change a Palooza”."
    
    show jeff neutral
    with qdissolve
    j "Right. Well it looks like Kana and Christina put in a lot of work for this event."

    m "I know, there’s a lot going on. Where should we begin?"

    j "Well, I see Christina over there working a game. And Kana’s on the other side of Love Valley working a different game."
    j "Where do you want to start, [name!q]?"

    menu:

        jc "Where do you want to start, [name!q]?{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Let’s visit Kana first":
            $ visited_kana = True
            j "Okay, let’s go."
            jump visitKana

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Let’s visit Christina first":
            $ visited_christina = True
            j "Okay, let’s go."
            jump visitChristina

label visitKana:

    #scene bg blackSolid with AlphaDissolve("biWipe", delay=0.25)

    scene bg festival with fade

    show kana neutral at Position(xpos=0.62, xanchor=0.5, ypos=0.5, yanchor=0.5)
    #with Dissolve(0.05)

    #$ renpy.pause(0.2)

    show kevin happy at Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show jeff neutral at Position(xpos=0.32, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve

    sv "You walk through the festival to Kana’s booth."

    k "Hi Kana!"

    show kana happy
    with qdissolve
    ka "Hi everyone! I’m glad you all could make it!"

    m "Of course! What’s going on behind you there? Is that a game?"

    show kana neutral
    with qdissolve
    ka "Yeah! You want to play?"

    m "Sure, what are the rules?"

    show kevin neutral
    with qdissolve
    ka "Well the point of the game is to take this fishing pole and fish the little people out of the water."

    show jeff surprised
    with qdissolve
    j "So, we are trying to make sure the people don’t drown?"

    ka "Right! They got washed out because of the rising sea levels."

    show kevin concerned
    with qdissolve
    k "This is a really depressing game."

    show kana happy
    with qdissolve
    ka "Well that’s kinda the point!"
    show kana neutral
    with qdissolve
    ka "We have this fun event, but we want to make sure everyone understands that climate change has real consequences."

    show jeff neutral
    with qdissolve

    show kevin confused
    with qdissolve
    k "But does it really? I don’t know. I’ve been checking out my Chatterbox and I’ve got a lot of friends who are saying that climate change is a hoax."

    show kana confused
    with qdissolve
    show jeff confused
    with qdissolve
    j "What proof do they have?"

    k "Hmm...I don’t really remember. They mentioned something about how it doesn’t make sense that there are still blizzards and stuff if global warming was real."
    
    show jeff concerned
    with qdissolve
    j "Well, did you try to do some research to see if what they said was true?"

    show kevin neutral
    with qdissolve
    k "I didn’t take LIBR 11O1 or anything but I’m not a dummy."

    show jeff neutral
    with qdissolve
    k "I Googled “Is global warming a hoax?” and a lot of my results were websites that said that it was."

    show kana neutral
    with qdissolve
    ka "I actually did quite a bit of research into the effects of global warming for these banners too. Not just Google though, I looked up scholarly information too."
    ka "For some people, climate change is a controversial topic but not really for scientists."

    show kevin confused
    with qdissolve
    k "Does that mean that Google is always wrong? Why would I have gotten so many results that said climate change was fake?"

    j "You were probably in a filter bubble." #link to TED talk

    show kevin concerned
    with qdissolve
    k "I think I would know if I was in a bubble, Jeff."

    show jeff confused
    with qdissolve
    j "It’s not a real bubble, Kevin."
    j "Eli Pariser created the term “filter bubble” to describe what happens when services like Google and Facebook try to tailor your online experiences based off things like other searches you’ve done and where you live."

    show kevin happy
    with qdissolve
    k "What’s wrong with that? It sounds kinda awesome."


    menu:

        kc "What’s wrong with that? It sounds kinda awesome.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I agree, filter bubbles sounds like a natural evolution of the technology. I think it’s great.":
            show jeff neutral
            with qdissolve
            j "Well it is nice in some respects, I guess. The more it filters out other information, the better chance you get results that are relevant to what you want."
            j "The problem is that sometimes it filters out information that contradicts your beliefs or interests but which you need in order to cover your bases."
            jump postFilterBubbleWorld

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I can see why it is a problem.":
            show jeff neutral
            with qdissolve
            m "It is nice in some respects, but the more it filters out other information, the better chance you get results that are relevant to what you want."
            m "The problem is that sometimes it filters out information that contradicts your beliefs or interests but which you need in order to cover your bases."
            jump postFilterBubbleWorld


label postFilterBubbleWorld:

    show kevin neutral
    with qdissolve
    k "Well, that makes sense. I guess you shouldn’t believe everything you read?"

    #show kana happy
    #with qdissolve
    j "That’s probably smart. Remember when we talked about evaluating those websites for research?"
    show kana neutral
    with qdissolve
    ka "You want to evaluate things you read in your everyday life too. Same idea."

    show jeff happy
    with qdissolve
    j "Especially things you read on social media."

    show jeff concerned
    with qdissolve
    j "Think about it, people post news articles or opinions on Facebook or Twitter or Chatterbox because those are things that they have some kind of reaction to—either they really agree with something or really disagree with something."
    j "Either way, there is a good chance that you are starting out with biased information."

    ka "In LIBR 11O1 we talked about it in the context of something called “social media literacy”."

    show kevin concerned
    with qdissolve
    k "Does that mean like, knowing how to find places like Facebook, Twitter, or Chatterbox?"
    k "How to log on, how to find friends, stuff like that?"

    show jeff confused
    with qdissolve
    j "Not really, it is more about thinking critically about information that you receive in social media, and also being a conscientious producer of information as well."

    show kevin neutral
    with qdissolve
    k "It is pretty cool the way that social media allows us to sort of share our opinions with the world."

    ka "Social media literacy is about sharing those informed opinions responsibly."

    show kana concerned
    with qdissolve
    ka "Not to mention other things that you always want to keep in mind when you do anything on the internet, like privacy, and personal branding."

    show kevin confused
    with qdissolve
    k "So it’s like that time when I forgot to make private the picture I Photoshopped of me and Emily Dickinson hanging out, and I ended up sharing it with the whole university."

    show kana neutral
    with qdissolve
    ka "I guess so."

    show kana surprised
    with qdissolve
    ka "Wait, what?"

    k "Ugh, it was so embarrassing. My Photoshopping skills were made fun of for weeks."

    show jeff concerned
    with qdissolve
    j "I don’t know that people were making fun of your Photoshopping skills, Kevin."

    show kevin concerned
    with qdissolve
    k "What else could it be?"

    show jeff surprised
    with qdissolve
    j "Umm...nothing. People can be jerks."
    show kana neutral
    show jeff neutral
    with qdissolve
    j "It’s not just jerks you have to look out for, though, you also want to keep in mind that potential employers, family members, and even your professors can see stuff that you post online."

    show kevin neutral
    with qdissolve
    k "That’s true. Most of the time I don’t even think about privacy when I post things online. I guess I should be more careful."

    menu:

        kc "That’s true. Most of the time I don’t even think about privacy when I post things online. I guess I should be more careful.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Honestly, I’m not sure this social media literacy stuff is that important. Don’t you have to just trust that when people post things online that they’ve checked out their information? All my Facebook, Twitter, and Chatterbox friends are really smart, I think I’m just going to believe them when they tell me things.":
            show jeff surprised
            show kana surprised
            show kevin surprised
            with qdissolve
            stop music fadeout 0.8
            stop ambient fadeout 0.8
            jump undergroundBunker

        "{font=SourceSansPro-Bold.ttf}Say:{/font} This was a really useful conversation!":
            m "We keep talking about evaluating sources, but I think I have a better idea now of what an important part of the process it really is!"
            m "And, for that matter, that it is something we need to do outside of the classroom too."
            jump thanksKana

label undergroundBunker:
    scene bg blackSolid with fade
    $ save_name = "Name: %s.\nScene: Bad Ending 5." % (name)
    scene bg tenYrsLater with None

    $ renpy.pause(2.0)

    scene bg blackSolid with fade

    scene bg bunker with fade

    play ambient "sfx/bunker-ambient.ogg"
    play music "music/Bunker.ogg"

    sv "You’re sitting in an underground bunker, wearing a hazmat suit. Canned foods line the shelves on the walls, and there are bottles of water on the floor next to you."

    mt "{font=SourceSansPro-SemiboldItalic.ttf}I’m so glad that I listened to my friends on Facebook when they warned everyone that spiders had obtained a nuclear bomb and were about to take over the world.{/font}"
    mt "{font=SourceSansPro-SemiboldItalic.ttf}Sure I had to quit my wildly successful job as an ice cream taster, cut off all ties with friends and family and empty out my savings to build this spider-proof shelter, but it will be worth it after the spider apocalypse is over and I’m the only one left standing.{/font}"
    mt "{font=SourceSansPro-SemiboldItalic.ttf}Granted, it’s been about six months and I really would have expected the bomb to have gone off now. Oh well, I guess I’ll just sit here and keep waiting. Anyway, where was I? “122,321,187 bottles of beer on the wall....”{/font}"
   
    "Game Over"
    if not persistent.achievement_bad_end5_unlocked:
        $ persistent.achievement_bad_end5_unlocked = True
        show achievement badEnd5:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
        sv "You just unlocked the “Bad Ending 5: Hiding in My Bomb Shelter” achievement."

    menu:

        goc "Game Over{fast}"

        "Try Again":
            stop music fadeout 0.8
            stop ambient fadeout 0.8
            jump socialMediaLiteracy

label socialMediaLiteracy:
    
    scene bg festival with fade

    sv "Ten years earlier..."

    play ambient "sfx/festival-ambient.ogg" fadein 0.8
    play music "music/Festival.ogg"
    $ save_name = "Name: %s.\nScene: Act 5 – The Festival." % (name)
    show kana neutral at Position(xpos=0.62, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show kevin neutral at Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show jeff neutral at Position(xpos=0.32, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve

    sv "Back at the festival, Kevin says, That’s true. Most of the time I don’t even think about privacy when I post things online. I guess I should be more careful."

    menu:

        kc "That’s true. Most of the time I don’t even think about privacy when I post things online. I guess I should be more careful.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} This was a really useful conversation!":
            m "We keep talking about evaluating sources, but I think I have a better idea now of what an important part of the process it really is!"
            m "And, for that matter, that it is something we need to do outside of the classroom too."
            jump thanksKana


label thanksKana:

    show kevin happy
    with qdissolve
    k "I agree! Well, thanks for the game, Kana! And the valuable lesson in not believing everything you read!"

    ka "Um, glad to help Kev."
    show kana happy
    with qdissolve
    ka "Thanks for coming to Climate Change a Palooza."
    show kana neutral
    with qdissolve
    ka "Have you guys visited Christina yet?"

    if visited_christina == True:
        menu:

            kac "Have you guys visited Christina yet?{fast}"

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We were just there. Kevin is now a master recycler.":
                show kana happy
                with qdissolve
                ka "I’m glad to hear it. Well I’ve got to get back."
                ka "I’ll see you guys on Monday for the class presentations?"
                show jeff happy
                with qdissolve
                j "Sure thing. See ya!"
                jump actFiveWrapup

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We stopped by there first. She sounds like she’s doing better since the whole...plagiarism thing":
                show kana happy
                with qdissolve
                ka "I’m glad to hear it. Well I’ve got to get back."
                ka "I’ll see you guys on Monday for the class presentations?"
                show jeff happy
                with qdissolve
                j "Sure thing. See ya!"
                jump actFiveWrapup

    else:
        menu:

            kac "Have you guys visited Christina yet?{fast}"

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We are heading over there now.":
                jump headingThereNow
                

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We are going over there now. I trust that we’ll be able to leave these drowning people in your capable hands.":
                jump headingThereNow


label headingThereNow:
    ka "Sounds good. Well I’ve got to get back."
    show kana happy
    with qdissolve
    ka "I’ll see you guys on Monday for the class presentations?"
    show jeff happy
    with qdissolve
    j "Sure thing. See ya!"
    jump visitChristina


label visitChristina:

    #scene bg blackSolid with AlphaDissolve("biWipe", delay=0.25)

    scene bg festival with fade

    show christina neutral at Position(xpos=0.62, xanchor=0.5, ypos=0.5, yanchor=0.5)
    #with Dissolve(0.05)

    #$ renpy.pause(0.2)

    show kevin neutral at Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show jeff neutral at Position(xpos=0.32, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve

    sv "You walk through the festival to Christina’s booth."

    m "Hey Christina!"

    c "What’s up, [name!q]? Jeff? Kevin?"

    show jeff happy
    with qdissolve
    j "Just checking out your event. It looks like it is going pretty well."

    show christina happy
    with qdissolve
    c "It is! We’ve already had a pretty good turn out."

    k "These decorations are pretty entertaining."

    c "Kana had a field day. I think they are pretty fun though."

    m "Definitely. So, what’s the game that you are running? Can we play?"

    c "Sure! Grab some different color beanbags. Each beanbag represents a different kind of recyclable."

    show kevin happy
    with qdissolve
    k "I think I see where this is going. We want to make sure that we throw the right beanbag into the right box."

    c "Exactly. It’s like sorting your recyclables."

    k "That sounds fun! You two mind if I give it a go?"

    j "Go crazy, Kev."
    show jeff neutral
    with qdissolve
    j "So, how have you been doing, Christina?"
    
    show christina neutral
    with qdissolve
    c "Since the whole plagiarism incident, you mean?"
    
    show kevin surprised
    with qdissolve
    ks "Ouch!"
    #JEFF: [Looks at Kevin, concerned]
    show jeff surprised
    with qdissolve

    show kevin confused
    with qdissolve
    k "Oh, sorry. I accidently sorted glass into plastic."

    show jeff confused
    with qdissolve
    j "Okay..."

    c "It’s okay, Jeff. You can ask about it."
    show christina happy
    show jeff neutral
    with qdissolve
    c "I’m doing much better since the whole thing, actually."

    show christina neutral
    with qdissolve

    show kevin neutral
    with qdissolve
    c "I was so paranoid after talking to Dr. Windham and Stephanie that I’ve been really intense about checking my work. Because of that, I actually think my papers are much better."
    c "I’m really sitting down and thinking about what kind of information I need in certain places and how I want to integrate the research that I find."

    show kevin concerned
    with qdissolve
    k "What do you mean, “integrate” research?"

    show christina confused
    with qdissolve
    c "You know, thinking about what you actually need to do with the research once you’ve found it."

    show jeff happy
    with qdissolve
    j "Right, locating information is only the first step."

    show christina neutral
    with qdissolve
    c "I met with Dr. Windham after I talked with Stephanie to get some ideas about how I could do a better job actually using the research that I’ve found."
    c "She mentioned that you want to start by asking yourself questions about the resource. Like, “Does this give me or my reader useful context?”"

    show jeff neutral
    with qdissolve
    j "Or, does the information that I want to use give evidence to support my claim?"

    c "Or, does this argue against the claim I want to make? You want to include that kind of information too."

    k "Wait, why would I want to include information that disagrees with my position? Wouldn’t that hurt my argument rather than help it?"

    c "Well, what makes an argument an argument is that it has more than one side. You choose one side, but your reader might disagree with you."
    c "If you can refute the opposing position then that makes your side, your argument, even stronger. Plus, you don’t want to just cherry pick information."

    show kevin happy
    with qdissolve
    k "Cherry pick? That sounds nice! Like a fun activity for a lazy summer afternoon."

    show christina happy
    with qdissolve
    c "Haha, well it isn’t so nice for research. Cherry picking is when you pick and choose what information you use."
    show kevin neutral
    show christina neutral
    with qdissolve
    c "Usually, it is only choosing information that agrees with you. It is a way to manipulate an argument to make it seem like you are in the right even when you might not be."

    j "Right, even if you don’t do it intentionally, you will still seem like you didn’t do very thorough research. If you do it intentionally, then you are doing incomplete research at best—"

    c "—and bad, dishonest research at worst. I’ve certainly learned my lesson about dishonest research!"

    m "I never thought about it that way."

    c "Dr. Windham said that once you’ve read through the text and decided if it is appropriate, you can incorporate that research into your paper in three ways: quoting, paraphrasing, or summarizing."

    m "Oh yeah, Stephanie talked to us about when we should quote things and when we should paraphrase them."

    show kevin confused
    with qdissolve
    k "Did she? I think I missed that."

    m "You were at practice. Let me see if I can jog my memory..."

    jump memoryJogging

label memoryJogging:

    if paraphrase_jogged == direct_quote_jogged == True:

        jump summarizingThings

    else:

        menu:

            sv "Choose a response"

            "{font=SourceSansPro-Bold.ttf}Say:{/font} You should paraphrase when..." if paraphrase_jogged == False:
                $ paraphrase_jogged = True
                m "You should paraphrase in most situations, when you feel like you can convey the original author’s general idea or intention in your own words."
                c "You still have to cite the original author when you paraphrase though!"
                jump memoryJogging

            "{font=SourceSansPro-Bold.ttf}Say:{/font} You should use a direct quote when..." if direct_quote_jogged == False:
                $ direct_quote_jogged = True
                m "You should use a direct quote when you need the original author’s exact phrasing to fully convey the author’s meaning."
                j "Or if you think they’ve said something in a really useful way."
                jump memoryJogging


label summarizingThings:

    show kevin concerned
    with qdissolve
    k "I see. Did Stephanie say anything about summarizing?"

    c "I don’t think so."
    c "Dr. Windham talked about it though, and mentioned that sometimes you’ll want to try to talk about someone’s overall argument, or larger themes and ideas that an author uses in a work."
    c "Then you sum those things up in a sentence or two."

    m "If you want to sum up a whole work, how would you cite that?"

    c "Well since you aren’t citing a specific page, you would just cite the whole work."
    c "You could say something like, “An overarching theme in {font=SourceSansPro-SemiboldItalic.ttf}The Scarlet Letter{/font} is hypocrisy” or something like that."
    c "You should include {font=SourceSansPro-SemiboldItalic.ttf}The Scarlet Letter{/font} in your works cited page."

    j "You could sum up the argument there and then refer to a specific paragraph or scene or something that illustrates that point—like, “An overarching theme in {font=SourceSansPro-SemiboldItalic.ttf}The Scarlet Letter{/font} is hypocrisy, as shown in the scene where....blah blah blah”"

    k "But you probably wouldn’t write “blah blah blah” though, right?"

    show jeff concerned
    with qdissolve
    j "No, Kevin. That’s probably a bad idea."

    show kevin neutral
    with qdissolve
    k "That’s what I figured. I’m actually pretty glad we stopped by to talk to you Christina, I was feeling a little stressed about what to do with all my awesome resources."
    k "I feel like I have a better idea of how to use my research now. " 

    show jeff neutral
    with qdissolve
    j "Teachers seem to leave that part out sometimes. It’s pretty important!"

    show christina happy
    with qdissolve
    c "It totally is!"
    c "I’m glad you stopped by too, I wanted to thank you guys for being so nice after all that stuff happened."
    show christina neutral
    with qdissolve
    c "Did you see Kana’s here too? You should stop by her booth before you leave, if you haven’t already."

    if visited_kana == True:
        show kevin happy
        with qdissolve
        k "Yeah, we were just over there."
        m "We saved people from drowning at Kana’s booth. We’re heroes."
        show christina happy
        with qdissolve
        c "Good for you! Well I’ve got to get back."
        c "I’ll see you guys on Monday for the class presentations?"
        show jeff happy
        with qdissolve
        j "Sure thing. See ya!"
        jump actFiveWrapup
    
    else:
        menu:

            cc "Did you see Kana’s here too? You should stop by her booth before you leave, if you haven’t already.{fast}"

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We are gonna head over now.":
                jump headingToKana

            "{font=SourceSansPro-Bold.ttf}Say:{/font} I’m not sure she’ll be able to beat sorting recyclables, but we’ll see!":
                jump headingToKana

            "{font=SourceSansPro-Bold.ttf}Say:{/font} We’ll go check it out. Thanks for letting us play!":
                jump headingToKana

label headingToKana:
    c "Cool. Well I’ve got to get back."
    show christina happy
    with qdissolve
    c "I’ll see you guys on Monday for the class presentations?"
    show jeff happy
    with qdissolve
    j "Sure thing. See ya!"
    jump visitKana                

label actFiveWrapup:
    stop music fadeout 0.8
    stop ambient fadeout 0.8
    scene bg genericCampus with fade
    $ save_name = "Name: %s.\nScene: Act 5 – Outside." % (name)

    play ambient "sfx/greenery-ambient.ogg"
    play music "music/Greenery.ogg" fadein 0.8

    show jeff neutral at leftmid
    show kevin neutral at right
    with qdissolve

    sv "After leaving the festival, Kevin, Jeff, and you walk down a sidewalk in a quieter part of campus."

    m "I’m glad we stopped by. It’s nice to do something to take my mind off of that presentation."

    j "I can’t believe we have to give them on Monday. These last couple of weeks have gone by so fast."

    k "I’m glad we started on it early, too. Otherwise I’d be crashing at the library this weekend."

    m "I might end up doing that anyway. I still have a bunch of stuff I need to tweak."

    j "I think that’s probably normal."
    show jeff concerned
    with qdissolve
    j "Don’t make yourself sick about it though."

    m "I won’t. I just put all of this work into it, so I want it to be good."

    show kevin concerned
    with qdissolve
    k "Now you guys are making me nervous about it."

    show jeff neutral
    with qdissolve
    j "I always get nervous about these things. But I tell myself: If you worked hard, and put time into it, that work will show."
    j "I feel pretty good about it, overall."
    show kevin neutral
    with qdissolve
    j "Actually, I found this little outing pretty useful for finishing my proposal."

    m "Really? How so?"

    j "A few different ways. Where should I begin?"

label actFiveWrapUpQuestions:

    if filter_bubbles_asked == social_media_lit_asked == reading_text_asked == integrating_sources_asked == True:
        if not persistent.achievement_critical_thinker_unlocked:
            $ persistent.achievement_critical_thinker_unlocked = True
            show achievement criticalThinker:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
            sv "You just unlocked the “Critical Thinker” achievement."
        jump actFiveWrapUpOver
    
    else:
        menu:

            sv "Choose a response."

            "{font=SourceSansPro-Bold.ttf}Ask:{/font} Kana mentioned something about filter bubbles. What is that again?" if filter_bubbles_asked==False:
                $ filter_bubbles_asked = True
                j "Often when we search places like Google and Facebook our results can be filtered in such a way that we are sometimes presented with information that only confirms our beliefs or shows one side of a story."
                j "This can negatively affect our research, because research involves considering all aspects of a topic and thinking critically about the information we consume."
                j "Anything else?"
                jump actFiveWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}Ask:{/font} Kana talked about social media literacy. What is that again?" if social_media_lit_asked == False:
                $ social_media_lit_asked = True
                j "Social media literacy is all about thinking critically about the information we consume in places like Facebook, Twitter, and Chatterbox."
                j "If we do research based off of things we read in those spaces, or use information we find in social media, we just need to evaluate it the same way we’d evaluate any information we might use in a research project."
                j "Anything else?"
                jump actFiveWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}Ask:{/font} Christina talked about ways to read a particular text. How was that useful?" if reading_text_asked == False:
                $ reading_text_asked = True
                j "Well, we’ve been talking about finding and evaluating resources, and thinking about how to read a particular text is a part of that."
                j "Once we’ve found the source, the next step is to figure out how to use it."
                j "Among other things, you want to think about if your source would give your reader some kind of context or background info that they will need."
                j "You also want to think about if the article is either giving evidence to back up a claim you make, or giving evidence that contradicts your claim."
                j "Anything else?"
                jump actFiveWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}Ask:{/font} How was our discussion of integrating sources useful?" if integrating_sources_asked == False:
                $ integrating_sources_asked = True
                j "It is important because you need to know what to do with the resources once you find them."
                j "You can either quote from them directly to help you make your point, paraphrase something they’ve said if you don’t need to use their exact words to convey their meaning, or you can just summarize an overall argument or a theme."
                j "No matter how you integrate these sources, though, you need to cite."
                j "Anything else?"
                jump actFiveWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t have any more questions." if filter_bubbles_asked == True or social_media_lit_asked == True or reading_text_asked == True or integrating_sources_asked == True:
                jump actFiveWrapUpOver

label actFiveWrapUpOver:

    m "That makes a lot of sense, Jeff. Thanks."

    show jeff happy
    with qdissolve
    j "No problem!"

    k "Well, we should probably head out, I want to get a nap before I head back to the library. Saving lives and recycling is pretty demanding."

    menu:
        kc "Well, we should probably head out, I want to get a nap before I head back to the library. Saving lives and recycling is pretty demanding.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} A nap sounds great. I’ll probably catch you two in the library later. If I don’t, I’ll see you first thing on Monday for our presentations!":
            jump seeingYa

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I think I’m gonna head straight to the library, if I take a nap I think I’ll sleep through the whole weekend. If I don’t see you in the library, I’ll see you first thing on Monday for our presentations!":
            jump seeingYa

label seeingYa:
    j "See ya!"
    show kevin happy
    with qdissolve
    k "Bye!"
    if not persistent.achievement_actFive_complete_unlocked:
        $ persistent.achievement_actFive_complete_unlocked = True
        show achievement actFiveComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
        sv "You just unlocked the “Act Five Completed” achievement."
    jump actFiveEnterPassword

label actFiveEnterPassword:
    $player_pass = renpy.input("Please enter the password for Act Six and press “Enter”", length=6)
    if player_pass.upper().strip() == actSix_pass:
        stop ambient fadeout 0.8
        stop music fadeout 0.8
        jump ActSix
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump actFiveEnterPassword