define n1 = Character("(Clerk 1)", screen ="bubble_say")
define n2 = Character("(Clerk 2)", screen ="bubble_say")
define n3 = Character("(Clerk 3)", screen ="bubble_say")
image combini_day:
    "images/bg/Convenience store.webp"
    zoom 3.0 xalign 0.6
image school_stairs = "images/bg/school_stairs_w.webp"
image school_class = "images/bg/school_classroom_w.webp"
screen selena_crying():
    zorder 120
    add "images/cg/CG5.webp" at cry_transform
transform cry_transform:
    alpha 0.0 zoom 0.8 xalign 0.9 yalign 0.5
    linear 1.5 alpha 1.0

label chapter3_1: #At the convenience store
    ## cut-in image of the list that Selena gives in the previous scene
    play music "audio/bgm_maoudamashii_acoustic50.ogg" volume 0.5
    scene black
    call screen chap("3", "Stranger") with dissolve
    call nextpage
    scene combini_day with dissolve:
        zoom 0.7
    show Blake frown at middef
    b "You’re closed?" (320,350,show_tail="rightbase",show_xmax=600,show_retain=3)
    show Blake:
        linear 0.5 xalign 0.6
    b "But the sign says-" (320,420,show_tail="righttop",show_xmax=600,show_retain=2)
    n1 "Sorry, sir! We’re just experiencing a little… delay, when it comes to opening." (850,600, show_tail="righttop",show_xmax=300,show_retain=1)
    n "The man, who I could only assume was the clerk, stood behind the door with just a crack open while frantically looking behind him every once in a while." (380,880,show_xmax=480, show_tail="narr")

    call nextpage
    n "If I didn’t know any better, I’d think this was some kind of diversion, and he was robbing the store."(50,50,show_tail="narr",show_xmax=700,show_retain=3)
    show Blake midclose
    n "He did seem pretty suspicious." (50,280,show_tail="narr",show_xmax=600,show_retain=2)
    n "And I don’t mean that he looked suspicious, I mean that he was sweating, twitching, looking around, and was holding a baseball bat behind his back…" (50,750,show_tail="narr",show_xmax=700,show_retain=1)
    n "Just saying, with all those elements, he seemed like a pretty suspicious guy." (500,1100,show_tail="narr",show_xmax=500)

    call nextpage
    show Blake open#another expression
    b "Oh? Well, alright then. Do you know how long it’s going to-" (450,320,show_tail="leftbase",show_xmax=400)
    window hide
    # play sound "crash.ogg"
    show Blake openmouth
    #eyes wide mouth wide
    # screen shake
    n "All of a sudden, the sound of several heavy objects crashing blasted through the interior of the convenience store." (50,800,show_tail="narr",show_xmax=800)
    show Blake frown
    call nextpage
    n2 "LOOK THERE IT IS!" (-50,-50,show_tail="yell",show_xmax=800,show_retain=4) with Shake((0, 0, 0, 0), 0.5, dist=10)
    n3 "GRAB IT WITH THE NET!" (450,350,show_tail="yell",show_xmax=800,show_retain=3) with Shake((0, 0, 0, 0), 0.5, dist=10)
    show Blake:
        linear 0.3 xalign 0.42#shocked
    b "What was that?" (350,750,show_tail="baseright",show_xmax=500,show_retain=2)
    n1 "Nothing." (950,950,show_tail="righttop",show_xmax=500,show_retain=1)

    n "It worries me how he said that with a straight face." (20,1080,show_tail="narr",show_xmax=800)

    call nextpage
    # show Blake #def eye mouth open
    show Blake frown: #mouth closed eyes wide
        linear 0.3 xalign 0.6
    b "Are you sure? Cause it seems like there’s something…" (400,380,show_tail="rightbase",show_xmax=400,show_retain=4)
    n2 "OH GOD, LOOK AT ITS TEETH!" (500,150,show_tail="yell",show_xmax=700,show_retain=3) with Shake((0, 0, 0, 0), 0.5, dist=10)
    b "Strange going on..." (320,500,show_tail="rightbase",show_xmax=320,show_retain=2)
    n3 " IT’S UP IN THE CEILING TILES! DON’T LET IT ESCAPE OUT THE BACK!" (450,500,show_tail="yell",show_xmax=550,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=10)
    b "Uh… in there… in the back."(400,950,show_tail="topright",show_xmax=380)

    call nextpage
    n1 "Oh no it’s … only a bat." (-0,250,show_tail="leftbase",show_xmax=600,show_retain=2)
    show Blake #wide eye
    b "A bat?" (580,480,show_tail="topleft",show_xmax=500,show_retain=1)
    n1 "Yes." (0,400,show_tail="lefttop",show_xmax=500)
    # play sound "Glass breaking noise!"

    call nextpage
    n "Suddenly, one of the cashiers came crashing out through the glass windows on the side of the store." (400,100,show_tail="narr",show_xmax=500,show_retain=3)
    n1 "Just a bat." (-10,350,show_tail="lefttop",show_xmax=500,show_retain=2)
    n "The cashier who was thrown out got right back up, grabbed his mop, and dashed around back." (450,700,show_tail="narr",show_xmax=400,show_retain=1)
    show Blake midclose
    n "...Oooookay, I’ve had enough of that. Just gonna ignore all of this before I get dragged into some strange monster hunting plot or something.." (350,1000,show_tail="narr",show_xmax=520)

    call nextpage
    show Blake frown lookaway #eyes def mouth close
    b "Well… if I can’t go in, can I buy some stuff from out here? I have a list." (400,400,show_tail="rightbase",show_xmax=380,show_retain=1)

    show Blake open
    n "I say this as I quickly hand him the note that Selena gave me, and watch him read the note while his other arm seems to swing at something behind the wall. I don’t know what it was, but it sounded like it was snarling and I was definitely not going in there." (20,800,show_tail="narr",show_xmax=700)

    call nextpage
    n1 "Okay, I’ll be right back with your items. \nYou can sit over there in the \nparking lot, and I’ll be right with you." (-20,70,show_tail="lefttop",show_xmax=400,show_retain=2)
    n "I then watched this man look at me as if it was the last time he expected to see me, take a deep breath, and then shut the door behind him. Along with several locks being engaged, scream something in another language, and then more snarling." (180,700,show_tail="narr",show_xmax=620,show_retain=1)
    n "Considering how unusual this day has been, this convenience store tops the charts in weirdness." (370,1090,show_tail="narr",show_xmax=500)

    call nextpage
    hide Blake
    n "I don’t know, I feel like, if I were watching this from an outsider’s perspective, I’d think this whole… episode, feels a bit weird and out of place. Like having a samurai duel in the middle of period drama about upper-class nobility in 19th-Century England." (150,200,show_tail="narr",show_xmax=600, show_retain=1)
    n "Still, they say that truth is often stranger than fiction. Least this’ll be an interesting story to tell to my descendants. If I ever have any." (250,800,show_tail="narr",show_xmax=630)


