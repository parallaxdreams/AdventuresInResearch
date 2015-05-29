##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActThree:
    call setupGameVariables from _call_setupGameVariables_1
    $ name = persistent.playerName
    jump ActThree

label ActThree:

    $ save_name = "Name: %s.\nScene: Act 3." % (name)
    
    if not persistent.ActThree_unlocked:
       $ persistent.ActThree_unlocked = True

    scene bg blackSolid with fade
    scene bg ActThree with None
    $ renpy.pause(3.0)

    scene bg calendar with fade
    
    show calendar backing:
        xpos 0
        ypos 0
    
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -2.876
        pause 1.0
        ease 0.75 xpos -3.755
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(4.5)
    
    scene bg movieSet with fade
    $ save_name = "Name: %s.\nScene: Act 3 – Movie Set." % (name)
    play ambient "sfx/movieSet-ambient.ogg"
    play music "music/MovieSet.ogg"
    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {font=SourceSansPro-SemiboldItalic.ttf}Hmm...I’ve got about an hour before my next class. I guess I could go to the library, but it’s so nice outside today.{/font}":
            jump movieFilmingBegins

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {font=SourceSansPro-SemiboldItalic.ttf}Hey—isn’t that the movie crew that Tony was talking about earlier this week?{/font}":
            jump movieFilmingBegins

label movieFilmingBegins:
    show georgeblucas at rightthird
    with qdissolve
    d "I just really feel like six zebras are too much for this scene. They’ll dominate the...the...emotional landscape of the shot."
    show georgeblucas:
        parallel:
            alpha 1.0
            linear 0.35 alpha 0.0
        parallel:
            easein 0.80 xalign -1.0

    $ renpy.pause(0.8)
    cm "What about five zebras?"
    
    show georgeblucas faceRight:
        parallel:
            alpha 0.0
            linear 0.35 alpha 1.0
        parallel:
            easeout 0.25 xalign  0.1

    d "You know, that’s crazy...but it just might work."

    m "............................."
    
    hide georgeblucas
    with qdissolve
    
    m "{font=SourceSansPro-SemiboldItalic.ttf}What the heck is this movie about? Speaking of puzzling things, is that Kevin?{/font}"
    

    show kevin neutral at rightmid
    with qdissolve
    k "Hey, [name!q]. I’m running into everybody today! I just came across Jeff here as he was leaving the library."

    show jeff neutral at leftmid
    with qdissolve
    
    j "Yeah, I’m starting my project. Dr. Windham was right, it is taking longer than I expected."
    
    k "I’ve got my research question, but I feel like I should be further along in the actual research."
    
    j "We’ve got some time before the next class. Do you have your smartphone? Why don’t we check out some resources now?"
    
    show kevin happy
    with qdissolve
    k "Good idea! It’s really crazy the things we can do with technology these days, isn’t it?"
    k "We can do research outside! We could do research on a plane! On a train! On a—"
    
    show jeff concerned
    with qdissolve
    j "Yeah...that’s great, dude. Why don’t you start by trying to find a good website?"
    
    show kevin concerned
    with qdissolve
    k "Oh. Yeah. Sure thing."

    show jeff neutral
    with qdissolve
    k "Let’s see........."

    show kevin happy
    with qdissolve
    k "Hey! What about this website? Check it out."
    
    show jeff surprised
    with qdissolve
    j "Actually, you might want to rethink this website."
    
    show kevin surprised
    with qdissolve
    k "Why? it’s about my topic."

    show kevin happy
    with qdissolve
    k "And it plays music!"

    k "Check this out!"
    stop music
    play music "music/larry_hornblatz_website.ogg"
    
    show jeff concerned
    with qdissolve
    j "Because you need to evaluate your sources, that’s why."
    
    show kevin surprised
    with qdissolve
    k "What do you mean evaluate my sources? I picked it out of my results list because it looked like it had the most to do with my topic."
    
    show jeff neutral
    with qdissolve
    j "That’s a good start. You always want to make sure that any websites, books, scholarly articles, newspapers and so on that you use for your research project are relevant to your topic."
    j "But that is only the beginning."

    m "Hey, Kevin."

    show kevin concerned
    with qdissolve
    k "Yeah?"

    menu:
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Could you stop the music, please?":
            jump poorLarryH
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} This music is killing me. Make it stop.":
            jump poorLarryH
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I feel like I'm trapped in some old Atari game. Turn off the music NOW.":
            jump poorLarryH

label poorLarryH:
    show kevin surprised
    with qdissolve
    k "Oh, okay."
    stop music

    m "Thanks."

    show kevin concerned
    with qdissolve

    k "I’m still confused about this whole evaluation thing."

    play music "music/MovieSet.ogg"
    k "What else do I need to know?"
    
    j "For one thing, can you find who wrote that article?"
    
    k "There is a name here. I don’t know why that is important."
    
    j "Remember when Stephanie told you about different types of information?"
    j "There are books and articles that are scholarly, which means that they are more trustworthy because they’ve been written by experts in the field."
    
    show kevin confused
    with qdissolve
    k "Ah I think I’m getting it. So I want to make sure that I’m using websites and stuff that have been created by experts."
    
    menu:
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Why is that important? I'm not following.":
            #m "Why is that important? I'm not following."
            show jeff concerned
            with qdissolve
            j "Well think about why you do research in the first place. You have a position that you are trying to back up, right?"
            m "Right."
            show jeff neutral
            with qdissolve
            j "Don’t you want people who know what they are talking about to help you back up that argument?"
            j "They’ve really studied the issues that they are writing about, so there is a much better chance that what they publish is more trustworthy."
            jump Hornblatz
            
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think I know why using information from an expert is important.":
            #m "I think I know why using information from an expert is important."
            jump Hornblatz
            
label Hornblatz:
    
    show kevin neutral
    with qdissolve
    k "What if the person who made this website, Video Gamez R Kool, is a scholar? At the bottom of the screen it says the copyright on the material is held by Larry Hornblatz."
    
    show kevin happy
    with qdissolve
    k "Maybe he’s Dr. Larry Hornblatz!"
    
    j "Could be! When you have an author’s name and want to find out whether or not they are scholars or experts, you can always just Google them."
    show kevin neutral
    with qdissolve
    k "Well that seems easy enough. Let’s see."
    show kevin concerned
    with qdissolve
    k "Larry Hornblatz............."
    show kevin confused
    with qdissolve
    k "I don’t really see anything about him on Google at all."
    
    j "Well that could be a sign too."
    show jeff concerned
    with qdissolve
    j "If he was an expert on video games, don’t you think something would have come up about him on the internet?"
    
    show kevin concerned
    with qdissolve
    k "I suppose so. It’s just a bummer, look at this quote on the top of the Video Gamez R Kool website:"
    k "“Many people argue that violent video games cause people to do stuff like murder other people. Whoever says that is wrong, and a total NOOB.”"

    show kevin happy
    with qdissolve
    k "That is my argument exactly!"
    
    show jeff confused
    with qdissolve
    j "Exactly?"
    
    k "Exactly!"
    
    show jeff concerned
    with qdissolve
    j "Kevin, do you honestly think a professor would call someone a “NOOB” in a scholarly article?"
    j "Scholarly works are written for other scholars and students, so they use more technical language."
    
    show kevin concerned
    with qdissolve
    k "So, bigger words, basically."
    
    show jeff confused
    with qdissolve
    j "Well, I guess."
    
    show kevin neutral
    with qdissolve
    k "I get what you are saying, even though I would argue that “NOOB” is a technical term commonly used by video game practitioners."
    k "I guess I’m a NOOB at researching."
    
    menu:
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Everyone is a NOOB at some point.":
            k "That’s really deep, [name!q]!"
            jump noobTalk

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Hey, don’t put yourself down!":
            show kevin confused
            with qdissolve
            k "I suppose you are right. Everyone is a NOOB at everything at some point."
            show kevin neutral
            with qdissolve
            jump noobTalk


