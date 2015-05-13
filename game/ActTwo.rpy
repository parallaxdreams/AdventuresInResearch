##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActTwo:
    call setupGameVariables
    $ name = persistent.playerName
    jump ActTwo

label ActTwo:
    
    $ save_name = "Name: %s.\nScene: Act 2." % (name)
    
    if not persistent.ActTwo_unlocked:
       $ persistent.ActTwo_unlocked = True

    scene bg blackSolid with fade
    scene bg ActTwo with fade
    $ renpy.pause(3.0)

    scene bg calendar with fade
    
    show calendar backing:
        xpos 0
        ypos 0
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -0.665
        pause 1.0
        ease 1.25 xpos -2.876
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(5.25)

    scene bg fountainDay with fade
    $ save_name = "Name: %s.\nScene: Act 2 – Fountain." % (name)

    play ambient "sfx/fountain-ambient.ogg"
    
    play sndfx "sfx/cb_tone.ogg"
    cbkevin "We still on to meet at the library?"
    
    m "{font=SourceSansPro-SemiboldItalic.ttf}I better let him know that I'm almost there.{/font}"

    play sndfx "sfx/cb_sent_tone.ogg"
    cbkme "Yeah, see you in five!"
    
    stop ambient fadeout 0.8
    scene bg libraryDVDs with fade
    $ save_name = "Name: %s.\nScene: Act 2 – Library." % (name)
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    show kevin neutral at right
    with qdissolve
    m "Hey, what’s up?"
    
    k "I’ve got to read {font=SourceSansPro-SemiboldItalic.ttf}Pride and Prejudice{/font} for my Women in Bonnets: A Retrospective class."
    
    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} You know these are DVDs and not books, right?":
            jump PrideAndDVDs

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} You are gonna watch the movie instead of reading the book? Are you sure that’s a good idea?":
            jump PrideAndDVDs

label PrideAndDVDs:

    show kevin confused
    with qdissolve
    k "Um, Yeah. Figured it would be easier to watch the movie."
    
    show stephanie neutral at leftthird
    with qdissolve
    s "Hey there! Can I help with anything?"
    
    show kevin happy
    with qdissolve
    k "Sure! I’m trying to find a copy of {font=SourceSansPro-SemiboldItalic.ttf}Pride and Prejudice{/font}."
    
    show stephanie happy
    with qdissolve
    s "It’s right over there."

    show stephanie concerned
    with qdissolve
    s "Are you looking for work or pleasure?"
    
    show kevin concerned
    with qdissolve
    k "What?! Work! Come on!"
    
    show stephanie neutral
    with qdissolve
    s "Hey, just checking! Here you go."
    
    show kevin surprised
    with qdissolve
    k "Oh, sorry, no—not the Keira Knightley version. It is great, but it leaves so much out!"

    show kevin neutral
    with qdissolve
    k "The BBC Version is longer and older, but I think it does a better job of capturing the sensibility of the era, that bittersweet tension borne of words unspoken..."
    
    s "Well alright then. I should mention though, that whatever DVD version you go with, it is no substitute for the book!"
    
    show kevin happy
    with qdissolve
    k "I know, right? I don’t think anyone has really been able to adapt Austen perfectly."
    k "I mean, that’s what my teacher says."
    show kevin neutral
    with qdissolve
    k "For this class. That I have to take."
    
    show stephanie concerned
    with qdissolve
    s "Hey, while I’m here, how is your research project coming along? The one about video games?"
    
    show kevin confused
    with qdissolve
    k "It’s going alright, I’ve got my research question and I’ve found some resources."
    
    show stephanie neutral
    with qdissolve
    s "That’s great! What have you found?"
    
    show kevin neutral
    with qdissolve
    k "Well I did a Google search for Video Games, Violence, and Teenagers and I found a newspaper article from a couple days ago."
    
    show stephanie concerned
    with qdissolve
    s "Sounds good. How are you planning to use your newspaper article?"
    
    show kevin concerned
    with qdissolve
    k "What do you mean?"
    
    show stephanie neutral
    with qdissolve
    s "As you’ve probably noticed already, research isn’t quite as cut and dried as people would like. For example, it isn’t enough to just find a resource that looks pretty good and relates to your topic."
    s "You have to think about the information cycle."
    
    show kevin surprised
    with qdissolve
    k "Information cycle? Really? I don’t know what that means, but it doesn’t sound fun."
    

    show stephanie happy
    with qdissolve
    s "It’s not that bad. Let’s go through it. Follow me and I’ll explain."
    
    scene bg libraryBrowsing with fade
    
    show stephanie neutral at left
    show kevin neutral at right
    with qdissolve
    s "This is our browsing section, where we keep a lot of our periodicals."
    s "Anyone care to guess what a periodical is?"
    

    menu:

        s "Anyone care to guess what a periodical is?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think I know!":
            menu:

                s "Anyone care to guess what a periodical is? {fast}"

                "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} A thing that comes out...periodically?":
                    show stephanie happy
                    with qdissolve
                    s "Pretty much! Periodicals are things like newspapers, magazines, and academic journals."
                    jump periodicalTalkCont

                "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Like newspapers and magazines and stuff?":
                    show stephanie happy
                    with qdissolve
                    s "That’s right. And academic journals. Any publication that comes out periodically."
                    s "Meaning weekly, biweekly, monthly, yearly, and so on."
                    jump periodicalTalkCont

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I have no idea what a periodical is.":
            show kevin concerned
            with qdissolve
            k "A thing that comes out...periodically?"
            show stephanie happy
            with qdissolve
            s "Pretty much! Periodicals are things like newspapers, magazines, and academic journals. Any publication that comes out periodically."
            s "Meaning weekly, biweekly, monthly, yearly, and so on."
            jump periodicalTalkCont
    
