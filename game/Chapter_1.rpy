label prologue:
    scene black
    # call chapter2_1
    call nextpage
    show screen navigation
    scene black
    play sound "audio/Twin-bell-alarm-clock.ogg" loop fadein 1
    n  "The alarm went off early again. {w}\nIt’s been doing that a lot more frequently." (40,300,show_tail="narr",show_xmax=840,show_retain=1)
    n  "I’d fix it, but I just can’t summon up the will to do so." (250,800,show_tail="narr",show_xmax=580)

    call nextpage
    stop sound
    scene bedroom with dissolve: #with blinking
        zoom 0.7
    play music "audio/Evening_Melody.ogg" fadein 4.5
    n "That alarm signals that it’s Friday, though to be honest, I’ve grown to dislike the sounds of my day-specific alarms." (330,50,show_tail="narr",show_xmax=500,show_retain=2)
    n "I can’t remember if I had selected those sounds because they seemed fine at the time, or if I just didn’t care enough to give it much thought." (140,600,show_tail="narr",show_xmax=600,show_retain=1)
    n "I knew I’d eventually grow to dislike the sound, but I didn’t think it’d be this quick." (40,1050,show_tail="narr",show_xmax=620)
    pause 1

    call nextpage
    # show CG1 with dissolve:
        # xalign 0.5 yalign 0.5
    n "Auto-pilot engaged." (50,100,show_tail="narr",show_xmax=300,show_ymax=200,show_retain=2)
    n "Perhaps this was a form of conditioning?" (140,360,show_tail="narr",show_xmax=500,show_retain=1)
    n "I hear the sound, I get ready for work." (320,980,show_tail="narr",show_xmax=500)

    call nextpage
    # show cutin_armup #(Blake laying in a foldout futon in the living room.) [PANEL 1]
    # play sound "sigh.ogg"
    # pause 1
    # show cutin_dressup # (Blake putting on a jacket and his shoes to leave the apartment.) [PANEL 2]
    show Blake lookaway frown at middef with dissolve # [PANEL 3]
    b "....Oh, right. I don’t work there anymore." (390,320,show_tail="baseright",show_xmax=380,show_retain=1)
    n "The auto-pilot was so ingrained in my mind that I was midway through putting on my tie before I remembered that I had already quit my job and didn’t need to go."  (150,950,show_tail="narr",show_xmax=700)
    hide Blake

    call nextpage
    show screen CG_1 with dissolve
    pause 0.2

    play sound "audio/sfx-dooropens.ogg"
    #   show cutin_door #Panel 2 (the door to the bedroom where he and Ashley used to sleep)
    n "That being said, staying here any longer wasn’t an option either." (20,25,show_tail="narr",show_xmax=550,show_retain=2)
    extend "..."
    n "...{p=1}\nI needed to go." (550,1100,show_tail="narr",show_xmax=400)

    call nextpage
    hide screen CG_1 with dissolve
    n "That one desire was overpowering my other senses. I should stay, talk it out, scream, do something, don’t let it go." (200,150,show_tail="narr",show_xmax=500,show_retain=2)
    n "All these thoughts which were once a cacophony of madness, now silent as still water." (170,600,show_tail="narr",show_xmax=550,show_retain=1)
    n "And the only thought left standing was that this story had run its course." (200,950,show_tail="narr",show_xmax=500)


    scene white with dissolve
    call nextpage
    call centersay("{size=50}{cps=10}I'm sorry...{/cps}{/size}")
    # play sound "door_open.ogg"
    window hide dissolve
    # show "key_and_note" with dissolve
    # pause 5
    # hide "key_and_note" with dissolve
    # play sound "door_close.ogg"
    return