label chapter3_2: ## Talking with Pat
    call nextpage
    # scene combini_parking_day #at alt position
    # play sound "crowd_noise.ogg" loop
    call nextpage
    n "I’m not alone here." (150,300,show_tail="narr",show_xmax=500, show_retain=1)
    n "It’s a convenience store, but the parking lot almost resembles a tailgating party. Were the items here really that special?" (250,600,show_tail="narr",show_xmax=500)

    call nextpage
    # show crowd_silhouette
    n "Maybe, but I get the feeling some people were just here having an impromptu party.{nw}" (50,10,show_tail="narr",show_xmax=400, show_retain=4)
    n ".....{nw}" (50,260,show_tail="narr",show_xmax=500, show_retain=3)
    n "This is a pretty weird neighborhood." (550,280,show_tail="narr",show_xmax=310, show_retain=2)
    ##
    play music "audio/bgm_maoudamashii_acoustic48.ogg" volume 0.5
    p "Hey buddy, got a light?" (900,620,show_tail="rightbase",show_xmax=300,show_retain=1)
    show Blake up frown at middef#confused
    b "Huh?" (580,670,show_tail="lefttop",show_xmax=500)
    hide Blake with dissolve

    call nextpage
    # play sound "crowd_noise.ogg" loop volume=0.5
    # H(ave the camera pan over to Pat rather than have him slide in if that’s possible, otherwise just do a fade-in)
    # show combini_parking_day #at location
    show Pat at middef with dissolve#at location
    # with #panright

    p "A light. Ya know, a lighter, for the cigarette?" (300,310,show_tail="rightbase",show_xmax=270,show_retain=2)
    b "Uh… sorry, I don’t smoke." (-50,800,show_tail="lefttop",show_xmax=500,show_retain=1)
    show Pat midclose frown
    n "He lets out the weary sigh of someone who’s had a rough day, and took the unlit cigarette out of his mouth." (380,1050,show_tail="narr",show_xmax=480)

    show Pat oneclose smile#different expression
    call nextpage
    p "Eh, probably shouldn’t be smoking anyways. Disgusting habit, bad for my health, and an unnecessary expense." (450,370,show_tail="leftbase",show_xmax=400,show_retain=3)
    n "As he says this, he puts the cigarettes back in the pack, and hook-shots the pack into the nearest garbage bin." (50,670,show_tail="narr",show_xmax=600,show_retain=2)
    n "Nothin’ but net." (50,900,show_tail="narr",show_xmax=400,show_retain=1)
    n "Why do I know that phrase?" (50,1100,show_tail="narr",show_xmax=500)

    call nextpage
    show Pat down open #serious expression
    p "You’re not from around here, are you?" (460,250,show_tail="leftbase",show_xmax=400,show_retain=2)
    b "Uh, what makes you say that?" (850,590,show_tail="rightbase",show_xmax=400,show_retain=1)
    p "Well, spend enough time ‘round here, you tend to recognize a few people." (400,900,show_tail="righttop",show_xmax=400)

    show white:
        alpha 0.7
    call nextpage
    p "See that guy over there? Calls himself Mace because he heard it in a movie once, real name’s Michael though. Hates it, says it’s too generic." (20,100,show_tail="lefttop",show_xmax=800,show_retain=4)
    p "The lady chatting up that mailman there is Gloria, she’s a flirting addict, she’ll flirt with anyone. Dunno how serious she gets. I don’t think she even came here to buy anything." (40,400,show_tail="lefttop",show_xmax=800,show_retain=3)
    p "And that’s Andrew. Everybody hates him, nobody remembers why." (30,700,show_tail="lefttop",show_xmax=800,show_retain=2)
    p "You, on the other hand. Never seen you before, you kinda stand out from the rest of these people." (50,920,show_tail="lefttop",show_xmax=400,show_retain=1)
    b "Well, yeah, I’m just… a visitor." (850,1350,show_tail="rightbase",show_xmax=500)

    hide white with dissolve
    call nextpage
    b "So... you live around here or something?"  (880,100,show_tail="rightbase",show_xmax=600,show_retain=5)
    show Pat up closed at bounce#laughing
    n "At this, he suddenly broke out laughing as if I told him the funniest joke in the world." (520,200,show_tail="narr",show_xmax=450,show_retain=4)
    show Pat normal
    n "It took him a minute to settle down." (620,420,show_tail="narr",show_xmax=240,show_retain=3)
    show Pat open
    p "Haaaaa." (390,600,show_tail="lefttop",show_xmax=400,show_retain=2)
    show Pat midclose frown
    p "Nah. I know someone-" (550,800,show_tail="lefttop",show_xmax=400,show_retain=1)
    n "All of a sudden, he pauses." (70,1150,show_tail="narr",show_xmax=400)

    call nextpage
    show Pat openmouth normal
    p "Well, I used to know someone who lives around here." (320,300,show_tail="baseright",show_xmax=300,show_retain=4)
    show Pat frown
    b "Used to know?" (850,600,show_tail="rightbase",show_xmax=400,show_retain=3)
    b "Ah, I’m sorry for your loss?" (850,800,show_tail="rightbase",show_xmax=400,show_retain=2)
    show Pat frown normal open
    p "Oh, no, I don’t mean that they died. It’s just that…" (350,900,show_tail="righttop",show_xmax=400,show_retain=1)
    n "Where he once seemed like an open book, now it seemed that his stance had shifted, becoming more closed off with this topic." (450,950,show_tail="narr",show_xmax=400)

    call nextpage
    show Pat down midclose
    p "We had... a falling out. And of course, I thought I could fix it. That I could take away all the pain, anger,
        and sorrow with just a handsome smile and a great speech." (400,330,show_tail="leftbase",show_xmax=450,show_retain=4)
    p "Always acting and never thinking." (470,420,show_tail="lefttop",show_xmax=400,show_retain=3)
    p "We ended things pretty badly overseas, so the first thing I did when I got home was ask about them at work,
        thinking that we could still be friends and colleagues." (500,680,show_tail="topright",show_xmax=480,show_retain=2)
    p "Then I learned that they had decided to quit." (550,800,show_tail="lefttop",show_xmax=300,show_retain=1)
    n "This sounds familiar." (350,1150,show_tail="narr",show_xmax=600)

    call nextpage
    show Pat openmouth
    p "So, I ignored the advice of everyone around, and rushed to her place to talk about things.." (420,300,show_tail="leftbase",show_xmax=400,show_retain=5)
    n "He sighed." (570,480,show_tail="narr",show_xmax=300,show_retain=4)
    show Pat up smile open
    p "I don’t really know what I expected. I went in there thinking that I could just… undo everything, because I’m so used to everything going my way. I mean… look at me." (400,600,show_tail="righttop",show_xmax=400,show_retain=3)
    n "He gestures to his well-toned physique, impeccably sculpted face, and general \"{i}I got this{/i}\" demeanor." (480,750,show_tail="narr",show_xmax=400,show_retain=2)
    show Pat down frown
    p "I got about as far as the corner of her street, when I felt something I hadn’t in a long time." (450,1070,show_tail="righttop",show_xmax=450,show_retain=1)
    show Pat midclose
    p "Doubt." (480,1200,show_tail="lefttop",show_xmax=400)

    call nextpage
    show Pat closed
    p "What was I even doing there? What could I possibly say or do to make things better? How do I fix this to make it go back to normal?" (300,250,show_tail="leftbase",show_xmax=560,show_retain=3)
    show Pat midclose
    p "Truth of the matter is, some things can’t be taken back. So, I left. Had my chauffeur turn the car around and drive off without accomplishing anything." (520,700,show_tail="baseleft",show_xmax=350,show_retain=2)
    show Pat open smile up
    p "Why am I even talking about this to a complete stranger?" (350,750,show_tail="righttop",show_xmax=400,show_retain=1)
    show Pat normal smile
    p "Sorry man, you’ve probably got better things to do than listen to me whine about my love life." (450,850,show_tail="lefttop",show_xmax=400)

    call nextpage
    show Pat normal with dissolve:
        xalign 0.8
    b "...why’d you break up?" (20,80,show_tail="leftbase",show_xmax=400,show_retain=4)
    p "Beg your pardon?" (480,270,show_tail="leftbase",show_xmax=400,show_retain=3)
    b "That person you were talking about, was she your girlfriend?" (20,490,show_tail="leftbase",show_xmax=320,show_retain=2)
    show Pat closed
    p "She… was someone I was fond of. We weren’t exclusive, but she was the person I was spending the most time with." (520,720,show_tail="leftbase",show_xmax=350,show_retain=1)
    b "Right. So what went wrong?" (-20,820,show_tail="leftbase",show_xmax=400)

    call nextpage
    show Pat open smile
    p "Hm… I suppose, the honeymoon phase had ended." (320,300,show_tail="rightbase",show_xmax=350,show_retain=3)
    show Pat smile
    p "I left overseas for a job, which gave me something I hadn’t experienced in a while. The feeling of freedom. I didn’t realize how much the prospect of commitment felt like a cage." (410,520,show_tail="lefttop",show_xmax=470,show_retain=2)
    b "But... I’m guessing, she wanted something more?" (-20,1050,show_tail="leftbase",show_xmax=400,show_retain=1)
    p "Eh, who doesn’t? I had always known we were going to have that conversation eventually, but I’d simply chosen to ignore it. We ignored a lot of things; our plans, our differences, our level of commitment." (390,920,show_tail="lefttop",show_xmax=500)

    call nextpage
    show Pat midclose down frown with Fade(1.0,1.0,1.0):
        xpos 0.6
    b "...Yeah, I get that." (-20,150,show_tail="leftbase",show_xmax=400,show_retain=5)
    p "Honestly, it was only a matter of time until it all came crashing down." (420,300,show_tail="leftbase",show_xmax=400,show_retain=4)
    b "And so, after that, you came back home and wanted to see her again." (-20,750,show_tail="leftbase",show_xmax=400,show_retain=3)
    show Pat closed
    p "...That was the plan." (450,820,show_tail="lefttop",show_xmax=400,show_retain=2)
    b "And now?" (-20,1050,show_tail="leftbase",show_xmax=400,show_retain=1)
    p "...." (520,1090,show_tail="lefttop",show_xmax=400)


    call nextpage
    n "The sound of a honking car cut him off. I turn to see a fancy limo out on the street, with the driver waving to this mysterious man." (20,30,show_tail="narr",show_xmax=800,show_retain=1)
    show Pat smile open normal
    p "Well, there’s my ride."  (420,300,show_tail="leftbase",show_xmax=400,show_retain=0)
    hide Pat with dissolve
    pause
    call nextpage
    b "Wait!" (920,500,show_tail="rightbase",show_xmax=400,show_retain=3)
    n "I step between him and the car. I don’t know why, this wasn’t my problem after all." (480,580,show_tail="narr",show_xmax=400,show_retain=2)
    show Pat at middef with dissolve: #expression?
        xalign 0.85
    b "Are you really just gonna walk away?" (920,1000,show_tail="rightbase",show_xmax=400,show_retain=1)
    show Pat smile closed
    p "...." (410,1000,show_tail="righttop",show_xmax=400)

    call nextpage
    b """What if she’s alone, crying, desperately seeking someone to tell her things are gonna get better.
        Are you really just going to leave her in that state to fend for herself?""" (-20,30,show_tail="lefttop",show_xmax=600,show_retain=5)
    show Pat frown open
    p "..." (520,400,show_tail="leftbase",show_xmax=400,show_retain=4)
    b "Aren’t you just running away because you don’t wanna deal with the fallout? And that’s why you ran away from home!" (-20,630,show_tail="lefttop",show_xmax=450,show_retain=3)
    n "...Ah, I said something unnecessary." (120,900,show_tail="narr",show_xmax=400,show_retain=2)
    show Pat smile
    p "...This isn’t just about me, is it?" (570,1020,show_tail="lefttop",show_xmax=300,show_retain=1)
    b "No. Sorry. \nI spoke out of turn." (-20,1280,show_tail="leftbase",show_xmax=500)
    n "What happened to all my fire?" (320,850,show_tail="narr",show_xmax=800)

    call nextpage
    show Pat closed openmouth at middef:
        yoffset 0
        ease 1.0 yoffset 40#sigh
    p "Seems like maybe we have something in common." (300,300,show_tail="rightbase",show_xmax=300,show_retain=3)
    show Pat oneclose smile
    p "Look, I can’t tell you how to handle your own love life issues. However, you might have a point. I am running away from this mess that I made." (470,500,show_tail="lefttop",show_xmax=400,show_retain=2)
    show Pat down
    p "If this were a movie, I’d admit that you’re right, rush down to her place with flowers and chocolate, and tell her that I was wrong about everything and I want to give us another shot."  (420,800,show_tail="righttop",show_xmax=400,show_retain=1)
    show Pat midclose frown
    p "The thing is… that’s just now this thing is gonna play out." (470,900,show_tail="lefttop",show_xmax=400)

    call nextpage
    show Pat smile open
    p "I wish I could say that I’m choosing to walk away for her own good, but the truth of the matter is…" (480,400,show_tail="lefttop",show_xmax=350,show_retain=3)

    show Pat closed frown
    p "I’m not strong enough to handle it." (600,750,show_tail="lefttop",show_xmax=350,show_retain=2)
    show Pat open
    p "Not yet at least." (510,1000,show_tail="lefttop",show_xmax=350,show_retain=1)
    b "...." (130,1180,show_tail="leftbase",show_xmax=350)

    call nextpage
    n1 "‘Scuse me sirs! I got your stuff here!" (400,-50,show_tail="yell",show_xmax=600,show_retain=3)
    hide Pat with dissolve
    n "Like a knife through butter, the store clerk managed to cut the tension by inserting himself between us with a cart full of shopping bags." (280,420,show_tail="narr",show_xmax=600,show_retain=2)
    # show cut-in of a shopping bag?
    n "He hands a bag of items that we asked for to each of us.{nw}" (450,710,show_tail="narr",show_xmax=380,show_retain=1)
    # hide cutin
    btr "{size=25}{cps=10}Later find out that he had mysteriously gone missing, leaving behind several strange symbols.{/cps}{/size} {p=3.0}" (0,1330, show_tail="btr",show_xmax=1300)


    call nextpage
    show Pat at middef
    p "Huh? Oh, right. I forgot why I came here-" (330,310,show_tail="rightbase",show_xmax=350,show_retain=3)
    # p "Wait, what’s that red stuff on your shoulder?"
    # n1 "What red stuff?"
    # b "The one on your shoulder, right there."
    # n1 "...."
    # "Was that… was that a thousand yard stare in his eyes or did his brain lock up?"
    # call nextpage