label noobTalk:

    show jeff neutral
    with qdissolve
    m "I know! But, anyway, to add to what Jeff was saying, looking at the language of something is another way to evaluate it."
    m "If the language has more discipline-specific terminology, chances are it is being written for an audience of other scholars."
    m "If it has more casual or informal language, chances are it was written for a general audience, so it is probably a popular source."
    
    show kevin concerned
    with qdissolve
    k "And it is important to think about the intended audience of something...why?"
    
    menu:
        
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I’m not sure, actually.":
            #m "I’m not sure, actually."
            j "Because different audiences have different information needs."
            j "Middle schoolers will need to know more basic information that involves less analysis than high school or college students."
            m "That makes sense. You have to go in a lot more detail on your papers in college than you did in high school."
            show kevin neutral
            with qdissolve
            jump PointOfView
            
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think I know why.":
            #m "I think I know why."
            m "Because different audiences have different information needs."
            m "Middle schoolers will need to know more basic information that involves less analysis than high school or college students."
            show kevin neutral
            with qdissolve
            k "That makes sense. You have to go in a lot more detail on your papers in college than you did in high school."
            jump PointOfView
            
label PointOfView:
    
    j "Also, thinking about the audience will help you figure out the author’s intention for writing."
    j "If the audience is other scholars or students, chances are the purpose is to educate, and add to a larger academic conversation."
    j "Authors might want the audience to buy something, or think in a certain way. When authors demonstrate bias, there is a very good chance that what they are writing isn’t trustworthy."
    
    m "There is another thing that’s bothering me about this website, Kevin."
    
    show kevin concerned
    with qdissolve
    k "What’s that?"
    
    m "The music seemed...old. When was the last time this website was updated?"
    
    k "Hmm, let’s see."
    $ vidgameyear = 2014-9
    k "Looks like it was last updated in [vidgameyear]. That’s not bad, right? Not even ten years!"
    
    show jeff confused
    with qdissolve
    j "Right, it’s 9 years. Which may as well be 90 years considering how much technology has changed since then."
    j "You are writing about technology—think about what video games were like in [vidgameyear]."
    
    show kevin confused
    with qdissolve
    k "Whoa. You are totally right!"
    show kevin neutral
    with qdissolve
    k "So what I’m hearing is that in addition to all that other stuff, I also need to pay attention to when something was published."
    show jeff neutral
    with qdissolve
    m "That makes sense to me. Think about if you were writing a paper on something medicine related, like the link between autism and vaccinations."
    m "Do you remember when all that was in the news a couple of years ago?"
    
    j "Right, there was an article that came out that linked vaccinations and autism and then it came out that the author’s data was incorrect."
    j "If you used his article as the basis for your argument, you would be totally wrong because you aren’t using the most recent information on the subject."
    
    k "So, even our scholars and experts can be wrong!"
    show kevin happy
    with qdissolve
    k "Larry Hornblatz is starting to look a little better, isn’t he?"
    
    show jeff concerned
    with qdissolve
    m "Umm...no."
    show kevin surprised
    with qdissolve

    show jeff neutral
    with qdissolve
    j "All this reminds me—in my LIBR 1101 class we had an acronym for remembering all of these evaluation criteria. It was CRAAP."
    
    show kevin concerned
    with qdissolve
    k "Come on, dude. Don’t say that. Someone probably worked really hard to come up with that acronym."
    
    show jeff confused
    with qdissolve
    j "No, Kevin, the acronym was CRAAP—C R A A P."
    show jeff neutral
    with qdissolve
    j "The “C” stands for currency, or remembering to look at the date of something when you evaluate it."
    j "The “R” stands for reliability, because we always have to think about if the information is biased or opinion based."
    j "Also reliability can be determined if the author includes his or her references, so we know where they are getting their information."
    
    show kevin neutral
    with qdissolve    
    k "Seems to me the “R” could also stand for “Relevancy”, which, if you’ll all remember, is the evaluation criteria that I got right off the bat."
    
    show jeff happy
    with qdissolve
    j "That’s actually a really good point, Kev. A website or article can be great, but it is worthless if it has nothing to do with your topic."
    
    m "What do the “A’s” stand for?"
    show jeff neutral
    with qdissolve
    j "The first “A” stands for Authority—who wrote the article? Are they an expert?"
    j "The second “A” stands for Accuracy—Is the information correct? Is it verified and supported by evidence?"
    j "And the “P” stands for Point of View and Purpose—who is the information being written for? And why is it being written? Is the author trying to sell you something?"
    
    m "You know, this is really useful info. I think I am going to write some of these evaluation criteria down."
    
    show kevin confused
    with qdissolve
    k "Okay, okay let me try searching for a different, better website."
    show kevin concerned
    with qdissolve
    k "What about this one?"
    show kevin neutral
    with qdissolve
    k "I Googled the author and found out that she is a professor. This article is published on an unbiased, reputable website."
    k "I can see that it was published recently so there is a good chance the information is up to date. No advertisements or corny music."
    
    show jeff happy
    with qdissolve
    j "You are right, this looks like a high quality website!"
    show kevin happy
    with qdissolve
    k "Yay me! You guys wanna grab a—"
    
    show georgeblucas at center
    with qdissolve
    d "No way! That’s not right!"
    
    show kevin surprised
    with qdissolve
    show jeff surprised
    with qdissolve
    cm "It is too right. Films are important because of the way they reflect the culture that produced them!"
    cm "They are tools that help us understand the world around us."

    d "That’s a nice idea, but it’s totally not true! Film shapes culture, it doesn’t reflect it. It is powerful because it can affect change!"
    show kevin concerned
    with qdissolve
    k "Hey guys, sorry to interrupt, but I’ve got my smartphone here, and as of a few minutes ago, I’m pretty handy with finding quality information on the internet."
    show kevin neutral
    with qdissolve
    k "I can find a website to help you guys see who is right!"
    
    show jeff concerned
    with qdissolve
    j "You know, for this situation, we might not want websites at all."
    j "It sounds like you each are taking a position and making an argument, so you’ll want scholarly information to back you up."
    j "We might need to find a book or a scholarly article."
    
    k "Okay, well, do you two want us to help you find a book that will help you solve your problems?"
    
    d "That’s a great idea."

    d "And Terry, when we find out that I’m right, you are wearing a chicken costume to set tomorrow."
    show georgeblucas:
        parallel:
            alpha 1.0
            linear 0.35 alpha 0.0
        parallel:
            easein 0.80 xalign -1.0
    $ renpy.pause(0.8)
    cm "So, you want me to play the giant chicken in the farmhouse nightmare scene?"
    show georgeblucas faceRight:
        parallel:
            alpha 0.0
            linear 0.35 alpha 1.0
        parallel:
            easeout 0.25 xalign  0.25
    d "Oh no, we actually have a real giant chicken for that."
    hide georgeblucas
    with qdissolve

    show jeff confused
    with qdissolve
    j "Man, what is this movie about?"
    
    m "It just keeps getting weirder and weirder."
    
    show jeff neutral
    with qdissolve
    j "Hey, [name!q] you have a smartphone too, don’t you? Maybe you can check the library’s catalog."
    
    m "Sure. I’ll start at the main library website page, westga.edu/library."
    
    show screenshot libraryHome
    with qdissolve
    j "Right."
    
    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Alright, I see the search box where I can look up things in the library catalog. Let’s jump right in.":
            show kevin concerned
            with qdissolve
            k "Wait, I’m a little lost. What are you talking about?"
            m "See that rectangular box in the middle of the screen? And that tab that says “books”?"
            m "That is where you can search the library catalog to see what books, DVDs, and government documents the library has."
            show kevin neutral
            with qdissolve
            jump usingTheCatalog

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I have no idea where to start.":
            j "See that rectangular box in the middle of the screen? And that tab that says “books”?"
            j "That is where you can search the library catalog to see what books, DVDs, and government documents the library has."
            jump usingTheCatalog
    
