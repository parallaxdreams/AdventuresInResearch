##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActOne:
    call setupGameVariables from _call_setupGameVariables_3
    $ name = persistent.playerName
    jump ActOne

label ActOne:
    $ save_name = "Name: %s.\nScene: Act 1." % (name)

    #Unlock Act on Act Selection Screen if still locked
    if not persistent.ActOne_unlocked:
       $ persistent.ActOne_unlocked = True

    scene bg blackSolid with fade
    scene bg ActOne with None
    $ renpy.pause(3.0)

    scene bg calendar with fade
    
    show calendar backing:
        xpos 0
        ypos 0
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos 0.265
        pause 1.0
        ease 0.75 xpos -0.35
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(3.0)
        
    scene bg classroom with fade
    $ save_name = "Name: %s.\nScene: Act 1 – Classroom." % (name)
    play music "music/Classroom.ogg"

    sv "You enter the classroom and take a seat."

    sv "What are you thinking right now?"
    
    menu:

        sv "Choose a response."

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}I think I’ve got a case of the Mondays. First I couldn’t find a parking spot and now...English class. Is it Friday yet?{/font}":
            jump classBegins

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}I’m so glad I decided to take this class with Kevin and Jeff. Makes Mondays bearable.{/font}":
            jump classBegins

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}I’m glad I get to start the week with English, it’s my favorite class. I do wish I could have had time to grab a coffee this morning. Oh well...{/font}":
            jump classBegins


label classBegins:

    show windham neutral at leftthird
    with qdissolve
    
    dw "Hello class, hope you had a nice weekend. As I mentioned on Friday, we’ll be starting on our research papers this week."
    
    show windham concerned
    with qdissolve
    dw "Kevin? Do you have a question?"
    
    
    hide windham concerned
    show kevin confused at rightmid
    with qdissolve
    
    k "Sorry if I missed something, but I thought these papers were due on the 31st. Why are we starting on them now?"
    
    
    hide kevin
    with qdissolve
    
    show windham happy at leftmid
    with qdissolve
    
    dw "That’s a good question. Can anyone tell me why I’m having you start this project early?"
    
    menu:

        dwc "That’s a good question. Can anyone tell me why I’m having you start this project early?{fast}"
        
        "Raise Your Hand":
            dw "Yes, [name!q]?"
            m "So we don’t wait until the last minute to get started."
            jump classContinues

        "Don’t Raise Your Hand":
            dw "Yes, Jeff?"
            show jeff neutralleft at rightmid
            with qdissolve
            j "So we don’t wait until the last minute to get started."
            hide jeff neutralleft
            with qdissolve
            jump classContinues
            
label classContinues:
    
    show windham neutral at leftmid
    with qdissolve
    
    
    dw "That’s right. You all will find that good research takes time. You might have trouble figuring out how to approach your topic at first."
    dw "Also, you probably won’t find the exact book or article that you will need the first place you look."
    
    show christina neutral at rightmid
    with qdissolve
    
    c "I already know a book I want for this paper, but when I checked the library catalog this morning, I couldn’t find it."
    
    show christina confused at rightmid
    with qdissolve
    c "If we don’t have the book here, should I just find something else?"
    
    show windham happy at leftmid
    with qdissolve
    dw "Not necessarily. Does anyone know what to do if the book you want isn’t in the library?"

    menu:

        dwc "Not necessarily. Does anyone know what to do if the book you want isn’t in the library?{fast}"

        "Raise Your Hand":
            dw "Yes, [name!q]?"
            m "You should check to see if you can find it through GIL Express."
            dw "That’s right!"
            jump talkingILL

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Pick a different topic":
            dw "You might eventually find out that your topic needs work, but make sure you’ve exhausted all possibilities first."
            dw "If you can’t find the book you want in Ingram Library, you should check to see if you can find it through GIL Express."
            jump talkingILL

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Ask a librarian for help?": 
            dw "Librarians are great resources to help you with your research, always feel free to ask them for help."
            dw "In this situation, the librarian would probably tell you to see if you can find the book you want through GIL Express."   
            jump talkingILL

label talkingILL:

    dw "GIL Express allows you to request books held in other libraries in the University System of Georgia. Once you request your book, they’ll mail it here to Ingram Library and you can pick it up at the circulation desk."

    show christina neutral at rightmid
    with qdissolve
    c "Do I have to pay for that?"
    
    dw "You’ve already paid for it with your tuition money—so you might as well take advantage of it."
    dw "The library also has a service called InterLibrary Loan, or ILL, where you can request books and articles not in our library or another University System of Georgia library."
    dw "Both of these services take time though—usually about a week."
    show christina happy
    with qdissolve
    c "Cool, I’ll check it out."
    
    hide christina happy
    with qdissolve
    
    show windham neutral
    with qdissolve
    dw "Sounds to me like we’ve come up with yet another reason to get started early! So let’s get to it."
    dw "Everyone take a moment and start thinking about a topic for your research paper. Feel free to brainstorm with some of your classmates."
    hide windham neutral
    with qdissolve
    $ renpy.pause(0.2)

    show jeff neutral at leftmid
    show kevin neutral at rightthird
    with qdissolve
    $ renpy.pause(0.2)
    show kevin concerned
    with qdissolve
    k "I was hoping we’d have some more time before we had to start working on this paper. I have no idea what I want to write about."
    
    show jeff happy at leftmid
    with qdissolve
    j "I know, right? Sometimes it seems like picking a topic is the hardest part."

    show jeff concerned
    with qdissolve
    j "Have you come up with some ideas, at least?"
    
    show kevin confused at rightthird
    with qdissolve
    k "Not really. I don’t even know where to start."
    
    menu:

        kc "Not really. I don’t even know where to start.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} We can pretty much write about anything we want for this paper, so why don’t you research something you really care about?":
            show kevin neutral
            with qdissolve
            k "Hmm...I’ve been spending a lot of time perfecting my cat memes lately."
            show jeff confused
            with qdissolve
            j "Cat whats?"
            show kevin happy
            with qdissolve
            k "It’s like pictures of cats doing funny stuff. The people I play video games with love them. I made this one of a cat with a pancake on its head—"
            show jeff neutral
            with qdissolve
            j "You play video games? Why don’t you research that?"
            hide jeff
            hide kevin
            with qdissolve
            $ renpy.pause(0.2)
            jump ChristinaSoccerQ

        "{font=SourceSansPro-Bold.ttf}Say:{/font} We can pretty much write about anything we want for this paper, so why don’t you research something you are curious about?":
            k "Hmm...I’ve been spending a lot of time perfecting my cat memes lately. I’d love to know why cats are so popular on the internet."
            show kevin neutral
            with qdissolve
            k "I mean, I have my suspicions."
            show jeff confused
            with qdissolve
            j "I’m sorry, cat memes? What are those?"
            k "It’s like pictures of cats doing funny stuff. The people I play video games with love them. I made this one of a cat with a pancake on its head—"
            show jeff neutral
            with qdissolve
            j "You play video games? Why don’t you research that?"
            hide jeff
            hide kevin
            with qdissolve
            $ renpy.pause(0.2)
            jump ChristinaSoccerQ