#     n1 "It’s ketchup."
#     p + b "...ketchup?"
#     n1 "Yes. Anyways…"
#     n1 "There was only one can of Helios Zenith: Grape Flavor."
#     n1 "Sorry friend, but first come first serve."
#     "He hands the can to the mysterious man."
#     n1 "Come back tomorrow-"
    # call nextpage
#     # Crashing sound from the store
#     n1 "Next week, and the stock should be replenished. Have a nice day."
#     ##
#     "I didn’t know it at the time, but that was the last time I would ever see that man. I learned later in the paper that he had mysteriously gone missing, leaving behind several strange symbols."
#     btr "..."
    # call nextpage
#     "That’s a lie, obviously."
#     "I’m not in the future-{nw}"
    p "Hey, you were looking for this too?" (500,450,show_tail="lefttop",show_xmax=380,show_retain=2)
    show can:
        zoom 0.5 xpos 0.3 ypos 0.5
    n "In his hand, he holds the the can." (600,610,show_tail="narr",show_xmax=250,show_retain=1)
    b "Yeah, I was just shopping for a…" (230,1310,show_tail="leftbase",show_xmax=350)

    call nextpage
    nv "Come to think of it, what is Selena to me now?"
    nv "We seemed to have a past together that I don’t remember."
    nv "She’s been nothing but friendly to me, even though this may be the first time we’ve truly met."
    nv "Are we friends now?"
    nvl clear

    call nextpage
    p "...?" (300,230,show_tail="rightbase",show_xmax=250,show_retain=7)
    n "I must’ve been standing there blankly again."  (500,250,show_tail="narr",show_xmax=350,show_retain=6)
    p "Anyone ever tell you that you have a habit of spacing out?" (230,480,show_tail="righttop",show_xmax=280,show_retain=5)
    b "S-Sometimes…." (920,620,show_tail="rightbase",show_xmax=320,show_retain=4)
    n "All the time." (700,650,show_tail="narr",show_xmax=250,show_retain=3)
    p "Heh, well… here, take this." (220,860,show_tail="righttop",show_xmax=250,show_retain=2)
    n "Without letting me reject it, he just places the can directly into my bag." (550,820,show_tail="narr",show_xmax=350,show_retain=1)
    hide can with moveoutbottom
    p "Consider it payment for listening to me bitch and moan about my love life." (350,1090,show_tail="righttop",show_xmax=350)

    call nextpage
    show Pat closed
    p """To be honest, it tastes awful but… I thought I’d try one for old time’s sake.
         But, like smoking, probably a bad habit to indulge in the past.""" (400,310,show_tail="baseleft",show_xmax=450,show_retain=4)
    b "Well, I… I mean… you can have it if you-" (900,470,show_tail="rightbase",show_xmax=350,show_retain=3)
    p "Sorry, can’t hear you, car running!" (250,610,show_tail="righttop",show_xmax=250,show_retain=2)
    n "As he walked right by me, with my hand stupidly outstretched with the can in hand to give it back,
        he mimes like a loud car engine is drowning out my voice." (40,830,show_tail="narr",show_xmax=450,show_retain=1)
    p "..." (470,750,show_tail="lefttop",show_xmax=250)
    hide Pat with dissolve
    pause 0.2

    call nextpage
    n "But then he stopped, with his back turned to me." (500,1100,show_tail="narr",show_xmax=350)
    show Pat open at middef with dissolve: #close eyes
        xpos 0.67 zoom 0.7
    p "Maybe some day, maybe in another life, our paths will converge again. Then I’ll be strong enough to face her again." (400,300,show_tail="rightbase",show_xmax=400,show_retain=5)
    p "Till then, it’s better she find someone who can give her the life I never could."  (320,500,show_tail="righttop",show_xmax=310,show_retain=4)
    p "And as for you, whatever problems you’re dealing with… I don’t know, sorry, I’m really bad at this thing." (540,560,show_tail="topleft",show_xmax=350,show_retain=3)
    p "Instead, I’ll just give you some advice that they used to tell me." (450,920,show_tail="lefttop",show_xmax=400,show_retain=2)
    p "Sometimes it’s better to just trust your instincts and see where they take you." (410,1020,show_tail="righttop",show_xmax=390,show_retain=1)
    b "What?" (650,1350,show_tail="leftbase",show_xmax=250)

    call nextpage
    hide Pat with dissolve
    show black with dissolve:
        alpha 0.5
    n "If I heard him right, he never answered. He just got in the car and was driven away." (140,210,show_tail="narr",show_xmax=700,show_retain=3)
    n "Could he be connected to…" (180,510,show_tail="narr",show_xmax=700,show_retain=2)
    n "...That’d be one hell of a contrived coincidence." (120,810,show_tail="narr",show_xmax=700,show_retain=1)
    n "But, stranger things have happened though." (260,1110,show_tail="narr",show_xmax=700)