label usingTheCatalog:

    m "Okay, cool. So let’s search to see if they have any books about how film relates to culture."
    m "I’m just gonna type in “film” and “culture” here."
    hide screenshot libraryHome
    with qdissolve
    j "Alright, let’s take a look at the results from this search."
    j "It looks like we have three choices: {font=SourceSansPro-SemiboldItalic.ttf}Films and Libraries{/font}, {font=SourceSansPro-SemiboldItalic.ttf}Breaking in to the Movies: Film and the Culture of Politics{/font}, and {font=SourceSansPro-SemiboldItalic.ttf}Film Production{/font}. [name!q], what book do you think we should choose?"

    menu:

         j "[name!q], what book do you think we should choose?{fast}"

         "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} How about {font=SourceSansPro-SemiboldItalic.ttf}Films and Libraries {/font}?":
            j "I don’t know about that one, from the title, it seems to be more about suggesting what films libraries should have in their collections."
            j "Maybe {font=SourceSansPro-SemiboldItalic.ttf}Breaking in to the Movies: Film and the Culture of Politics{/font}?"
            j "The title looks relevant, anyway."
            j "Let’s click on it to see if we can get any more info on it."
            jump aboutThatBook

         "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What about {font=SourceSansPro-SemiboldItalic.ttf}Breaking in to the Movies: Film and the Culture of Politics{/font}?":
            if not persistent.achievement_appropriate_book_unlocked:
                $ persistent.achievement_appropriate_book_unlocked = True
                show achievement appropriateBook:
                    xalign 0.97 yalign 0.03
                    alpha 0.0
                    easeout 0.6 alpha 1.0
                    pause 2.0
                    easeout 0.9 alpha 0.0
                $ renpy.pause(0.1)
                play sndfx "sfx/achievement.ogg"
            j "That looks pretty good. The title looks relevant, anyway."
            j "Let’s click on it to see if we can get any more info on it."
            jump aboutThatBook

         "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Maybe the book called {font=SourceSansPro-SemiboldItalic.ttf}Film Production{/font}?":
            show jeff concerned
            with qdissolve
            j "Hmm I don’t know. The title makes it sound like it was written for people interested in the technical aspects of film, or breaking into the industry."
            j "Remember when we were evaluating things, and we said we needed to keep the audience in mind?"
            m "Good point. What about {font=SourceSansPro-SemiboldItalic.ttf}Breaking in to the Movies: Film and the Culture of Politics{/font}?"
            show jeff neutral
            with qdissolve
            j "That looks pretty good. The title looks relevant, anyway."
            j "Let’s click on it to see if we can get any more info on it."
            jump aboutThatBook

label aboutThatBook:
    
    show screenshot bookRecordCN
    with qdissolve
    k "Wow, there is a lot of information about that book."

    j "Once you click on the title of a book you are interested in, it takes you to what is called the “record.”"
    j "Here you can find when the book was published, who the author is, check out some similar items there on the right hand side, and, most importantly, get the book’s call number."
    jump importantPartsOfRecord

label importantPartsOfRecord:

    if author_important_asked == date_published_asked == similar_items_asked == call_number_asked == True:
        jump letsGoFindThatBook

    else:

        menu:

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Why is it important who the author is?" if author_important_asked == False:
                $ author_important_asked = True
                j "Well if you want to find a particular book, the author is a good way to make sure you have the book you want. Sometimes books have the same titles."
                jump importantPartsOfRecord

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Why is it important to know when the book was published?" if date_published_asked == False:
                $ date_published_asked = True
                j "For one thing, to make sure you have the right book, or the edition of the book you want."
                j "For a lot of projects you might want to make sure that you are working with the resources that have been most recently published and therefore are most up to date."
                jump importantPartsOfRecord

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Similar items?" if similar_items_asked == False:
                $ similar_items_asked = True
                j "Yeah, it’s pretty sweet. If you find a book you like, the library catalog suggests books that are similar to that book that you might want to check out."
                j "A lot of book records also have subjects listed. Do you see that?"
                m "Yeah."
                j "You can click on those to do a new search of books that are categorized with the same subject as the book you want."
                jump importantPartsOfRecord

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is the call number?" if call_number_asked == False:
                $ call_number_asked = True
                j "The call number is how you find your book."
                j "Books in the library are arranged according to the Library of Congress Classification system and are grouped by subject."
                j "So there is a good chance that once you find the book you want, there will be other books around it that will also be helpful."
                jump importantPartsOfRecord