label periodicalTalkCont:
    s "Our browsing area is not the only place you can find these materials though."
    
    show stephanie neutral
    with qdissolve
    s "You’ve already found a newspaper article online, and the library also subscribes to a number of different databases where you can access newspapers, some that are hundreds of years old."
    
    show kevin happy
    with qdissolve
    k "Seriously? That’s pretty awesome. What does that have to do with a—what did you call it again?"
    
    m "Information cycle."
    
    s "Right! Well, what kind of information do you get in a newspaper?"
    
    menu:

        s "Right! Well, what kind of information do you get in a newspaper?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Information on current events?":
            s "Exactly!"
            jump allAboutNewspapers
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Weather?":
            s "Sure! For our discussion about the information cycle, though, what we want to focus on is that newspapers contain info on current events."
            jump allAboutNewspapers
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Obituaries?":
            s "Sure! For our discussion about the information cycle, though, what we want to focus on is that newspapers contain info on current events."
            jump allAboutNewspapers
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Sports?":
            s "Sure! For our discussion about the information cycle, though, what we want to focus on is that newspapers contain info on current events."
            jump allAboutNewspapers

label allAboutNewspapers:

    s "Newspapers are able to have information on current events because they have a relatively short publication cycle."
    s "If a newsworthy event occurs, a newspaper can cover that event pretty quickly both in its print version and online."
    
    show kevin neutral
    with qdissolve
    k "That’s true. Whenever there is a natural disaster or terrorist attack, newspapers usually have information on those things up on their websites pretty quick."
    
    s "And in their print versions by the next day. Television programs, Facebook, Twitter, radio, and blogs can often address those events as they are happening, if not immediately after."
    s "Why do you think it is important for researchers to keep this quick turnaround in mind when they use newspapers, tv, radio, or blogs in their research?"
    jump whyImportantNewspapers


label whyImportantNewspapers:

    if newspapers_choice_one_picked == newspapers_choice_two_picked == True:
        #m "Nothing comes to mind."
        jump afterEventNews

    elif newspapers_choice_one_picked == True or newspapers_choice_two_picked == True:
        s "Right, anything else?"
        jump whyImportantNewspapersQuestions

    else:
        jump whyImportantNewspapersQuestions

label whyImportantNewspapersQuestions:

    menu:

        #if newspapers_choice_one_picked == newspapers_choice_two_picked == False:
        s "Why do you think it is important for researchers to keep this quick turnaround in mind when they use newspapers, tv, radio, or blogs in their research?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Because when something gets quickly published about an event, there is a very good chance that all of the facts about that event aren’t yet in?" if newspapers_choice_one_picked == False:
            $ newspapers_choice_one_picked = True
            #s "Right, what else?"
            jump whyImportantNewspapers
    
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Maybe because when something gets quickly published about an event, there is a very good chance that the newspaper or tv show might have incorrect information?" if newspapers_choice_two_picked == False:
            $ newspapers_choice_two_picked = True
            #s "Right, anything else?"
            jump whyImportantNewspapers