label chapter3_3: #Sad Selena
#Setting: Selena apartment - exterior for first few lines, then interior for the rest
    play music "audio/Sketch.ogg"
    call nextpage
    scene s_ext with fade
    show Blake frown at middef
    n "My walk back to Selena’s place felt longer than before." (50,20,show_tail="narr",show_xmax=700,show_retain=4)
    n "Maybe it was because I was carrying something heavy on my mind?" (180,170,show_tail="narr",show_xmax=700,show_retain=3)
    show Blake lookaway
    b "...guess lots of people are having relationship troubles." (350,640,show_tail="topright",show_xmax=360,show_retain=2)
    n "When I got back, I saw that the truck had been moved. In addition, I didn’t see Selena anywhere." (480,800,show_tail="narr",show_xmax=370,show_retain=1)
    n "Guess she must've gone inside, waiting to watch that series." (300,1150,show_tail="narr",show_xmax=750)

    call nextpage

    scene house_hallway with fade
    n "I stepped through the threshold, expecting her to greet me with a joke or relief at seeing the snacks." (50,120,show_tail="narr",show_xmax=500,show_retain=5)
    n "But that didn’t happen." (580,300,show_tail="narr",show_xmax=300,show_retain=4)
    n "Weird.{w} Did she step out?" (250,500,show_tail="narr",show_xmax=600,show_retain=2)
    n "No, then, why’d she leave the door unlocked?" (450,820,show_tail="narr",show_xmax=400,show_retain=1)
    n "The door to her bedroom was cracked open, and inside I could hear…" (350,1120,show_tail="narr",show_xmax=500)

    call nextpage
    show Blake closed frown with dissolve:
        xalign 0.9 yanchor 0.0 ypos 0.3
    #play sound "sobbing.ogg" loop
    btr "{size=50}{cps=5}. . . . .{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)
    n "The sound I heard was something I didn’t expect though." (80,40,show_tail="narr",show_xmax=700,show_retain=1)
    n "I heard the unmistakable sound of sobbing." (160,200,show_tail="narr",show_xmax=600,show_retain=0)
    scene s_int with fade
    show screen selena_crying

    n "I carefully peeked into the crack in the door, and just out of the corner, I could see Selena sitting against the wall, holding something in her arms and… crying?"  (40,1000,show_tail="narr",show_xmax=800)
    call nextpage
    n "From this angle, I couldn’t see, and while I was curious, I didn’t know if I should intrude on this scene." (20,50,show_tail="narr",show_xmax=500,show_retain=3)
    n "The thought of what the mysterious man said flashed in my mind, was I making the same choice as he did?" (-40,500,show_tail="narr",show_xmax=350,show_retain=2)
    n "Was it right to leave her in this state?" (170,1050,show_tail="narr",show_xmax=600,show_retain=1)
    n "What should I do?" (420,1200,show_tail="narr",show_xmax=600)

    call nextpage
    btr "{size=20}{cps=5}. . . . .  {nw}{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)
    # show note_pen:
        # yanchor 0.0 zoom 0.5
        # ypos 1.0 xpos 0.45
        # linear 0.3 ypos 0.3
    hide screen selena_crying
    scene house_hallway with fade
    n "On the floor, I saw the notepad and pen, and an idea came to me. I don’t know if it was a good idea or not, but it was the best I had at the moment." (70,1080, show_tail="narr",show_xmax=790)

    call nextpage