label letsGoFindThatBook:

    j "A lot of book records will also let you see a table of contents, that way you can see if it is really a book you want."
    j "It looks like our book has a table of contents, do you want to check it out, [name!q]?"

    m "Sure."
    show screenshot bookRecordTOC
    with qdissolve
    m "Hmm...these chapters look pretty good. I say let’s check it out. It looks like I can text this call number to myself! How cool."
    m "I’ll go ahead and do that and we can head over to the library!"

    stop ambient fadeout 0.8
    stop music fadeout 0.8
    scene bg libraryStacks with fade
    $ save_name = "Name: %s.\nScene: Act 3 – Library." % (name)
    show jeff neutral at left
    show kevin concerned at right
    with qdissolve
    k "We have the book’s call number: PN1994 .G54 2002. How do we find the book using this string of letters and numbers?"
    
    j "First we need to see what floor it’s on. The book’s record we looked at earlier said this book was located in the stacks."
    j "It might also say it is located in the Government Documents section, Reference, Special Collections, etc."

    show kevin neutral
    with qdissolve
    k "Okay, so it is somewhere in the stacks. That’s two whole floors of books."

    j "Well you can also see in the book record that it says A-H books are on the 2nd floor and J-Z are on the 3rd floor."

    show kevin concerned
    with qdissolve
    k "A-H? J-Z?"

    j "Those refer to the first letter of the call number. Our call number begins with a “P” so it is on the 3rd floor."
    show kevin neutral
    with qdissolve
    k "I think I’m getting it. So we need to take our call number and then look for those little call number range signs on the sides of the bookshelves."

    m "You need to find the call number range that your particular call number falls within."

    k "That’s not too difficult, actually. I had worked myself up to think it was gonna be this huge deal."    

    m "No, it’s not that bad. It might take some time to find the book on the shelf, but once you do, you are set."
    m "And if you get stuck, you can always ask a librarian or someone else for help."
    
    k "Speaking of helpful librarians, there’s Stephanie. I bet she’ll be impressed at our mad book finding skills!"
    
    show jeff surprised
    with qdissolve
    j "She’s probably busy, maybe we shouldn’t bother—"
    
    k "Hey Stephanie!"
    
    show stephanie neutral at center
    with qdissolve
    s "Hi again you three."

    show jeff neutral    
    show kevin happy
    with qdissolve
    k "We just found an awesome book."
    
    s "Cool! Is this for your research project?"

    m "Actually no. We are helping the film crew solve an argument."
    
    s "I’m glad to see you are being generous with your researching skills! You might also want to think about finding a scholarly article in a database."
    s "If you want to come downstairs, I’ll walk you through how to use a database."

    show kevin neutral
    with qdissolve
    k "Actually that would be really helpful. I always get lost when I try to use those things on my own."
    
    scene bg libraryPCs with fade
    
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    show stephanie neutral at left
    show kevin neutral at center
    show jeff neutralleft at right
    with qdissolve
    s "Okay, Kevin. I’ll let you drive. Go ahead and head over to the library homepage."

    show screenshot libraryHome
    with qdissolve
    k "Alright. Done and done. What’s next?"

    show stephanie concerned
    with qdissolve
    s "We are looking for databases, where do you think we should go?"

    menu:

        s "We are looking for databases, where do you think we should go?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} GALILEO and Databases?":
            show stephanie neutral
            with qdissolve
            s "Right, go ahead and click that link on the left side of the screen, Kevin."
            jump gettingToDatabases

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} The library catalog?":
            show stephanie neutral
            with qdissolve
            s "No, we’d use that when we are searching for books, government documents, things like that. We want GALILEO and databases."
            s "Go ahead and click that link on the left side of the screen, Kevin."
            jump gettingToDatabases

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Google?":
            show stephanie happy
            with qdissolve
            s "Haha, not right this moment. It can be useful, but you can’t always find scholarly articles for free on Google."
            s "You can find the databases we subscribe to here by clicking on GALILEO and databases, though!"
            show stephanie neutral
            with qdissolve
            s "Go ahead and click that link on the left side of the screen, Kevin."
            jump gettingToDatabases

label gettingToDatabases:
    show screenshot galileoHome
    with qdissolve
    k "Got it."
    show kevin concerned
    with qdissolve
    k "Where to now? Do I just type in my search terms at the search box at the top of the screen?"

    show stephanie concerned
    with qdissolve
    s "That is certainly an option open to you. If you type it in, how many results to you get?"
    hide screenshot
    with qdissolve

    show kevin neutral
    with qdissolve
    k "Wow, 1.6 million results! That’s crazy! That’s like, Google-level crazy."

    show stephanie neutral
    with qdissolve
    s "That’s because this box is something called Discovery. It is a tool that searches a bunch of databases at once."
    s "It can be useful when you want to look at your topic from a number of different perspectives."
    s "You almost always want to use the options on the left side of the screen to narrow your search, though."

    show jeff happyleft
    with qdissolve
    j "Right, so we have the option to narrow our results to only things that were published in Scholarly (Peer-Reviewed) Journals."
    show jeff neutralleft
    with qdissolve
    j "That’s handy when a professor asks for scholarly articles."

    s "For that matter, you can also narrow to magazines, newspapers, things like that if you need to."
    s "You can also use the slider to narrow your results to specific publication dates."

    show kevin confused
    with qdissolve
    k "Why would you want to do that?"

    s "Some professors will ask that you only find articles published in the last ten years or so."
    s "As time goes by, new things get published about certain topics and sometimes they make older research obsolete."
    show kevin neutral
    with qdissolve
    j "I think we talked about this before, didn’t we? How this is especially true for things like the sciences."

    show stephanie happy
    with qdissolve
    s "Sounds right! Anyway, all that is to say there are a number of different things you can do here to bring your number down quite a bit."
    show stephanie neutral
    with qdissolve
    s "Unless you add more search terms, or narrow your topic, though, there are still going to be more results than you can get through."
    s "That’s why we want to focus on one specific database."

    k "Okay, I’m going back to where we were before we searched the Discovery tool."
    show screenshot galileoHome
    with qdissolve
    k "How can I find a specific database?"

    show stephanie concerned
    with qdissolve
    s "That’s a great question, Kevin. Have you guys been exploring GALILEO?"
    
    hide screenshot
    with qdissolve
    show kevin concerned
    with qdissolve
    k "That’s the guy who invented the telescope, right?"
    
    show stephanie happy
    with qdissolve
    s "Haha, that’s right. But the GALILEO to which I was referring is not a {font=SourceSansPro-SemiboldItalic.ttf}guy{/font}, it stands for Georgia Library Learning Online. With some capitalization tweaking, anyway."
    
    m "Oh, I know what you are talking about. That’s the database we use to search for scholarly articles and other online resources, right?"
    
    show stephanie surprised
    with qdissolve
    s "Actually, no. Not to be nitpicky, but GALILEO isn’t a database."
    show stephanie neutral
    with qdissolve
    s "It’s more of an online portal to databases that we have to pay to subscribe to."
    s "GALILEO is paid for with a mixture of tax dollars and your tuition money, so you should get as much use out of it as you can."
    
    m "I’m confused. If GALILEO isn’t a database, then what is?"
    
    s "Databases are things like Academic Search Complete, or PsychINFO, both of which are provided to us through EBSCOhost."
    s "People sometimes say they want to search EBSCO, but this is the company name, not the database name. EBSCO owns many databases."
    s "You follow?"
    show jeff happyleft
    with qdissolve
    j "I always forget that each database has its own name. It helps to remember that a lot of databases are focused on a subject, like history or chemistry."
    
    #s "Right. And Academic Search Complete is an interdisciplinary database, which means you can search a lot of different subjects."

    j "If you know the name of the database you want, you can look it up in the Database A-Z list."

    show stephanie happy
    with qdissolve
    s "That’s right, Jeff. If you don’t know which database you want, though, you can search by subject, or by type."
    show jeff neutralleft
    with qdissolve

    k "Type?"

    show stephanie neutral
    with qdissolve
    s "Like, databases that contain newspapers, or reference databases, or biographical information."
    s "There are many different kinds of databases. Let’s check one out. I’m going to take you all to a database called Academic Search Complete."

    show kevin neutral
    with qdissolve
    k "Oh, I’ve heard of that!"
    show screenshot galileoHome
    with qdissolve
    s "Great! Since we know the name of the database we want we can find it by looking at Databases A-Z and then “A” for Academic Search Complete."

    k "Okay...let me see."
    show screenshot acCompleteHome
    with qdissolve
    k "Got it. Hey, this kind of looks like the Discovery tool we just used. Am I going to get a million results here?"

    s "No, not here. This is only going to search one database, where Discovery searched tens, if not hundreds. Academic Search Complete is actually neither completely academic nor complete, but for our purposes it will do the trick."
    s "It’s a multidisciplinary database, so it covers a lot of different subjects."

    k "Okay so I’m just going to try to put in the same search terms we used earlier: “film” and “culture”."
    k "Let’s see!"
    hide screenshot
    with qdissolve
    k "Hmm...I still get almost 16,000 results."

    show stephanie concerned
    with qdissolve
    s "Well, what can we glean from this? What do you think, [name!q]?"

    menu:

        s "Well, what can we glean from this? What do you think, [name!q]?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} That we should just give up this searching databases stuff and use Google already. This is too much work, see ya.":
            show stephanie surprised
            show kevin surprised
            show jeff surprisedleft
            stop music fadeout 0.8
            stop ambient fadeout 0.8
            jump sharkDentistEnding

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think it means that our search is too broad, or too vague.":
            show stephanie neutral
            with qdissolve
            s "I agree. From what I’m hearing about the kinds of info you want, instead of “film” and “culture” you want to look into film theory."
            s "You’d probably figure that out with presearching, but it seems like we are on a time crunch."
            s "It would be even better if you had an idea of what you meant by culture or if you had specific kinds of film or even specific films themselves to search."
            jump moreDatabaseSearching