label afterEventNews:
    s "It is important to think about when a resource we want to use was published."
    s "The earlier that something is published about an event after that event occurs, the higher the chance that information may be incomplete or incorrect."
    
    show kevin concerned
    with qdissolve
    k "If that is the case, is it ever acceptable to use an information source like a newspaper or radio show? Are they all incomplete and inaccurate?"
    
    s "That is a really good question, Kevin, and it is why I originally asked you how to plan to use your newspaper article. Newspapers, television shows, blogs and the like all have their place in research."
    s "Let me show you some other types of information sources, and hopefully this will become a little clearer. Let’s walk over to the reference section."
    
    scene bg libraryReference with fade
    
    show stephanie neutral at left
    show kevin neutral at rightmid
    with qdissolve
    s "Reference materials are another kind of information source that you might use in your research. They include things like dictionaries, encyclopedias, and atlases."
    s "We’ve already touched on what these resources contain and when you’d want to use them. Do you remember when, [name!q]?"
    
    menu:
        
        s "We’ve already touched on what these resources contain and when you’d want to use them. Do you remember when, [name!q]?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} When we were talking about coming up with a topic?":
            #m "When we were talking about coming up with a topic?"
            s "That’s right. It is a part of a process called Presearching."
            jump PresearchingActTwo
        
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} When we were talking about presearching?":
            #m "When we were talking about presearching?"
            s "That’s right!"
            jump PresearchingActTwo

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I don’t remember.":
            #m "I don’t remember."
            s "We touched on reference materials when were were discussing presearching."
            jump PresearchingActTwo

label PresearchingActTwo:

    s "Presearching is the process of doing basic research to learn more about your topic so you can research more effectively."
    s "With that in mind, what kind of information do you think reference materials contain?"
    
    menu:
        
        s "With that in mind, what kind of information do you think reference materials contain?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Information on current events, like newspapers?":
            #m "Information on current events, like newspapers?"
            s "No, things like encyclopedias and dictionaries take much longer to get published than newspapers do, so the information they contain generally isn’t as current as you’d find in a newspaper or magazine."
            jump ReferenceInfoCycle
            
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} General information on a topic.":
            #m "General information on a topic."
            s "That’s right, I’m glad to see you were paying attention!"
            s "Things like encyclopedias and dictionaries take much longer to get published than newspapers do, so the information they contain generally isn’t as current as you’d find in a newspaper or magazine."
            jump ReferenceInfoCycle
            
label ReferenceInfoCycle:

    s "Because it takes reference materials so long to get published, there is a good chance that the information they contain is more complete and that the authors have had time to contextualize it."
    s "Generally that means reference materials are fairly trustworthy."
    
    m "So we should use reference materials at the beginning of our research process and for basic facts that we might want to cite in our actual papers."
    
    s "Exactly. Let’s move on to the computers and I’ll show you some different kinds of information sources that you’d want to use as a part of your research."
    
    scene bg libraryPCs with fade
    
    show stephanie neutral at leftmid
    show kevin neutral at right
    with qdissolve
    s "Okay, why don’t you take a seat, [name!q], and drive the computer for us?"
    
    m "Sure thing. Should I go to the library’s web page?"
    
    s "That’s right, if it isn’t already up, type in westga.edu/library."
    show screenshot libraryHome
    with qdissolve
    m "I’m here, what next?"
    
    s "We are going to explore resources that you have access to that aren’t physically in the library."
    
    show kevin concerned
    with qdissolve
    k "This looks familiar. This is where to you go find books, right?"
    
    s "It is! You can search the library catalog from the search box to see what books we have in the stacks, what periodicals we have, even what DVDs you can check out."
    
    show kevin neutral
    with qdissolve
    k "I didn’t know you could search the DVD collection from here too! [name!q], can you see if they have {font=SourceSansPro-SemiboldItalic.ttf}Sense and Sensibility{/font}?"

    m "Before we go down that rabbit hole—did you say periodicals? Like the magazines and newspapers we just talked about?"

    hide screenshot libraryHome
    with qdissolve
    s "That’s right. You can use the library catalog to see what newspapers, magazines, and academic journals we have in our physical collection."
    s "That said, the library catalog does not list the tens of thousands of online periodicals and articles we have access to."

    m "What’s the difference between a print and an online periodical? Besides the obvious?"

    s "They are mostly the same. The print version of {font=SourceSansPro-SemiboldItalic.ttf}The New York Times{/font} is the same as the online version that we have access to."
    s "For that matter, the scholarly article you find in an online academic journal is the same article you’d find in the print version of that same academic journal."
    s "One main difference I can think of is that online newspaper articles have comments sections."
    s "This can be interesting, because when the comments are thoughtful, that aspect of the online newspaper can often turn the article into more of a conversation."
    s "Also, online versions can often be searched by keyword."

    show kevin happy
    with qdissolve
    k "That’s pretty cool. Now, about {font=SourceSansPro-SemiboldItalic.ttf}Sense and Sensibility{/font}..."

    show stephanie concerned
    with qdissolve
    s "I think I’m going to let you figure that one out on your own, Kev."
    
    show kevin neutral
    with qdissolve
    k "I suppose we should learn how to do all this ourselves."
    
    show stephanie neutral
    with qdissolve
    s "Right! As nice as it would be, you can’t have a librarian around all the time."
    s "While you do have one close by, though, let me ask: from what you already know about books, how do you two think a book compares to reference materials or periodicals?"
    
    jump bookComparison
    
