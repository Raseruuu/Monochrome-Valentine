image hug = "images/CG/Hug.webp"
image station_ext:
    "images/bg/Station.webp"
    zoom 3.0
image station_ext_run:
    "images/bg/Station_run.webp"
    zoom 3.0
image station_int:
    "images/bg/Station2.webp"
    zoom 2.0
image bagel_int:
    "images/bg/store_interior.webp"

    zoom 2.0 xalign 0.0 yalign 0.1
image street2:
    "images/bg/street_by_konett.webp"
    zoom 0.7 xalign 1.0
transform hugtransform:
    xalign 0.5 yalign 0.8
screen CG_hug():
    zorder 120
    add "hug" at hugtransform


label chapter5_1: #Saying Goodbyes
        # Setting: Train Station - Daylight - Exterior
    scene black

    call screen chap("5", "goodbye") with dissolve
    hide screen chap
    play music "audio/Until_We_Meet_Again.ogg" fadein 2.0
    call nextpage
    $ bedtime=""
    # scene sky_bright with dissolve
    # play sound "moving truck engine.ogg"
    scene sky_morning with dissolve
    n "I think most people might feel a little awkward after the events of last night." (400,20,show_tail="narr",show_xmax=480,show_retain=4)
    n "Not Selena though." (500,240,show_tail="narr",show_xmax=300,show_retain=3)
    n "She woke up before me and was back to her usual energetic self." (50,580,show_tail="narr",show_xmax=600,show_retain=2)
    n "You'd think last night was just a dream." (50,780,show_tail="narr",show_xmax=600,show_retain=1)
    n "But I could still feel the warmth of her hand in mine." (50,980,show_tail="narr",show_xmax=600)

    call nextpage

    n "And..." (50,80,show_tail="narr",show_xmax=600,show_retain=5)
    n "..." (80,220,show_tail="narr",show_xmax=600,show_retain=4)
    show Selena at middef with dissolve
    s "You okay?" (500,350,show_tail="leftbase",show_xmax=380,show_retain=3)
    b "Huh! Ah, right, sorry, just… um… thinking about… stuff." (-50,780,show_tail="leftbase",show_xmax=600,show_retain=2)
    s "Heh, alright."  (550,820,show_tail="lefttop",show_xmax=600,show_retain=1)
    s "I was just saying, I think we're at the end of the line." (600,980,show_tail="lefttop",show_xmax=280)

    call nextpage
    scene station_ext with dissolve #(train station exterior)
    show Selena at middef
    s "Heh, we had fun together didn't we?" (450,180,show_tail="rightbase",show_xmax=400,show_retain=5)
    b "Yeah." (-50,310,show_tail="leftbase",show_xmax=600,show_retain=4)
    s "...are you sad?" (520,380,show_tail="leftbase",show_xmax=600,show_retain=3)
    b "Yeah." (-50,580,show_tail="leftbase",show_xmax=600,show_retain=2)
    show Selena concerned
    s "Me too." (550,680,show_tail="lefttop",show_xmax=600,show_retain=1)
    # "Selena sighed."
    show Selena frown crying
    # play sound "sigh.ogg"
    pause
    s "Me too." (520,850,show_tail="lefttop",show_xmax=600)

    call nextpage
    # new selena expression?
    show Selena opensmile up
    s "Guess we were having so much fun together, that we forgot that this couldn't last forever. Eventually we'd have to split." (400,330,show_tail="rightbase",show_xmax=400,show_retain=5)
    show Selena smile concerned
    s "Much as I wish we could spend more time together." (530,380,show_tail="leftbase",show_xmax=400,show_retain=4)
    show Selena frown
    s "Your phone's still not working?" (550,580,show_tail="lefttop",show_xmax=400,show_retain=3)
    b "Ah, yeah, guess I forgot to charge it." (-50,780,show_tail="leftbase",show_xmax=600,show_retain=2)
    show Selena lookaway smile:
        linear 0.3 xoffset 20
        linear 0.3 xoffset -20
        repeat 3
        linear 0.3 xoffset 0
    s "Hm, hold on."  (550,780,show_tail="lefttop",show_xmax=600,show_retain=1)
    show Selena opensmile open up
    n "After fumbling in her pockets for a bit, she hands me a business card with a very fancy design. It stands in stark contrast to mine, which seems like I just used a default template. Wish I brought some with me." (50,980,show_tail="narr",show_xmax=750)

    call nextpage
    b "Thanks, sorry I didn't bring any of my own." (-50,40,show_tail="lefttop",show_xmax=600,show_retain=3)
    show Selena smile
    s "Heh, it's fine. I mean, who still uses business cards right?" (530,280,show_tail="leftbase",show_xmax=350,show_retain=2)
    show Selena closed opensmile at bounce
    s "Obviously, the same girl who uses an actual camera instead of the one on her phone, apparently!" (500,600,show_tail="lefttop",show_xmax=380,show_retain=1)
    n "We shared a brief laugh, and though we both knew it was time to part, neither of us was willing to take that final step." (20,980,show_tail="narr",show_xmax=700)

    call nextpage
    show Selena smile open
    b "So, where will you go now?" (40,80,show_tail="leftbase",show_xmax=400,show_retain=5)
    s "Well, probably gonna take this truck and move back in with my parents for a while. But I'll probably take the scenic route." (500,340,show_tail="baseleft",show_xmax=400,show_retain=4)
    show Selena lookaway opensmile horizontal
    s "What's the point of this truck if I can't drive it anywhere cool, right?" (360,620,show_tail="righttop",show_xmax=400,show_retain=3)
    show Selena up smile open
    s "What about you? What're your plans?" (500,780,show_tail="lefttop",show_xmax=400,show_retain=2)
    n "That's a good question. I guess I didn't really think about it. I asked her to take me to the station, but truthfully, I'm not sure."  (50,950,show_tail="narr",show_xmax=420,show_retain=1)
    n "What do I want?" (470,1160,show_tail="narr",show_xmax=600)

    call nextpage
    b "I guess for now, I'll probably do the same thing. My parents' place isn't too far, just gotta get on the train then take a few bus stops. Not like I can go back to my old place, so I'll hunker down there until I cam come up with a solid plan, maybe find a new job. My savings won't last forever, after all." (-10,50,show_tail="lefttop",show_xmax=800,show_retain=6)
    show Selena lookaway frown
    s "Yeah." (520,500,show_tail="leftbase",show_xmax=400,show_retain=5)
    n "She looks away from me." (100,600,show_tail="narr",show_xmax=400,show_retain=4)
    s "Yeah…" (550,700,show_tail="leftbase",show_xmax=400,show_retain=3)
    n "She says it again." (100,900,show_tail="narr",show_xmax=400,show_retain=2)
    n "Was she disappointed?" (400,1040,show_tail="narr",show_xmax=400,show_retain=1)
    n "Did I do something wrong?" (500,1200,show_tail="narr",show_xmax=400)

    call nextpage
    show Selena #look away
    n "Before I could ask, she unlocks the doors, continuing to look away from me."(60,60,show_tail="narr",show_xmax=800,show_retain=3)
    n "\nWithout saying a word, I carefully exit the truck and walk around to her window, where she avoids eye contact with me. However, the look on her face told me that she was disappointed with something."(60,600,show_tail="narr",show_xmax=400,show_retain=2)
    n "With what, I'm not sure."(460,600,show_tail="narr",show_xmax=400,show_retain=1)
    n "Hope it wasn't about last night."(460,780,show_tail="narr",show_xmax=400,show_retain=0)
    nvl clear

    call nextpage

    b "Um, so, guess this is it then?" (-30,90,show_tail="topleft",show_xmax=400,show_retain=3)
    show Selena open
    s "..." (600,600,show_tail="leftbase",show_xmax=400,show_retain=2)
    b "I um, ahem, I- I promise I'll call you, just as soon as my phone charges." (-50,580,show_tail="lefttop",show_xmax=400,show_retain=1)
    show Selena squiggly
    s "...." (550,780,show_tail="lefttop",show_xmax=400)

    call nextpage

    n "She sticks her hand out of the driver-side window, her pinky outstretched." (400,40,show_tail="narr",show_xmax=450,show_retain=5)
    n "...." (720,250,show_tail="narr",show_xmax=400,show_retain=4)
    show Selena concerned at middef
    s "Promise?" (400,600,show_tail="righttop",show_xmax=400,show_retain=3)
    b "Of course, we really don't have to-" (400,1000,show_tail="rightbase",show_xmax=400,show_retain=2)
    show Selena horizontal smile
    s "Promise me." (400,1000,show_tail="righttop",show_xmax=400,show_retain=1)
    n "She wasn't gonna let me go without a definitive answer, I suppose." (500,1100,show_tail="narr",show_xmax=450)

    call nextpage
    n "I hooked my pinky with hers, immediately feeling a little embarrassed since we both seemed far too old for this." (40,100,show_tail="narr",show_xmax=650,show_retain=5)
    b "I promise that I'll call you as soon as I can." (20,440,show_tail="topleft",show_xmax=400,show_retain=4)

    show Selena closed up
    s "Okay." (500,600,show_tail="lefttop",show_xmax=400,show_retain=3)
    hide Selena with dissolve
    n "She took a deep breath." (500,800,show_tail="narr",show_xmax=400,show_retain=2)
    n "Inhaled." (600,950,show_tail="narr",show_xmax=400,show_retain=1)

    n "And then screamed into her palms!" (350,1100,show_tail="narr",show_xmax=400)  with Shake((0, 0, 0, 0), 0.5, dist=10)

    call nextpage
    scene station_ext with dissolve:
        xalign 0.8
    show Selena closed opensmile at middef, bounce #jump
    s "Phew! Okay, I feel better now." (450,180,show_tail="leftbase",show_xmax=400,show_retain=2)
    show Selena open smile
    n "She looked at me and smiled her trademark smile." (20,600,show_tail="narr",show_xmax=400,show_retain=1)
    show Selena lookaway opensmile
    s "Alright, I'm gonna go grab a bagel down the street, right there." (500,780,show_tail="lefttop",show_xmax=350)

    # Show a bagel store or whatever that is, maybe we have a BG for that as a cut-in image
    call nextpage
    show Selena open smile
    s "Well, take care Blake. We are but two ships passing in the night, and I hope we pass again soon." (350,300,show_tail="rightbase",show_xmax=350,show_retain=3)
    b "Did you just come up with that?" (850,550,show_tail="righttop",show_xmax=400,show_retain=2)
    show Selena closed
    s "No, of course not, I stole it from a tagline for tea." (400,700,show_tail="topright",show_xmax=400,show_retain=1)

    n "HOW IS THAT A TAGLINE FOR TEA?!" (200,1150,show_tail="narr",show_xmax=700) with Shake((0, 0, 0, 0), 0.5, dist=10)

    call nextpage
    hide Selena with dissolve
    pause 0.5
    n "And with that, pressed her foot to the pedal and drove off." (100,150,show_tail="narr",show_xmax=650,show_retain=3)
    n "Hm?" (100,400,show_tail="narr",show_xmax=400,show_retain=2)
    n "Ah, there's that feeling again." (400,700,show_tail="narr",show_xmax=400,show_retain=1)
    n "Regret." (620,1100,show_tail="narr",show_xmax=400)

    call nextpage
    n "Should I have gone with her?" (200,200,show_tail="narr",show_xmax=400,show_retain=3)
    n "It could've been fun." (250,400,show_tail="narr",show_xmax=400,show_retain=2)
    n "Yeah. Well, too late now." (400,800,show_tail="narr",show_xmax=400,show_retain=1)
    n "Maybe in another life." (500,1000,show_tail="narr",show_xmax=350)
    # [End scene]