label sharkDentistEnding:
    
    scene bg blackSolid with fade
    $ save_name = "Name: %s.\nScene: Bad Ending 3." % (name)
    scene bg tenYrsLater with fade

    $ renpy.pause(2.0)

    scene bg blackSolid with fade

    scene bg sharkDentist with fade
    #play ambient "sfx/underwater-ambient.ogg"
    play music "music/Shark.ogg" noloop
    m "{font=SourceSansPro-SemiboldItalic.ttf}All my friends were so concerned when I gave up on using databases for searching, but I think everything turned out alright.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Sure, I failed out of college and the only job I could get is as a dental assistant for sharks but, you know, at least I get to interact with wildlife.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}And I really think having ten fingers is kind of greedy. Yeah, that was definitely the right decision. Now, have they fed the shark yet? He gets bitey when he’s hungry....{/font}"
    
    "Game Over"
    if not persistent.achievement_bad_end3_unlocked:
        $ persistent.achievement_bad_end3_unlocked = True
        show achievement badEnd3:
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
            jump resultsTryAgain

label resultsTryAgain:
    $ save_name = "Name: %s.\nScene: Act 3 – Library." % (name)
    scene bg libraryPCs with fade
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    show stephanie concerned at left
    show kevin neutral at center
    show jeff neutralleft at right
    with qdissolve
    
    menu:

        s "Well, what can we glean from this? What do you think, [name!q]?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think it means that our search is too broad, or too vague.":
            show stephanie neutral
            with qdissolve
            s "I agree. From what I’m hearing about the kinds of info you want, instead of “film” and “culture” you want to look into film theory."
            s "You’d probably figure that out with presearching, but it seems like we are on a time crunch."
            s "It would be even better if you had an idea of what you meant by culture or if you had specific kinds of film or even specific films themselves to search."
            jump moreDatabaseSearching

label moreDatabaseSearching:

    show kevin concerned
    with qdissolve
    k "Hmm yeah, we probably should have asked that. Even so, we are getting results that look interesting."
    show kevin neutral
    with qdissolve
    k "Here’s one called “Social Class, Cultural Repertoires, and Popular Culture: The Case of Film.”"

    s "That might work."
    s "It looks like this article is available as a PDF. You can email that article to yourself or print it out and read it through before you give it to the film crew."

    k "No time! I’ll just grab that one and...let’s see...this one, “Global Trauma and Narrative Cinema” and print them out and let the film crew work it out."
    
    show kevin confused
    with qdissolve
    k "Wait, where is the article?"

    show stephanie concerned
    with qdissolve
    s "Ahh yes, you don’t see the article because it isn’t here. That doesn’t mean that we don’t have it at all, though—it might be in a different database."

    show kevin concerned
    show jeff happyleft
    with qdissolve
    j "I remember this—you can click that button that says “Find it UWG” and if we have it, it will pop up there."

    show jeff neutralleft
    with qdissolve
    k "Looks like we don’t have it. I guess I’d have to order it from InterLibrary Loan. If I had the time, I mean. Oh well, they’ll have to deal with just this one."

    show stephanie neutral
    with qdissolve
    s "If you click on the article, you can see some more information about it."
    show screenshot acCompleteRecord
    with qdissolve
    s "This is called the record, and it is kinda like a book record in that it contains a lot of info about the item."
    s "We don’t have immediate access to this article, but you can use the subject terms or author-provided keywords to do a search for things like this article."

    show jeff happyleft
    with qdissolve
    j "Another thing that is pretty cool here is that you can click that link on the right that says “cite” and it will tell you how to cite the article."
    hide screenshot
    with qdissolve
    j "All you have to do is copy and paste it into your bibliography."

    show stephanie concerned
    with qdissolve
    s "Not so fast there."
    show jeff surprisedleft
    with qdissolve
    s "It is a really useful tool, but they usually aren’t 100%% right."

    s "They can take a lot of the footwork out of putting the citations together, but you’ll still want to check it against a style guide."
    show jeff neutralleft
    with qdissolve

    show kevin neutral
    with qdissolve
    k "Wow, that is actually really awesome."

    show stephanie neutral
    with qdissolve
    s "Well, we’ve found the info we need pretty quickly, but for longer research projects, it’s not so easy and quick."
    s "For the paper that you guys are working on, you’ll probably want to explore a few different databases."
    
    show kevin happy
    with qdissolve
    k "I can do that! Thanks a lot for your help, Stephanie!"

    s "You’re welcome! If you need more help, we have walk-in research office hours Monday-Thursday from 11-5."
    show kevin neutral
    with qdissolve
    k "I’m gonna go run this info to the movie crew. I’ll catch you all later."
    
    j "Bye, Kevin."

    play sndfx "sfx/cb_tone.ogg"
    m "See ya, Kev."
    hide kevin
    with qdissolve
    
    m "Oh, I’m so sorry Stephanie, I’m getting a Chatterbox message. I’ll check out those librarian office hours the next time I get stuck."
    
    show stephanie happy
    with qdissolve
    s "Sounds great! I’ll see you all later. Good luck with your research!"
    
    m "Thanks Stephanie! See you later. Probably tomorrow."
    
    j "Thanks again, Stephanie!"
    
    hide stephanie
    with qdissolve
    
    play sndfx "sfx/cb_tone.ogg"
    cbkana "Hey, [name!q] what are you up to?"
    
    m "Hey Jeff, the Chatterbox message is from Kana!"

    j "What’s she up to?"

    m "Hang on a sec, I’ll find out."

    play sndfx "sfx/cb_sent_tone.ogg"
    cbkme "Hi Kana. I’m in the library with Jeff."
    
    play sndfx "sfx/cb_tone.ogg"
    cbkana "I’m in the library too. I was gonna see if you wanted to meet up to work on our projects?"
    
    play sndfx "sfx/cb_sent_tone.ogg"
    cbkme "Sure we are on the first floor near the computers, wanna meet us here?"
    
    play sndfx "sfx/cb_tone.ogg"
    cbkana "Sure! See you in a sec"
    
    m "Kana’s gonna meet us down here to work on our projects."
    
    j "She was in my LIBR 1101 class last semester, so she should be able to help us navigate GALILEO."
    
    m "Cool. Well while we are waiting for her, maybe we can search GALILEO?"
    
    j "Remember, Stephanie said we should pick a specific database. Click “Browse by Subject”."

    show kana happy at leftmid
    with qdissolve
    ka "Hi, you two."

    j "That was fast! Hey Kana, we were just talking about subject specific databases. Do you use them for art?"
    
    show kana neutral
    with qdissolve
    ka "Yeah, I use the database Art Full Text all the time."
    ka "When I’m researching artists or specific works of art, it is much faster to search a database dedicated only to art."
    ka "Saves a lot of time, and I get much better results than I would in a database like Academic Search Complete or Proquest Research Library."
    ka "I found Art Full Text on the art research guide, actually."
    
    m "What’s a research guide?"
    
    ka "A research guide is a collection of resources related to a certain discipline, subject, or class put together by a librarian who knows a lot about that topic."

    m "Oh, is it that list of resources that comes up when you search for databases in GALILEO by subject?"


    ka "Actually, no. But it is the same kind of idea."
    ka "If you go to the library homepage, you’ll see a link that says “research guides” near where you search for books."
    ka "Once you click on that link you can type in a subject like “art” or “history” and it will pull up a list of research guides that relate to that subject."

    j "You can also browse research guides by subject too."

    m "So they are both lists of resources relating to a topic. I guess I don’t understand what the difference is between them."

    ka "The main difference is that librarians create the research guides."
    ka "GALILEO lists most of the resources the library has access to that relate to a topic, but that is going to be a huge list."

    show jeff happyleft
    with qdissolve
    j "Right, and not all of the things on the GALILEO subject lists are going to be relevant."
    show jeff neutralleft
    with qdissolve
    j "Research guides are made up of resources that a librarian has decided are the best for a particular subject, or even a class."
    j "Also, the resources listed on research guides are usually in order of relevance, or importance."

    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Research guides sound interesting, I’m going to go check one out that relates to my topic.":
            jump databaseSearching

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} That sounds like it might be cool. I’ll check it out later.":
            jump databaseSearching