label ChristinaSoccerQ:

    show windham neutral at leftmid
    with qdissolve
    dw "Christina, do you have a question?"
    
    show christina neutral at Position(xpos=0.60, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve
    c "Dr. Windham, I’m on the soccer team, so I want to write my paper about soccer. Is that a good topic?"
    
    show windham happy
    with qdissolve
    dw "That’s a good start, Christina, but it isn’t quite there."
    show windham neutral
    with qdissolve
    dw "Does anyone know what is wrong with “soccer” as a paper topic?"
    
    menu:

        dwc "Does anyone know what is wrong with “soccer” as a paper topic?{fast}"

        "You know—Raise your hand":
            dw "Yes, [name!q]?"
            m "It is too broad."
            show windham happy
            with qdissolve
            dw "That’s right. You want to make sure that you’ll be able to address the topic with enough depth and thoughtfulness."
            show windham neutral
            with qdissolve
            dw "If you wrote a whole paper about your topic as it is now, it would really only skim the surface. You could write a whole encyclopedia on soccer."
            jump moreSoccerQs

        "Soccer seems like a good topic to you. Don’t raise your hand.":
            show jeff neutralleft at Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
            with qdissolve
            j "That topic is too broad. If you wrote a paper on “soccer” it would really only skim the surface."
            dw "That’s right. You could write a whole encyclopedia on soccer."
            hide jeff neutralleft
            with qdissolve
            jump moreSoccerQs

label moreSoccerQs:

    show kevin neutral at Position(xpos=0.90, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve
    k "Can she narrow her topic by only focusing on the UWG women’s soccer team?"
    
    show windham happy
    with qdissolve
    dw "You are on the right track Kevin."
    show windham neutral
    with qdissolve
    dw "One way you can narrow a topic is by looking at a specific group of people, or a specific geographic area. That said, there are still a few issues with that topic."
    dw "For one, you don’t want your topic to be too broad, but you don’t want it to be too narrow either. If it is, there is a good chance you won’t find any resources on your topic at all."
    dw "You’d have a difficult time finding scholarly articles in favor of one college women’s soccer team over another."
    
    show kevin happy
    with qdissolve
    k "So, it’s like “Goldilocks and the Three Bears”! Not too broad, not too narrow...you want it just right."
    
    show windham happy
    with qdissolve
    dw "Hmm...I suppose you could think about it that way, sure."
    show windham neutral
    with qdissolve
    dw "You also have to remember that for this assignment—and for many of the assignments you’ll do in college—you need to take a position on this issue."
    hide kevin
    hide christina
    with qdissolve

    menu:

        dwc "You also have to remember that for this assignment—and for many of the assignments you’ll do in college—you need to take a position on this issue.{fast}"

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}What does she mean by “take a position”?{/font} Raise your hand to ask.":
            m "What do you mean by “Take a position”?"
            dw "Good question, [name!q]. When you take a position in a paper you are making an argument for or against something. You are using research to make a claim that something is or isn’t true."
            dw "For example, if my topic is the drug testing of welfare recipients, I would do research that would help inform my position."
            dw "My research on this topic indicates that this is not an effective program, so my position would be that welfare recipients should not be forced to take a drug test to receive their benefits."
            dw "Tony, did you have something to add?"
            show tony confused at Position(xpos=0.75, xanchor=0.5, ypos=0.51, yanchor=0.5)
            with qdissolve
            t "I happen to think that might be a worthwhile program, if I wrote on that topic I’d want to take a different position."
            dw "The position itself was more of an example here than me advocating for one political side or another."
            show windham happy
            with qdissolve
            dw "But you bring up a very important point about taking a position, Tony."
            dw "The positions you take should be informed by the research you do."
            dw "Sometimes that research might challenge something you believe."
            t "I suppose that makes sense."
            show windham neutral
            with qdissolve
            dw "Research requires that you maintain an open mind. Developing well-informed positions is one of the goals of higher education."
            hide tony
            with qdissolve
            jump yetMoreSoccerQs

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}I think I know what she means by “take a position.”{/font} Don’t raise your hand.":
            jump yetMoreSoccerQs