label chapter5_2: #Closure with Ashley
    scene station_int with fade #(platform/daylight)
    call nextpage

    n " \"The Red Line Train will be arriving in 5 minutes.\" "  (150,150,show_tail="narr",show_xmax=500,show_retain=5)
    n "At least, that's what the screen predicted, the trains were always just a little off from the predicted time." (50,400,show_tail="narr",show_xmax=400,show_retain=4)
    n "..." (550,700,show_tail="narr",show_xmax=400,show_retain=3)
    n "Strange, I still feel regret." (50,800,show_tail="narr",show_xmax=400,show_retain=2)
    n "Was this the right decision?" (50,1000,show_tail="narr",show_xmax=400,show_retain=1)
    n "..." (650,1200,show_tail="narr",show_xmax=400)

    call nextpage
    n "Well, whether it's right or wrong, it's too late now." (80,200,show_tail="narr",show_xmax=600,show_retain=2)
    n "From the top of the stairs, leading down to the platform where I was, a group of people started descending. Guess they didn't want to risk missing the train either." (100,400,show_tail="narr",show_xmax=700,show_retain=1)
    n "....?" (100,700,show_tail="narr",show_xmax=400)

    call nextpage
    n "Huh, that's funny. In that crowd there peering down at their phone..." (200,200,show_tail="narr",show_xmax=400,show_retain=2)
    n "That person looks a lot like Ashley." (200,550,show_tail="narr",show_xmax=400,show_retain=1)
    n "They stop when they notice something in my direction, and seem to be stomping closer." (350,800,show_tail="narr",show_xmax=400)

    call nextpage

    play music "audio/Midnight_Snowfall.ogg"
    a "Blake?"  (20,-20,show_tail="lefttop",show_xmax=400,show_retain=4)
    n "They called my name." (200,200,show_tail="narr",show_xmax=400,show_retain=3)
    a "Blake!" (20,350,show_tail="lefttop",show_xmax=400,show_retain=2)
    n "This person who looked suspiciously like Ashley marched all the way up to me and put her hands on my shoulders, forcing me to look at her." (70,465,show_tail="narr",show_xmax=450,show_retain=1)
    n "Ah, yep. This is definitely Ashley." (540,700,show_tail="narr",show_xmax=340)

    call nextpage
    b "Oh… hey." (800,200,show_tail="rightbase",show_xmax=400,show_retain=2)
    n "Definitely didn't know what to say to her." (200,300,show_tail="narr",show_xmax=400,show_retain=1)
    n "What I do know that it was like my heart just did a double backflip… and not in a good way." (300,700,show_tail="narr",show_xmax=550)

    call nextpage
    show Ashley down frown at middef,bounce with dissolve
    a "Do not \"oh hey\" me." (450,200,show_tail="leftbase",show_xmax=400,show_retain=5)
    a "You just randomly disappeared." (480,400,show_tail="leftbase",show_xmax=400,show_retain=4)
    show Ashley lookaway concerned
    a "I know that we're not…" (500,450,show_tail="lefttop",show_xmax=400,show_retain=3)
    n "She trailed off, as if the words were stuck in her throat and refused to manifest." (50,550,show_tail="narr",show_xmax=400,show_retain=2)
    n "To be fair, the feeling was mutual." (80,850,show_tail="narr",show_xmax=400,show_retain=1)
    n "There was a strong urge to run, to flee, to avoid the issue." (100,1050,show_tail="narr",show_xmax=400)

    call nextpage
    n "No." (20,30,show_tail="narr",show_xmax=400,show_retain=7)
    n "I can't run from this." (20,160,show_tail="narr",show_xmax=400,show_retain=6)
    n "If I don't face this, then… it's not fair to her either." (480,140,show_tail="narr",show_xmax=400,show_retain=5)
    b "I'm sorry." (-50,500,show_tail="baseleft",show_xmax=400,show_retain=4)
    show Ashley down open
    a "Don't mind it, now where's your phone?" (480,600,show_tail="leftbase",show_xmax=400,show_retain=3)
    b "Oh, it's been dead for a while, but that's not what I meant." (-50,730,show_tail="baseleft",show_xmax=400,show_retain=2)
    show Ashley up
    a "Eh?" (550,700,show_tail="lefttop",show_xmax=400,show_retain=1)
    b "..." (20,830,show_tail="lefttop",show_xmax=400)

    call nextpage
    nv "Long inhale."
    nv "Exhale."
    nv "What would she want to hear?"
    nv "I don't know."
    nvl clear

    call nextpage
    n "What do I want to say, then?" (20,-20,show_tail="narr",show_xmax=400,show_retain=3)
    b "I'm sorry I couldn't see how much you were suffering alone. I'm sorry that I made you feel like you couldn't talk to me about what you were going through. I'm sorry that I couldn't be the person you needed most." (-10,720,show_tail="leftbase",show_xmax=900,show_retain=2)
    a "..."  (550,880,show_tail="topleft",show_xmax=400,show_retain=1)
    stop music fadeout 1.0
    b "If I could, I'd go back, try to be a better man to you. Listen to you, pay attention to your needs. I wouldn't have strung you along for so long just because I-" (50,1230,show_tail="leftbase",show_xmax=800)

    call nextpage
    # https://youtu.be/xGtsiqJDyYs?t=700 up until about 14:00 is the song I'm imagining. Don't use this actual song, it just sets the scene.
    # show ashley #new expression, sigh?
    play music "audio/Meeting.ogg"
    show Ashley lookaway:
        yoffset 0
        ease 1.0 yoffset 40
    a "Why are you telling me this now?" (500,200,show_tail="leftbase",show_xmax=400,show_retain=3)
    show Ashley concerned
    a "What are you trying to accomplish here?"  (550,400,show_tail="leftbase",show_xmax=400,show_retain=2)
    show Ashley midclose down
    a "To absolve yourself?" (450,600,show_tail="leftbase",show_xmax=400,show_retain=1)
    show Ashley lookaway
    a "You overly sentimental fool." (520,700,show_tail="lefttop",show_xmax=400,show_retain=0)
    # call nextpage
    # This would be a great spot for a cg
    hide Ashley with dissolve
    n "She pressed her forehead into my chest."(50,900,show_tail="narr",show_xmax=600)
    show Ashley closed frown up at middef with dissolve:
        zoom 1.2
    call nextpage
    a "It's fine. What's done is done, and this is just the way things turned out." (390,200,show_tail="rightbase",show_xmax=400,show_retain=4)
    show Ashley open smile concerned
    a "As much as I wish things could go back to how they were before, that's just not an option here." (450,300,show_tail="leftbase",show_xmax=400,show_retain=3)
    n "Her voice cracked as she wrapped her arms around my back." (500,450,show_tail="narr",show_xmax=360,show_retain=2)
    show Ashley lookaway
    a "I never wanted things to get this bad, my time with you was special to me, even if things ended the way they did." (420,710,show_tail="righttop",show_xmax=400,show_retain=1)
    show Ashley open
    a "You're not a bad person, I don't hate you. Your actions made me cry more than once, yes, but that doesn't mean I want you to just disappear from my life." (450,1000,show_tail="righttop",show_xmax=450)

    call nextpage
    show Ashley midclose
    b "I'm sorry." (-40,100,show_tail="topleft",show_xmax=400,show_retain=3)
    a "Stop apologizing." (480,300,show_tail="leftbase",show_xmax=400,show_retain=2)
    show Ashley open
    a "That curtain has fallen on that part of our life, so now it's time to go on to another act." (500,580,show_tail="leftbase",show_xmax=380,show_retain=1)
    b "Sorry, I just… I don't want to leave things like this. I want to do at least one thing for you, to take even a tiny bit of the pain I caused you to go away." (-40,800,show_tail="topleft",show_xmax=500)

    call nextpage
    show Ashley closed
    a "Then, can I stay like this for just a little bit? Would that be okay with you?" (480,250,show_tail="leftbase",show_xmax=400,show_retain=4)
    b "You can stay there for as long as you need to." (-40,400,show_tail="topleft",show_xmax=400,show_retain=3)
    a "Thank you." (480,550,show_tail="lefttop",show_xmax=400,show_retain=2)
    b "You're too good for someone like me." (-10,700,show_tail="lefttop",show_xmax=400,show_retain=1)
    show Ashley frown
    a "..." (750,1100,show_tail="lefttop",show_xmax=400)

    call nextpage
    show Ashley open up
    b "I wish things could be different." (-50,30,show_tail="topleft",show_xmax=400,show_retain=5)
    a "I know." (500,300,show_tail="lefttop",show_xmax=400,show_retain=4)
    b "I'm sorry I didn't try to talk to you before."(-50,400,show_tail="topleft",show_xmax=400,show_retain=3)
    show Ashley concerned lookaway
    a "I'm sorry, too."  (500,600,show_tail="lefttop",show_xmax=400,show_retain=2)
    b "Sorry for leaving without telling you."(-50,700,show_tail="topleft",show_xmax=400,show_retain=1)
    show Ashley up open smile
    a "I forgive you." (500,900,show_tail="lefttop",show_xmax=400)

    call nextpage
    b "What happens to us now?" (-50,200,show_tail="leftbase",show_xmax=400,show_retain=3)

    a "...I'm going to leave this city, try to start over."  (500,300,show_tail="leftbase",show_xmax=400,show_retain=2)
    b "Then, do you want me to go with you?" (-50,600,show_tail="leftbase",show_xmax=400,show_retain=1)
    show Ashley lookaway
    a "...." (600,600,show_tail="lefttop",show_xmax=400)

    call nextpage
    show Ashley open
    a "A part of me would like that." (500,120,show_tail="leftbase",show_xmax=400,show_retain=5)
    a "But, I've never been a fan of re-reading an old story." (480,330,show_tail="leftbase",show_xmax=400,show_retain=4)
    show Ashley closed
    a "We can't be together like we were, and it's for the best if we find our own paths." (500,600,show_tail="leftbase",show_xmax=400,show_retain=3)
    show Ashley open concerned
    a "I know that. Though, I do wish you could come with me, that's just not an option available to us. I'm sorry." (450,780,show_tail="lefttop",show_xmax=430,show_retain=2)
    b "I understand." (-50,1110,show_tail="leftbase",show_xmax=400,show_retain=1)
    show Ashley open smile
    a "I care for you, that's why I feel that you should find your own way." (500,1100,show_tail="lefttop",show_xmax=400)

    # Train arriving noise
    call nextpage
    show Ashley open smile at middef with dissolve
    n "Ashley let go just as the train was coming in, she didn't let me see her face as she started walking towards the doors." (50,40,show_tail="narr",show_xmax=750,show_retain=3)
    show Ashley up
    a "Maybe in another life things could be different. I would hope so." (470,500,show_tail="lefttop",show_xmax=410,show_retain=2)
    a "Until then, do me two small kindnesses; first when you think of me in the future, please let it be a happy memory." (450,700,show_tail="lefttop",show_xmax=430,show_retain=1)
    a "Secondly, find a place where you belong, don't let the chains of the past hold you back." (420,1050,show_tail="lefttop",show_xmax=450)

    call nextpage #20

    n "She plants a small peck on my lips and then backs away." (280,500,show_tail="narr",show_xmax=600,show_retain=2)
    a "Take care, Blake N Lawrence. If I see you again someday, I would hope that we're both living happier lives than before." (400,700,show_tail="righttop",show_xmax=400,show_retain=1)
    hide Ashley with Dissolve(1.5)
    n "The train doors close as Ashley steps in." (500,900,show_tail="narr",show_xmax=350)

    # Ashley on the train could also be a good CG
    call nextpage
    scene station_int with dissolve:
        xalign 0.4 yalign 0.0
        linear 40.0 xalign 1.0

    n "She presses her hand against the glass, and we watch each other leave. In more ways than one." (450,20,show_tail="narr",show_xmax=500,show_retain=4)
    n "In my heart I feel a pang of regret, and part of me wishes that I would've just gotten on that train with her." (150,450,show_tail="narr",show_xmax=500,show_retain=3)
    n "But she was right." (360,650,show_tail="narr",show_xmax=500,show_retain=2)
    n "It was better if we go our separate ways. I just wish her the best of luck in finding what it is she's looking for." (20,780,show_tail="narr",show_xmax=600,show_retain=1)
    n "Her last requests rang in my mind as I leaned against a pillar on the platform." (360,1050,show_tail="narr",show_xmax=500)

    call nextpage
    show Blake closed frown at middef
    b "Find a place where I belong."  (500,200,show_tail="leftbase",show_xmax=300,show_retain=6)
    n "Instantly my mind flashed to Selena." (20,150,show_tail="narr",show_xmax=450,show_retain=5)
    n "Why am I thinking of her now?" (510,250,show_tail="narr",show_xmax=315,show_retain=4)
    n "Don't tell me…" (550,400,show_tail="narr",show_xmax=500,show_retain=3)
    n "No, of course not, it's too soon. That would just be a rebound right? Rebounds aren't good for anyone, right?" (10,650,show_tail="narr",show_xmax=450,show_retain=2)
    n "Besides, it's only been a day." (450,950,show_tail="narr",show_xmax=430,show_retain=1)
    n "Just get on the next train, go to my parent's house, find a new job, and forget this impulsively crazy feeling." (200,1100,show_tail="narr",show_xmax=630)

    # Flashback line
    hide Blake
    call nextpage
    show screen black_border
    show Ashley at middef
    show flashback:
        alpha 0.4
    with dissolve
    a "Don't let the chains of the past hold you back." (450,400,show_tail="baseleft",show_xmax=460)
    hide screen black_border with dissolve
    play music "audio/Beside_bgm_maoudamashii_acoustic29.ogg" volume 0.4
    call nextpage
    hide Ashley
    hide flashback
    with dissolve
    n "......"  (70,300,show_tail="narr",show_xmax=500,show_retain=4)
    n "Dammit." (70,450,show_tail="narr",show_xmax=500,show_retain=3)
    n "Screw it all." (40,620,show_tail="narr",show_xmax=500,show_retain=2)
    n "If Selena were in my shoes, she'd just go for it, regardless of the social rules." (70,800,show_tail="narr",show_xmax=600,show_retain=1)
    show Blake closed smile at middef with dissolve
    b "Just trust my instincts, right?" (500,1100,show_tail="lefttop",show_xmax=500)

    call nextpage
    show Blake open frown with dissolve
    n "Well, my instincts were basically screaming: \"What are you doing here, you colossal moron? Go after her, this is basically a romcom movie moment, perfectly set up for you.\" Is what they're saying." (150,30,show_tail="narr",show_xmax=720,show_retain=4)
    n "....." (100,340,show_tail="narr",show_xmax=500,show_retain=3)
    n "Inhale." (650,500,show_tail="narr",show_xmax=500,show_retain=2)
    n "Exhale." (650,700,show_tail="narr",show_xmax=500,show_retain=1)
    show Blake smile closed
    b "Goddammit." (550,950,show_tail="narr",show_xmax=500)

    call nextpage
    hide Blake with dissolve
    n "As if a starting gun had been fired into the air, I leapt into action! Thinking to myself that I could catch up to her!" (120,300,show_tail="narr",show_xmax=6500,show_retain=2)
    n "She couldn't have gotten that far right?" (150,600,show_tail="narr",show_xmax=500,show_retain=1)
    n "What's a little bit of running, anyways?" (150,800,show_tail="narr",show_xmax=500)
    # [End scene]