label databaseSearching:

    j "So, Kana, when you are searching in the databases, what keywords were you using?"

    show kana confused
    with qdissolve
    ka "Keywords?"

    show jeff confusedleft
    with qdissolve
    j "We talked about them in LIBR 1101, keywords are like your search terms."

    show kana neutral
    with qdissolve
    ka "Oh, duh. That’s right. Well I decided to look up things like censorship, museums, paintings, sculpture, first amendment—"
    show jeff neutralleft
    with qdissolve
    m "Wait, didn’t you say you were writing about censorship of art in museums? Why did you choose those keywords?"

    ka "What keywords would you use?"

    menu:

        ka "What keywords would you use?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Censorship of art in museums":
            show jeff concernedleft
            with qdissolve
            j "I don’t know about that, actually. You never want to search for whole phrases or questions."
            m "Oh, you are right. The keywords are the most important words or ideas in your research question."
            show jeff neutralleft
            with qdissolve
            m "That still doesn’t explain why you searched for things like “sculpture” and “first amendment”"
            jump searchingWithKeywords
       
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Censor, art, museums":
            ka "I searched for those too, they are the most important ideas and words in my research question."
            ka "Those aren’t the only words I can use in my search though."
            jump searchingWithKeywords


label searchingWithKeywords:

    ka "You always have to think about the fact that the way you describe something might not be the way someone else would describe something."
    ka "You don’t want to just stop at the words in your research question and their synonyms, you also want to think about related concepts."
    ka "For instance, sculpture is a kind of art, and the first amendment is the issue that my paper is focused on."

    m "I think I understand. So the next time I’m searching for something and I get totally stuck and can’t find anything, I can go back and try to think of different keywords to use in my search."

    j "Right. Or you can just start by brainstorming keywords and you can use Boolean operators to search them all at once."

    m "What kind of operators?"

    show jeff happyleft
    with qdissolve
    j "Boolean. It’s a fun word. Try it."

    m "Boolean."

    show kana happy
    with qdissolve
    ka "Boooooolean."

    show kana neutral
    with qdissolve
    m "It is a pretty fun word."

    show kana happy
    with qdissolve
    ka "You know what else is fun? The story of how George Boole died!"

    show jeff concernedleft
    with qdissolve
    m "Umm...really?"

    show kana neutral
    with qdissolve
    ka "Boole was so dedicated to teaching that one day he walked through a rainstorm to get to his class. He taught soaking wet and got sick."
    ka "Boole’s wife believed that you had to cure someone by using that which caused the illness. So, she kept him soaking wet while he was sick in bed and he died!"

    m "Sounds like she should have been more critical about where she got her medical information."

    show jeff neutralleft
    with qdissolve
    j "Right? Anyway, Boolean operators are “AND”, “OR”, and “NOT”. You use them in the library catalog and in databases to narrow or broaden your search."

    m "Keep going. I’m not sure I follow yet."

    ka "Okay, think about how the search boxes are set up in a database. There are usually a few different boxes on different lines, right?"

    m "Right."

    play sndfx "sfx/cb_tone.ogg"
    ka "In between those boxes are usually drop-down menus where you can choose a Boolean operator."

    play sndfx "sfx/cb_tone.ogg"
    m "Hey, I’m getting a Chatterbox message from Tony."

    m "He says the movie needs some extras, do you guys want to go?"
    
    show jeff concernedleft
    with qdissolve
    j "After the stuff we heard the movie crew talking about today, I’m a little nervous."
    show jeff happyleft
    with qdissolve
    j "But sure, why not? I could use a break."
    
    show kana happy
    with qdissolve
    ka "Me too, that should be fun!"

    stop ambient fadeout 0.8
    stop music fadeout 0.8
    scene bg movieSetExtras with fade
    $ save_name = "Name: %s.\nScene: Act 3 – Movie Set." % (name)
    play ambient "sfx/movieSet-ambient.ogg"
    play music "music/MovieSet.ogg"
    show booleanEveryone at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)

    m "Here we are. Looks like there was a pretty big turnout for extras, I think we might be too late."

    show jeff neutral at Position(xpos=0.33, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show kana neutral at Position(xpos=0.15, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with qdissolve

    ka " Well, if we can’t be movie stars, we can still take advantage of all these people in costume."
    ka "This could be a pretty useful set up to help us think about how Boolean operators work!"
    
    m "Say what?"

    ka "Let’s think about this in terms of the extras over there, those men talking to those women."

    m "Okay..."

    ka "Cool. So let’s say that each person is a keyword, a search term."

    ka "Let’s start by saying we want everyone wearing pants in the shot."
    hide booleanEveryone
    show booleanPants at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve

    m "Wait, how did that happen?"

    show kana happy
    with qdissolve
    ka "The power of imagination. Just go with me here."

    m "But—"

    show kana neutral
    with qdissolve


    ka "Anyway, now let’s say that I want everyone with pants AND a blue shirt in the shot."

    hide booleanPants
    show booleanPantsANDblueShirt at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve

    ka "What happened?"

    menu:

        ka "What happened?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} All that guy’s friends went away.":
            jump BooleanContinues

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} You got fewer people in the shot.":
            jump BooleanContinues

label BooleanContinues:

    ka "Right, so you can begin to see how “AND” narrows a search. I used AND here and went from three people to one by adding another search term."
    ka "What do you think will happen if I use “OR”?"

    menu:

        ka "What do you think will happen if I use “OR”?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I have no idea":
            jump moreBooleanStuff

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} You’ll have more people in the shot?":
            jump moreBooleanStuff