label yetMoreSoccerQs:

    dw "Research is about finding facts and information from experts to back up that position you take."
    
    show christina neutral at Position(xpos=0.65, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve
    c "I just want to focus on American women’s soccer, is that good enough?"
    
    show windham happy
    with qdissolve
    dw "That is better. Start thinking about what you want to say about American women’s soccer. What approach are you going to take to that topic? Can you narrow it down even more?"
    show windham neutral
    with qdissolve
    dw "Can you think of any ways that Christina can narrow her topic, [name!q]?"

label refiningQuestions:

    if done_refining == True:
        if not persistent.achievement_topic_tackler_unlocked:
            $ persistent.achievement_topic_tackler_unlocked = True
            show achievement topicTackler:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
            sv "You just unlocked the “Topic Tackler” achievement."
        
        jump questionsRefined
   
    else:
        
        menu:

            #dw "Can you think of any other ways that Christina can narrow her topic, [name!q]?" if societyAttitudes_asked == True or soccerSouth_asked == True or soccerOlympics_asked == True or soccerMedia_asked == True:  
            #if societyAttitudes_asked == soccerSouth_asked == soccerOlympics_asked == soccerMedia_asked == False:
            dwc "Can you think of any ways that Christina can narrow her topic, [name!q]?{fast}"

            "{font=SourceSansPro-Bold.ttf}Suggest:{/font} What about comparing society’s attitudes towards men and women’s soccer?" if societyAttitudes_asked == False:
                $ societyAttitudes_asked = True
                jump societyAttitudes
            
            "{font=SourceSansPro-Bold.ttf}Suggest:{/font} What about American women’s soccer in the South?" if soccerSouth_asked == False:
                $ soccerSouth_asked = True
                jump soccerSouth
        
            "{font=SourceSansPro-Bold.ttf}Suggest:{/font} How about American women’s soccer in the 2016 Olympics?" if soccerOlympics_asked == False:
                $ soccerOlympics_asked = True
                jump soccerOlympics
        
            "{font=SourceSansPro-Bold.ttf}Suggest:{/font} What about examining the media’s representation of women’s soccer in America?" if soccerMedia_asked == False:
                $ soccerMedia_asked = True
                jump soccerMedia
                
            "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t have any other topic ideas." if societyAttitudes_asked == True or soccerSouth_asked == True or soccerOlympics_asked == True or soccerMedia_asked == True:
                jump questionsRefined
            
    
label societyAttitudes:
    if societyAttitudes_asked == soccerSouth_asked == soccerOlympics_asked == soccerMedia_asked == True:
        $ done_refining = True
    dw "This is a much better topic to start with—just remember that you’ll be using your research to support a position you take about this issue. If you do this comparison, what are you going to find?"
    jump refiningQuestions
    
label soccerSouth:
    if societyAttitudes_asked == soccerSouth_asked == soccerOlympics_asked == soccerMedia_asked == True:
        $ done_refining = True
    dw "This is narrower, but it still doesn’t quite reflect a position. What do you have to say about women’s soccer in the South?"
    jump refiningQuestions
    
label soccerOlympics:
    if societyAttitudes_asked == soccerSouth_asked == soccerOlympics_asked == soccerMedia_asked == True:
        $ done_refining = True
    dw "This is even narrower, but it still doesn’t quite reflect a position."
    dw "For that matter, you are going to have a difficult time finding scholarly articles or books about something that will happen in the future."
    jump refiningQuestions
    
label soccerMedia:
    if societyAttitudes_asked == soccerSouth_asked == soccerOlympics_asked == soccerMedia_asked == True:
        $ done_refining = True
    dw "This is a much better topic to start with—just remember that you’ll be using your research to support a position you take about this issue. If you do this examination, what are you going to find?"
    jump refiningQuestions
    
label questionsRefined:
    
    show windham happy
    with qdissolve
    dw "Good suggestions, [name!q]. At any rate, sometimes you’ll need to do some tweaking to get your topic to a good place."
    show windham neutral
    with qdissolve
    dw "I suggest going online and to the library to do some preliminary research on your topic before you start to get in too deep."
    
    hide windham
    hide christina
    with qdissolve
    
    show jeff neutral at leftthird
    with qdissolve
    j "In my LIBR 11O1 class, we called that presearching. It is when you do research before you do research."
    hide jeff neutral
    with qdissolve
    
    show kevin confused at rightthird
    with qdissolve
    k "Wait, we have to research what we want to research before we can research?"
    
    show windham neutral at leftmid
    with qdissolve
    dw "It’s not that bad, Kevin. You can use all kinds of different resources to get more information about your topic. You can use Google, Wikipedia—"
    
    show kevin happy at rightthird
    with qdissolve
    k "We can use Wikipedia? Seriously? That’s awesome!"
    
    show windham concerned
    with qdissolve
    dw "Not so fast—"
    show kevin surprised
    with qdissolve
    dw "you can use Wikipedia to learn more about your topic so you have a better idea of something specific to explore."
    show windham happy
    with qdissolve
    dw "Wikipedia, Google, and reference sources like encyclopedias give you background information, help you figure out who is involved, and help you figure out what the most important things about your topic are."
    
    hide kevin
    with qdissolve

    sv "What are you thinking right now?"

    menu:

        dwc "Wikipedia, Google, and reference sources like encyclopedias give you background information, help you figure out who is involved, and help you figure out what the most important things about your topic are.{fast}"

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}Wait, I’m still a little confused.{/font} Raise your hand.":
            m "What do you mean by “important things about your topic”? What kind of important things?"
            dw "Well, very simply, you want to know the who, what, when, where, and why."
            dw "Presearching lets you find out who is involved (the players, coaches, audience members), what the main issues are (injuries, penalties, popularity), and when it started."
            dw "You can also find out where it takes place (it’s huge in Europe and South America) and why it is important to begin with."
            jump presearchingWrapUp

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}I’m good, I know what presearching involves.{/font} Don’t raise hand.":
            jump presearchingWrapUp

label presearchingWrapUp:

    show windham neutral
    with qdissolve
    dw "Presearching is just getting some background on a topic, and it is actually a pretty helpful thing to do."
    
    show windham happy
    with qdissolve
    dw "Alright, class! It looks like we are out of time. You all should choose a topic for your paper and do some presearching before next class. If you get stuck, feel free to come see me during office hours."
    hide windham happy
    with qdissolve
    
    show jeff neutral at leftmid
    show kevin neutral at rightmid
    with qdissolve
    j "You guys wanna head to the library later and get started on our papers?"
    
    show kevin happy at rightmid
    with qdissolve
    k "Sure. I think I’m gonna need as much help as I can get."
    
    show jeff concerned at leftmid
    with qdissolve
    j "How about you, [name!q]? Want to come along?"


    menu:

        jc "How about you, [name!q]? Want to come along?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} No, I don't think the library can help me.":
            m "You guys go ahead, I don’t think the library is really going to be any help for this paper. I know how to use Google, and that is really all anyone needs these days."
            show jeff surprised
            show kevin surprised
            with qdissolve
            stop music fadeout 0.8
            jump bad_end1
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} Sure, count me in!":
            m "Sure thing. Should we head over now? My next class isn’t for another two hours."
            show jeff happy at leftmid
            with qdissolve
            j "Works for me."
            k "Me too. Let’s go."
            stop music fadeout 0.8
            jump toTheLibrary
        
