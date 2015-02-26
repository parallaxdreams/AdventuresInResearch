##
## Adventures in Research (2012-2015)
## by Dean Sullivan and Jessica Critten
## (dsulliva@westga.edu) and (jcritten@westga.edu)
## University of West Georgia
##

#######################################################################

#This label is only triggered from Act Selection Screen and needs to pull player name from persistent variable.
label restartActFour:
    call setupGameVariables
    $ name = persistent.playerName
    jump ActFour

label ActFour:

    $ save_name = "Name: %s\nScene: Act IV" % (name)

    if not persistent.ActFour_unlocked:
       $ persistent.ActFour_unlocked = True

    scene bg blackSolid with fade
    scene bg ActFour with fade
    $ renpy.pause(3.0)

    scene bg calendar with fade

    show calendar backing:
        xpos 0
        ypos 0
    
    #Can reuse this show statement with different atl settings for other dates in game
    show calendar dates:
        xpos -3.755
        pause 1.0
        ease 1.20 xpos -5.225
        #pause 5.0
    
    show calendar_alpha
    $ renpy.pause(4.5)

    scene bg classroom with fade
    $ save_name = "Name: %s\nScene: Act IV – Classroom" % (name)
    play music "music/Classroom.ogg" noloop
    show windham neutral at rightmid
    with qdissolve
    dw "Before you all leave, I made some comments on the drafts that you submitted earlier this week. Most of you are on the right track!"
    stop music fadeout 0.3
    play music "music/SadPlagiarism.ogg" fadein 0.8
    dw "Before I return your papers to you, though, I want to take a moment to talk about plagiarism."
    
    menu:
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}Uh oh, that’s not good.{/i}":
            jump WhatsWindhamUpTo

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} (Uncomfortable fidgeting)":
            jump WhatsWindhamUpTo

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}Not plagiarism again, we just talked about this!{/i}":
            jump WhatsWindhamUpTo


label WhatsWindhamUpTo:

    show windham concerned
    with qdissolve
    dw "We touched on this at the beginning of class, but I feel the need to stress to you all again how important it is to do your own work in this course and, really, throughout the remainder of your college and professional careers."
    
    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}I wonder if somebody cheated!{/i}":
            jump WindhamTalksPlagiarism

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}I wonder if I cheated! I don’t think I did...{/i}":
            jump WindhamTalksPlagiarism

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}Why is she talking about this in class again?{/i}":
            jump WindhamTalksPlagiarism


label WindhamTalksPlagiarism:

    dw "Before you turn in your final drafts, I want you all to review the university’s honor code. You can find it in the Student Handbook and in the syllabus. I also want to  remind all of you of the severe consequences of academic dishonesty."
    dw "If you are caught plagiarizing in this course, at the very least you will fail the plagiarized assignment. Depending on the severity, you may also fail the course altogether and get the incident on your university record."
    dw "You could even get expelled from the university."
    
    menu:

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}Holy crap!{/i}":
            jump WindhamTriesToSalvageClass

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}Expelled? Seriously? That’s heavy!{/i}":
            jump WindhamTriesToSalvageClass

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} {i}I didn’t realize it could get that bad, yikes.{/i}":
            jump WindhamTriesToSalvageClass

    