label bookComparison:
    
    if done_comparing == True:
        
        jump doneComparingBooks


    elif books_longer_asked == True or books_published_later_asked == True:

        menu:

            s "How else do you think a book compares to reference materials or periodicals?"
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Books are longer than periodicals." if books_longer_asked == False:
                #m "Books are longer than periodicals."
                s "That they are—usually, at least. And for that matter, they are usually shorter than things like encyclopedias. What do you think that means?"
                m "That they probably go into more depth than a magazine or newspaper?"
                s "Most of the time, yes. And they probably go into more depth than an encyclopedia or dictionary too—think about it, an encyclopedia is big because it contains tons of information about a bunch of different things."
                s "Often, a book is focused on a specific topic."
                s "Or is a collection of chapters that all relate to a specific topic or theme."
                $ books_longer_asked = True
                if books_longer_asked == books_published_later_asked == True:
                    $ done_comparing = True
                jump bookComparison
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Books take longer to get published than newspapers and magazines do." if books_published_later_asked == False:
                #m "Books take longer to get published than newspapers and magazines do."
                s "Right! Most people don’t know just how long it takes for a book to get published though—from the time someone starts writing to when it is actually published can be between 1-2 years. Sometimes even longer!"
                k "So if it takes books longer to get published, they probably don’t contain much current information, right?"
                s "Most of time, yes."
                s "The reason this is important is that when a book is published, ideally the author has had some time to process and contextualize the information."
                k "So, it is the same kind of idea as a reference book?"
                s "Yes and no—we’ve discussed reference materials being just an overview of a topic. Books—especially the kinds of books that you’d want to use in a research project in college—will be more of an analysis of a topic."
                s "Often the author will do his or her own research to assert a specific position, rather than just presenting the more straightforward facts on that topic."
                $ books_published_later_asked = True
                if books_longer_asked == books_published_later_asked == True:
                    $ done_comparing = True
                jump bookComparison
        
    else: 
    
        menu:

            s "While you do have one close by, though, let me ask: from what you already know about books, how do you two think a book compares to reference materials or periodicals?{fast}"
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Books are longer than periodicals." if books_longer_asked == False:
                #m "Books are longer than periodicals."
                s "That they are—usually, at least. And for that matter, they are usually shorter than things like encyclopedias. What do you think that means?"
                m "That they probably go into more depth than a magazine or newspaper?"
                s "Exactly, and they probably go into more depth than an encyclopedia or dictionary too—think about it, an encyclopedia is big because it contains tons of information about a bunch of different things."
                s "Usually a book is focused on a specific topic."
                $ books_longer_asked = True
                if books_longer_asked == books_published_later_asked == True:
                    $ done_comparing = True
                jump bookComparison
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Books take longer to get published than newspapers and magazines do." if books_published_later_asked == False:
                #m "Books take longer to get published than newspapers and magazines do."
                s "Right! Most people don’t know just how long it takes for a book to get published though—from the time someone starts writing, it usually takes between 1-2 years. Sometimes even longer!"
                k "So if it takes books longer to get published, they probably don’t contain much current information, right?"
                s "Most of time, yes."
                s "The reason this is important is that when a book is published, ideally the author has had some time to process and contextualize the information."
                k "So, it is the same kind of idea as a reference book?"
                s "Yes and no—we’ve discussed reference materials being just an overview of a topic. Books—especially the kinds of books that you’d want to use in a research project in college—will be more of an analysis of a topic."
                s "Often the author will do his or her own research to assert a specific position, rather than just presenting the more straightforward facts on that topic."
                $ books_published_later_asked = True
                if books_longer_asked == books_published_later_asked == True:
                    $ done_comparing = True
                jump bookComparison