label chapter1:
    # call screen chap("1", "Encounter")
    call screen chap("1", "Encounter")
    # Show the city skyline changing in lighting,
    ### this is to indicate the passage of time between the first scene and the next scene.
    ## PAGE 1
    call nextpage
    scene city2 with dissolve:
        zoom 0.7
    pause 0.1
    show city with dissolve:
        zoom 0.7
    pause 1
    show sky_bright with dissolve
    pause 1.2
    show park with dissolve
    pause 1.2
    scene lake with dissolve #at (pan from wherever the bridge is in the image to the opposite side)
    # play sound "birds_morning.ogg"
    # queue sound "birds_morning.ogg" volume 0.5
    n "It’s like I’m a marionette guided by invisible strings to my destination." (300,60,show_tail="narr",show_xmax=550)
    # Pause the BG image panning, hold on the image for a second or two  [WAT]

    call nextpage
    n "What am I even doing here?" (50,100,show_tail="narr",show_xmax=580,show_retain=2)
    n "I thought it would hurt more, that's what everyone always said." (180,500,show_tail="narr",show_xmax=650, show_retain=1)
    n "For me, rather than pain, I felt a cold emptiness. Over time, that chasm in my chest just kept growing until..." (300,900,show_tail="narr",show_xmax=580)

    call nextpage
    # play sound "sigh.ogg"
    pause 0.2
    n "I just lost control of my actions. I don’t know on what level I’m operating now." (150,50,show_tail="narr",show_xmax=700, show_retain=2)
    n "Is it logic? Emotions? Some other driving force?" (100,550,show_tail="narr",show_xmax=600, show_retain=1)
    n "I don’t know. I don’t really know anything anymore." (180,950,show_tail="narr",show_xmax=500)

    call nextpage
    # play sound "shuffling(pocket).ogg"
    show memento: #(A USB drive in the shape of a ring)
        yalign 0.6 xalign 0.4
    n "In my hand, a memento from the past two years." (30,50,show_tail="narr",show_xmax=550, show_retain=4)
    n "A month ago, this would’ve sparked joy; made me feel like she was with me, even when we were too busy to hang out." (30,260,show_tail="narr",show_xmax=700, show_retain=3)
    n "But now..." (500,750,show_tail="narr",show_xmax=300, show_retain=2)
    n "Now I feel... angry, sad, empty." (450,930,show_tail="narr",show_xmax=400, show_retain=1)
    n "How did things get like this?" (500,1150,show_tail="narr",show_xmax=350,)
    hide memento with dissolve
    call nextpage
    # Cut in image of the memento at the bottom of the screen.  (WAT)
    # show cutin_momento at center # half dark
    n  "'Throw it, get rid of it.'"  (350,50,show_tail="narr",show_xmax=500,show_retain=4)
    n "It was as if a voice spoke directly into my ear, and my body reacted to its siren call." (30,450,show_tail="narr",show_xmax=650, show_retain=3)
    n  "I reared back my hand, memento tightly grasped."(50,660,show_tail="narr",show_xmax=500, show_retain=2)
    n "Would this hurt her? Would she feel sad that I threw this away? Would she even care?" (460,880,show_tail="narr",show_xmax=400, show_retain=1)
    n  "Is this what I want?"(400,1180,show_tail="narr",show_xmax=470)
    pause 0.2

    call nextpage
    # show blake at middef with dissolve
    show Blake lookaway frown at middef with dissolve
    n  "I hesitated. To an outside observer, I must’ve looked insane." (30,50,show_tail="narr",show_xmax=700, show_retain=3)
    n "Miming a throwing motion, wrestling with myself about whether to get rid of something that was once so precious to me." (30,500,show_tail="narr",show_xmax=740, show_retain=2)
    n  "On one side, I thought that things could return to normal." (30,750,show_tail="narr",show_xmax=650, show_retain=1)
    n  "We've had our fights before. We’ve even had moments where it looked like we were going to split up for good, but we always found our way back to each other." (220,975,show_tail="narr",show_xmax=650)
    n  "Ashley..." (220,975,show_tail="narr",show_xmax=650)
    
    call nextpage
    # scene flashback #white background, black grids
    scene flashback
    show screen black_border
    show Ashley frown midclose at middef:
        alpha 0.75
    with Dissolve(1.5)
    a "I can’t do this anymore." (290,180,show_tail="baseright",show_xmax=300, show_retain=3)
    n  "Not this time though." (-35,780,show_tail="narr",show_xmax=350, show_retain=2)
    show Ashley frown down midclose
    a "I feel as though you’re never truly with me, when we’re together. Like, you’re only here because you feel like you have to, not because you want to."(500,450,show_tail="topleft",show_xmax=390, show_retain=1)
    n "On the other side of my mind, was just raw emotion. Irrational impulses compelled me to do this." (-50,980,show_tail="narr",show_xmax=630)
    call nextpage
    show Ashley up
    a "And for a long time, I’ve blamed myself. Thought that I wasn’t being good enough for you." (530,330,show_tail="baseleft",show_xmax=350, show_retain=3)
    show Ashley open frown down
    a "But the truth is, we’re just not right for each other, and I don’t think you’ll ever be the person I want you to be." (500,460,show_tail="topleft",show_xmax=370, show_retain=2)
    n "My hands tightened around the memento’s edges, as my rationality gave way to despair." (20,810,show_tail="narr",show_xmax=650,show_retain=1)
    a "I’m sorry, but I can’t do this anymore." (500,1050,show_tail="lefttop",show_xmax=380)

    hide Ashley
    hide screen black_border
    call nextpage
    scene lake with dissolve
    n  "Just a brief moment." (50,110,show_tail="narr",show_xmax=550,show_retain=2)
    n "It just took a brief moment for my arm to swing forth, and my fingers to loosen their grip for it to go flying out of my hand as a yell of frustration rang out." (20,350,show_tail="narr",show_xmax=850,show_retain=1)
    n "Time seemed slow as I watched the memento veer way off course from where I intended, soaring off to the side, over the bridge, and I realized too late that doing this didn’t feel right." (20,590,show_tail="narr",show_xmax=700)


    call nextpage
    scene white with dissolve
    n "Regret." (50,250,show_tail="narr",show_xmax=3850,show_retain=1)
    n  "That’s what I was feeling now." (20,350,show_tail="narr",show_xmax=850)

    call nextpage
    show lake
    n "But, it was too late." (50,150,show_tail="narr",show_xmax=600,show_retain=3)
    n "It was gone now. Though I could not see it for myself, I heard the splash as the memento hit the water just beyond the bridge. Weird, it sounded heavier than I imagined." (320,400,show_tail="narr",show_xmax=550,show_retain=2)
    n "For a brief moment, a part of me wanted to dive into the lake and search for it." (100,800,show_tail="narr",show_xmax=650,show_retain=1)
    n "But that was a pain, it’s already gone. It’s too late. There’s no way I could ever get it back. It’d be a waste of effort." (450,1000,show_tail="narr",show_xmax=420)

    call nextpage
    n "I turn around, not knowing where I’ll go now, but suddenly feeling tired... "(20,280,show_tail="narr",show_xmax=780,show_retain=2)
    n "I think to look around for a motel or--{nw}" (80,400,show_tail="narr",show_xmax=780,show_retain=1)
    stop music

    s "{size=60}HEY, LITTERBUG! YOU DROPPED SOMETHING!{/size}" (200,450,show_tail="yell",show_xmax=750) with Shake((0, 0, 0, 0), 0.5, dist=30)
    #"A voice addresses me, not from my own mind, but from... the bridge?"
    play music "audio/Smile_Sweetly.ogg" fadein 4.5
    call nextpage
    show lake # at "lookaround" (zoom 1.5, move around, before zoom 1.0)
    show CG2 with dissolve
    n "In the distance, I spot the owner of the annoyed voice." (50,50,show_tail="narr",show_xmax=630,show_retain=3)
    n "In her hand I see..." (100,300,show_tail="narr",show_xmax=400,show_retain=2)
    # show memento:
    #     xanchor 0.0 xpos 0.15
    #     zoom 0.5
    #     yanchor 0.0
    #     ypos 1.0
    #     ease 0.3 ypos 0.4
    show CG2:
        xanchor 0.5 yanchor 0.5
        xpos 0.5 ypos 0.5
        zoom 1.0
        linear 1.0 zoom 1.8 xpos 0.55 ypos 0.25

    n "The memento." (30,960,show_tail="narr",show_xmax=400,show_retain=1)
    s "Wait right there, I’ll come to you!" (600,750,show_tail="topleft",show_xmax=400)
    hide CG2 with dissolve

    call nextpage
    n "The girl jogged her way over to me, and stared me as if trying to get a read on the kind of person I was." (100,650,show_tail="narr",show_xmax=500,show_retain=1)
    show Selena frown down at middef:
        yanchor 0.0
        ypos 1.0
        ease 0.3 ypos 0.2
        #with popup
    n "At least, that’s what I think she was doing." (450,930,show_tail="narr",show_xmax=400)

    call nextpage
    s "So... do you always just throw random objects at people?" (350,250,show_tail="baseright",show_xmax=345)
    # "She hands me back the memento that I had so carelessly thrown away."
    show memento: #at "give back transform (enter from bottom, pause, exit bottom with zoom in)
        zoom 0.1 xalign 0.5 yalign 0.6
        ease 1 zoom 0.5
        pause 0.5
        ease 1 zoom 2.0 yanchor 0.0 ypos 1.0
    pause 2.2


    call nextpage
    b "Ah. Sorry. You’re not hurt are you?" (930,680,show_tail="rightbase",show_xmax=400,show_retain=1)
    show Selena up smile
    s "Who? Me? Nah. Believe it or not, I’m much more durable than I look." (420,700,show_tail="topright",show_xmax=430)
    show Selena horizontal  # Selena’s expressions change (as if she’s waiting for a conversation to start).
    # (Maybe pan the camera down slightly to look at the memento so we only see Selena’s body from the neck down in the background.)
    # show lake at starein
    # show selena_base at starein:
    #     zoom 0.3
    # with ease
    # pause 3

    #####################################################
    call nextpage
    show lake:
        zoom 1.15 xalign 0.5 yalign 0.1
    show Selena:
        zoom 1.15 xalign 0.5 yalign 0.1
    show memento:
        xalign 0.4 yalign 0.8 zoom 0.6
    with Dissolve(1.5)
    n "I muster a weak smile as my eyes rest upon the memento in my hand." (-20,80,show_tail="narr",show_xmax=300,show_retain=3)
    show Selena squiggly midclose #new expression
    n "Ha... I just got this back, feeling regret for getting rid of it. And I already want to repeat the same actions as if it’ll somehow make me feel better. \nWhat’s wrong with-" (200,400,show_tail="narr",show_xmax=600,show_retain=2)
    s "Oi, litterbug! You in there?" (500,750,show_tail="topleft",show_xmax=400,show_retain=1)
    b "Huh?" (800,1200,show_tail="baseright",show_xmax=200)
    pause
    call nextpage
    hide memento
    show Selena at middef with dissolve
        #expression
    s "Hm... It’s pretty rude to stare so blatantly, you know?" (400,300,show_tail="baseright",show_xmax=450,show_retain=3)
    b "Ah! W-wait, no, I-I wasn’t, I swear!" (-10,600,show_tail="leftbase",show_xmax=400,show_retain=2) with Shake((0, 0, 0, 0), 0.5, dist=20)
    show Selena bounce up opensmile closed at bounce #laugh

    n "Suddenly she breaks out into a laugh!" (250,750,show_tail="narr",show_xmax=500,show_retain=1)
    
    s "It's fine, I’m just messing with you.\n Jokes aside..." (500,950,show_tail="lefttop",show_xmax=400)