label WindhamTriesToSalvageClass:

    show windham neutral
    with qdissolve
    stop music fadeout 2.0
    
    dw "Anyway, didn’t mean to end the class on such an unhappy note!"
    play music "music/Classroom.ogg" fadein 4.0
    dw "Let me know if any of you have questions about the comments on your drafts."

    show windham happy
    with qdissolve
    dw "I hope you all have a great weekend. See you on Monday!"
    
    hide windham
    with qdissolve

    show kevin neutral at leftmid
    with qdissolve
    k "Hey, [name!q]. Saw you sweating a little during Dr. Windham’s speech. Do you have something to confess?"
    
    m "No! Well, I haven’t looked at my draft yet, so I hope not. Honestly, sometimes I’m a little confused about what counts as plagiarism."
    
    show jeff neutralleft at right
    with qdissolve
    j "It makes me kinda paranoid. It is crazy all of the different things that are considered plagiarism."
    
    m "I never really thought about it that way. I wasn’t paranoid before, but I think I am now."
    
    show kevin concerned
    with qdissolve
    k "What do you mean “different things that are considered plagiarism”?"
    k "Isn’t plagiarism just cutting and pasting other people’s words and claiming them as your own?"
    
    j "Actually, that is only one kind of plagiarism. There are lots more."
    
    k "Seriously?"
    
    j "Yeah, man."
    
    show kevin neutral
    with qdissolve
    k "Well I’ve gotta run to practice, but maybe you can tell me about the different kinds of plagiarism later?"
    
    j "That sounds like a thrilling way to spend an afternoon."
    
    show kevin happy
    with qdissolve
    k "Great! I’ll see you guys later."
    
    m "Yeah, Kevin. See ya."
    
    hide kevin with qdissolve

    show jeff confusedleft
    with qdissolve
    j "I worry about that kid sometimes."
    
    m "You and me both."
    
    show jeff concernedleft
    with qdissolve
    j "Hey, is she alright?"
    
    m "Kevin?"
    
    show jeff confusedleft
    with qdissolve
    j "No, Christina. Look over there, she’s still sitting at her desk. She looks like she got some bad news."

    menu:    
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Should we see if she’s okay?":
            jump checkingOnChristina

        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Maybe we should just leave her alone if she’s upset?":
            jump checkingOnChristina


label checkingOnChristina:
    
    j "It wouldn’t hurt to ask. If she doesn’t feel like talking we can always leave her alone."
    
    m "Okay, sounds good."
    
    show jeff concernedleft
    with qdissolve
    j "Hey Christina. Is everything okay?"
    
    stop music fadeout 0.3
    play music "music/SadPlagiarism.ogg"
    show christina concerned at left
    with qdissolve
    c "Is it that obvious?"
    
    j "That everything isn’t okay? Kinda."
    
    show christina sad
    with qdissolve
    c "I just feel like an idiot. I got my draft back from Dr. Windham and apparently she gave that whole speech in the class because of me. I guess I plagiarized."
    
    m "Don’t feel like an idiot. We were literally just talking about how confusing plagiarism can be sometimes."
    
    show christina concerned
    with qdissolve
    c "I honestly didn’t mean to. I took some stuff from this website but I cited the website in my bibliography."
    
    j "Did you cite the words you took from that website in your actual paper? Like, did you put them in quotes?"
    
    show christina confused
    with qdissolve
    c "No, I didn’t think I had to. I just copied the paragraph. It said everything I wanted to say."
    
    j "Well at least you know now, so you won’t make the same mistake when you have to turn in the paper for a grade."

    c "I’m still not really sure how to fix it. What would you do, [name!q]?"
    
    menu:
    
        c "I’m still not really sure how to fix it. What would you do, [name!q]?{fast}"
        
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} Honestly, I would just leave out the citation altogether the next time I want to use something I found on the internet. If you don’t tell the professor where you got the information she probably won’t find it.":
            show christina surprised
            show jeff surprisedleft
            stop music fadeout 0.8
            jump actFourBadEnding
        
        "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I would just make sure that every time I used someone else’s words I would set it off in quotation marks and cite it.":
            jump makeSuretoCite