label doneComparingBooks:
    
    m "Aren’t books better for academic research than periodicals, too?"

    show stephanie concerned
    with qdissolve
    s "That’s an interesting question!"

    show tony neutral at Position(xpos=0.60, xanchor=0.5, ypos=0.51, yanchor=0.5)
    with qdissolve
    t "What’s an interesting question?"

    show stephanie neutral
    with qdissolve
    s "Hey Tony, I didn’t see you there. We are talking about kinds of information sources. [name!q] thought that books were better for academic research than periodicals."
    s "I know you and I have talked about the difference between books and periodicals before. What do you think?"

    show tony happy
    with qdissolve
    t "I would say that among other things, it depends on the book and the periodical. There are some popular books and scholarly periodicals."

    show kevin concerned
    with qdissolve
    k "Popular books? Like {font=SourceSansPro-SemiboldItalic.ttf}Twilight{/font}?"
    show tony confused
    with qdissolve
    t "I guess. That’s the sparkly vampire one right?"
    k "Well it explores a larger supernatural mythology that also includes werewolves."
    k "As we all know, though, these monsters are really just metaphors for aspects of the human condition."
    t "If anything in my human condition sparkles, I would probably go to the doctor."

    m "Are you saying that books aren’t good for research if a lot of people like them?"

    show tony concerned
    with qdissolve
    t "Oh, no, sorry. I can see the confusion."
    
    show kevin neutral
    with qdissolve
    t "The word “popular” refers to things written for more general audiences."
    show tony neutral
    with qdissolve
    t "It doesn’t necessarily mean it was a bestseller, or something like that."
    t "Scholarly books and scholarly articles are usually written for other scholars, students, things like that."

    m "So scholarly materials are better for research then?"

    t "Well that depends on what kind of information you need for your research."
    t "Scholarly materials have usually gone through a peer-review process, which means that other scholars have read them and given them the stamp of approval."
    t "That means scholarly materials are usually more trustworthy, and better if you need something credible to back up a position you’ve taken in your research."

    show stephanie happy
    with qdissolve
    s "That’s right, Tony! Popular materials might be useful in research too, though."
    show stephanie neutral
    with qdissolve
    s "Newspapers are considered popular, but you might need to use them to discuss how, for instance, communities respond to a certain event."
    s "You might want to use a popular magazine to see how journalists respond to certain events or issues in popular culture."

    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I can see how knowing the difference between scholarly and popular materials is important.":
            s "I’m glad to hear it!"
            jump gottaRun

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} That’s interesting and all, but I really don’t think it is important if something is scholarly or popular. My teacher isn’t going to know the difference, so why should I care?":
            show stephanie surprised
            show kevin surprised
            show tony surprised
            with qdissolve
            jump zombies

label zombies:

    stop music fadeout 0.8
    stop ambient fadeout 0.8

    scene bg blackSolid with fade
    $ save_name = "Name: %s.\nScene: Bad Ending 2." % (name)
    scene bg tenYrsLater with fade

    $ renpy.pause(2.0)

    scene bg blackSolid with fade

    scene bg zombies with fade

    #play ambient "sfx/zombies-ambient.ogg"
    play music "music/Zombies.ogg"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Scholars warned us that this could happen, but we didn’t listen! That one guy with the blog and the goatee said that a zombie outbreak would never happen and we all believed him.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}If only I had cared about the distinctions between scholarly and popular materials when I had the chance...Maybe I could have done something. Now, do I lock myself on the first floor or in the basement?{/font}"

    "Game Over"
    if not persistent.achievement_bad_end2_unlocked:
        $ persistent.achievement_bad_end2_unlocked = True
        show achievement badEnd2:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"

    menu:

        "Game Over{fast}"

        "Try Again":
            stop music fadeout 0.8
            jump ScholarlyPop

label ScholarlyPop:

    scene bg libraryPCs with fade
    $ save_name = "Name: %s.\nScene: Act 2 – Library." % (name)
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    show stephanie neutral at leftmid
    show kevin neutral at right
    show tony neutral at Position(xpos=0.60, xanchor=0.5, ypos=0.51, yanchor=0.5)
    with qdissolve

    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I can see how knowing the difference between scholarly and popular materials is important.":
            s "I’m glad to hear it!"
            jump gottaRun