# ####################################################################################################jeroz
    call nextpage
    show Selena stand midclose frown horizontal:
        linear 1.0 zoom 0.8 #yalign 0.1
    n "Her mood, tone, and body language completely shifted. From the kind of cool girl you’d be hanging out with in class, to a girl who is probing you for information." (100,50,show_tail="narr",show_xmax=700,show_retain=4)
    show Selena smile #default expression
    s "{cps=35}What's your deal? Something bothering you? Is that why you’ve been throwing stuff at an innocent girl who's just-{/cps}" (500,550,show_tail="topleft",show_xmax=340, show_retain=3)
    pause 0.6
    show Selena lookaway #new expression
    pause 1
    show Selena midclose
    s "-Just taking a dawn stroll and resting on a bridge?"(420,900,show_tail="lefttop",show_xmax=480, show_retain=2)
    n "Something about her tone didn’t sound right, like there was another reason she was out here.\nIf this were a game I’d press her for info." (-50,980,show_tail="narr",show_xmax=500,show_retain=1)
    n "And yet, somehow, I feel like I wouldn’t be able to get a straight answer out of her.\nWe are strangers after all. So I’ll just drop the subject." (470,1060,show_tail="narr",show_xmax=490)
    scene park with dissolve
    call nextpage
    show Selena open up at middef with dissolve
    b "It’s... a long story." (30,50,show_tail="lefttop",show_xmax=500,show_retain=5)
    show Selena midclose horizontal
    s "Hmmm, that so?" (500,300,show_tail="baseleft",show_xmax=300,show_retain=4)
    show Selena open up at middef

    s "Maybe you wanna talk about it? Sometimes airing things out to a sympathetic ear can make people feel better." (550,550,show_tail="lefttop",show_xmax=330,show_retain=3)
    btr "What she said wasn’t wrong." (0,1330, show_tail="btr",show_xmax=800)
    n "I know that talking about it could make me feel better. Yet still..." (50,900,show_tail="narr",show_xmax=600,show_retain=1)
    n "I looked away, as if talking about it would be a shameful act. That I should just suffer in silence and not burden this stranger with my problems." (200,1080,show_tail="narr",show_xmax=650)

    call nextpage
    s "Wait right here a sec." (420,350,show_tail="rightbase",show_xmax=350)
    hide Selena with moveoutleft
    # play sound "walking.ogg
    pause 1
    show Selena at middef with moveinleft
    n "After walking up to the vending machine, and making a quick purchase, she returns with her hands held firmly behind her back." (40,650,show_tail="narr",show_xmax=500,show_retain=1)
    s "Here." (600,550,show_tail="leftbase",show_xmax=400)

    call nextpage
    show Selena with ease:
        xalign 0.8
    show can with moveinleft:
        xalign 0.15 zoom 0.5 yalign 0.55
    # show cutin_can # with moveinright (of Selena’s hand holding a can of some kinda drink you’d get from a vending machine)
    n "From behind her back, she produced a canned drink. It wasn’t my favorite, but I appreciated the gesture nonetheless."(350,950,show_tail="narr",show_xmax=500)

    call nextpage
    # play sound "opening_can.ogg"
    hide can with dissolve
    s "Ya know, when people drink things, sometimes they find it difficult to hear things. Like when someone wants to talk about something bothering them. Wouldn’t it be convenient if someone could talk about their problems without worrying if someone could hear and judge them?" (670,780,show_tail="topright",show_xmax=600)

    call nextpage
    show Selena with ease:
        xalign 0.5
    b "Isn’t... isn’t that supposed to food? Like, you can’t hear someone over the crunch of-{nw}" (20,150,show_tail="leftbase",show_xmax=400,show_retain=2) ## [jeroz]
    show Selena bounce closed at bounce
    s "What’s that? Can’t hear you while I’m drinking!" (520,850,show_tail="lefttop",show_xmax=360,show_retain=1)
    btr ". . ." (400,1330, show_tail="btr",show_xmax=800)

    hide Selena with dissolve
    call nextpage
    scene lake with dissolve
    n "Rather than look at her, I instead choose to focus on the lake. I don’t know, maybe I should try it. Pretend like she’s not here. Maybe I would feel a little better." (50,50,show_tail="narr",show_xmax=550,show_retain=2)
    n "Not like I had anything to lose." (150,500,show_tail="narr",show_xmax=400,show_retain=1)
    n "I let out a long, drawn-out sigh." (200,850,show_tail="narr",show_xmax=400)
    #btr "...."

    play music "audio/Midnight_Snowfall.ogg" fadein 4.5
    scene sky_bright with dissolve
    call nextpage
    n "For just a brief moment, I thought I saw her again." (200,50,show_tail="narr",show_xmax=500,show_retain=2)
    show screen CG_1 with dissolve
    n  "I was back in that hallway..." (70,250,show_tail="narr",show_xmax=400,show_retain=1)
    b "I was... close to someone, for a long time." (550,750,show_tail="righttop",show_xmax=400,show_retain=0)

    hide screen CG_1 with dissolve
    # scene flashback
    nv "I could see her again; the first day we met, she strode into our dingy basement office with the manager."
    nv "She seemed so... out of place."
    nv "She wore a nicely tailored suit, carried a briefcase, had this sort of air about her that made me think that this was a girl who would be more natural commanding departments rather than working alongside one."
    nv "She seemed so far out of my league, so I never considered that we’d be anything more than coworkers."
    nvl clear

    ## FLASHBACK AGAAAAAAIN ######################
    show screen black_border
    call nextpage
    show Ashley down frown at middef with dissolve:
        xalign 0.35
    n "We used to work in {b}I.T.{/b} together, I remember she told me that she had been demoted as part of a retaliatory efforts by the company due to, as she put it..." (80,60,show_tail="narr",show_xmax=860,show_retain=3)
    a "Machiavellian-esque bullshit." (480,380,show_tail="baseleft",show_xmax=400,show_retain=2)
    n "It was like I was hearing her voice again." (450,550,show_tail="narr",show_xmax=400,show_retain=1)
    b "I wish I could say that we had a stereotypical romantic confession, but to be honest... we were just doing routine system maintenance when she asked." (-70,850,show_tail="narr",show_xmax=850)

    call nextpage
    show Ashley up oneclose smile with fade
    a "Yes. I am considering this to be a date. "(480,350,show_tail="lefttop",show_xmax=400,show_retain=2)
    show Ashley open

    extend"Though, I’d also like it if we just took a nice walk after work. I know how I look to others, but I don’t need expensive dinner reservations or gifts, I’d much rather spend time with someone like you than anyone else in the company." (480,350,show_tail="lefttop",show_xmax=400,show_retain=1)
    b "I guess it sounds pretty boring, but it’s the truth. She asked me, and we started dating before I really knew what was going on. In retrospect, maybe I shouldn’t have let things get that far. Maybe I should’ve been a better partner." (-50,1000,show_tail="narr",show_xmax=850)

    hide Ashley with dissolve
    call nextpage
    show memento with moveinbottom:
        zoom 0.5 xalign 0.5 yalign 0.85
    n "I looked down at the gift in my hand, and it was like I was seeing it again for the first time. The day she got me this, we were walking back from work, thinking about where we were gonna go for the weekend. It was a simple routine, one we’d played out several times, auto-pilot engaged. But on this day, she went off the beaten path. She lead us off to side and pulled out a small box from her purse." (50,380,show_tail="narr",show_xmax=800)

    hide memento with dissolve
    show Ashley at middef with dissolve:
        xalign 0.3
    call nextpage
    show Ashley smile
    a "Here. I know I’m... not the easiest person to be with, but I really do appreciate your company. So, I had this made for you." (500,320,show_tail="baseleft",show_xmax=380,show_retain=3)
    show Ashley concerned midclose
    a "Ah! Don’t read too much into it. It’s just... I wanted to show you that... I really care about you." (440,500,show_tail="topleft",show_xmax=460,show_retain=2)
    b "It didn’t hit me at first, what this gift meant. Look at it, it’s a ring from one of my favorite game franchises, that houses a thumb drive." (-50,800,show_tail="narr",show_xmax=850,show_retain=1)
    b "It’s thoughtful, practical, and romantic. She really went out of her way to give this to me, and what did I give her instead?" (60,1050,show_tail="narr",show_xmax=800)

    call nextpage
    show Ashley open up with fade
    b "A few days later, I repaid the gift she’d put a lot of thought and effort into giving me with a  box of rare chocolates from a fancy confectionary a few blocks down from our apartment, something I thought girls would like, something I thought she would like." (470,20,show_tail="narr",show_xmax=480,show_retain=4)

    a "Oh. Um, these seem... pretty expensive? Thank you for this gift, " (400,510,show_tail="topleft",show_xmax=450,show_retain=3)
    show Ashley closed
    extend "I... really appreciate it." (400,510,show_tail="topleft",show_xmax=450,show_retain=2)
    n "That’s what she said at the time, but it wasn’t the reaction I expected. I didn’t question it at the time, didn’t want to, couldn’t see the writing on the wall. Maybe if I had taken just a moment to think about how she must’ve been feeling, I could’ve seen what came next..." (20,800,show_tail="narr",show_xmax=850,show_retain=1)
    n "Another sigh escaped my lips, as the memory of the last day of our relationship played in my head like a film projected onto the wall." (100,1110,show_tail="narr",show_xmax=720)

    call nextpage
    show Ashley open frown with fade
    a "Yes, it’s true. I’m transferring out of the department."(450,350,show_tail="lefttop",show_xmax=400,show_retain=1)
    show Ashley midclose frown
    extend" I apologize for dumping this on you out of nowhere but..."(450,350,show_tail="lefttop",show_xmax=400,show_retain=1)
    extend" the truth is... about us...{w=1.0}{nw}" (450,350,show_tail="lefttop",show_xmax=400,show_retain=1)
    show Ashley concerned
    extend" I think we should break up." (450,350,show_tail="lefttop",show_xmax=400,show_retain=1)
    n "She’d always been this unbreakable wall of strength, determination, and confidence. Yet when she told me that... I saw anger, sadness, regret as clear as day, all painted on her face. It felt like this had been the hardest decision she’d ever had to make, and I hadn’t noticed it until the very last moment. When it was already too late to stop it." (40,900,show_tail="narr",show_xmax=750)
    hide Ashley
    call nextpage
    show Ashley frown with fade:
        alpha 0.4 yanchor 0.0 ypos 0.15 #check shadow to make it slightly darker
    n  "And in the moment, I just thought; \"Please. Don’t do this.\"" (100,120,show_tail="narr",show_xmax=400,show_retain=3)
    n  "But..." (150,350,show_tail="narr",show_xmax=300,show_retain=2)
    n "At the same time, another voice in the back of my mind told me something that had been ignored this whole time." (350,650,show_tail="narr",show_xmax=450,show_retain=1)
    n  "She deserves better than me." (470,910,show_tail="narr",show_xmax=380)