label moreBooleanStuff:

    ka "Let’s see!"

    ka "So let’s start by saying that I want everyone with a blue shirt in the shot."

    hide booleanPantsANDblueShirt
    show booleanBlueShirt at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve

    ka "How many people do I have?"

    j "Two."


    ka "Right."


    ka "Now, let’s say that I want everyone with a blue shirt OR a skirt."

    hide booleanBlueShirt
    show booleanBlueShirtORskirt at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve

    ka "How many people are in the shot?"


    m "Four."

    ka "Right again! “OR” makes it so you are searching for instances where any of your search terms are present."
    ka "It broadens your search, and sometimes can broaden it quite a bit."

    ka "Let’s say I want men OR women in the shot..."
    hide booleanBlueShirtORskirt
    show booleanWomenORmen at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve
    

    j "So the broader your search term—here, men and women are much less specific than the kinds or colors of the clothes they are wearing—the more results you will get."
    j "That’s true for “AND” too."

    ka "Exactly."

    ka "So, the last Boolean operator is “NOT”. Do you have an idea of how that might work, [name!q]?"

    menu:

        ka "So, the last Boolean operator is “NOT”. Do you have an idea of how that might work, [name!q]?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} No.":
            ka "Well, let’s go back to our extras. Let’s start by saying I want women in the shot."
            hide booleanWomenORmen
            show booleanWomen at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
            with dissolve
            ka "Now, let’s say I want all women but NOT ones wearing pink."
            jump BooleanNot

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I think so.":
            m "Let’s go back to our extras. Let’s start by saying I want women in the shot."
            hide booleanWomenORmen
            show booleanWomen at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
            with dissolve
            m "Now, let’s say I want all women but NOT ones wearing pink."
            jump BooleanNot

label BooleanNot:

    hide booleanWomen
    show booleanWomenNOTpink at Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    with dissolve

    m "We lost one of the women. So “NOT” narrows the search too."

    ka "Right. More specifically, it excludes irrelevant results."
    ka "For example, if you did a search about “kids diets” depending on the database, you’d probably get a lot of results about baby goats."

    m "Baby goats are called kids?"

    ka "Yes, it is pretty adorable."

    m "So if I searched for “kids” AND “diets” NOT “goats” I’d get things about human kids, not goat kids."

    ka "Right. And I liked that you picked up on the fact that you can combine these Boolean operators to get better results!"

    j "Okay, [name!q], can you sum up how Boolean operators affect a search?"
    j "What does “AND” do?"

    menu:

        j "What does “AND” do?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “AND” narrows the search.":
            $ boolean_and_right = True
            j "Right! When you use “AND” you are telling the database or catalog that you want to find every time your search terms are together."
            jump BooleanQuizOR

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “AND” broadens the search.":
            j "Actually, no."
            j "When you use “AND” you are telling the database or catalog that you want to find every time your search terms are together."
            j "It narrows the search."
            jump BooleanQuizOR


label BooleanQuizOR:

    j "Okay, what about “OR”?"

    menu:

        j "Okay, what about “OR”?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “OR” narrows the search.":
            j "Actually, no."
            j "When you use “OR” you are telling the database or catalog that you want to find every time either one of your search terms turn up somewhere."
            j "It broadens the search, sometimes by a lot."
            jump BooleanQuizNot

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “OR” broadens the search.":
            $ boolean_or_right = True
            j "Right! When you use “OR” you are telling the database or catalog that you want to find every time either one of your search terms turn up somewhere."
            j "It broadens the search, sometimes by a lot."
            jump BooleanQuizNot

label BooleanQuizNot:

    j "What about “NOT”?"

    menu:

        j "What about “NOT”?{fast}"

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “NOT” narrows the search.":
            $ boolean_not_right = True
            j "Right! When you use “NOT” you are telling the database or catalog that you want to exclude certain words or related ideas."
            j "It helps focus your search."
            jump doneWithBoolean

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} “NOT” broadens the search.":
            j "Actually, no."
            j "When you use “NOT” you are telling the database or catalog that you want to exclude certain words or related ideas."
            j "It helps focus your search."
            jump doneWithBoolean

label doneWithBoolean:
    if boolean_and_right == boolean_or_right == boolean_not_right == True:
        if not persistent.achievement_boolean_expert_unlocked:
            $ persistent.achievement_boolean_expert_unlocked = True
            show achievement booleanExpert:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
    m "Kana, Jeff, thanks a lot for your help."
    m "Boolean is kind of a tricky concept, but I think I’m getting the hang of it."

    j "No prob."

    show kana happy
    with qdissolve
    ka "Happy to help!"
    
    m "Well guys, I think I’m gonna head back to the library. See you later!"
    
    ka "See ya!"
    
    show jeff happy
    with qdissolve
    j "See you later."
    
    stop music fadeout 0.8
    stop ambient fadeout 0.8
    scene bg libraryPCs with fade
    $ save_name = "Name: %s.\nScene: Act 3 – Library." % (name)
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Maybe it’s a movie about female zebras who get kidnapped from the zoo and whisked away in hot air balloons.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}They crash land at a farm in rural Georgia only to find out that the farmers have been doing crazy experiments on their livestock.{/font}"
    
    m ".................................."
    
    m "{font=SourceSansPro-SemiboldItalic.ttf}Anyway, I should probably organize all my notes on all the research stuff I learned today.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Ugh, what a mess. I just can’t get my mind around it.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Hey! I know! I’ll try that online chat reference service. It’s supposed to be available 24/7.{/font}"
    m "{font=SourceSansPro-SemiboldItalic.ttf}Let’s see, I’ve gotta go to the library homepage.{/font}"
    show screenshot libraryHome
    with qdissolve
    m "{font=SourceSansPro-SemiboldItalic.ttf}Ah! There it is. That’s easy. I guess I’ll just type in my question and see how it goes.{/font}"
    
    jump chattingLibrarian