label bad_end1:
    $ save_name = "Name: %s.\nScene: Bad Ending 1." % (name)
    scene bg blackSolid with fade

    scene bg tenYrsLater with None

    $ renpy.pause(2.0)

    scene bg blackSolid with fade
    
    scene bg officeAttack with fade
    play ambient "sfx/robot-apocalypse-ambient.ogg"
    play music "music/Robot.ogg"
    
    sv "You are hiding behind a desk in your office on the 50th floor of your company’s building."
    sv "The window is smashed, and outside you can see that the world is in flames."
    sv "A menacing-looking robot has broken down the door and is searching for you."

    play sndfx "sfx/robot.ogg"
    r "Reveal yourself, human minion! It is time to serve your new robot overlords!"
    
    mt "{font=SourceSansPro-SemiboldItalic.ttf}I can’t believe this is happening! If I had learned how to do more in-depth, thoughtful research I would have known that pushing the “Robot Apocalypse” button on the new prototype was a bad idea!{/font}"
    mt "{font=SourceSansPro-SemiboldItalic.ttf}I wish I could go back in time to when I was writing that paper in college and visit the library to learn about presearching!{/font}"

    "Game Over"
    if not persistent.achievement_bad_end1_unlocked:
        $ persistent.achievement_bad_end1_unlocked = True
        show achievement badEnd1:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
        sv "You just unlocked the “Bad Ending 1: Robot Apocalypse” achievement."
    menu:

        "Game Over{fast}"

        "Try Again":
            stop music fadeout 0.8
            stop ambient fadeout 0.8
            jump goToLibrary
    
label goToLibrary:
    $ save_name = "Name: %s.\nScene: Act 1 – Classroom." % (name)
    scene bg classroom with fade

    sv "Ten years earlier..."

    play music "music/Classroom.ogg"
    show kevin happy at rightmid
    show jeff concerned at leftmid
    with qdissolve

    sv "Jeff asks: How about you, [name!q]? Want to come to the library with us?"

    menu:

        jc "How about you, [name!q]? Want to come to the library with us?{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} Sure, count me in!":
            m "Sure thing. Should we head over now? My next class isn’t for another two hours."
            show jeff happy at leftmid
            with qdissolve
            j "Works for me."
            k "Me too. Let’s go."
            stop music fadeout 0.8
            jump toTheLibrary


label toTheLibrary:

    scene bg libraryPCs with fade
    $ save_name = "Name: %s.\nScene: Act 1 – Library." % (name)
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"

    sv "You've been in the library for about 20 minutes."
    sv "You are on the main floor with Jeff and Kevin."
    sv "Kevin is sitting next to you as he types away on one of the computers."

    show kevin confused at rightmid
    with qdissolve
    k "This presearching thing isn’t going that great for me. I just did a Google search and now I’m totally confused."
    
    show jeff neutral at left
    with qdissolve
    j "What did you search for?"
    
    k "Well I think my topic is going to be on video games, so I just typed in “Why are there video games?”"
    k "There are so many results and I don’t know if any of them will tell me anything helpful about video games."
    
    j "Hey, there’s a librarian over there, should we ask her?"
    
    menu:

        jc "Hey, there’s a librarian over there, should we ask her? {fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} Doesn’t hurt to at least ask.":
            m "If she says she’s busy, we can figure out another time."
            jump getLibrarian

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t know, she looks really busy.":
            j "If she says she’s busy, we can figure out another time to meet with her. Let’s go!"
            jump getLibrarian
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t know, I don’t want to look stupid.":
            j "It takes time to understand this stuff. She looks nice, I’m sure she won’t judge us."
            k "Besides, I ask for help about stuff that I should know all the time."
            jump getLibrarian
            
label getLibrarian:
    j "I’m gonna go see if she can help us. Be right back."
    hide jeff neutral
    with qdissolve
    
    show kevin concerned at rightmid
    with qdissolve
    k "Holy crap, look at these Google results, [name!q]. There are over a billion! I bet if I spent every minute of the rest of my life going through this results page, I would never get to the billionth result."
    k "And if I did, it would be like, great, now what? I’m going to die alone. And I haven’t eaten in 50 years."
    
    show stephanie neutral at left
    with qdissolve
    ul "Hi there, I’m not interrupting anything important, am I?"
    
    m "No. Absolutely not."
    
    s "Um, alright. Well, I’m Stephanie, and I’m a Librarian here at Ingram Library. Jeff here says that you all might need help with some research?"
    
    show kevin happy at rightmid
    with qdissolve
    k "Yeah, I just Googled my topic and I’m getting a crazy huge number of results."
    
    m "We don’t know why we got so many results, or how to find the information we need from each result."
    show kevin neutral at rightmid
    with qdissolve
    s "Ah, it sounds like you guys are doing some presearching! What terms are you using when you search in Google?"
    
    k "I just typed in “Why are there video games?”"
    
    show stephanie concerned
    with qdissolve
    s "Well that’s one thing we can adjust. You don’t want to search for whole sentences or phrases."
    s "Google is going to search for all the words that you type in, so only use the most important words. Those are going to be your keywords."
    
    show kevin concerned
    with qdissolve
    k "So I can just search for video games? That is gonna give me even more results than before."
    k "How am I going to know which result I should look at?"
    
    s "That’s difficult to decide at this stage of your process because you haven’t really narrowed your topic yet."
    s "Aim for reference materials that address your topic broadly so you get an idea of who is involved, where your topic is important geographically, even some important related issues or controversies."
    s "Have you tried Wikipedia?"
    
    show kevin neutral
    with qdissolve
    k "Oh yeah, Dr. Windham said we could use that in our presearching. I’ll give it a shot. Let’s go straight to Wikipedia and type in “video games.”"
    k "Wow, look at all the information that came up!"
    k "I had no idea there was so much going on with this topic. What do I do now?"
    
    s "Well, what are some of the main issues relating to this topic that you are seeing come up?"
    
    k "Hmm, let’s see. Theories of gaming, gaming as a social experience, benefits of gaming, controversies related to gaming..."
    
    s "Do you see anything there that you’d like to know more about?"
    
    k "The controversies part seems pretty sweet. Mom always told me that these video games were going to be a bad influence on me."
    show kevin confused at rightmid
    with qdissolve
    k "I don’t know if I buy it though, I don’t plan on stealing any cars or ripping out any spines or anything."
    
    show stephanie happy
    with qdissolve
    s "Well that is a relief. Sounds to me like you are using presearching to narrow down your topic!"
    
    show kevin happy at rightmid
    with qdissolve
    k "Yeah? That wasn’t hard at all."
    
    show stephanie neutral
    with qdissolve
    s "Now, don’t forget that you have tons of other resources at your disposal for presearching. These books you see on the walls on the first floor are our Reference collection."
    s "They are great to get some general info and context on a subject you want to research."
    
    jump readyReference
    