# ####################################
    hide screen black_border
    play music "audio/Smile_Sweetly.ogg" fadein 4.5
    scene lake with fade
    call nextpage
    show Blake lookaway frown at middef:
        xpos 0.7
    b "And now, the story’s over. If I had to be honest, it sucks. That’d be putting it mildly, but I don’t know what else to do." (500,330,show_tail="baseright",show_xmax=500,show_retain=1)
    b "I wish there was something I could do to make it right, to do something that’ll change everything, to go back in time and stop myself from failing to see what was right in front of me. But I can’t do that. What’s done is done, and I have to live with this now." (600,780,show_tail="righttop",show_xmax=550)

    call nextpage
    # play sound "cancrumble.ogg"
    hide Blake
    n "Suddenly she stood up, I thought that she might want to walk away from this convo, I was a pretty bad-"  (350,50,show_tail="narr",show_xmax=500,show_retain=1)
    show Selena down opensmile at middef:
        yanchor 0.0
        ypos 1.0
        ease 0.3 ypos 0.2
    pause 0.5
    #shakescreen
    y "{size=40}WAAAAAAH!{/size}" (-20,540,show_tail="yell",show_xmax=600, show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=20)
     ##Define yell as separate pos (0,0) image
    ## "Startled by the sudden yell, I had hopped back as if Selena had become a human bomb! What the shit?"
    # show [panel of Blake shocked] at saybounce (right lower) [jeroz]
    y "{size=40}!!!{/size}" (500,800,show_tail="yell",show_xmax=350) with Shake((0, 0, 0, 0), 0.5, dist=20)
    ## "She then looked directly at me, wiped the tears from her eyes, and then put on a smile."
    show Selena opensmile down # smile in new expression
    s "Know what I do when I get frustrated and don’t know what to do? I scream!" (380,900,show_tail="topright",show_xmax=350)

    call nextpage
    hide Selena with moveoutleft

    n "She cupped her hands around her mouth and inhaled..." (20,100,show_tail="narr",show_xmax=550, show_retain=1)
    y "MY LANDLORD IS A JERK!" (-50,500,show_tail="yell",show_xmax=600) with Shake((0, 0, 0, 0), 0.5, dist=20)
    show Selena at middef with dissolve
    s "See, just like that." (450,650,show_tail="topleft",show_xmax=400,show_retain=3)
    b "That’s... probably an inconvenience to other people and-" (10,950,show_tail="leftbase",show_xmax=350,show_retain=2)
    show Selena openmouth down
    s "{size=40}I DON'T CAAAARE,\n I'M SAD!{/size}" (400,800,show_tail="yell",show_xmax=500,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=20)
    show lake:
        xoffset 40
        pause 0.1
        xoffset 0
    show Selena smile:
        xoffset 40
        pause 0.1
        xoffset 0
    n  "She nudged my shoulder." (100,1120,show_tail="narr",show_xmax=600)

    call nextpage
    show Selena smile up with fade
    s "Sometimes, you just gotta trust your instincts and let things out, ya know? Bottling it all up can’t be healthy, I think people can live with a little inconvenience." (520,550,show_tail="topleft",show_xmax=400,show_retain=1)
    b  "..." (850,1300,show_tail="baseright",show_xmax=300)

    call nextpage
    n "I know what she was trying to say, but I just didn’t really feel like doing what she was doing. I thought that it’d be an inconvenience to others. That it’d make me stand out or look stupid. That it was just a waste of time or effort. Yeah, almost every part of my body rejected her logic." (50,650,show_tail="narr",show_xmax=800,show_retain=3)
    n "....." (180,1000,show_tail="narr",show_xmax=300,show_retain=2)
    n "Almost." (400,1100,show_tail="narr",show_xmax=300,show_retain=1)
    n "Inhale." (650,1180,show_tail="narr",show_xmax=300)

    scene sky_bright with dissolve
    call nextpage
    y "I HATE MY JOB, MY COWORKERS KEPT CALLING US IN TO FIX PROBLEMS THAT THEY CAUSED AND THEN BLAMED US WHEN WE WEREN’T DOING IT FAST ENOUGH!" (100,200,show_tail="yell",show_xmax=750,show_retain=2)  with Shake((0, 0, 0, 0), 0.5, dist=20)
    y "{size=40}IF IT’S SO EASY, THEN DO IT YOURSELVES!{/size}" (280,600,show_tail="yell",show_xmax=750,show_retain=1)  with Shake((0, 0, 0, 0), 0.5, dist=20)

    n "She stifled a laugh." (430,950,show_tail="narr",show_xmax=450)

    scene park
    show Selena openmouth at middef
    with dissolve
    call nextpage  ###
    s "That’s what you yelled about? Thought you’d yell about that girl you were just talking about." (470,310,show_tail="baseright",show_xmax=450,show_retain=2)
    b "Yeah well... I’m not quite ready for that yet." (850,750,show_tail="rightbase",show_xmax=450,show_retain=1)
    show Selena opensmile
    s "Alright, alright fair enough." (450,900,show_tail="righttop",show_xmax=450)
    # n "She held out her hand."

    call nextpage
    show Selena closed
    s "I’ve gotta say, Litterbug, this is probably one of the strangest first meetings I’ve ever had." (350,270,show_tail="rightbase",show_xmax=350,show_retain=5)
    b "Yeah same with- wait, do you think my name is Litterbug?" (850,230,show_tail="rightbase",show_xmax=450,show_retain=4)
    show Selena smile open up
    s "Well, what else am I gonna call you?" (450,600,show_tail="righttop",show_xmax=450,show_retain=3)
    b "How about Blake? Blake Lawrence." (850,850,show_tail="rightbase",show_xmax=450,show_retain=2)
    s "...huh..." (400,940,show_tail="topright",show_xmax=250,show_retain=1)
    b "Mm?" (750,1250,show_tail="baseright",show_xmax=450)

    show Selena lookaway frown  #thinking expression
    call nextpage
    s "I don’t know... that name sounds... familiar." (370,250,show_tail="baseright",show_xmax=350,show_retain=4)
    b "Maybe it’s just one of those names people swear they’ve heard somewhere before?" (850,350,show_tail="rightbase",show_xmax=500,show_retain=3)
    show Selena smile midclose horizontal #different expression
    s "Yeah... maybe?" (330,630,show_tail="topright",show_xmax=450,show_retain=2)
    n "Why did it feel like she was hiding something? Maybe I was just overthinking it?" (460,810,show_tail="narr",show_xmax=400,show_retain=1)
    s "Hmmmmm..." (350,1050,show_tail="topright",show_xmax=300)
    call nextpage
    show Selena frown:
        ease 0.5 zoom 0.8
    n "I felt like I was being carefully examined by a discerning eye at this point." (20,50,show_tail="narr",show_xmax=850,show_retain=4)
    b "Y-Yeah?" (850,350,show_tail="baseright",show_xmax=350,show_retain=3)
    b "I’m certain we’ve met somewhere before. But I can’t really-" (200,650,show_tail="narr",show_xmax=550,show_retain=2)
    play music "audio/Ringtone_bgm_maoudamashii_8bit01.ogg"
    show Selena openmouth open up
    s "...." (380,950,show_tail="topright",show_xmax=350,show_retain=1)
    b "...." (850,1300,show_tail="baseright",show_xmax=350)

    call nextpage
    stop music
    play sound "audio/sfx-bleep.ogg"
    show phone:
        alpha 0.0 xalign 0.2 yalign 0.8 zoom 0.5
        ease 0.5 alpha 1.0 yalign 0.7
    show Selena lookaway openmouth with ease:
        xalign 1.0
    n "I watched as her hand slowly moved to take her ringing phone out of her pocket, knowing full-well where that jingle came from."(20,30,show_tail="narr",show_xmax=680,show_retain=2)
    n " But I didn’t really feel like addressing it, since the look in her eyes was telling me that she... had forgotten to change the ringtone." (20,240,show_tail="narr",show_xmax=500,show_retain=1)
    show Selena smile open
    s "I’ll be right back." (650,550,show_tail="topright",show_xmax=350)
    hide Selena
    hide phone
    with dissolve
    play music "audio/Smile_Sweetly.ogg" fadein 4.5
    n "Before waiting for my answer, she turns off to the side and walks a few steps away, talking to someone on the other end. I couldn’t fully hear the entire conversation, mostly because she was speaking fluent Japanese." (50,810,show_tail="narr",show_xmax=800,show_retain=1)
    n "Which, an average person living here might not speak, but... though I don’t look it, my dad was in the military and stationed in Japan when I was middle school." (75,1090,show_tail="narr",show_xmax=800)

    call nextpage
    n "My Japanese language skills have become quite rusty since we moved years ago, but I could still pick up some snippets of the conversation."(20,30,show_tail="narr",show_xmax=600,show_retain=3)
    s "Yeah I’m awake... what do you mean... that’s today... you’re kidding... what about Akihiro, Yuu, or Ryan... what do you mean they went to a convention... I would’ve gone... not much left to pack... could probably..." (870,300,show_tail="topright",show_xmax=550,show_retain=2)
    n "Suddenly her eyes drift to me and she goes silent for a bit. It’s true that I haven’t known her for that long, however... somewhere in my mind, when I saw that look in her eye, I couldn’t help but feel that she was cooking up some kind of plan." (-30,690,show_tail="narr",show_xmax=550,show_retain=1)
    s "...might have a backup plan... yeah... I’m fine... okay, bye." (850,950,show_tail="topright",show_xmax=320)
    play sound "audio/sfx-bleep.ogg"
    call nextpage
    show Selena at middef:
        xpos 0.35
        yanchor 0.0
        ypos 1.0
        ease 0.3 ypos 0.2
    n "She looked as though she really wanted to tell me something but was unsure of-" (20,30,show_tail="narr",show_xmax=850,show_retain=3)
    s "So this is gonna be a weird one and I know we’ve just met but um...{nw}{w=0.8}" (480,500,show_tail="leftbase",show_xmax=400,show_retain=1)
    s "Could I ask for... a small request?" (480,600,show_tail="lefttop",show_xmax=400,show_retain=0)
    $ persistent.read_Chapter1=True
    return