label gottaRun:

    s "Well, folks, the LIBR 1101 class I teach is in a few minutes so I’ve gotta run. I hope this discussion was helpful."
    s "Before you leave you should head up to the stacks and look around."
    s "Send me an email if you have any more questions, or if you’d like to set up a research consultation."
    
    m "Thanks, Stephanie!"
    hide stephanie
    with qdissolve

    t "I’ll see you guys later."
    hide tony
    with qdissolve
    
    show kevin happy
    with qdissolve
    k "Hey, [name!q], I have an hour or two before my next class, do you want to run upstairs real quick? I didn’t even know there were other floors!"
    
    m "Yeah, let’s go!"
    
    stop ambient fadeout 0.8
    stop music fadeout 0.8
    scene bg libraryStacks with fade
    show kevin confused at center
    with qdissolve

    m "It sure is quiet up here."

    k "I just don’t understand. They are bookshelves, why do they call them “stacks”?"
    
    m "You know, Kevin, for once I agree with you. But hey, when in Rome..."
    
    show kevin concerned
    with qdissolve
    k "When in Rome...what?"
    
    m "It’s a saying, Kev. Google it."
    
    show kevin happy
    with qdissolve
    k "Right. I totally knew that."
    k "When in Rome...roam the stacks."
    
    m "Close, but...no. Speaking of roaming the stacks, isn’t that Kana, from Dr. Windham’s class over there with a pile of books? We should probably help her."
    
    show kevin neutral
    with qdissolve
    k "Sure!"
    hide kevin with qdissolve

    show kevin happy at rightthird
    with qdissolve

    play sndfx "sfx/BooksDropped.ogg"
    k "HEY KANA, NEED A HAND?" with hpunch
    
    show kana surprised at left
    with qdissolve
    show kevin surprised
    with qdissolve
    ka "Ack! Sorry, you totally scared me."

    show kana neutral
    with qdissolve
    ka "Hey, you are in Dr. Windham’s class, aren’t you?"
    
    k "Yeah, we both are. Didn’t mean to sneak up on you, let me just help you pick up all these books on the floor..."
    
    show kevin concerned
    with qdissolve
    m "These books are huge. Jeff Koons? Robert Mapplethorpe? Are you an artist?"
    
    ka "Yeah, a bunch of these are for classes, and some are for inspiration for Climate Change A Palooza. I’m designing the posters."
    
    k "I’m sorry, Climate change a-what?"
    
    ka "Climate Change a Palooza! It’s a festival to raise awareness for climate change. There are going to be a bunch of booths and games and things in Love Valley in a couple weeks."
    
    m "That sounds cool. I think our friend Jeff was talking about it the other day."
    
    ka "Jeff from class? I know him, we took LIBR 1101 together last semester."
    show kevin neutral
    with qdissolve
    k "He’s a cool guy. He’s been helping us a lot with this research project for class."
    
    ka "I’m actually pretty excited for this project, I’m thinking about writing about museums that censor art. I’ll probably use some of the pictures in these books as primary sources."
    
    menu:

        ka "I’m actually pretty excited for this project, I’m thinking about writing about museums that censor art. I’ll probably use some of the pictures in these books as primary sources.{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {font=SourceSansPro-SemiboldItalic.ttf}Hey, I know what a primary source is!{/font}":

            menu:

                "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} A primary source is like a first hand account of something, right?":
                    ka "Yeah, a primary source is usually something that is created under the period of study, or first hand accounts of something."
                    ka "That includes stuff like letters, photos, diaries, and maps. Primary sources can also be things like works of fiction or art. The idea is that they are the things that you study or analyze to create a secondary source."
                    jump nowOnToSecondarySources

                "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} A primary source is your most important source, right?":
                    ka "Hmm...not really. A primary source is usually something that is created under the period of study, or first hand accounts of something."
                    ka "That includes stuff like letters, photos, diaries, and maps. Primary sources can also be things like works of fiction or art. The idea is that they are the things that you study or analyze to create a secondary source."
                    jump nowOnToSecondarySources

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {font=SourceSansPro-SemiboldItalic.ttf}Primary source? What’s that?{/font}":
            m "I don’t think I know what what a primary source is. It is your most important source?"
            ka "They are important, but that’s not really what a primary source means. A primary source is usually something that is created under the period of study, or first hand accounts of something."
            ka "That includes stuff like letters, photos, diaries, and maps. Primary sources can also be things like works of fiction or art. The idea is that they are the things that you study or analyze to create a secondary source."
            jump nowOnToSecondarySources

label nowOnToSecondarySources:

    menu:
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Wait, what is a secondary source?":
            ka "A secondary source is something that analyzes a primary source."
            ka "In my paper, if I wanted to analyze a particular piece of censored art and write about why I think it should or shouldn’t be censored, I would be creating a secondary source."
            ka "The art that I am analyzing would be a primary source."
            ka "I would probably want to do research to find things that scholars or art critics have written about why a piece of art has been censored to back up my position too—those would also be secondary sources."
            jump sourceTypesContinued
    
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Hey, I know what a secondary source is!":
            m "A secondary source is something that analyzes a primary source."
            m "In her paper, if Kana wanted to analyze a particular piece of censored art and write about why she thinks it should or shouldn’t be censored, she would be creating a secondary source."
            m "The art that Kana is analyzing would be a primary source."
            m "She’d probably want to find things that scholars or art critics have written about censored art to back up her position—those would also be secondary sources."
            jump sourceTypesContinued