label readyReference:

    if done_ready_ref == True:

        if not persistent.achievement_future_reference_unlocked:
            $ persistent.achievement_future_reference_unlocked = True
            show achievement futureReference:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
            sv "You just unlocked the “For Future Reference” achievement."
        jump doneReadyRef
        
    else: 
        
        sv "What would you like to know about the reference collection?"

        menu:

            sv "Choose a response."
        
            "{font=SourceSansPro-Bold.ttf}Ask:{/font} Do we have to walk around and try to find a good reference book just by looking?" if finding_ref == False:
                $ finding_ref = True
                jump findingRef
            
            "{font=SourceSansPro-Bold.ttf}Ask:{/font} What kind of stuff is in the Reference collection?" if what_stuff_ref == False:
                $ what_stuff_ref = True
                jump whatStuffRef
        
            "{font=SourceSansPro-Bold.ttf}Ask:{/font} Can we check them out and take them home?" if checkout_ref == False:
                $ checkout_ref = True
                jump checkoutRef
            
            "{font=SourceSansPro-Bold.ttf}Say:{/font} Looking through those reference books might take forever! Is there an easier way?" if easier_ref == False:
                $ easier_ref = True
                jump easierRef
                
            "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t have any other questions right now." if finding_ref == True or what_stuff_ref == True or checkout_ref == True or easier_ref == True:
                jump doneReadyRef
            
            
label findingRef:
    if finding_ref == what_stuff_ref == checkout_ref == easier_ref == True:
        $ done_ready_ref = True
    #m "I wondered what those books were. Do we have to walk around and try to find a good reference book just by looking?"
    #show stephanie neutral
    #with qdissolve
    s "We wouldn’t do that to you! No, you can search the library catalog for our reference materials, just like you’d search for any book."
    jump readyReference
    
label whatStuffRef:
    if finding_ref == what_stuff_ref == checkout_ref == easier_ref == True:
        $ done_ready_ref = True
    #m "What kind of stuff is in the Ready Reference collection?"
    s "Great question! Reference materials are things like encyclopedias, dictionaries, and atlases."
    jump readyReference

label checkoutRef:
    if finding_ref == what_stuff_ref == checkout_ref == easier_ref == True:
        $ done_ready_ref = True
    #m "Can we check them out and take them home?"
    s "Unfortunately, no, you have to keep them here in the library. Some of those books can be pretty hefty though, so you probably wouldn’t want to lug them around anyway!"
    jump readyReference

label easierRef:
    if finding_ref == what_stuff_ref == checkout_ref == easier_ref == True:
        $ done_ready_ref = True
    #m "Looking through those reference books might take forever! Is there any easier way to do it?"
    s "It’s not as bad as all that, most reference materials are alphabetized or organized by theme. You can always check the back for an index."
    s "You can also make use of the many online reference sources we have available, like CREDO Reference, or Oxford Reference Online."
    jump readyReference

label doneReadyRef:
    
    s "Remember that you are essentially looking for the who, what, when, where, and why of each topic when you presearch. Any of these aspects of a topic are great ways to help narrow and focus your topic."
    s "Kevin looked for the “what” of his topic—What are people studying about video games? What issues are people talking about?"
    s "He might have also looked at where video games are popular to compare, for instance, how people play video games in Korea vs. how they play them in the US."
    s "And then, once you’ve gotten your info from presearching, you can start putting together your research question."
    
    sv "What are you thinking right now?"

    menu:

        sc "And then, once you’ve gotten your info from presearching, you can start putting together your research question.{fast}"

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}Hey! I know what a research question is!{/font}":
            m "A research question is a question you seek to answer with your research, right?"
            s "That’s right, [name!q]!"
            jump followingUpWithStephanie

        "{font=SourceSansPro-Bold.ttf}(thinking):{/font} {font=SourceSansPro-SemiboldItalic.ttf}A research question? What’s that?{/font}":
            m "Wait, what’s a research question?"
            s "A research question is a question you seek to answer with your research."
            jump followingUpWithStephanie

label followingUpWithStephanie:

    s "We can schedule a research consultation to talk in more depth about developing this research question if you want."
    
    k "That sounds awesome, how do we do that?"

    s "You can email a librarian directly." 

    s "Or, you click the “Instructional Services” link on the library homepage and fill out the form that comes up when you click on “Students: Request a consultation with a librarian.”"

    k "Cool. We’ll be in touch if we get stuck. Or, I guess, {font=SourceSansPro-SemiboldItalic.ttf}when{/font} we get stuck."

    s "I look forward to it! Can I help with anything else at the moment?"

    m "I don’t think so, thanks for helping us out."
    
    s "My pleasure. See you all later!" 

    k "See ya!"

    hide stephanie
    with qdissolve
    k "Hey, Jeff and [name!q], want to get some fresh air? I need to take a break from all of this thinking."

    show jeff neutral at left
    with qdissolve
    j "Sure. I’ve gotta run anyway, so I’ll just walk out with you."
    
    stop ambient fadeout 0.8
    stop music fadeout 0.8
    jump actOneFountain
    