label chapter5_3: #Running after Selena
    scene station_ext_run with dissolve
    # https://www.youtube.com/watch?v=QOnXWk-Bwno just imagine that song playing over this section
    call nextpage
    # add image motion lines converging into center to depict spriting motion
    n "Goddammit I hate running!" (600,250,show_tail="narr",show_xmax=230,show_retain=2)
    n "Years of sitting behind a desk has not been great on my physical fitness!" (350,500,show_tail="narr",show_xmax=500,show_retain=1)
    n "I haven't been running that long! Why am I so out of breath!" (380,950,show_tail="narr",show_xmax=500)

    #scene bagel_ext (exterior of the bagel shop)
    call nextpage
    n "The moving truck's not here!" (150,300,show_tail="narr",show_xmax=500,show_retain=2)
    n "Dammit! Did I run this way for nothing?" (150,600,show_tail="narr",show_xmax=500,show_retain=1)
    n "Maybe someone knows something inside?" (150,800,show_tail="narr",show_xmax=500)

    scene bagel_int with dissolve
    call nextpage
    n3 "Hello, welcome to-{nw}" (50,200,show_tail="leftbase",show_xmax=500,show_retain=2)
    show Blake up frown at middef, bounce#pop up animation
    b "No time- wait, don't I know you from… nevermind!" (500,600,show_tail="lefttop",show_xmax=500,show_retain=1)
    b "Listen, did a woman driving a moving truck just come in here to buy some bagels?" (520,900,show_tail="lefttop",show_xmax=330)

    call nextpage
    n3 "Girl roughly your height?"  (50,20,show_tail="topleft",show_xmax=340,show_retain=5)
    show Blake down
    b "Yes." (550,350,show_tail="leftbase",show_xmax=500,show_retain=4)
    n3 "Wearing a hat?" (50,400,show_tail="topleft",show_xmax=500,show_retain=3)
    show Blake smile
    b "Yep!" (550,650,show_tail="lefttop",show_xmax=500,show_retain=2)
    n3 "Has a demeanor that can only be described as, brighter than the white hot intensity of the sun?" (50,700,show_tail="topleft",show_xmax=500,show_retain=1)
    show Blake opensmile
    b "Yes! That's her! Was she here?" (500,1100,show_tail="lefttop",show_xmax=400)

    call nextpage
    n3 "Oh yeah, she was just here. Ate a few bagels by that table right over there, kinda seemed like comfort food if you ask me." (50,60,show_tail="topleft",show_xmax=500,show_retain=3)
    show Blake openmouth
    b "Which way'd she go, please?" (550,350,show_tail="leftbase",show_xmax=350,show_retain=2)
    n3 "Huh? Oh right, uhhh, right there." (20,630,show_tail="topleft",show_xmax=500,show_retain=1)
    n "He points down the street to the west." (50,920,show_tail="narr",show_xmax=500)

    call nextpage
    n3 "Right down Mulberry Street, she took her truck and went down that direction. If you hurry you might be able to catch her." (50,20,show_tail="topleft",show_xmax=500,show_retain=3)
    b "Okay, thanks!" (550,520,show_tail="lefttop",show_xmax=500,show_retain=2)
    show Blake:
        ease 0.3 xpos 0.0 xanchor 1.0
    n "My body was already anticipating the physical toll I was about to exert on it, but I didn't care! I bolted out at the door like a bat out of hell!" (250,700,show_tail="narr",show_xmax=600,show_retain=1)
    n3 "H-Hey! Don't you want to buy some bagels? There's a special going on!" (50,980,show_tail="topleft",show_xmax=500)

    scene street2 with dissolve
    call nextpage
    n "Okay, he said go down Mulberry street! Right!" (50,80,show_tail="narr",show_xmax=500,show_retain=3)
    n "I had just about broken into a sprint, putting the bagel shop past me when I spotted a familiar sight in the parking lot behind the bagel shop." (50,280,show_tail="narr",show_xmax=800,show_retain=2)
    n "That's the moving truck right there!" (50,690,show_tail="narr",show_xmax=500,show_retain=1)
    n "Oh thank merciful god it's just right there!" (50,920,show_tail="narr",show_xmax=500)

    call nextpage
    scene sky_bright with dissolve
    hide Blake
    n "I immediately turned around and made a beeline for the truck, just trying to push my legs a bit further." (20,60,show_tail="narr",show_xmax=700,show_retain=3)
    n "By the time I got to the truck, my legs were like puddy, my heart was beating faster than a hummingbird's wings. I braced my hand against the side of the truck as I took a few moments to breathe." (50,300,show_tail="narr",show_xmax=600,show_retain=2)
    b "{size=50}S-Selena!!!{/size}" (350,570,show_tail="yell",show_xmax=500,show_retain=1)
    n "I choked out, but no one was there?" (480,1000,show_tail="narr",show_xmax=400)

    call nextpage
    with fade
    n "I looked through the window, but she wasn't there either." (80,100,show_tail="narr",show_xmax=500,show_retain=3)
    n "But, in the window I saw the driver-side door open." (50,300,show_tail="narr",show_xmax=500,show_retain=2)
    n "So, I slowly walked around the edge, and around the corner I peered Selena leaning against the truck, toolbox by her leg, looking sullen." (50,520,show_tail="narr",show_xmax=450,show_retain=1)
    show Selena frown concerned at middef with dissolve: #sad
        xpos 0.7
    b "S-Selena?" (-50,950,show_tail="lefttop",show_xmax=500)

 ############################

    call nextpage ## 10
    play music "audio/bgm_maoudamashii_acoustic13.ogg" volume 0.5
    show Selena up openmouth at bounce #bounce and shocked
    n "She twitched, and slowly looked in my general direction." (50,20,show_tail="narr",show_xmax=500,show_retain=4)
    n "Her gaze remained fixated on me, as if I was some kinda illusion that'd vanish if she blinked." (20,250,show_tail="narr",show_xmax=450,show_retain=3)
    s "Blake?" (750,400,show_tail="leftbase",show_xmax=500,show_retain=2)
    b "Yeah. That's me… hey… sorry… I'm just a bit… oh god..." (-50,620,show_tail="lefttop",show_xmax=500,show_retain=1)
    n "I slipped, but instead of hitting pavement, I landed in Selena's embrace." (50,1020,show_tail="narr",show_xmax=700)
    # screenshake
    scene black with dissolve

    # CG of selena hugging Blake, probably something like this: https://preview.redd.it/zfbpcoooknb51.jpg?width=1920&format=pjpg&auto=webp&s=27488d1c61a03a626512b116fd3c3fedb2ade128 and https://i.pinimg.com/originals/c8/c1/5b/c8c15bcd293eedf5a7372f0b0571f064.jpg
    show screen CG_hug with dissolve
    call nextpage
    s "You're really here?" (400,350,show_tail="rightbase",show_xmax=500,show_retain=3)
    b "Yep, I'm really here." (550,520,show_tail="lefttop",show_xmax=300,show_retain=2)
    s "No I mean, WHY are you here? Weren't you gonna go to your parent's place?" (350,600,show_tail="righttop",show_xmax=350,show_retain=1)
    b "Yeah, I was." (520,820,show_tail="lefttop",show_xmax=300)

    call nextpage
    b "Things sorta… changed though." (550,220,show_tail="leftbase",show_xmax=300,show_retain=2)
    s "Like what?" (350,520,show_tail="righttop",show_xmax=300,show_retain=1)
    b "Well… the thing is…" (560,620,show_tail="lefttop",show_xmax=300)

    call nextpage
    n "Crap, why was I here?" (560,convo_ypos(-150),show_tail="narr",show_xmax=300,show_retain=1)
    n "I'm just operating on emotions and instinct, I can't really put this into coherent words. At least, none that don't sound really creepy."(550,convo_ypos(40),show_tail="narr",show_xmax=420,show_retain=0)
    call nextpage
    n "Oh hey, Selena! I just realized that I want to spend more time with you and didn't want to part because my ex helped me receive some closure and told me to find a place I belong and I think that place is with you!"(520,convo_ypos(-150),show_tail="narr",show_xmax=450,show_retain=1)
    n "Come on, brain! It's been like a day. Just… gimme some time to at least untangle my emotions."(560,convo_ypos(400),show_tail="narr",show_xmax=300,show_retain=0)

    call nextpage
    n "Crap, was I silent again?" (80,30,show_tail="narr",show_xmax=300,show_retain=1)
    n "Say something so it seems like you were paying attention." (400,40,show_tail="narr",show_xmax=450,show_retain=0)
    b "We still haven't finished watching the remake of, Of Vampires and Boxers." (550,320,show_tail="leftbase",show_xmax=300,show_retain=2)
    s "Huh?" (250,620,show_tail="righttop",show_xmax=300,show_retain=1)
    b "Well, I was curious about how the remake would handle the flawed masterpiece episode where the Boxer shows up to save Vamairi from a rival vampire and uses the power of friendship to beat the crap out of someone he should have no chance against. The fight choreography in that episode was cinematic genius, the way they worked around the budgetary limitations, right?" (500,600,show_tail="topleft",show_xmax=450)

    call nextpage
    s "..." (250,350,show_tail="rightbase",show_xmax=300,show_retain=2)
    b "And… um…" (550,520,show_tail="lefttop",show_xmax=300,show_retain=1)
    n "I cleared my throat, well more like coughed it out" (400,920,show_tail="narr",show_xmax=400)

    call nextpage
    b "And, also, because… traveling with you." (500,220,show_tail="leftbase",show_xmax=300,show_retain=5)
    b "Sounded… kinda cool." (600,380,show_tail="leftbase",show_xmax=300,show_retain=4)
    b "Plus we're going in the same direction, so… it'd probably be more interesting to travel together than to take separate transportation." (540,500,show_tail="topleft",show_xmax=380,show_retain=3)
    b "Or… something." (500,880,show_tail="topleft",show_xmax=300,show_retain=2)
    b "Sorry, I think I'm babbli-" (600,1050,show_tail="topleft",show_xmax=300,show_retain=1)
    n "She shut me up with a kiss." (50,1150,show_tail="narr",show_xmax=300)

    call nextpage
    hide screen CG_hug with dissolve
    n "Is that butterflies, I feel butterflies." (30,20,show_tail="narr",show_xmax=650,show_retain=4)
    n "Wait, no, come back, don't pull away yet!" (50,220,show_tail="narr",show_xmax=700,show_retain=3)
    show Selena concerned at middef:
        zoom 2.0
    s "...sorry, but you know, follow my instincts and stuff. You know." (350,780,show_tail="righttop",show_xmax=300,show_retain=2)
    n "...." (550,920,show_tail="narr",show_xmax=300,show_retain=1)
    n "I quickly plant a kiss on her cheek in return." (550,1060,show_tail="narr",show_xmax=300)
    hide Selena with dissolve
    call nextpage
    show screen CG_hug with dissolve
    b "Yeah, same." (550,320,show_tail="leftbase",show_xmax=300,show_retain=5)
    n "She goes bright red and tries to hide her face in my shoulder." (50,520,show_tail="narr",show_xmax=500,show_retain=4)
    s "You know, this is probably just a rebound thing." (350,720,show_tail="righttop",show_xmax=350,show_retain=3)
    b "Pretty likely."  (550,870,show_tail="lefttop",show_xmax=300,show_retain=2)
    s "We might get hurt later." (350,960,show_tail="righttop",show_xmax=300,show_retain=1)
    b "Maybe." (550,1070,show_tail="lefttop",show_xmax=300)

    call nextpage
    s "I'm pretty sure everyone in the world would say this is a bad idea."  (350,320,show_tail="rightbase",show_xmax=400,show_retain=3)
    b "Yeah, well, everyone in the world can go to hell." (550,350,show_tail="lefttop",show_xmax=300,show_retain=2)
    s "Blake, you're such a… I don't even know." (290,620,show_tail="righttop",show_xmax=400,show_retain=1)
    s "You might end up hating me, I can be a little hard to deal with." (290,820,show_tail="righttop",show_xmax=400)

    call nextpage
    b "Well, I don't hate you now. So, let's just see how far we can take this and hope that if we do split up later, we'll have more good memories than bad ones?" (480,350,show_tail="leftbase",show_xmax=400,show_retain=4)
    b "But I think that... not thinking about things kinda got me in a bad place to begin with so how about… We just take things nice and slow, see where they take us, okay?" (500,500,show_tail="lefttop",show_xmax=380,show_retain=3)
    s "Okay, yeah, that sounds nice. I can do that." (280,650,show_tail="righttop",show_xmax=300,show_retain=2)
    b "Good." (450,980,show_tail="lefttop",show_xmax=400,show_retain=1)
    s "Good." (250,980,show_tail="righttop",show_xmax=300)

    call nextpage
    b "...So, you gonna let me up, or…?" (500,320,show_tail="leftbase",show_xmax=300,show_retain=5)
    s "No. Ten more minutes." (300,380,show_tail="righttop",show_xmax=300,show_retain=4)
    b "Why ten?" (550,480,show_tail="leftbase",show_xmax=300,show_retain=3)
    s "Now it's twenty." (300,620,show_tail="righttop",show_xmax=300,show_retain=2)
    b "We're probably gonna get kicked out of the parking lot." (580,770,show_tail="lefttop",show_xmax=400,show_retain=1)
    s "Forty." (250,920,show_tail="righttop",show_xmax=300)
    hide screen CG_hug
    call nextpage
    scene sky_morning
    show Selena at middef with Dissolve(1.5):
        zoom 0.8
    n "This girl… she can be cute, childish, stubborn, impulsive, kind, emotional, and an endless source of positivity."(50,600,show_tail="narr",show_xmax=700, show_retain=2)
    n"She's got a lot of strengths and flaws, but somehow… " (150,800,show_tail="narr",show_xmax=700,show_retain=1)
    show Selena closed with Dissolve(1.0)
    n"I think spending time with her will be anything but boring." (200,950,show_tail="narr",show_xmax=700,show_retain=0)
    # [End scene, play credits]
    return