label chattingLibrarian:

    if chat_crap_asked == chat_scholarly_asked == chat_keywords_asked == chat_galileo_asked == chat_subjdbase_asked == chat_boolean_asked == True:
        if not persistent.achievement_chatty_cathy_unlocked:
            $ persistent.achievement_chatty_cathy_unlocked = True
            show achievement chattyCathy:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
        m "That’s all. Thanks a lot Laura!"
        l "You’re welcome!"
        jump actThreeWrapUp

    else:

        menu:

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} My friends mentioned that there was this acronym to help them remember what all they need to do to evaluate information. I think it was called CRAAP. Do you know what those letters stand for again?" if chat_crap_asked == False: 
                $chat_crap_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "I know all about the CRAAP test!"
                    l "Here’s what all the letters in the acronym stand for:"
                    l "(C)urrency—How recent is the information?; How recently has the website been updated?; Is it current enough for your topic?"
                    l "(R)eliability—What kind of information is included in the resource?; Is content of the resource primarily opinion? Is is balanced?; Does the creator provide references or sources for data or quotations?"
                    l "(A)uthority—Who is the creator or author?; What are the credentials?; Who is the publisher or sponsor?; Are they reputable?; What is the publisher’s interest (if any) in this information?; Are there advertisements on the website?"
                    l "(A)ccuracy—Is the information correct? Where did it come from? Are the author’s claims supported by evidence? Has it been reviewed or checked? Is grammar/spelling/punctuation correct?"
                    l "(P)urpose/Point of View—Is this fact or opinion?; Is it biased? Is the creator/author trying to sell you something?"
                    l "Can I help you with anything else?"
                    jump chattingLibrarian
                else:
                    l "I know all about the CRAAP test!"
                    l "Here’s what all the letters in the acronym stand for:"
                    l "(C)urrency—How recent is the information?; How recently has the website been updated?; Is it current enough for your topic?"
                    l "(R)eliability—What kind of information is included in the resource?; Is content of the resource primarily opinion? Is is balanced?; Does the creator provide references or sources for data or quotations?"
                    l "(A)uthority—Who is the creator or author?; What are the credentials?; Who is the published or sponsor?; Are they reputable?; What is the publisher’s interest (if any) in this information?; Are there advertisements on the website?"
                    l "(A)ccuracy—Is the information correct? Where did it come from? Are the author’s claims supported by evidence? Has it been reviewed or checked? Is grammar/spelling/punctuation correct?"
                    l "(P)urpose/Point of View—Is this fact or opinion?; Is it biased? Is the creator/author trying to sell you something?"
                    l "Can I help you with anything else?"
                    jump chattingLibrarian

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} How can I tell if something I’m reading is scholarly?" if chat_scholarly_asked == False:
                $ chat_scholarly_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "There are a few things to keep in mind when you are trying to determine if your resource is scholarly."
                    l "Scholarly materials have been written by scholars or experts, so often the author will be a doctor or a professor."
                    l "Scholarly materials are also often longer, use technical language or jargon, do not have many pictures or ads, and usually cite their sources and have some kind of bibliography."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian
                else:
                    l "There are a few things to keep in mind when you are trying to determine if your resource is scholarly."
                    l "Scholarly materials have been written by scholars or experts, so often the author will be a doctor or a professor."
                    l "Scholarly materials are also often longer, use technical language or jargon, do not have many pictures or ads, and usually cite their sources and have some kind of bibliography."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} How do I come up with keywords?" if chat_keywords_asked == False:
                $ chat_keywords_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "Well you want to start with your research question, or topic."
                    l "Think about what the main words or ideas from your research question are—those are your keywords."
                    l "The way you describe something could be different than the way that someone else might describe something, so you’ll also want to think of some synonyms for your keywords and also some related concepts."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian
                else:
                    l "Well you want to start with your research question, or topic."
                    l "Think about what the main words or ideas from your research question are—those are your keywords."
                    l "The way you describe something could be different than the way that someone else might describe something, so you’ll also want to think of some synonyms for your keywords and also some related concepts."
                    l "Can I help you with anything else?" 
                    jump chattingLibrarian

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} What is GALILEO?" if chat_galileo_asked == False:
                $ chat_galileo_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "GALILEO stands for Georgia Library Learning Online and it is an online portal to databases that schools and libraries in the state of Georgia subscribe to."
                    l "GALILEO contains databases, databases contain journals, and journals contains articles."
                    l "Can I help you with anything else?" 
                    jump chattingLibrarian
                else:
                    l "GALILEO stands for Georgia Library Learning Online and it is an online portal to databases that schools and libraries in the state of Georgia subscribe to."
                    l "GALILEO contains databases, databases contain journals, and journals contains articles."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian  

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} What’s a subject specific database, and why would I want to use it?" if chat_subjdbase_asked == False:
                $ chat_subjdbase_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "Subject specific databases are what they sound like—databases that contain resources that relate to a certain subject or discipline."
                    l "It might help to think about these next to something like Academic Search Complete, which is a multidisciplinary database that has resources for all kinds of subjects—psychology, history, science, English, etc."
                    l "You can think of Academic Search Complete like a big department store—you can get a bit of everything there and often you can get something good enough for what you need."
                    l "Let’s say you are a marathon runner, though, and you need a pair high quality running shoes. You’d probably want to find a store that specializes in running shoes to have the best chance that you’ll get the shoe you want."
                    l "The speciality store is like a subject specific database."
                    l "More often than not, you’ll want to search subject specific databases in your research, especially when you are farther along in your major."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian
                else: 
                    l "Subject specific databases are what they sound like—databases that contain resources that relate to a certain subject or discipline."
                    l "It might help to think about these next to something like Academic Search Complete, which is a multidisciplinary database that has resources for all kinds of subjects—psychology, history, science, English, etc."
                    l "You can think of Academic Search Complete like a big department store—you can get a bit of everything there and often you can get something good enough for what you need."
                    l "Let’s say you are a marathon runner, though, and you need a pair high quality running shoes. You’d probably want to find a store that specializes in running shoes to have the best chance that you’ll get the shoe you want."
                    l "The speciality store is like a subject specific database."
                    l "More often than not, you’ll want to search subject specific databases in your research, especially when you are farther along in your major."
                    l "Can I help you with anything else?"
                    jump chattingLibrarian

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} What are Boolean Operators and how do they affect my search?" if chat_boolean_asked == False:
                $ chat_boolean_asked = True
                if first_chat == True:
                    $ first_chat = False 
                    l "Hi [name!q], I’m Laura from Olympia, Washington."
                    l "I’m a part of a cooperative of libraries that help each other answer their patrons’ reference questions."
                    l "I’m reading your question and will be with you shortly."
                    l "Boolean operators are words that help you narrow or broaden your search as needed."
                    l "AND and NOT both narrow your search, and OR broadens your search."
                    jump chattingLibrarian
                else:
                    l "Boolean operators are words that help you narrow or broaden your search as needed."
                    l "“AND” and “NOT” both narrow your search, and “OR” broadens your search."
                    jump chattingLibrarian

            "{font=SourceSansPro-Bold.ttf}[name!q] types:{/font} That’s all. Thanks a lot Laura!" if chat_crap_asked == True or chat_scholarly_asked == True or chat_keywords_asked == True or chat_galileo_asked == True or chat_subjdbase_asked == True or chat_boolean_asked == True:
                l "You’re welcome!"
                jump actThreeWrapUp

label actThreeWrapUp:
    if not persistent.achievement_actThree_complete_unlocked:
        $ persistent.achievement_actThree_complete_unlocked = True
        show achievement actThreeComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
    jump actThreeEnterPassword

label actThreeEnterPassword:
    $player_pass = renpy.input("Please enter the password for Act Four and press “Enter”", length=6)
    if player_pass.upper().strip() == actFour_pass:
        stop ambient fadeout 0.8
        stop music fadeout 0.8
        jump ActFour
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump actThreeEnterPassword