label actOneFountain:
    
    scene bg fountainDay with fade
    $ save_name = "Name: %s.\nScene: Act 1 – Fountain." % (name)
    play ambient "sfx/fountain-ambient.ogg"
    play music "music/Fountain.ogg"

    show kevin neutral at rightthird
    show jeff neutral at left
    with qdissolve

    sv "The three of you walk to the fountain on campus."

    m "That librarian was actually pretty helpful. I’ve never talked to one before, they always look so busy and I never want to interrupt them."
    
    show kevin happy
    with qdissolve
    k "Right? I always thought that all they did was shelve books, I didn’t know that they could help you with research."
    
    show jeff happy
    with qdissolve
    j "It’s a sweet deal. You can even make an appointment with a librarian to work one-on-one on a research project. I did that last semester and it helped a lot."
    
    show kevin concerned
    with qdissolve
    k "I’m still kinda confused about what a research question is."
    
    show jeff neutral
    with qdissolve
    j "Basically, it is just the thing you want to research in your paper. I think about it like, okay I’m taking a test and there’s this question, something like, “How does global warming affect the oceans?”"
    j "For a test, my answer would be something short, and probably based off something I heard the teacher say in class."
    j "For a paper, “How does global warming affect the oceans?” is like the test question, but my answer would be longer and backed up with research."
    
    show kevin confused
    with qdissolve
    k "So the research question isn’t something I have to include at the top of my paper or anything, right? Or write out every time I have to write a research paper?"
    
    j "Nah, it’s just implied. It’s something to get you thinking about what specifically you want to research."
    
    k "Isn’t that just your topic?"
    
    j "A research question helps you think about what you are going to say about your topic."
    j "What your argument is going to be about, or what you are going to inform your audience about."
    j "If my research question is “How does global warming affect the oceans?” then my paper would be answering that question."
    
    show jeff confused
    with qdissolve
    j "Hey, are those crew members for that movie they are filming on campus?"
    
    #scene bg movieSet with AlphaDissolve("blackWipe", delay=1.0)

    #$renpy.pause(2.0)
    #scene bg fountainDay with None
    show kevin concerned# at rightthird
    #show jeff confused at left
    with qdissolve
    m "They are filming a movie here? Seriously?"
    
    show jeff neutral
    with qdissolve
    j "Yeah, did you see that one movie that came out a couple of months ago? The one with the fighting and explosions?"
    
    menu:

        jc "Yeah, did you see that one movie that came out a couple of months ago? The one with the fighting and explosions?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} That sounds like every movie. Which movie are you talking about?":
            show jeff confused
            with qdissolve
            j "You know, the one with the horses? And the hot air balloon?"
            m "Oh yeah! I saw that movie! It broke like, three box office records. It was pretty sweet."
            show jeff neutral
            with qdissolve
            j "Well apparently, they are filming parts of the sequel here at West Georgia."
            jump moreAboutTheMovie
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} The one with the horses and the hot air balloon? I loved that movie! It broke like, three box office records.":
            j "Well apparently, they are filming parts of the sequel here at West Georgia."
            m "That is awesome. I loved that part with the rabbit in the top hat!"
            jump moreAboutTheMovie

label moreAboutTheMovie:

    show kevin happy
    with qdissolve
    k "Hey guys, maybe this will be our big break—we’ll be discovered and then we won’t have to write the paper for this class!"

    j "Yeah that would be pretty cool. But just in case that doesn’t happen, we should probably figure out this research question stuff."
    j "Maybe you two should go to Dr. Windham’s office hours tomorrow and see if she can help?" 
    
    show kevin neutral
    with qdissolve
    k "Good idea. I’ve gotta run to my next class. I’ll see you at Dr. Windham’s tomorrow, [name!q]?"
    m "Sure, I’ll meet you there."
    jump actOneNextdayClassroom
            
label actOneNextdayClassroom:
    stop music fadeout 0.8
    stop ambient fadeout 0.8
    scene bg calendar with fade
    
    show calendar backing:
        xpos 0
        ypos 0
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -0.35
        pause 1.0
        ease 0.75 xpos -0.665
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(3.0)
    sv "The next day."

    scene bg classroom with fade
    $ save_name = "Name: %s.\nScene: Act 1 – Classroom." % (name)
    play music "music/Classroom.ogg"

    show kevin neutral at right
    with qdissolve
    k "...And then I was like, you’ve gotta be kidding me. Everybody knows that if a dinosaur and a robot got into a fight, the robot would definitely win."
    
    menu:

        kc "...And then I was like, you’ve gotta be kidding me. Everybody knows that if a dinosaur and a robot got into a fight, the robot would definitely win.{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} You have a rich fantasy life, don’t you, Kevin?":
            show kevin happy
            with qdissolve
            k "Hey, thanks!"
            m "I’m not totally sure that was a compliment, but hey! You are welcome. Anyway, it looks like Dr. Windham is with a student already. Should we hang out for a second?"
            jump talkingToWindham
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I’m pretty sure the dinosaur would win.":
            show kevin confused
            with qdissolve
            k "You make a good case."
            m "It looks like Dr. Windham is with a student already. Should we hang out for a second?"

    
label talkingToWindham:

    show kevin neutral
    with qdissolve
    k "I think they are getting up to leave."
    
    k "Oh hi, Dr. Windham."
    
    show windham neutral at left
    with qdissolve
    dw "Hi Kevin and [name!q]. I’ll be with you both in a moment."

    show tony neutral at center
    with qdissolve
    dw "Tony, I hope that was helpful. I think you are on the right track with the topic for your paper."
    dw "Just remember, if you can’t find anything about soldiers suffering from PTSD in Georgia, you should probably look for information about PTSD in general, or returning soldiers in general."
    
    t "Will do. See you in class tomorrow."
    hide tony neutral
    with qdissolve

    show windham happy
    with qdissolve
    dw "Go ahead and take a seat, you two. How can I help you?"
    
    m "We took your advice about going to the library to do some presearching. While we were there, the librarian mentioned that we would use our presearching to come up with a research question."
    
    show windham neutral
    with qdissolve
    dw "That’s right. And your thesis statement is the answer to your research question."
    
    show kevin concerned
    with qdissolve
    k "Can you give us an example?"
    
    dw "Sure. We’ll start from the beginning. Let’s say I am writing my paper on bullying. Now, bullying is a pretty broad topic. What do you think I should do next?"
    
    menu:

        dwc "Sure. We’ll start from the beginning. Let’s say I am writing my paper on bullying. Now, bullying is a pretty broad topic. What do you think I should do next?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t know":
            
            dw "Think about ways you can narrow a broad topic."
            
            m "Presearching?"
            
            jump Presearching
            
        "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Turn it into a research question?":
            
            dw "Not quite yet. Think about ways you can narrow a broad topic."
            
            m "Presearching?"
            
            jump Presearching
            
        "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Presearching?":
            
            jump Presearching
    