#     # scene transition to show the passage of time cause I don’t want to describe him taking the notepad and pen, writing something on it, and then putting it on the can
    scene black with fade #with screenwipe
    pause 1
    scene s_int with fade #with screenwipe
    n "This was such an unusual idea, and I didn’t know if it was gonna work." (150,500,show_tail="narr",show_xmax=550,show_retain=1)
    n "What I ended up doing was making a note, and sliding it under the door." (260,880,show_tail="narr",show_xmax=580)

    call nextpage
    n "{b}The first note{/b}:\n\n\"I won’t leave you unless you want me to.\"" (50,150,show_tail="narr",show_xmax=600,show_retain=2)
    n "{b}The second note{/b}:\n\n\"You’ve been a good person to me, and I want to return the favor to you.\"" (50,530,show_tail="narr",show_xmax=790,show_retain=1)
    n """{b}The third note{/b}:\n\n\"I’ve never been good at this sort of thing, and I don’t know any phrase that can make you feel better.
        But… I’ll be here, so you don’t have to be alone.\"""" (50,950,show_tail="narr",show_xmax=790)

    call nextpage
    n "And like that… I just waited, sitting with my back to the wall. I could hear hear shuffling behind the door, and sniffling, though she tried to suppress it." (30,210,show_tail="narr",show_xmax=830,show_retain=4)
    n "Something she said earlier rang in my ear." (300,450,show_tail="narr",show_xmax=500,show_retain=3)
    n "Sometimes you just have to trust your instincts." (250,750,show_tail="narr",show_xmax=600,show_retain=2)
    btr "{size=50}{cps=5}. . . . .  {nw}{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)
    n "Just trust my instincts?" (50,1110,show_tail="narr",show_xmax=300)
    #"...."

    call nextpage
    n "I scooted over and without looking, I stuck my hand inside the room. Just my hand though." (480,60,show_tail="narr",show_xmax=400,show_retain=4)
    n "At first, nothing happened." (50,350,show_tail="narr",show_xmax=700,show_retain=3)
    n "I thought that this was stupid and cringy." (60,490,show_tail="narr",show_xmax=600,show_retain=2)
    n "Maybe I’m making things worse?" (40,650,show_tail="narr",show_xmax=600,show_retain=1)
    n "But to my surprise…" (350,1150,show_tail="narr",show_xmax=600)

    call nextpage
    n "I felt a hand, gently grip my own." (60,150,show_tail="narr",show_xmax=800,show_retain=4)
    n "Even though I couldn’t see her, even though she was trying to be as quiet as possible… her grip told me everything." (350,450,show_tail="narr",show_xmax=600,show_retain=3)
    n "I thought about saying something, but that would just ruin the moment." (250,680,show_tail="narr",show_xmax=600,show_retain=2)
    n "Ah." (700,950,show_tail="narr",show_xmax=600,show_retain=1)
    n "Something about this felt familiar." (260,1150,show_tail="narr",show_xmax=800)

    call nextpage
    scene black with dissolve
    show screen black_border
    scene school_class with dissolve:
        xanchor 0.5 xpos 0.5
    n "I remember hearing about something going down in the classroom next door." (250,550,show_tail="narr",show_xmax=600,show_retain=2)
    n "And a girl had bumped into me while running away from the scene." (400,750,show_tail="narr",show_xmax=450,show_retain=1)
    n "Rumors spread quickly. Rumors that she was in a fight, that she’d been accused of cheating, that she’d finally snapped due to bullying, that she’d had an affair with the teacher’s son. All kinds of shit." (50,1000,show_tail="narr",show_xmax=800)

    call nextpage
    scene school_stairs with dissolve:
        xanchor 0.4 xpos 0.5
    n "Later that day, I got strong-armed into taking over cleanup duties for a classmate." (50,150,show_tail="narr",show_xmax=800,show_retain=3)
    n "Said he had a hot date." (80,330,show_tail="narr",show_xmax=800,show_retain=2)
    n "That I never had anything to do, so I should just handle the cleaning duties for that day." (50,850,show_tail="narr",show_xmax=800,show_retain=1)
    n "Jackass, you’re only in middle school. Your hot date is just going to WcRonaldQueendies for an after-school meal." (150,1050,show_tail="narr",show_xmax=700)

    call nextpage
    scene school_class with dissolve:
        xanchor 0.5 xpos 0.5
    n "Still, who was I to disagree? My nature has always been a passive one." (350,100,show_tail="narr",show_xmax=500,show_retain=3)
    n "So I just did what I was told, because what was the point in raising a fuss?" (270,450,show_tail="narr",show_xmax=580,show_retain=2)
    n "They weren’t gonna do it, and someone had to." (150,750,show_tail="narr",show_xmax=700,show_retain=1)
    n "Might as well be the foreigner who barely spoke the language and had no friends." (400,1000,show_tail="narr",show_xmax=430)

    call nextpage
    scene school_stairs with dissolve
    n "When I was taking out the trash, I remember hearing someone crying beneath the stairwell." (50,500,show_tail="narr",show_xmax=600,show_retain=3)
    n "I remember trying to look and someone shouting back in English to not look at them." (50,750,show_tail="narr",show_xmax=700,show_retain=2)
    n "My first instinct, like always, was to remain passive." (150,950,show_tail="narr",show_xmax=650,show_retain=1)
    n "Just ignore it and walk away, go about my business, it doesn’t concern me." (250,1120,show_tail="narr",show_xmax=600)

    call nextpage
    n "...." (50,50,show_tail="narr",show_xmax=600,show_retain=4)
    n "............." (50,200,show_tail="narr",show_xmax=600,show_retain=3)
    n "Not this time." (50,350,show_tail="narr",show_xmax=600,show_retain=2)
    n "I tapped the side of the stairwell with my palm, and reached my hand down over the railing, being very careful to not look at them, like they wanted." (250,850,show_tail="narr",show_xmax=600,show_retain=1)
    n "It seemed stupid at the time, it was just something I had read in a manga." (70,1130,show_tail="narr",show_xmax=750)

    call nextpage
    n "To my surprise, then… just like back then, a person I couldn’t see gripped my hand. A person who held back a wave of sorrow beneath the mask of a happy girl." (300,250,show_tail="narr",show_xmax=550,show_retain=2)
    n "I wish I could say that we started a nice friendship here, that this is where we got to know each other and share in our hardships." (150,550,show_tail="narr",show_xmax=700,show_retain=1)
    n "But that’s not the way this story ends." (350,950,show_tail="narr",show_xmax=430)

    call nextpage

    n "The teacher, at the top of the stairs happened to pass by, thought I was shirking my cleanup duties." (30,30,show_tail="narr",show_xmax=700,show_retain=4)
    n "And so, my nature being what it was, I let go and left them there." (130,240,show_tail="narr",show_xmax=750,show_retain=3)
    n "Even as the teacher reprimanded me on the way back to the classroom, the only thought on my mind was the guilt of leaving her in that state." (250,650,show_tail="narr",show_xmax=600,show_retain=2)
    n "I always wondered if she felt a moment of peace, or if I had just made things worse?" (150,930,show_tail="narr",show_xmax=700,show_retain=1)
    n "I’d always intended to talk to her about it, to apologize for not doing more." (350,1110,show_tail="narr",show_xmax=500)

    call nextpage
    n "But by the next day, this girl with endless positivity was back to her normal self and just as unapproachable by someone like me as before." (50,300,show_tail="narr",show_xmax=800,show_retain=3)
    n "We lived in two separate worlds, that was just the reality of it." (450,550,show_tail="narr",show_xmax=450,show_retain=2)
    n "So I left the memory as it was." (300,850,show_tail="narr",show_xmax=500,show_retain=1)
    n "Just a memory." (520,920,show_tail="narr",show_xmax=360)

    call nextpage
    scene black with dissolve
    hide screen black_border
    # Scene transition back to Selena’s apartment interior
    scene s_int with dissolve
    n "....." (450,300,show_tail="narr",show_xmax=500,show_retain=3)
    n "Ah, so that was how I knew her." (250,450,show_tail="narr",show_xmax=500,show_retain=2)
    n "She squeezed my hand, and I squeezed back to let her know that I was still here."  (250,750,show_tail="narr",show_xmax=500,show_retain=1)
    n "And I wasn’t going anywhere this time." (270,980,show_tail="narr",show_xmax=500)

    return