label sourceTypesContinued:

    k "Okay, just to get it straight—I’m writing my paper in Dr. Windham’s class on video games. If I wanted to analyze how violent a specific video game is, the video game would be my primary source?"
    
    ka "Right. Or let’s say you want to interview someone who plays video games. If you are analyzing someone’s reaction to playing a video game, that interview could be a primary source."
    
    k "Could be a primary source? It isn’t always?"
    
    ka "Sometimes it gets complicated...you really have to think about how you are using the information."
    ka "If you do an interview and you analyze the interview, that interview was a primary source, and your analysis of it is a secondary source."
    ka "Let’s say your interview was with a video game expert, though, and they were talking about how they’ve already analyzed that video game. If you use that interview, you could be using it as a secondary source."
    
    k "So basically, a primary source is the thing you are analyzing, and a secondary source is the analysis."
    
    ka "That sounds about right to me."
    
    show kevin confused
    with qdissolve
    k "Man, research is a lot of work—not only do you have to think about different kinds of information, you also have to think about whether or not something is a primary or a secondary source."
    
    ka "Actually, there are tertiary sources too."
    
    show kevin surprised
    with qdissolve    
    k "What did you call me?"
    
    show kana happy
    with qdissolve    
    ka "Haha, no—tertiary, like a third kind of source. Tertiary sources are things like reference materials, things that sum up, or condense other resources."
    
    show kevin happy
    with qdissolve
    k "Wow, I really wish I had taken LIBR 1101. It sounds like you and Jeff learned a lot in that class."
    
    ka "It was pretty useful!"
    
    show kevin concerned
    with qdissolve
    k "All this learning is making me thirsty. You guys wanna go downstairs and grab a coffee?"
    
    show kana neutral
    with qdissolve
    ka "Sure, just let me check out these books and I’ll meet you at the coffee shop."
    
    scene bg libraryPatio with fade

    show kana happy at left
    show kevin neutral at center
    with qdissolve

    #play music [ "music/gb_swing_cityL_jazz_patio.ogg", "music/gb_buddy_jazz_patio.ogg", "music/gb_park_bench_jazz_patio.ogg" ] fadein 2.0
    play music "music/gb_swing_cityL_jazz_patio.ogg" fadein 2.0

    menu:    
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} How cool is it that we have a coffee shop in the library?":
            jump coffeeShopContinues

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I’m at this coffee shop pretty much every day. I didn’t realize there was a whole library attached to it for a long time.":
            jump coffeeShopContinues