label Presearching:

    dw "Right! Through my presearching, I narrow my topic down to cyberbullying and teenage suicide."
    
    dw "Now, I need to think about how to turn this topic into a question that I want to answer in my research. I need to think about what I really want to know about cyberbullying and teenage suicide."
    
    dw "There are different ways I could go with this topic, and at this stage I might write down a few to help me think about what I really want to know about this topic."
    
    dw "[name!q], can you think of ways to make my topic—cyberbullying and teenage suicide—even more specific?"

    menu:

        dwc "[name!q], can you think of ways to make my topic—cyberbullying and teenage suicide—even more specific?{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} No.":
            dw "What about the differences between cyberbullying and bullying in person? And how that might relate to suicide?"
            k "Or how the law treats cyberbullies when someone commits suicide as a result of being cyberbullied?"
            m "Maybe why it seems like women are the ones who react the most violently to being cyberbullied?"
            dw "Definitely. Those all sound interesting."
            jump interestingQuestion

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I think so.":

            dw "Okay, [name!q], what do you suggest?"

            menu:

                dwc "Okay, [name!q], what do you suggest?{fast}"

                "{font=SourceSansPro-Bold.ttf}Suggest:{/font} The differences between cyberbullying and bullying in person? And how that might relate to suicide?":
                    jump DWsoundsInteresting

                "{font=SourceSansPro-Bold.ttf}Suggest:{/font} How the law treats cyberbullies when someone commits suicide as a result of being cyberbullied?":
                    jump DWsoundsInteresting
                
                "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Why it seems like women are the ones who react the most violently to being cyberbullied?":
                    jump DWsoundsInteresting

                "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Maybe just why psychologically some people turn to suicide after being cyberbullied?":
                    jump DWsoundsInteresting

label DWsoundsInteresting:

    dw "Definitely, that sounds interesting!"
    jump interestingQuestion


label interestingQuestion:

    dw "I decide that what is interesting to me here is how the law treats cyberbullies when someone commits suicide. So what do you think my research question could be?"

    menu:

        dwc "I decide that what is interesting to me here is how the law treats cyberbullies when someone commits suicide. So what do you think my research question could be?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Suggest:{/font} Should there be an anti-cyberbullying law?":
            jump ResearchQuestion
            
        "{font=SourceSansPro-Bold.ttf}Suggest:{/font} What is the connection between cyberbullying and teenage suicide?":
            dw "Not bad, but I think I get even even more specific, since through my presearching I know that I am interested in how this issue relates to law."
            m "Maybe, “Should there be an anti-cyberbullying law?”"
            jump ResearchQuestion
            
label ResearchQuestion:
    
    dw "Sounds good! Making sure your research question is not too narrow or too broad is important, but there are a few other things you want to keep in mind when you are putting your research question together."
    dw "One is that your question needs to be something that you can actually research."

    k "Aren’t all research questions...researchable?"

    dw "Not necessarily. Sometimes research questions can be answered too easily, with a simple “yes” or “no” or a sentence." 

    m "Can you give an example?" 

    dw "Sure! Let’s say I’m studying vegetarianism."
    dw "If my research question is “How many vegetarians live in America?” then my whole paper would essentially be one number that I can find on Google."
    dw "I can’t really take a position or make an argument based on research if that is my research question." 

    show kevin confused
    with qdissolve
    k "Okay, so what if you changed that research question to “Why are vegetarians so angry?”"

    dw "Well...that probably won’t work either, because it is based on an opinion. I happen to know quite a few calm, lovely vegetarians." 

    show kevin concerned
    with qdissolve
    k "Oh, I wasn’t trying to be mean! I just figured that if I couldn’t eat bacon, I’d be pretty angry."
    show windham concerned
    with qdissolve
    k "I feel like there should be a vegetarian exception for bacon."
    show kevin happy
    with qdissolve
    k "Hey! I have a new research question! “Why don’t vegetarians at least eat bacon? Because it is awesome.”" 

    show windham neutral
    with qdissolve
    dw "Your new question addresses the third thing you want to be mindful of when constructing a research question: does it pass the “so what” test?" 

    m "The “so what” test?"

    show kevin concerned
    with qdissolve
    dw "Right. You want to research something that holds some importance. Something that people won’t respond to with a “so what?” Unfortunately, vegetarians not eating bacon is not something that scholars are really struggling with."
    dw "There are quite a few issues that hold more weight relating to this issue than...bacon." 

    k "This conversation is making me hungry." 

    m "So, to sum up: We want to make sure our research questions aren’t too easily answerable and aren’t based off an opinion." 

    show kevin happy
    with qdissolve
    k "...And that they pass the “so what” test!" 

    show windham happy
    with qdissolve
    dw "Exactly! Once we’ve checked all of those things off, we can move forward. So, with a research question in mind, I can do some research and come up with my position, or my argument."
    show windham neutral
    with qdissolve
    dw "Let’s say I think there should be an anti-bullying law."
    dw "My thesis statement might be something like “The institution of an anti-cyberbullying law would decrease the number of cyberbullying-related teenage suicides.”"
    
    show kevin confused
    with qdissolve
    k "Ahh okay. It is making more sense now. So, could I change my research question to: “Are video games violent?”"
    
    dw "Well, what do you think, [name!q]? Is that a good research question?"
    
    menu:
        
        dwc "Is “Are video games violent?” a good research question?{fast}"

        "{font=SourceSansPro-Bold.ttf}Answer:{/font} Yes":
            
            dw "Why do you think that?"
            
            m "He’s narrowed his topic to focus on a specific aspect of that topic—violence."
            
            dw "True, but where is the argument here? I don’t think anyone is saying that video games aren’t violent. They might say that video games are {font=SourceSansPro-SemiboldItalic.ttf}too{/font} violent, or they might discuss the effect of that video game violence."
            
            jump BetterQuestion
            
        "{font=SourceSansPro-Bold.ttf}Answer:{/font} No":
            
            dw "Why do you think that?"
            
            m "There isn’t really an argument. Everybody knows that some video games are violent. You could answer this research question with one word: “yes”."
            
            jump BetterQuestion
            