label makeSuretoCite:
            show jeff neutralleft
            with qdissolve
            j "I would do that too whenever I quote directly from a source. You aren’t always going to do that though."
            
            show christina concerned
            with qdissolve
            c "Do what? Use direct quotations? How are you supposed to ever use the research you find then?"
            
            j "This gets back to what I was talking with [name!q] and Kevin about before we came over. There are different kinds of plagiarism and also different ways to responsibly integrate the sources you can use."
            
            m "Like what?"
            stop music fadeout 2.0
            j "You know, I think that Stephanie can explain this stuff better than me. Should we check with her?"
            
            play music "music/Classroom.ogg" fadein 3.0
            show christina confused
            with qdissolve
            c "Who is that?"
            
            m "Stephanie is a librarian who has helped us out with this project. I bet she knows a lot about citing sources."
            
            show kana neutral at center
            with qdissolve
            ka "Hey guys, are you still here? I had to talk to Dr. Windham about something with my draft."
            
            j "We are about to head over to the library to talk to Stephanie about citation and plagiarism."
            
            ka "Mind if I tag along? I’ve got a citation question too, actually!"
            
            show christina neutral
            with qdissolve
            c "Alright, alright, let’s go. I guess I need whatever help I can get!"
            stop music fadeout 0.8
            jump actFourtoTheLibrary

label actFourBadEnding:

    scene bg blackSolid with fade
    $ save_name = "Name: %s\nScene: Bad Ending IV" % (name)
    scene bg tenYrsLater with fade

    $ renpy.pause(2.0)

    scene bg blackSolid with fade

    scene bg moonLandscaper with fade

    play music "music/Moonscape.ogg" noloop
    m "{i}Sigh, I wish I wouldn’t have been so lax about plagiarism when I was in college. After my teacher caught me plagiarizing and I got that “F” in class I felt like I couldn’t show my face in polite society.{/i}"
    m "{i}Which is good, I guess, because the only job I could get after “the incident” was on the moon. Sure is lonely up here. At least there is no one up here to witness my shame.{/i}"
    
    "Game Over"
    if not persistent.achievement_bad_end4_unlocked:
        $ persistent.achievement_bad_end4_unlocked = True
        show achievement badEnd4:
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
            jump whyCite

label whyCite:

        scene bg classroom with fade
        $ save_name = "Name: %s\nScene: Act IV – Classroom" % (name)
        play music "music/SadPlagiarism.ogg"
        show jeff concernedleft at right
        show christina confused at left
        with qdissolve

        menu:
    
            c "I’m still not really sure how to fix it. What would you do, [name!q]?{fast}"
        
            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I would just make sure that every time I used someone else’s words I would set it off in quotation marks and cite it.":
                jump makeSuretoCite