# label chapter5_4: #Next chapter of their lives*
#Setting: On the open road

    # pan down from a sky bg to the moving van on the side of the road or something
    # fade out into ANOTHER cg, this time of both of them in the back of the truck, huddled around a laptop

    # show screen Laptop
    # call nextpage
    # s "Ah!" (250,convo_ypos(20),show_tail="leftbase",show_xmax=300,show_retain=2)
    # b "What's up? Are we running out of snacks?"(800,convo_ypos(20),show_tail="rightbase",show_xmax=300,show_retain=2)
    # s "No, well, yes to the second part. But that's not what I'm talking about."(250,convo_ypos(20),show_tail="leftbase",show_xmax=300,show_retain=2)
    # b "Oh, then what is it?"(800,convo_ypos(20),show_tail="rightbase",show_xmax=300,show_retain=2)
    # s "I was just thinking, is this a Watchmix and Chill, thing?"(250,convo_ypos(20),show_tail="leftbase",show_xmax=300,show_retain=2)
    #
    # b "Do you want it to be?"(800,convo_ypos(20),show_tail="rightbase",show_xmax=300,show_retain=2)
    # s "....."(800,convo_ypos(20),show_tail="leftbase",show_xmax=300,show_retain=2)
    # A few cg variants of her eyes looking around, as if thinking, weighing the pros and cons and all that stuff, then ends with a mischievous smirk
    # she closes the laptop, which also closes blacks out the screen
    # return
    # After the credits are done rolling, fade into a sky bg, then pan down to the city (or just zoom out from a sky shot of the city bg so it shows the city. Think cone)
# After the city BG functioning as the establishing shot, cut to an office space, a conference room specifically