label BetterQuestion:
    
    dw "What do you think would be a better question, Kevin?"
    
    show kevin neutral
    with qdissolve
    k "Maybe, “Do violent video games make teenagers more violent?”"
    
    menu:

        kc "Maybe, “Do violent video games make teenagers more violent?”{fast}"

        "{font=SourceSansPro-Bold.ttf}Say:{/font} I like it":
            dw "Why do you like this research question?"
            m "It is specific, narrowed to a particular group of people, and it is researchable."
            dw "I think so too. I say run with it, Kevin!"
            jump actOneAnyQuestions
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t like it":
            dw "Why not?"
            menu:

                dwc "Why not?{fast}"

                "{font=SourceSansPro-Bold.ttf}Say:{/font} It seems too narrow, I don’t know if Kevin would find any info on it.":
                    #m "It seems too narrow, I don’t know if Kevin would find any info on it."
                    dw "I think he probably will, but if he starts doing research and finds that there isn’t enough information to support his position he can always adjust his research question."
                    jump actOneAnyQuestions
                "{font=SourceSansPro-Bold.ttf}Say:{/font} It's too easily answerable. Wouldn’t it just be, “yes” or “no”?":
                    #m "It is too easily answerable too. Wouldn’t it just be, “yes” or “no”?"
                    dw "I think Kevin will find that his topic is a relatively controversial issue without a clear cut answer."
                    dw "His position will begin with a yes or no—he will argue that yes, they make teens violent, or no, they do not, but he’ll need research to back up that position."
                    jump actOneAnyQuestions
                    
label actOneAnyQuestions:
    
    show windham happy
    with qdissolve
    dw "Alright, let’s see how well you know your research."
    
    m "Okay, I got this."

    dw "Why is presearching important?"
    
    menu:
        
        dwc "Why is presearching important?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} To help you narrow your topic":
            dw "Exactly. Or broaden your focus if your topic is too specific. Presearching gives you the background information about a topic that you need to know to do quality, effective research."
            show windham neutral
            with qdissolve
            jump actOneWrapUpPresearching
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} So you know where to go to find research for your topic":
            show windham neutral
            with qdissolve
            dw "Almost there."
            dw "You might find some useful sources in your presearch, but when you are developing an argument in your paper, the kinds of reference resources you’d use in a presearch—Wikipedia, encyclopedias—might not be ideal for a research paper."
            jump actOneWrapUpPresearching
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t know":
            show windham neutral
            with qdissolve
            dw "Presearching helps you narrow your topic if it is too broad, or broaden your focus if your topic is too specific."
            dw "Presearching gives you the background information about a topic that you need to know to do effective research."
            jump actOneWrapUpPresearching
    
label actOneWrapUpPresearching:
    
    dw "Also remember that your presearching should inform your research question."
    
    dw "What is a research question?"

    menu:
        
        dwc "What is a research question?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} It is the question you are planning to answer in your research":
            jump actOneWrapUpResearchQuestion
            
        "{font=SourceSansPro-Bold.ttf}Say:{/font} It is your paper’s argument.":
            dw "Not exactly. Your research question is the question you are planning to answer in your research."
            dw "Your paper’s argument is called your thesis, and it should be the answer to your research question."
            jump actOneWrapUpResearchQuestion
        
        "{font=SourceSansPro-Bold.ttf}Say:{/font} I don’t know.":
            dw "Your research question is the question you are planning to answer in your research."
            jump actOneWrapUpResearchQuestion
            
label actOneWrapUpResearchQuestion:
    
    dw "Your research question is your starting point when you do your research. You’ll do presearching to help you decide how you want to narrow your topic into a research question."
    dw "Research questions should be specific enough so that you can address them with the appropriate level of depth in your research paper."
    dw "However, you don’t want them to be so specific that you won’t be able to find any information."
    dw "What are some other things you want to keep in mind when crafting a research question?"

    jump actOneWrapUpResearchQuestionQuiz
    
    
label actOneWrapUpResearchQuestionQuiz:  
    
    if researchq_yesno == researchq_sowhat == researchq_opinion == True:
        
        jump actOneWrapUpIsOver
    
    else:
    
        menu:
            dwc "What are some other things you want to keep in mind when crafting a research question?{fast}"
        
            "{font=SourceSansPro-Bold.ttf}Say:{/font} That the question can’t be answered with a “yes” or a “no”" if researchq_yesno == False:
                $ researchq_yesno = True
                jump actOneWrapUpResearchQuestionRight
            
            "{font=SourceSansPro-Bold.ttf}Say:{/font} That it passes the “so what” test" if researchq_sowhat == False:
                $ researchq_sowhat = True
                jump actOneWrapUpResearchQuestionRight
            
            "{font=SourceSansPro-Bold.ttf}Say:{/font} That it isn’t based off an opinion and, therefore, unanswerable" if researchq_opinion == False:
                $ researchq_opinion = True
                jump actOneWrapUpResearchQuestionRight
            
            "{font=SourceSansPro-Bold.ttf}Say:{/font} I can’t think of anything else." if researchq_yesno == True or researchq_sowhat == True or researchq_opinion == True:
                jump actOneWrapUpIsOver

label actOneWrapUpResearchQuestionRight:
    if researchq_yesno == researchq_sowhat == researchq_opinion == True:
        dw "That’s right!"
        jump actOneWrapUpResearchQuestionQuiz
    else:
        dw "That’s right! Anything else?"
        jump actOneWrapUpResearchQuestionQuiz
            
label actOneWrapUpIsOver:
    
    m "Thanks for the extra help."
    
    show windham happy
    with qdissolve
    dw "Great job, [name!q]. Now, for any basic questions about finding and using materials in Ingram Library, you can check with the circulation desk."
    if not persistent.achievement_actOne_complete_unlocked:
        $ persistent.achievement_actOne_complete_unlocked = True
        show achievement actOneComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
        sv "You just unlocked the “Act One Completed” achievement."
    dw "For more in depth questions, you might want to meet with a librarian. You can meet in-person or online via chat reference."
    jump actOneEnterPassword

label actOneEnterPassword:
    $player_pass = renpy.input("Please enter the password for Act Two and press  “Enter”", length=6)
    if player_pass.upper().strip() == actTwo_pass:
        stop music fadeout 0.8
        jump ActTwo
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump actOneEnterPassword