label actFourtoTheLibrary:
    
    scene bg libraryBrowsing with fade
    $ save_name = "Name: %s\nScene: Act IV – Library" % (name)
    play ambient "sfx/library-ambient.ogg"
    play music "music/Library.ogg"

    show stephanie neutral at leftedge
    show christina neutral at Position(xpos=0.38, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show kana neutral at Position(xpos=0.60, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show jeff neutralleft at rightedge
    with qdissolve
    s "Hi there, everyone! How’s the project going?"
    
    with qdissolve
    ka "We just turned in a draft. We actually have some questions about citing, if you have a sec."
    
    with qdissolve
    c "And plagiarism too."
    

    s "I don’t think we’ve met yet."
    
    show stephanie happy
    with qdissolve
    s"I’m Stephanie."
    
    show christina happy
    with qdissolve
    c "Hey, I’m Christina."
    
    show stephanie neutral
    with qdissolve
    s "I’m glad to help you guys understand citation and plagiarism better. They are both pretty closely related, you know."
    
    show christina neutral
    with qdissolve
    c "Oh, I know. I found out the hard way today."
    
    show stephanie concerned
    with qdissolve
    s "I see."
    
    c "Here’s my paper."

    c "Dr. Windham highlighted that paragraph and said that I plagiarized it, but I cited it at the end."
 
    show stephanie surprised
    with qdissolve   
    s "But you didn’t let your reader know that the information you included did not come from you."

    s "Even if you did, you never want to lift a whole paragraph from another source. Your paper needs to be a reflection of you, and your thoughts."
    
    show christina concerned
    with qdissolve
    c "Well this person said what I wanted to say. I don’t think I could have said it any better."
    
    show stephanie neutral
    with qdissolve
    s "If a resource says something especially well, then it is okay to include what they say word for word if you set it off in quotations and either do a footnote or an in-text citation, depending on what citation style you are working with."
    
    show jeff confusedleft
    with qdissolve
    j "By “citation style” do you mean like MLA, APA, Chicago, stuff like that?"
    
    s "Exactly."
    
    show christina confused
    with qdissolve
    c "What is an in-text citation?"
    
    show jeff neutralleft
    with qdissolve
    j "Here’s an example from my paper. I’m writing in MLA style."
    
    #[IN TEXT CITATION EXAMPLE:
    "{font=Coustard-Regular.ttf}{size=-3}{color=#d9d9d9}“...our study found that individuals who have admitted to illegally downloading music also tend to purchase music legally more often than people who do not download music illegally...” (Mitchell 23).{/color}{/size}{/font}"
    
    show christina neutral
    with qdissolve
    c "Oh, I’ve seen those before. That should be easy enough."
    
    show stephanie happy
    with qdissolve
    s "That’s a great example, Jeff."

    show stephanie concerned
    with qdissolve
    s "Do any of you know how you should cite information that you paraphrase?"

    show christina confused
    with qdissolve
    c "Paraphrase?"
    show christina neutral
    with qdissolve
    c "You mean, like, put things that people have said into your own words?"

    c "If it is in your own words, you don’t need to cite that, do you?"
    
    show stephanie neutral
    with qdissolve
    s "Good question, Christina. Paraphrasing other people’s words without giving them credit is considered plagiarism too."
    s "This is probably the kind of plagiarism that people are most guilty of—sometimes they’ll change a word or two around and think that is enough."
    
    show kana happy
    with qdissolve
    ka "So pretty much every time we are using something from someone else we need to cite it."

    show stephanie happy
    with qdissolve
    s "Right. You have to let your reader know that the idea isn’t yours."

    show jeff concernedleft
    with qdissolve
    j "So, how do you cite something that you’ve paraphrased?"

    show kana neutral
    with qdissolve

    show stephanie neutral
    with qdissolve
    s "Let’s take the example from Jeff’s paper."
    s "As a rule of thumb, you want to paraphrase unless the original author has said something in a way that if you changed the words you would also change the meaning."

    show jeff neutralleft
    with qdissolve
    j "So I could have paraphrased that direct quote, because they were really just summing up the findings of their study."

    show stephanie happy
    with qdissolve
    s "Right."

    show stephanie concerned
    with qdissolve
    s "Any suggestions about how we could paraphrase this sentence:"

    "{font=Coustard-Regular.ttf}{size=-3}{color=#d9d9d9}“...our study found that individuals who have admitted to illegally downloading music also tend to purchase music legally more often than people who do not download music illegally...” (Mitchell 23).{/color}{/size}{/font}"

    m "Maybe: {font=Coustard-Regular.ttf}{size=-3}{color=#d9d9d9}The study consulted has found that people who pirate music are more likely to buy music legally.{/color}{/size}{/font}"

    show stephanie neutral
    with qdissolve
    s "That works. If you wanted to cite that, you would just add the in-text citation at the end of the sentence."
    s "So: {font=Coustard-Regular.ttf}{size=-3}{color=#d9d9d9}The study consulted has found that people who pirate music are more likely to buy music legally (Mitchell 23).{/color}{/size}{/font}"
    s "You might also consider phrasing it this way, to make the sentence flow more smoothly: {font=Coustard-Regular.ttf}{size=-3}{color=#d9d9d9}Mitchell found that people who pirate music are more likely to buy music legally (23).{/color}{/size}{/font}"

    show christina happy
    with qdissolve
    c "Alright, I think I’ve got it."

    c "I just need to make sure that if I take a direct quote or paraphrase something that I cite the original author. And then I’m set, right?"

    s "You definitely want to cite in those situations, but you also want to make sure to avoid idea or style plagiarism too."


label typesofPlagiarism:

    if idea_plagiarism_asked == style_plagiarism_asked == True:
        jump JeffHasMoreToSay

    else:
        menu:

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What’s idea plagiarism?" if idea_plagiarism_asked == False:
                $ idea_plagiarism_asked = True
                s "Idea plagiarism is what it sounds like—taking someone else’s idea and passing it off as your own."
                jump typesofPlagiarism

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What’s style plagiarism?" if style_plagiarism_asked == False:
                $ style_plagiarism_asked = True
                s "Style plagiarism can be tricky—it is when you copy someone else’s flow of logic, or the way they’ve organized their information."

                show christina confused
                with qdissolve
                c "Why would that be plagiarism?"
                s "Well the way that something is organized affects its overall meaning."
                s "And when it comes down to it, it is still copying something from someone else."

                show christina neutral
                with qdissolve
                c "I guess that makes sense."
                jump typesofPlagiarism


label JeffHasMoreToSay:

    j "Talking about different kinds of plagiarism is helpful, I feel like I have a better idea of things to look out for."
    j "There’s always something that’s confused me though."

    show stephanie concerned
    with qdissolve
    s "Oh yeah? What’s that?"

    j "Sometimes I put things in my paper that no one has really said, it’s just stuff that I assume everyone knows."

    show jeff concernedleft
    with qdissolve
    j "I worry that I should find that information somewhere so I can cite it."

    show stephanie neutral
    with qdissolve
    s "Ahh, you are talking about things that are considered common knowledge."
    s "Determining what is and isn’t common knowledge can be confusing."

    show stephanie confused
    with qdissolve
    s "If you think about it, what might be common knowledge to you or, academically speaking, your discipline, is not common knowledge to everyone."
    s "I’ve read that if you can find the information in five reliable sources it counts as common knowledge, but I don’t know if that is a hard and fast rule."

    show jeff confusedleft
    with qdissolve
    j "That seems...overly complicated."
    j "Do we have to look for something in five places if we want to include it in a paper without citing it?"

    show stephanie concerned
    with qdissolve
    s "Unfortunately this issue isn’t cut and dry."
    s "I would add that in our digital age, you might well be able to find a piece of information in five places but you’d still need to cite it if those five places have just copy and pasted something."
    s "Other people claim that common knowledge is something that is considered to not have been written or created by somebody, such as “World War II began on September 1, 1939” or “Earth has one moon”."
    s "We know this is a complicated distinction. If you are ever in doubt, ask your professor."

    show kana concerned
    with qdissolve
    ka "I use pictures a lot in my work, and I know I have to cite those too. I’m honestly not sure the best way to do it though."

    show stephanie neutral
    with qdissolve
    s "You’ll need to cite any images you use just like you would cite other people’s words or ideas."
    s "It really depends on the style you’re using, and where the image came from."

    ka "What if it’s something I saw in a museum?"

    s "Then you will probably need to include the museum’s name in your citation."

    show kana happy
    with qdissolve
    ka "I see. That helps a lot, thanks Stephanie!"

    show jeff neutralleft
    with qdissolve

    show christina happy
    with qdissolve
    c "That was super helpful, Stephanie. Thank you. Thanks to you too, guys."
    c "I feel better about the plagiarism situation now that I actually know how to cite a source."

    show stephanie happy
    with qdissolve
    s "Glad to hear it Christina."

    show stephanie neutral
    with qdissolve
    s "Feel free to visit us at the library again if you have any other questions."

    show christina neutral
    with qdissolve
    c "Will do. For now, though, I’ve gotta run off to a Climate Change a Palooza meeting."

    show kana neutral
    with qdissolve
    ka "Me too, I’ll walk out with you. See you all in class!"

    show stephanie happy
    with qdissolve
    s "Bye ladies!"

    hide kana
    hide christina
    with qdissolve


    show stephanie neutral
    with qdissolve
    s "Well, Jeff and [name!q], my office hours are about to start, do either of you have any questions about anything we just talked about? I’m happy to continue the conversation!"

    show jeff happyleft
    with qdissolve
    j "No, I’m good. I’ll see you both later!"
    hide jeff with qdissolve

    m "I do have a question or two, actually."
    show stephanie concerned
    with qdissolve

    jump actFourWrapUpQuestions


label actFourWrapUpQuestions:

    if paraphrase_asked == style_plag_asked == idea_plag_asked == common_know_asked == image_ethics_asked == intext_citation_asked == True:
        if not persistent.achievement_honesty_policy_unlocked:
            $ persistent.achievement_honesty_policy_unlocked = True
            show achievement honestyPolicy:
                xalign 0.97 yalign 0.03
                alpha 0.0
                easeout 0.6 alpha 1.0
                pause 2.0
                easeout 0.9 alpha 0.0
            $ renpy.pause(0.1)
            play sndfx "sfx/achievement.ogg"
        m "I don’t have any other questions. Thanks!"
        show stephanie happy
        with qdissolve
        s "No problem. See you later!"
        hide stephanie with qdissolve
        jump actFourWrapUp

    else:

        menu:

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is paraphrase plagiarism again?" if paraphrase_asked == False:
                $ paraphrase_asked = True
                show stephanie neutral
                with qdissolve
                s "Paraphrase plagiarism is rephrasing someone else’s idea without giving them credit."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is style plagiarism again?" if style_plag_asked == False:
                $ style_plag_asked = True
                show stephanie neutral
                with qdissolve
                s "Style plagiarism is copying the order of another person’s writing or logic."
                s "If you mimic someone else’s formatting, you are committing style plagiarism."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is idea plagiarism again?" if idea_plag_asked == False:
                $ idea_plag_asked = True
                show stephanie neutral
                with qdissolve
                s "Idea plagiarism is claiming someone else’s idea as your own."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} How do I know if something is common knowledge?" if common_know_asked == False:
                $ common_know_asked = True
                show stephanie neutral
                with qdissolve
                s "There isn’t a hard and fast rule about this, and what is considered “common knowledge” is different in different disciplines."
                s "Generally common knowledge is information that most people know or can find out easily."
                s "You might also think about it as information that can’t be attributed to just one source. When in doubt, cite it."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} How can I use images ethically?" if image_ethics_asked == False:
                $ image_ethics_asked = True
                show stephanie neutral
                with qdissolve
                s "Cite any images you use in the same way that you’d cite words and thoughts you borrow from other sources."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} What is in-text citation again?" if intext_citation_asked == False:
                $ intext_citation_asked = True
                show stephanie neutral
                with qdissolve
                s "In-text citation is a way for you to tell your reader exactly what you are using from another source and what that source is."
                s "Each citation style has its own form of in-text citation, so make sure that you are using the correct in-text citation style."
                show stephanie concerned
                with qdissolve
                s "Anything else?"
                jump actFourWrapUpQuestions

            "{font=SourceSansPro-Bold.ttf}[name!q]:{/font} I don’t have any other questions. Thanks!" if paraphrase_asked == True or style_plag_asked == True or idea_plag_asked == True or common_know_asked == True or image_ethics_asked == True or intext_citation_asked == True:
                show stephanie happy
                with qdissolve
                s "No problem. See you later!"
                hide stephanie with qdissolve
                jump actFourWrapUp


label actFourWrapUp:
    if not persistent.achievement_actFour_complete_unlocked:
        $ persistent.achievement_actFour_complete_unlocked = True
        show achievement actFourComplete:
            xalign 0.97 yalign 0.03
            alpha 0.0
            easeout 0.6 alpha 1.0
            pause 2.0
            easeout 0.9 alpha 0.0
        $ renpy.pause(0.1)
        play sndfx "sfx/achievement.ogg"
    jump actFourEnterPassword

label actFourEnterPassword:    
    $player_pass = renpy.input("Please enter the password for Act Five and press  < Enter >", length=6)
    if player_pass.upper().strip() == actFive_pass:
        stop ambient fadeout 0.8
        stop music fadeout 0.8
        jump ActFive
    else:
        "Sorry, that password wasn’t correct. Please try again."
        jump actFourEnterPassword
    
    