label coffeeShopContinues:

    ka "I know, right? It’s a pretty nice atmosphere for studying too."
    
    show tony happy at Position(xpos=0.80, xanchor=0.5, ypos=0.51, yanchor=0.5)
    with qdissolve
    t "Hey, did you guys find what you wanted?"
    
    show kana neutral
    with qdissolve
    ka "Hey Tony! Yeah, I found some great art books. I’m looking for inspiration for the Climate Change A Palooza posters I’m designing."
    
    m "Between Climate Change A Palooza and that movie they are filming, there sure is a lot going on on campus over the next few weeks!"
    
    show tony neutral
    with qdissolve
    t "Oh yeah, I’ve been providing security for the movie. It’s definitely...interesting."
    
    show kevin concerned
    with qdissolve
    k "Interesting? What do you mean?"
    
    show tony confused
    with qdissolve
    t "It’s difficult to describe. If you guys come down to the set to watch some filming, you’ll see."
    
    show kevin surprised
    with qdissolve
    k "We can do that? Watch the filming? Seriously?"
    
    show tony neutral
    with qdissolve
    t "Sure, as long as you don’t jump up and down screaming and run into the shot. Although in this weird movie, you might not be too out of place."
    
    show kevin happy
    with qdissolve
    k "Dude, can we go right now?"
    
    t "They aren’t filming here right now. I’ll let you know when they set up for some new scenes. What’s your Chatterbox name?"
    
    m "©PopCultureFan94"
    
    show kana happy
    with qdissolve
    ka "Let me know too, I love movies! I’m ©KanaPaints"
    
    k "I’m ©AustenFan18"
        
    show kana surprised
    show tony surprised
    with qdissolve

    e "..................................................."
    
    show kevin surprised
    with qdissolve
    k "What?"
    k "Like...Austin, TX. I was born there. In Texas."
    
    show tony confused
    with qdissolve
    t "Isn’t Austin spelled with an “i”?"
    
    show kevin confused
    with qdissolve
    k "Yeah...that one was taken already."
    
    m "And weren’t you born in Dallas? Georgia, not Texas?"
    
    k "Well..."
    
    show tony happy
    with qdissolve
    t "No shame in liking Jane Austen, bro. I dig that BBC version of {font=SourceSansPro-SemiboldItalic.ttf}Pride and Prejudice{/font}."
    
    show kevin happy
    with qdissolve
    k "It’s the best one, right?!"
    
    t "Without question. Anyway, I’m ©Semper_Fi."
    
    m "Well I’ve gotta head out, I want to ask Stephanie a question before my next class."
    
    m "Thanks, everyone. I’ll see you later."

    stop music fadeout 1.0
    
    scene bg libraryReference with fade
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Man, my brain hurts. Who knew there was so many different kinds of...stuff?{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Books, journals, databases...Wait a second, I didn’t even get a coffee.{/font}"
    
    show stephanie neutral at center
    with qdissolve
    m "{font=SourceSansPro-SemiboldItalic.ttf}Hey, there’s Stephanie, it looks like her class is over.{/font}"
    m "Hey Stephanie, I hate to bother you, but do you have a sec?"

    show stephanie happy
    with qdissolve
    s "You’re not a bother, that’s what I’m here for!  What’s up?"
    
    m "Well, we talked about a ton of stuff today and there was something I wanted to clarify."
    
    show stephanie concerned
    with qdissolve
    s "What’s that?"
    jump EndofActTwo
    
label EndofActTwo:
    
    if done_wrapping_up_ActTwo == True:
        m "I don’t have any more questions. Thanks for your help!"
        if not persistent.achievement_information_wrangler_unlocked:
            $ persistent.achievement_information_wrangler_unlocked = True
            show achievement informationWrangler:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
        jump ActTwoWrapup
        
    else:
    
        menu:
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Can you explain the information cycle again?" if infocycle_asked == False:
                #m "Can you explain the information cycle again?"
                show stephanie neutral
                with qdissolve
                s "The information cycle refers to how different media cover an event after it happens."
                s "Information sources like tv, radio, newspapers, and magazines cover the event sooner after it happens, and that might mean that the information may be incorrect or incomplete because they don’t yet have all the information."
                s "Information sources like books, scholarly articles and even encyclopedias don’t publish on events and ideas until sometime after that event has occurred so in some cases they may be more reliable sources."
                s "Anything else?"
                $ infocycle_asked = True
                if infocycle_asked == different_sources_asked == popular_scholarly_asked == info_source_differences_asked == True:
                    $ done_wrapping_up_ActTwo = True
                jump EndofActTwo
            
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What are the differences between primary, secondary, and tertiary sources?" if different_sources_asked == False:
                #m "What are the differences between primary, secondary, and tertiary sources?"
                show stephanie neutral
                with qdissolve
                s "A primary source is something that was created during the time period under study—this might include first hand accounts like diaries, interviews, or videos of an event. This also includes things like fiction and art."
                s "A secondary source analyzes a primary source."
                s "A tertiary source is something like an encyclopedia that summarizes or compiles information on a particular subject."
                s "Anything else?"
                $ different_sources_asked = True
                if infocycle_asked == different_sources_asked == popular_scholarly_asked == info_source_differences_asked == True:
                    $ done_wrapping_up_ActTwo = True
                jump EndofActTwo
            
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is the difference between a popular and scholarly source?" if popular_scholarly_asked == False:
                #m "What is the difference between a popular and scholarly source?"
                show stephanie neutral
                with qdissolve
                s "There are a number of differences, but the overarching idea really goes back to the author—a popular source might be written by a journalist, or someone who is interested but not necessarily an expert in that subject."
                s "Scholarly sources are written by scholars, or experts—people who have studied that subject extensively. Because they know so much about that subject, chances are that those sources are more reliable to use as resources in your research."
                s "Anything else?"
                $ popular_scholarly_asked = True
                if infocycle_asked == different_sources_asked == popular_scholarly_asked == info_source_differences_asked == True:
                    $ done_wrapping_up_ActTwo = True
                jump EndofActTwo
            
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Why is it important to know about different kinds of information sources?" if info_source_differences_asked == False:
                #m "Why is it important to know about different kinds of information sources?"
                show stephanie neutral
                with qdissolve
                s "You need to know the difference between things like newspaper articles and books—different kinds of information sources—because each of those sources contain different kinds of information."
                s "When you write a paper, you need to think about what kind of information you need for that paper—do you need current information? You’d probably want a newspaper."
                s "Do you need to find out what kind of research has already been done on your topic? You’d probably want a book or a scholarly article."
                s "Looking for background information on a topic? You’d probably want an encyclopedia."
                s "Anything else?"
                $ info_source_differences_asked = True
                if infocycle_asked == different_sources_asked == popular_scholarly_asked == info_source_differences_asked == True:
                    $ done_wrapping_up_ActTwo = True
                jump EndofActTwo
            
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I don’t have any more questions. Thanks for your help!" if infocycle_asked == True or different_sources_asked == True or popular_scholarly_asked == True or info_source_differences_asked == True:
                jump ActTwoWrapup
            
label ActTwoWrapup:
    s "You’re welcome. Have a great day!"
    if not persistent.achievement_actTwo_complete_unlocked:
        $ persistent.achievement_actTwo_complete_unlocked = True
        show achievement actTwoComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
    jump actTwoEnterPassword

label actTwoEnterPassword:
    $player_pass = renpy.input("Please enter the password for Act Three and press “Enter”", length=6)
    if player_pass.upper().strip() == actThree_pass:
        stop ambient fadeout 0.8
        stop music fadeout 0.8
        jump ActThree
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump actTwoEnterPassword