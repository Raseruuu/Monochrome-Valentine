image officeBG:
    "images/bg/office.jpg"
    zoom 1.8
image officehallway:
    "images/bg/officehallway.jpg"
    zoom 1.8 xalign 0.0
image elevator:
    "images/bg/elevator.jpg"
    zoom 1.5
image handshake:
    "images/CG/finalCG.webp"

transform cgtransform:
    zoom 0.8 yalign 0.5
    xalign 0.5
screen CG_handshake():
    zorder 120
    add "handshake" at cgtransform
label pan_Ashley:
    scene officeBG with dissolve:
        xalign 0.9
    return
label pan_Marie:
    scene officeBG with dissolve:
        xalign 0.1
    return
label pan_Pat:
    scene officeBG with dissolve:
        xalign 0.0
    return

define c1 = Character("Coworker1",
            callback=speaker("Coworker1"),
            screen ="bubble_say",
            what_text_align=0.5
            )

define c2 = Character("Coworker2",
            callback=speaker("Coworker2"),
            screen ="bubble_say",
            what_text_align=0.5
            )
define c3 = Character("Coworker3",
            callback=speaker("Coworker3"),
            screen ="bubble_say",
            what_text_align=0.5
            )
define c4 = Character("Coworker4",
            callback=speaker("Coworker4"),
            screen ="bubble_say",
            what_text_align=0.5
            )

image Coworker1_m_speaking:

    "Characters/Coworkers/cw1_m_open.png"
    pause 0.1
    "Characters/Coworkers/cw1_m_closed.png"
    pause 0.1
    repeat
layeredimage coworker_1:
    always:
        "Characters/Coworkers/cw1_base.png"
    group eyebrows:
        attribute up:
            "Characters/Coworkers/cw1_e_up.png"
        attribute down default:
            "Characters/Coworkers/cw1_e_down.png"
    group mouth:
        attribute frown default:
            WhileSpeaking("Coworker1","Coworker1_m_speaking","Characters/Coworkers/cw1_m_closed.png")
    zoom 1.2
image Coworker2_m_frown_speaking:
    "Characters/Coworkers/cw2_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw2_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_frown.png"
    pause 0.08
    repeat
image Coworker2_m_smile_speaking:
    "Characters/Coworkers/cw2_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_smile3.png"
    pause 0.1
    "Characters/Coworkers/cw2_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_smile.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw2_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw2_m_frown.png"
    pause 0.08
    repeat
layeredimage coworker_2:
    always:
        "Characters/Coworkers/cw2_base.png"
    group mouth:
        attribute frown:
            WhileSpeaking("Coworker2","Coworker2_m_frown_speaking","Characters/Coworkers/cw2_m_frown.png")
        attribute smile default:
            WhileSpeaking("Coworker2","Coworker2_m_smile_speaking","Characters/Coworkers/cw2_m_smile.png")
    zoom 1.2
image Coworker3_m_frown_speaking:
    "Characters/Coworkers/cw3_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw3_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_frown.png"
    pause 0.08
    repeat
image Coworker3_m_smile_speaking:
    "Characters/Coworkers/cw3_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_smile3.png"
    pause 0.1
    "Characters/Coworkers/cw3_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_smile.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw3_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw3_m_frown.png"
    pause 0.08
    repeat
layeredimage coworker_3:
    always:
        "Characters/Coworkers/cw3_base.png"
    group mouth:
        attribute frown:
            WhileSpeaking("Coworker3","Coworker3_m_frown_speaking","Characters/Coworkers/cw3_m_frown.png")
        attribute smile default:
            WhileSpeaking("Coworker3","Coworker3_m_smile_speaking","Characters/Coworkers/cw3_m_smile.png")
    zoom 1.2
image Coworker4_m_frown_speaking:
    "Characters/Coworkers/cw4_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw4_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_frown.png"
    pause 0.08
    repeat
image Coworker4_m_smile_speaking:
    "Characters/Coworkers/cw4_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_smile3.png"
    pause 0.1
    "Characters/Coworkers/cw4_m_smile2.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_smile.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_open.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_open2.png"
    pause 0.1
    "Characters/Coworkers/cw4_m_open2.png"
    pause 0.08
    "Characters/Coworkers/cw4_m_frown.png"
    pause 0.08
    repeat
layeredimage coworker_4:
    always:
        "Characters/Coworkers/cw4_base.png"
    group mouth:
        attribute frown:
            WhileSpeaking("Coworker4","Coworker4_m_frown_speaking","Characters/Coworkers/cw4_m_frown.png")
        attribute smile default:
            WhileSpeaking("Coworker4","Coworker4_m_smile_speaking","Characters/Coworkers/cw4_m_smile.png")
    zoom 1.2
label chapter5_4:
    window hide
    call screen chap("Epilogue", "Another story") with dissolve
    hide screen chap
    call nextpage
    play music "audio/Peace_bgm_maoudamashii_acoustic38.ogg"
    scene black with dissolve
    # After the credits are done rolling, fade into a sky bg, then pan down to the city (or just zoom out from a sky shot of the city bg so it shows the city. Think cone)

    # After the city BG functioning as the establishing shot, cut to an office space, a conference room specifically
    show Ashley open down frown at middef with dissolve:
        yoffset 500
    call nextpage
    n"2:15pm is the current time."(40,convo_ypos(-120),show_tail="narr",show_xmax=800,show_retain=2)
    n"The meeting was supposed to happen at 1:30, but our clients seemed to be running late."(40,convo_ypos(50),show_tail="narr",show_xmax=800,show_retain=1)
    n"I can't tell if it's incompetence, poor planning, a power move, or just disrespect for a client to arrive this late when it was them\n who requested us."(40,convo_ypos(60),show_tail="narr",show_xmax=800,show_retain=0)
    call nextpage
    scene officeBG with dissolve
    n"Around me, I could see my coworkers distracting themselves by mindlessly scrolling through their phones, engaging in idle chatter, or just staring blankly out the windows."(40,convo_ypos(-120),show_tail="narr",show_xmax=800,show_retain=3)
    n"Me, on the other hand, I had only recently moved here and barely knew the names of these people and my phone was being charged so I had nothing but my thoughts to occupy my time."(40,convo_ypos(80),show_tail="narr",show_xmax=800,show_retain=2)
    n"Unfortunately, an idle mind, leads to wandering."(40,convo_ypos(80),show_tail="narr",show_xmax=800,show_retain=1)
    n" Which is why I ended up thinking about the last encounter I had with my, now former, boyfriend."(40,convo_ypos(80),show_tail="narr",show_xmax=800,show_retain=0)
    call nextpage
    # -------------
    # Flashback scene
    scene flashback
    show screen black_border

    scene station_int with dissolve
    show Blake open frown at middef with dissolve
    b "I'm sorry."(480,300,show_tail="baseleft",show_xmax=460)

    hide Blake
    # a "Stop apologizing."
    show Ashley lookaway frown at middef with dissolve
    a "Stop apologizing." (480,convo_ypos(300),show_tail="leftbase",show_xmax=400,show_retain=1)
    show Ashley open smile at middef with dissolve
    a "That curtain has fallen on that part of our life, so now it's time to go on to another act." (450,convo_ypos(10),show_tail="topleft",show_xmax=460)
    # Flashback ends
    # -----------------
    hide screen black_border
    call nextpage
    # Screen shake and single THUD sound
    scene officeBG with Shake((0, 0, 0, 0), 0.5, dist=40) :
        xalign 0.9
    show coworker_1 down:
        xalign 0.1 yalign 0.25
    c1 "M-Ms Santiago? Are you alright?"(180,300,show_tail="baseleft",show_xmax=460)
    show Ashley concerned open smile at middef with dissolve:
        xpos 0.4 xanchor 0.0 yoffset 30
    a "I'm fine, just contemplating the mistakes of my youth."(700,300,show_tail="baseright",show_xmax=460)
    c1 "What?" (180,300,show_tail="baseleft",show_xmax=460,show_retain=0)

    hide coworker_1 up with dissolve
    show Ashley closed
    a "Don't worry about it."(700,300,show_tail="baseright",show_xmax=460,show_retain=1)
    show Ashley open at middef:
        ease 0.5 xpos 0.4 xanchor 0.0 yoffset 0
    n"I picked my head up off the table, acting like nothing happened."(40,convo_ypos(600),show_tail="narr",show_xmax=600,show_retain=0)
    call nextpage
    show Ashley closed
    n"My forehead stung." (40,convo_ypos(400),show_tail="narr",show_xmax=600,show_retain=2)
    n"That's to be expected though when one smashes their head into the table to punish themselves for their embarrassing, morning soap-opera level memories."(40,convo_ypos(40),show_tail="narr",show_xmax=600,show_retain=1)
    show Ashley open
    n"I mean, it was a pleasant memory from someone I care deeply about. But I wasn't about to show vulnerability in front of my coworkers."(140,convo_ypos(80),show_tail="narr",show_xmax=600,show_retain=0)
    call nextpage

    show Ashley frown up with dissolve
    a "Any word from the client?" (700,300,show_tail="baseright",show_xmax=460,show_retain=2)
    c1 "Oh, they should be-" (100,380,show_tail="baseleft",show_xmax=460,show_retain=1)

    m "{size=45}Sorry we're late!{/size}" (80,600,show_tail="yell",show_xmax=750,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=30)
    #Have this dialogue box be a shout and shake it, then pan the BG (if possible) over to the other end of the office BG
    scene officeBG with dissolve:
        xalign 0.1
    show Marie closed concerned openmouth at middef with Shake((0, 0, 0, 0), 0.5, dist=20)
    n"Before my superior could finish his sentence, a frazzled-looking young woman bursts through the door, with forms and folders spilling out of her arms." (480,20,show_tail="narr",show_xmax=460,show_retain=1)
    call nextpage
    show Marie open frown up at bounce
    m "Our deepest apologies, we ran into some unexpected delays, but we're here now!" (480,600,show_tail="baseleft",show_xmax=500,show_retain=0)
    call nextpage
    call pan_Ashley

    show Ashley down midclose frown at middef with dissolve:
        xalign 0.9

    a "The meeting was set for 1:30."(520,convo_ypos(0),show_tail="baseleft",show_xmax=460,show_retain=3)
    m "I know! I'm so sorry!"(20,convo_ypos(0),show_tail="baseleft",show_xmax=460,show_retain=2)
    n"As if on reflex, this girl bowed her head, forgetting that she was carrying several items in her arms,{w} which caused them to spill out all over the floor."(520,convo_ypos(0),show_tail="narr",show_xmax=460,show_retain=0)
    call nextpage
    call pan_Marie
    show Marie closed down frown at middef:
        ypos 0.4 yanchor 0.0
    n"My nearest coworkers took it upon themselves to help her gather her things, which she both apologized and thanked them for."(460,convo_ypos(-80),show_tail="narr",show_xmax=520,show_retain=3)

    p "You need some help there, Marie?" (20,convo_ypos(120),show_tail="baseleft",show_xmax=460,show_retain=2)
    show Marie open openmouth up
    m "Um… I… no, thanks! I'll just… I'll just handle this, go on without me, please."(480,convo_ypos(80),show_tail="baseleft",show_xmax=460,show_retain=1)
    p "Well, if you say so."(20,convo_ypos(0),show_tail="baseleft",show_xmax=460,show_retain=0)
    call nextpage
    hide Marie
    call pan_Pat
    show Pat at middef with dissolve
    n"From the hallway, a man steps into the room." (520,convo_ypos(0),show_tail="narr",show_xmax=460,show_retain=2)  # Either have a CG of Pat entering the office, or just slide his sprite into frame

    n"He's a very handsome looking man, but I couldn't help but feel an aura of pride radiating off him. He carried himself like a man very proud of his achievements."(520,convo_ypos(40),show_tail="narr",show_xmax=460,show_retain=1)
    n"I don't think I'm gonna like him very much if he turns out to be the arrogant type."(520,convo_ypos(220),show_tail="narr",show_xmax=460,show_retain=0)
    call nextpage
    c1 "I take it you must be…" (940,convo_ypos(20),show_tail="baseright",show_xmax=460,show_retain=2)
    show Pat oneclose
    p "Victor J. Patrick, at your service."(540,convo_ypos(20),show_tail="baseleft",show_xmax=460,show_retain=1)
    show Pat open
    p "I go by Pat instead of Vic, long story, won't bore you with the details."(540,convo_ypos(120),show_tail="baseleft",show_xmax=460,show_retain=0)
    call nextpage
    show Pat oneclose at bounce
    n"As he introduces himself, he goes around the table shaking hands with everyone, giving them a supernova smile and that super model wink that I can see from here." (520,convo_ypos(-40),show_tail="narr",show_xmax=460,show_retain=1)
    n " His performance makes my coworkers' hearts flutter like school girls in a summer romcom."(520,convo_ypos(200),show_tail="narr",show_xmax=460,show_retain=0)
    # As he's doing this, have the BG pan back to where Ashley was, I'm unsure if her sprite would be on-screen or not.
    call nextpage
    call pan_Ashley
    show Ashley midclose frown at middef with dissolve
    n"Then he gets to me, holding out his hand, as if waiting for me to play the role I'm expected to play:"(520,convo_ypos(40),show_tail="narr",show_xmax=460,show_retain=2)
    show Ashley lookaway
    n"A girl completely smitten by his charm and good looks, and willing to overlook his rudeness because he's just oh so dreamy."(520,convo_ypos(80),show_tail="narr",show_xmax=460,show_retain=1)
    show Ashley down open
    n" Sure he's a bad boy, but maybe I can change him!"(520,convo_ypos(140),show_tail="narr",show_xmax=460,show_retain=0)
    call nextpage
    call pan_Pat
    show Pat at middef with dissolve
    p "Well, don't leave me hanging here."(500,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=2)
    n"As he shoots me that look, I think he was expecting me to fall over like everyone else."(500,convo_ypos(-60),show_tail="narr",show_xmax=460,show_retain=1)
    n"Unfortunately for him, I am not a fresh-faced college student with an interest in pretty boys who put more time in their appearance than I do."(500,convo_ypos(80),show_tail="narr",show_xmax=460,show_retain=0)
    call nextpage
    scene officeBG:
        xalign 0.9
    show coworker_1 up:
        xalign 0.2 yalign 0.25
    c1 "Ms. Santiago?"(400,convo_ypos(10),show_tail="baseleft",show_xmax=460,show_retain=2)
    show Ashley down open frown at middef with dissolve:
        xpos 0.4 xanchor 0.0 yoffset 30
    a "I have something to say."(700,convo_ypos(30),show_tail="baseright",show_xmax=460,show_retain=1)
    show coworker_1 down
    c1 "What are you doing?"(300,convo_ypos(200),show_tail="topleft",show_xmax=460,show_retain=0)
    hide coworker_1
    call nextpage
    show Ashley midclose at middef with dissolve
    a "Mr. Patrick-"(500,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=3)
    p "Call me, Pat."(10,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=2)
    a "Mr. Patrick."(500,convo_ypos(-100),show_tail="baseleft",show_xmax=460,show_retain=1)
    a "Correct me if I'm wrong, but the meeting was scheduled for 1:30pm today, correct?"(500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=0)
    call nextpage
    call pan_Marie
    show Marie closed concerned openmouth at middef
    m "Th-that's correct ma'am! And I'm sorry-"(500,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=1)
    n"I held up my hand to cut her off."(500,convo_ypos(40),show_tail="narr",show_xmax=460,show_retain=0)

    call nextpage
    call pan_Ashley
    show Ashley down midclose frown at middef with dissolve
    a "And what time is it now, Mr. Patrick?"(500,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=0)
    call pan_Marie
    show Ashley open  at middef with dissolve:
        xanchor 0.0 xpos 0.9
    show Pat lookaway frown at middef with dissolve
    p "Uh…"(500,convo_ypos(-100),show_tail="baseleft",show_xmax=460,show_retain=2)
    n"Dumbfounded that I seemed to be totally immune to his charms, he produced his cellphone from his pocket."(500,convo_ypos(-80),show_tail="narr",show_xmax=460,show_retain=1)
    p "It's about 2:20pm now."(500,convo_ypos(220),show_tail="baseleft",show_xmax=460,show_retain=0)
    call nextpage
    show Pat with ease:
        xanchor 1.0 xpos 0.70

    show Ashley frown midclose down at middef:
        xanchor 0.0 xpos 1.0
        ease 0.3 xanchor 0.0 xpos 0.35
    a "Right. It was your party that requested this meeting, and it was yours who set the date and time."(560,convo_ypos(490),show_tail="righttop",show_xmax=520,show_retain=1)
    a" You made us wait here for nearly an hour. We had to move a lot of things to get this meeting set up. This is a very poor first impression to make on potential business partners, you are aware of this?"(560,convo_ypos(120),show_tail="righttop",show_xmax=600,show_retain=0)

    call nextpage
    p "I…"(360,convo_ypos(40),show_tail="baseleft",show_xmax=460,show_retain=2)
    a "I'll be honest, I'm not a fan of working with people who make such a disrespectful first impression. So explain to me… why are you so late? Is this some kind of power move? Do you think us beneath you and that you needed to show dominance?"(600,convo_ypos(270),show_tail="righttop",show_xmax=600,show_retain=1)
    p "Well, the thing is-"(200,convo_ypos(260),show_tail="lefttop",show_xmax=520,show_retain=0)
    call nextpage

    a "Furthermore, you seem very inconsiderate to your assistant over there. It makes me wonder if you'll treat us the same way?"(600,convo_ypos(380),show_tail="righttop",show_xmax=600,show_retain=0)
    hide Pat
    call nextpage
    show coworker_1 down:
        xalign 0.1 yalign 0.25
    show Ashley open at middef:
        ease 0.2 xpos 0.4 xanchor 0.0
    c1 "M-Ms. Santiago, please!"(360,convo_ypos(40),show_tail="baseleft",show_xmax=600,show_retain=2) with Shake((0, 0, 0, 0), 0.5, dist=10)
    call nextpage
    n"My superior stepped between us, his round body physically blocking us from view of each other as if we were two children in an argument about to take a swing at each other."(370,convo_ypos(380),show_tail="narr",show_xmax=600,show_retain=1)
    show coworker_1 up
    c1 "On behalf of the company, I humbly apologize for the sharp words of our new team member, Mr. Patrick! Of course, we're more than willing to start over!"(140,convo_ypos(160),show_tail="lefttop",show_xmax=600,show_retain=0)
    hide Ashley
    hide coworker_1
    with dissolve
    call nextpage

    n"A superior kowtowing to please a client, a familiar sight. I looked around the room, wondering if I had gone too far? I said what I felt, but it was true that I was new here. Still, I can't be the only one who was thinking it. I'm just the only one who had the strength to say it."(50,convo_ypos(40),show_tail="narr",show_xmax=600,show_retain=1)
    n"At this display, Pat stifled a laugh, something I hadn't expected him to do. Usually, when I chew people out, they either tuck their tails between their legs or issue a quickly-worded poorly thought-out rebuttal until they just give up and go home."(180,convo_ypos(420),show_tail="narr",show_xmax=600,show_retain=0)
    call nextpage
    scene officeBG:
        xalign 0.5
    show Pat closed smile up at middef
    with dissolve
    p "No, she's absolutely right."(360,convo_ypos(40),show_tail="baseleft",show_xmax=600,show_retain=0)
    call nextpage
    call pan_Marie
    show Marie open down frown at middef:
        ypos 0.4 yanchor 0.0 xpos 0.6 xanchor 0.2
    show Pat frown up at middef:
        ypos 0.4 yanchor 0.0 xpos 0.1 xanchor 0.2
    n"At this, Pat walks over to his assistant Marie, and helps her pick the documents up off the floor."(20,convo_ypos(-40),show_tail="narr",show_xmax=600,show_retain=1) # Pan the BG back over to where Marie entered
    p "Sorry Marie, I should've carried some stuff to ease the burden off you."(240,convo_ypos(280),show_tail="baseleft",show_xmax=600,show_retain=0)
    call nextpage
    show Marie concerned openmouth
    m "Um, I…"(720,convo_ypos(20),show_tail="rightbase",show_xmax=600,show_retain=4)
    p "Look, i don't really say it much and it's a bit embarrassing to say it in public. But, I really do appreciate everything you do, so I'll try to be more considerate to you in the future, okay?"(40,convo_ypos(120),show_tail="baseleft",show_xmax=700,show_retain=3)
    show Marie concerned open3
    m "Mr. Patrick-"(600,convo_ypos(40),show_tail="baseright",show_xmax=600,show_retain=2)
    show Pat smile
    p "Pat."(340,convo_ypos(40),show_tail="baseleft",show_xmax=700,show_retain=1)
    n"This was also a pleasant surprise. I half-expected him to put all the blame on his assistant, since that tended to be how this show went down. Though, I can't tell if he's being sincere right now or if it's just because I put him on the spot. I'll reserve my judgement until later."(40,convo_ypos(0),show_tail="narr",show_xmax=800,show_retain=0)
    call nextpage
    scene officeBG with fade
    show Pat frown at middef
    p "And, as for everyone here." (500,convo_ypos(40),show_tail="baseleft",show_xmax=340,show_retain=1)
    show Pat closed
    p "I humbly apologize for being late, there were some… unexpected delays that were entirely my fault. I couldn't stop them, but I could've at least called ahead to inform you of the situation."(480,convo_ypos(40),show_tail="topleft",show_xmax=400,show_retain=0)
    call nextpage
    show Pat with ease:
        xanchor 1.0 xpos 0.70

    show Ashley openmouth midclose down at middef:
        xanchor 0.0 xpos 1.0
        ease 0.3 xanchor 0.0 xpos 0.35
    a "So why didn't you?" (580,convo_ypos(420),show_tail="righttop",show_xmax=340,show_retain=4) with Shake((0, 0, 0, 0), 0.5, dist=10)
    # Screenshake
    p "..."(200,convo_ypos(40),show_tail="lefttop",show_xmax=340,show_retain=3)
    show Ashley frown
    a "...?"(580,convo_ypos(-140),show_tail="righttop",show_xmax=340,show_retain=2)
    p "I uh… I kinda forgot what your business number was."(200,convo_ypos(0),show_tail="lefttop",show_xmax=340,show_retain=1)
    show Ashley openmouth open at middef:
        xanchor 0.0 xpos 0.35
        linear 0.2 yoffset -10
        linear 0.2 yoffset 0
    a "...are you being serious, right now?"(580,convo_ypos(80),show_tail="righttop",show_xmax=340,show_retain=0)
    call nextpage
    show Pat frown open
    p "Yeah, though I don't look it, I get a bit nervous talking on phones. And, I had a bunch of different numbers in my call log, so I wasn't sure which one was the right one."(200,convo_ypos(350),show_tail="lefttop",show_xmax=600,show_retain=4)
    a "Couldn't you have guessed based on when you last called?" (600,convo_ypos(160),show_tail="righttop",show_xmax=500,show_retain=3)
    show Pat closed frown
    p "Well, the thing about that is..."(200,convo_ypos(40),show_tail="lefttop",show_xmax=600,show_retain=2) # Pause between these two lines for a brief moment, as if Pat is trying to come up with a reason for why he couldn't just do what Ashley suggested
    show Pat smile open
    p "That it's an excellent idea and I wish I would've thought of it sooner."(20,convo_ypos(0),show_tail="lefttop",show_xmax=420,show_retain=1)
    p "In anycase, I apologize for being late, and you were right to call me out on it."(480,convo_ypos(-140),show_tail="lefttop",show_xmax=420,show_retain=0)
    call nextpage

    hide Ashley
    show coworker_1 down with dissolve:
        xalign 0.9 yalign 0.18
    c1 "Mr. Patrick-" (500,convo_ypos(40),show_tail="rightbase",show_xmax=600,show_retain=5)
    p "Pat." (280,convo_ypos(40),show_tail="topleft",show_xmax=600,show_retain=4)
    show coworker_1 up
    c1 "Mr. Pat, you have nothing to apologize for, if anything we should be the one apologizing to you for-"(500,convo_ypos(40),show_tail="righttop",show_xmax=600,show_retain=3)
    p "What's your name, sir?"(280,convo_ypos(50),show_tail="lefttop",show_xmax=600,show_retain=2)
    c1 "Me? Uh, Khan Yun is my name."(500,convo_ypos(0),show_tail="righttop",show_xmax=600,show_retain=1)
    p "Mr. Khan Yun, you don't have to be so formal with me."(280,convo_ypos(0),show_tail="lefttop",show_xmax=600,show_retain=0)

# A fun thing to do during this negotiation scene might be to adopt an ace attorney format, where the camera switches back and forth between the two sides. In which case, we might need to create a sprite for Khan and Marie… or not.
# Maya wasn't always by Phoenix's side in the scenes,
#so it can be fine with just Pat and Ashley representing their two sides.
    scene black with dissolve
    scene officeBG with dissolve

    show Pat at middef:
        xanchor 1.0 xpos 0.70 yoffset 40
    with dissolve
    call nextpage
    p "So, this meeting was about me signing on to work for this company as a talent?" (280,convo_ypos(40),show_tail="baseleft",show_xmax=600,show_retain=5) # Have Pat's sprite sit down when he says the word, ‘so'
    show coworker_1 down with dissolve:
        xalign 0.9 yalign 0.18
    c1 "That is correct, once we get resituated here, we can go over the forms and contracts and negotiate to your liking."(500,convo_ypos(240),show_tail="righttop",show_xmax=600,show_retain=4)
    p "That's good, but I'd like to add something."(280,convo_ypos(80),show_tail="lefttop",show_xmax=600,show_retain=3)
    c1 "Oh?"(500,convo_ypos(0),show_tail="righttop",show_xmax=600,show_retain=2)
    p "Yeah."(280,convo_ypos(0),show_tail="lefttop",show_xmax=600,show_retain=1)
    stop music
    n"Pat gestures to my direction." (500,convo_ypos(-120),show_tail="narr",show_xmax=600,show_retain=0)

    call nextpage
    play music "audio/Chill_bgm_maoudamashii_acoustic06.ogg"
    p "If possible, I'd like Ms. Santiago to be my Producer."(280,convo_ypos(40),show_tail="baseleft",show_xmax=600,show_retain=4)

    c1 "Ms. Ashley Santiago? I'm sorry, what?"(500,convo_ypos(240),show_tail="righttop",show_xmax=600,show_retain=3)
    n"Even I was caught off guard by that." (500,convo_ypos(-120),show_tail="narr",show_xmax=600,show_retain=2)
    p "Her, the girl who verbally handed me my own ass, I'd like her to be my producer."(280,convo_ypos(40),show_tail="lefttop",show_xmax=600,show_retain=1)
    show coworker_1 up
    c1 "Well, I… Mr. Pat, we have a number of talented agents to assist you in that matter. Surely one of them would be more than adequate. Furthermore, ms Santiago is a new hire, though she's quite talented, she's never had to manage talent before."(780,convo_ypos(40),show_tail="righttop",show_xmax=800,show_retain=0)
    call nextpage
    hide Pat
    hide coworker_1
    n"He's not wrong, I was hired for a desk job, not to manage the talent. Hell, I was only in this meeting in particular to write down the details of the meeting." (50,convo_ypos(40),show_tail="narr",show_xmax=600,show_retain=0)

    show Pat at middef with dissolve
    p "Mr Khan, I'll be very clear about this. I have no patience for yes-men, I'd prefer to work with someone who has the courage to tell me when I'm being an ass. My gut is telling me that working with Ms Santiago instead of another producer would be awesome."(180,convo_ypos(340),show_tail="lefttop",show_xmax=700,show_retain=1)

    show Pat with ease:
        xanchor 1.0 xpos 0.70

    show Ashley frown open down at middef:
        xanchor 0.0 xpos 1.0
        ease 0.3 xanchor 0.0 xpos 0.35
    a "Excuse me, hey, Hi. I'm sitting right here. Don't I get a say in this?" (700,convo_ypos(230),show_tail="righttop",show_xmax=450,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=10) # Screen shake when Ashley finally speaks up
    call nextpage
    show Pat closed
    p "Well, if you go along with this, I'm prepared to offer you…" (180,convo_ypos(340),show_tail="lefttop",show_xmax=700,show_retain=2)

    n "He takes a slip of paper and a pen from the conference table, writes something, and slides it over to us across the table." (100,convo_ypos(80),show_tail="narr",show_xmax=700,show_retain=1)# Have the BG actually slide over to Ashley's side, in addition, new asset, a slip of paper with something written on it

    p "That, in exchange."(180,convo_ypos(80),show_tail="lefttop",show_xmax=700,show_retain=0)
    call nextpage
    nv "Those of us at this end of the table gather around to see what he wrote on the slip of paper."
    stop music
    nvl clear
    show coworker_2 with dissolve:
        xalign 0.5 yalign 0.8
    nv "....."
    hide coworker_2 with dissolve
    show coworker_3 with dissolve:
        xalign 0.5 yalign 0.8
    nv "....."
    hide coworker_3 with dissolve
    show coworker_4 with dissolve:
        xalign 0.5 yalign 0.8
    nv "....."
    hide coworker_4 with dissolve
    show Ashley down closed frown
    play music "audio/Amusement_bgm_maoudamashii_acoustic_44.ogg"
    nv "And then collectively lose our shit on the inside."
    nvl clear
    hide Pat
    hide Ashley
    nv "Fortunately, we're all trained business professionals so if we were shocked by what he was offering in exchange, we didn't show it." # Remove the slip of paper
    nvl hide
    nvl clear
    show coworker_1 with dissolve:
        xalign 0.9 yalign 0.18
    c1 "Excuse us for one moment, team huddle up!"(500,convo_ypos(240),show_tail="righttop",show_xmax=600,show_retain=2)

    n "The closest members gathered into a huddle to look at the slip of paper again."(50,convo_ypos(40),show_tail="narr",show_xmax=600,show_retain=1) # Put the slip of paper back up

    c1 "..."(500,convo_ypos(40),show_tail="righttop",show_xmax=600,show_retain=0)
    call nextpage

    hide coworker_1 with dissolve
    show coworker_2 frown with dissolve:
        xalign 0.5 yalign 0.8
    nv "....." # Cut all sound and pause the screen for a moment as if they're all stunned. Also, keep the slip of paper on screen
    hide coworker_2 frown with dissolve
    show coworker_3 frown with dissolve:
        xalign 0.5 yalign 0.8
    nv "....." # Cut all sound and pause the screen for a moment as if they're all stunned. Also, keep the slip of paper on screen
    hide coworker_3 with dissolve
    show coworker_4 frown with dissolve:
        xalign 0.5 yalign 0.8
    nv "....." # Cut all sound and pause the screen for a moment as if they're all stunned. Also, keep the slip of paper on screen
    hide coworker_4 with dissolve
    call nextpage

    show Ashley frown open down at middef:
        xanchor 0.0 xpos 1.0
        ease 0.3 xanchor 0.0 xpos 0.35
    a "..."(500,convo_ypos(40),show_tail="rightbase",show_xmax=600,show_retain=2)
    show coworker_1 up with dissolve:
        xalign 0.1 yalign 0.25
    c1 "So...?"(180,convo_ypos(340),show_tail="lefttop",show_xmax=700,show_retain=1)
    show Ashley lookaway
    a "I know, this is a very generous offer."(500,convo_ypos(0),show_tail="righttop",show_xmax=600,show_retain=0)
    call nextpage
    hide coworker_1 with dissolve
    show coworker_3 with dissolve:
        xalign 0.1 yalign 0.25
    c3 "We'd be crazy not to take this, right?"(180,convo_ypos(580),show_tail="lefttop",show_xmax=700,show_retain=1)
    show Ashley open up
    a "It does make more business sense, however… I'll remind you that I'm not a producer nor am I in the department that manages the talent."(700,convo_ypos(0),show_tail="righttop",show_xmax=720,show_retain=0) # Remove the slip of paper
    call nextpage
    hide coworker_3 with dissolve
    show coworker_2 with dissolve:
        xalign 0.1 yalign 0.25
    c2 "What even is a producer, right? It's not like you need some special training, just make sure he doesn't do anything stupid."(180,convo_ypos(580),show_tail="lefttop",show_xmax=700,show_retain=1)
    show Ashley concerned frown midclose

    a "I'm not sure how I feel about playing mommy to some guy who seemed to like the verbal thrashing I gave him."(700,convo_ypos(40),show_tail="righttop",show_xmax=720,show_retain=0)
    call nextpage
    hide coworker_2 with dissolve
    show coworker_1 down with dissolve:
        xalign 0.1 yalign 0.25
    c1 "I'm not here to judge, I only care about if he makes money. And projections do show that he's very popular with the girls aged 15-40. The executives are looking to expand into other demographics, after all."(180,convo_ypos(580),show_tail="lefttop",show_xmax=700,show_retain=2)
    a "That being said, surely we have someone else who can babysit him, right?"(700,convo_ypos(140),show_tail="righttop",show_xmax=720,show_retain=1)
    c1 "Maybe, but let me show what he's offering again."(180,convo_ypos(20),show_tail="lefttop",show_xmax=700,show_retain=0)
    call nextpage
    hide coworker_1 with dissolve
    show Ashley concerned frown lookaway at middef with dissolve

    n"He shows me the piece of paper once more." (50,convo_ypos(440),show_tail="narr",show_xmax=600,show_retain=1)# show the slip of paper again
    a "...I'm still a bit conflicted."(500,convo_ypos(140),show_tail="lefttop",show_xmax=500,show_retain=0)
    nvl clear
    scene officeBG:
        xalign 1.0
    nv"Suddenly, someone nearby started chanting in a barely hushed tone, \"Do it. Do it. Do it. Do it.\""
    nv"Which lead to other coworkers chanting as well."
    nv"Even the boss was joining in."
    nvl clear
    nv"...."
    nv"Inhale."
    nv"Exhale."
    menu:
        "You ever feel like, you can see the moment where your life can split off into two directions?":
            pass
        "That's kinda how I feel right now, actually.":
            pass
    nvl clear
    nv"On one hand, I came here to start a new chapter in my life, I was hoping that it'd be a nice, quiet, peaceful one for a while. Getting involved with this seems like it'd be pretty stressful."
    nv"On the other hand, that is a very generous offer and if I agree to it, we're all but guaranteed to land this client. That and I guess he's not that bad of a guy? A bit immature, acts before thinking, and the kind of guy who just fills me with the strong desire to punch someone."
    nv"I need a tiebreaker."
    stop music
    nv" What would Blake do?"

# ------------------------------
    call nextpage
    play music "audio/Memory_maoudamashii23.ogg"
    # Flashback line
    # b ""
    scene flashback
    show screen black_border

    scene station_int with dissolve
    show Blake lookaway frown at middef with dissolve
    b "I'm sorry."(480,300,show_tail="baseleft",show_xmax=460,show_retain=2)
    n "Really, Blake?\nIs that really all you said to me?\n You Dummy! "(480,480,show_tail="narr",show_xmax=460,show_retain=1)


    n "... What did I say to him ?"(480,700,show_tail="narr",show_xmax=460,show_retain=0)
    hide Blake with dissolve
    call nextpage
    show Ashley at middef with dissolve
    a "Don't let the chains of the past hold you back."(480,300,show_tail="baseleft",show_xmax=460,show_retain=0)

# Flashback over
    scene officeBG
    hide screen black_border
# ------------------------------
    call nextpage
    stop music
    n"{size=100}THUD!{/size}" (80,600,show_tail="yell",show_xmax=750,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=30)
    play music "audio/Amusement_bgm_maoudamashii_acoustic_44.ogg"
    #Thud sound and screen shake as it fades back into the present
    show coworker_1 down with dissolve:
        xalign 0.1 yalign 0.25

    c1 "Ms. Santiago, please! You'll break something if you keep doing that!" (180,convo_ypos(580),show_tail="lefttop",show_xmax=700,show_retain=3)
    show Ashley concerned frown closed at middef:
        xanchor 0.0 xpos 1.0
        ease 0.5 xanchor 0.0 xpos 0.35
    a "Sorry, I just felt that I needed to hit something."(700,convo_ypos(20),show_tail="righttop",show_xmax=720,show_retain=2)
    n "That was my own line too! Still, maybe I should take my own advice."(80,convo_ypos(0),show_tail="narr",show_xmax=750,show_retain=1)
    show Ashley frown down open
    a "Okay, I can do this."(700,convo_ypos(40),show_tail="righttop",show_xmax=720,show_retain=0)
    call nextpage
    scene officeBG:
        ease 0.4 xalign 0.0
    show Pat at middef with dissolve:
        xanchor 1.0 xpos 0.70 yoffset 20

    show Ashley frown open down at middef:
        xanchor 0.0 xpos 1.0
        ease 0.3 xanchor 0.0 xpos 0.35
    $ window_bg=True
    "I break from the huddle, and slowly walk over to Pat's side of the table." # Pan the BG
    show Ashley midclose
    "I lock eyes with him, as if trying to discern some hidden secret beneath those crystal clear eyes of his-"
    extend"\n\nFOCUS!"
    extend"\nDon't get drawn into his orbit."
    "This was gonna be an important decision, I could feel it. Maybe that's superstitious, but I know what I have to do."
    $ window_bg=False
    call nextpage
    show Ashley open
    a "Do you have something broken in your head?" (700,convo_ypos(400),show_tail="righttop",show_xmax=720,show_retain=4)
    p "What?" (180,convo_ypos(0),show_tail="lefttop",show_xmax=700,show_retain=3)
    a "You don't even know me, or my qualifications."(700,convo_ypos(0),show_tail="righttop",show_xmax=720,show_retain=2)
    show Ashley midclose
    a "And you want me to be your producer? Why is that, exactly? There's way more talented people at this, why me specifically? And don't gimme that line about not liking yes-men, I invented that line."(700,convo_ypos(0),show_tail="righttop",show_xmax=720,show_retain=1)
    p "Well, I can't really explain it outside of that, but…"(180,convo_ypos(120),show_tail="lefttop",show_xmax=700,show_retain=0)
    show Pat closed frown
    call nextpage
    n"His demeanor suddenly shifts."(**comicboxtop("narr",80,0))
    call nextpage
    show Pat openmouth open down

    p "An old friend of mine used to say, sometimes it's better to trust my instincts even when I don't know why. I guess that's kinda what I'm doing now." (**comicboxtop("left",0,1))
    show Pat smile at middef with ease:
         xanchor 1.0 xpos 0.70 yoffset 0
    n "He slowly stood up and faced me."(**comicboxtop("narr",80,0))
    call nextpage
    n"In a weird way, this sorta resembled those old kung-fu movies that Blake liked to watch."(**comicboxtop("narr",0,2))

    n"Where two powerful warriors face each other on the field of battle, sizing each other up."(**comicboxtop("narr",20,1))
    n"Waiting for just the right moment to make the first strike. But one of them has a smug grin on his face, and the other thinks he's a pretty boy who definitely spends more on his hair than I spend on my rent."(**comicboxtop("narr",80,0))
    call nextpage
    show Ashley open frown up
    # Pause here for a moment… and then play a cell-phone ringing sfx
    play music "audio/Ringtone_bgm_maoudamashii_8bit01.ogg"

    n"....."(**comicboxtop("narr",80,1))
    stop music
    hide Ashley with dissolve
    play sound "audio/sfx-bleep.ogg"
    n"....."(**comicboxtop("narr",80,0))
    call nextpage
    show Marie up openmouth at middef with dissolve:
        xpos 1.0 xanchor 0.7
    play music "audio/Peace_bgm_maoudamashii_acoustic38.ogg"
    m "M-Mr. Pat, sir. It's um… your grandmother."(**comicboxtop("right",80,3))
    show Pat up frown
    p "Really? What about?"(**comicboxtop("left",0,2))
    show Marie open3 concerned
    m "Uh, she's saying something about… um… the volume remote on her TV is stuck?"(**comicboxtop("right",0,1))
    show Pat smile
    p "Sorry, guys, I know this is really unprofessional, but… I gotta take this. I'll be back in just a few minutes, okay? Cool!"(**comicboxtop("left",40,0)) # Have Pat slide out of frame
    show Pat at middef with ease:
        xanchor 1.0 xpos 0.0
    hide Marie with dissolve
    call nextpage
    n". . . . . . . ." (**comicboxtop("narr",-300,0))
    call nextpage
    show coworker_1 down:
        xalign 0.1 yalign 0.25
    show Ashley lookaway frown at middef with dissolve:
        xpos 0.4 xanchor 0.0
    c1 "So, um-" (**comicboxtop("left",0,1))
    a "I'm gonna grab a drink."(**comicboxtop("right",0,0))



    play music "audio/Chill_bgm_maoudamashii_acoustic06.ogg"
# Fade to black, and fade in to to an office-hallway. If possible, include a vending machine. If even more possible, try to find a vending machine sfx but one that gets stuck. There's a brief moment where the BG is gonna be panned left and right later, so keep the BG zoomed in
    call nextpage
    scene officehallway with dissolve
    show Ashley down frown at middef with dissolve

    a "Dammit." (**comicboxtop("mid",0,0))
    show Ashley midclose
    $ window_bg=True
    call nextpage
    show Ashley up
    "I was just coming out here to the hallway vending machine, to get a drink."
    show Ashley down
    extend" But, just my luck though, the machine is stuck!"
    show Ashley concerned
    call nextpage
    "I'm about to just give up, when I suddenly remembered; The day I first got here, the machine was also broken.{w}\nMy supervisor was running me and other new hires through orientation, one of them got their money eaten by the machine."
    show Ashley down
    call nextpage
    "..."
    show Ashley lookaway up
    extend "Take a quick peek around the corners to make sure no one's watching, in case I can get written up for damaging company property." # Pan the BG left and right then back to center
    show Ashley down midclose openmouth2
    call nextpage
    "If I remember correctly..."
    show Ashley midclose frown
    extend "\nThe supervisor kicked the machine."
    show Ashley open opensmile
    extend "\n\nRight..."
    show Ashley up midclose smile
    extend "About..."
    show Ashley open opensmile
    extend "Here!" with Shake((0, 0, 0, 0), 0.5, dist=20) # Screen shake and impact noise, as well as two cans falling, or just one, not sure if the 2nd one is needed yet
    show Ashley with ease:
        yoffset 40
    extend "\nThere we go." # If Ashley's sprite is on screen, pan it down a bit, then back up as if she's bending down to get something. Otherwise just pan the camera down slightly before putting it back up.
    call nextpage
    show Pat at middef:
        xanchor 1.0 xpos 0.0
        ease 0.2 xanchor 1.0 xpos 0.70 yoffset 20

    show Ashley openmouth up:
        yoffset -60
        ease 0.2 xanchor 0.8 xpos 1.0 yoffset 0
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    p "S'up?" (**comicboxtop("left",0,3))
    show Ashley down
    a "AGH!" (**comicboxtop("right",0,2)) with Shake((0, 0, 0, 0), 0.5, dist=10)# Screen shake fx
    show Ashley frown
    a "What?!"(**comicboxtop("right",0,1))
    p "Oh, uh, I was just saying I think we got off on the wrong foot."(**comicboxtop("left",0,0))
    show Ashley lookaway
    call nextpage
    a "Is that it?" (**comicboxtop("right",0,4))# Sound FX of a can opening
    show Pat closed
    p "Sorry for startling you."(**comicboxtop("left",0,3))
    show Ashley midclose
    a "...." (**comicboxtop("right",0,2))# If we have a VA have her actually drink from a can instead of faking it, it's usually better to actually drink and eat rather than fake it
    show Pat open
    p "Yeah, my bad. So, given any thought to the offer?"(**comicboxtop("left",0,1))
    show Ashley open up
    a "Not particularly."(**comicboxtop("right",0,0))
    call nextpage
    p "Don't wanna go through with it?"(**comicboxtop("left",-40,3))
    show Ashley concerned lookaway
    a "Hm, if you must know, I'm undecided."(**comicboxtop("right",0,2))
    show Ashley down
    a "On one hand, I moved here to keep my head down and live a normal, peaceful life."(**comicboxtop("right",0,1))

    # Play SFX of the can being dropped in a trash barrel
    show Ashley midclose
    a "On the other hand, staring at spreadsheets for several hours is mind-numbingly dull."(**comicboxtop("right",20,0))
    call nextpage
    show Pat up
    p "Sounds like you need a tiebreaker, something to tip the scale." (**comicboxtop("left",0,3))
    show Ashley up
    a "And I suppose that's where you come in?"(**comicboxtop("right",0,2))
    show Ashley down
    n"He just shrugs his shoulders, so confident that he can convince me. That arrogance of his would definitely be a problem."(**comicboxtop("narr",0,1))
    n"..."(**comicboxtop("narr",60,0))
    play music "audio/Cool_maoudamashii22.ogg"
    call nextpage
    show Pat frown
    show Ashley up
    a "Alright. Then, have you ever heard of an elevator pitch?"(**comicboxtop("right",0,4))
    a "You've got until I get back to the conference room to convince me to sign on as your glorified babysitter."(**comicboxtop("right",0,3))
    show Ashley smile
    a "But, fail to convince me, and this whole pestering me thing ends."(**comicboxtop("right",60,2))
    show Ashley open
    a" Deal?"(**comicboxtop("right",0,1))
    show Pat smile down
    p "Deal."(**comicboxtop("left",-40,0))
    call nextpage
    show Ashley frown
    n"And there goes that smile again."(**comicboxtop("narr",0,0))
    call nextpage
    scene elevator with fade:
        xalign 1.0
    show Pat closed at middef with dissolve
    # This next part is mostly dialogue, but it'd be a great section for manga paneling, for this build, just stick to various office BGs and sprites if that can even be found
    pa "So, you say you're not thrilled at the prospect of working with me. I get that, 'tis human nature."
    show Pat open down
    pa "But, I can see that look in your eyes and the way you command the room."
    show Pat frown
    pa "You're way better than this station. Look at them, they've got you taking notes on their behalf! That's such a waste of your potential."
    call nextpage
    show Pat down openmouth2 at bounce
    pa "So, run with me, and you can tell the next overpaid hairpiece who sends you on a coffee run to go screw themselves."
    show Pat closed smile
    pa "But I get it, you don't know anything about me. What I'm asking is crazy, right?"
    call nextpage
    show Pat open frown
    pa "Well, maybe it's not so bad to do something crazy once in a while. The adventure is definitely more fun than the destination."
    show Pat closed smile up
    pa "Sure, you can play it sensible. The uncrowned queen of office life."
    show Pat open opensmile
    extend "\nOr… you can take a chance and see what happens next!"
    call nextpage
    scene elevator:
        xalign 1.0
        linear 8.0 xalign 0.0
    show Pat openmouth2 at middef, bounce:
        ease 0.2 xanchor 1.0 xpos 1.1

    pa "Don't you wanna get away from this same old office drudgery?"
    show Pat frown down
    extend"\nTo never have someone ask you to cover their workload, to spend day after day reading through reports and charts and graphs?"
    pa "Having to say, \"yes sir\", to some fresh-faced college kid whose daddy works on the board of directors."
    show Pat closed

    pa "'Cause you can be another face in the crowd,{w=1.0}"
    show Pat oneclose smile

    extend" or you can be like me. "
    show Pat open opensmile
    extend"\nStay in your lane like they expect you to do, or you can take a leap of faith with me."
    show Pat smile closed at middef,bounce:
        xanchor 1.0 xpos 1.1
    pa "And see just how this adventure plays out."
    "God, he talks so much.{w} \nDoes he just like hearing the sound of his own voice?{w} \nWell, I guess it's my turn."

    "Wait, why does this sound familiar? {w}\nLike. Worse, but familiar. {w}\nWhatever. {w}\nJust roll with it."
    scene elevator:
        xalign 1.0
    show Pat smile closed at middef:
        xanchor 1.0 xpos 1.1

    show Ashley frown down at middef:
        xanchor 0.0 xpos -0.1
    with fade
    call nextpage
    aa "Okay, Mr. Confident. You talk a big game, but I'm not convinced."
    call nextpage
    aa "I can't tell if you love the sound of your own voice or if you ripped that speech of yours from somewhere else."
    show Pat open
    call nextpage
    pa "Little of both."
    show Ashley midclose openmouth2
    call nextpage
    aa "Well, I hate to break it to you, but..."
    show Ashley frown
    extend "\nI'm no princess..."
    extend "\nTrapped in a gilded cage."
    call nextpage
    aa "So thanks, but your 1st-year psychology-student-mixed-with-motivational-speaker show won't work on me."
    call nextpage
    show Ashley open
    aa "I'm not one of your swooning fangirls who obsessively check your social media profiles for a shirtless selfie pic."
    call nextpage
    show Ashley smile
    aa "But really, love the confident display you put on for me."
    call nextpage
    show Ashley lookaway
    call nextpage
    aa "If you weren't so handsome, maybe you could've had a brilliant career as a life coach."
    call nextpage
    show Ashley open up frown
    pa "Oh you think I'm handsome?"
    show Ashley down
    call nextpage
    aa "Don't push your luck, Patrick."
    call nextpage
    show Ashley midclose

    aa "You're way off base, by the way."
    call nextpage
    aa" I'm not unhappy with, as you described it, the drudgery of office life. I'm perfectly okay with this part I'm playing, I've got everything I need right here and then some. So no, I don't need your help to fly, because I'm not trying to leave."
    call nextpage
    aa "You'll have to take that journey yourself, Pat."
    call nextpage
    pa "So is this really how you'd like to spend your days?"
    call nextpage
    show Pat down frown
    pa "Waking up at the asscrack of dawn. Commuting to a 9-5 job for half your life. Doing the same routine 5 days a week. Misery, monotony, meetings, and office politics?"
    call nextpage
    aa "It may be boring to you, but at least I know what to expect. It's stable... while you're asking for chaos."
    call nextpage
    show Ashley closed
    aa "If I get mixed up with you, "
    show Ashley open
    extend"\npeople will never shut up about it the second they find out who I am;"
    show Ashley lookaway
    extend"\nthe disgraced executive of a fortune 500 company turned producer for a vain model with dreams of stardom."
    show Ashley midclose
    call nextpage
    aa "Talk about a train wreck."
    call nextpage
    show Pat up smile
    pa "But maybe it could help lighten that burden you're carrying around."
    call nextpage
    show Ashley open up
    aa "What?"
    call nextpage
    show Pat closed smile
    pa "Like I said, the journey is more fun than the destination. Plus, look at me."
    call nextpage
    pa "You've basically dragged my ass up and down these hallways, but I've had this stupid grin plastered on my face the whole time. I haven't enjoyed a conversation like this in a while."
    show Pat open
    call nextpage
    pa "Actually, my face kinda hurts from smiling."
    call nextpage
    show Pat down
    pa "Look, I'm not asking you to put your entire life on hold for me. I'm just asking that you take a chance on me, and allow me the opportunity to ease that pain you've been carrying around since I first laid eyes on you."
    call nextpage
    aa "..."
    call nextpage
    pa "You can fool everyone else, but I can see it. Birds of a feather and all that, jazz."
    call nextpage
    pa "The story of a girl fallen from grace and a cowardly guy with a handsome jawline, trying to ease the burdens we carry, now that's a hell of a show that seems worth watching."
    call nextpage
    pa "But, a deal's a deal. Guess I failed, so I'll respect your wishes. Sorry if I caused you any discomfort, I have a tendency to… sorta do things my way at other people's expense. Sorry again."
    stop music
    # They're back at the conference room now
    scene black with dissolve
    pause 1.0
    play music "audio/Peace_bgm_maoudamashii_acoustic38.ogg"
    scene officeBG with dissolve:
        xalign 0.1
    "Not skipping a beat, Pat turned the charm back on and sat back down at the conference table, as if the conversation we just had didn't happen."
    show Pat closed frown at middef with dissolve
    p "So, people, sorry for the delay. Elevator's broken, had to take a roundabout way back."(500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=2)
    show Pat oneclose smile
    p "But I'm here now, so I believe you had some forms for me to look over before signing?"(500,convo_ypos(-40),show_tail="topleft",show_xmax=460,show_retain=1)
    show Pat up open frown
    show coworker_1 up:
        xalign 0.9 yalign 0.75
    c1 "Um, yes, but as to the matter of Ms Santiago taking on the role of your producer..."(380,convo_ypos(360),show_tail="baseright",show_xmax=460,show_retain=0)
    call nextpage
    hide coworker_1 with dissolve
    show Pat closed up smile
    p "Oh, yeah. Sorry about that, I got a little caught up in the moment." (500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=4)
    show Pat open
    p "We can just forget that. Anyways, without further delay..." (500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=3)
    show Pat down
    p "Let's get to work." (500,convo_ypos(-60),show_tail="topleft",show_xmax=460,show_retain=2)
    show Pat closed
    p "Okay, so, next order of business would be..." (500,convo_ypos(0),show_tail="topleft",show_xmax=460,show_retain=1)
    call nextpage
        # Placeholder for the Blake line here that should be placed in scene 05 during the big fix update.


    # aa "Hang on!" with Shake((0, 0, 0, 0), 0.5, dist=40)
    a "{b}{size=60}Hold it!{/b}{/size}"  (80,800,show_tail="yell",show_xmax=750,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=40)

    call pan_Ashley
    show Ashley midclose down frown at middef:
        xpos 0.3 xanchor 0.0
    "I don't look it, but I always hated being the center of attention. All those eyes, staring at me, expecting something from me. It's unnerving. Take a breath girl. Take a breath."
    show Ashley up open

    a "This offer of yours." (500,convo_ypos(60),show_tail="baseright",show_xmax=460,show_retain=3) # Show the slip of paper again from earlier
    a "It's pretty generous, {w}but you're essentially asking me to take time off from the job I was hired here to do in order to follow you along."(500,convo_ypos(40),show_tail="topright",show_xmax=460,show_retain=1)
    show Ashley lookaway down

    a "That's a huge potential loss in earnings, and it depends entirely on how popular you are."(780,convo_ypos(220),show_tail="righttop",show_xmax=750,show_retain=0)
    call nextpage
    call pan_Pat
    show Pat closed frown normal at middef with dissolve

    p "..." (500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=3)

    show Pat open smile
    p "Fair enough, what would you propose?" (500,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=2)
    a "Well for starters, how about a cut of your earnings. That's pretty standard for this sort of arrangement, isn't it?"(**comicboxtop("right",20,1))
    show Pat closed
    p "Fair enough, you are taking a big risk, so I won't ask you to work for pennies."(**comicboxtop("left",80,0))
    call nextpage
    scene officeBG with dissolve:
        xalign 0.5
    show Pat at middef:
        xanchor 0.02 xpos 0.0
    show Ashley at middef:
        xanchor 0.65 xpos 1.0
    p "I'll give you 5\%, how's that?"(**comicboxtop("left",0,3))
    show Ashley down frown
    a "Do I look like I was born this morning?"(**comicboxtop("right",0,2))
    show Ashley up frown

    a "15\%" (**comicboxtop("right",0,1))
    show Pat down frown
    p "Well, why don't you just ask for my blood while you're at it!"(**comicboxtop("left",0,0))
    call nextpage
    show Pat up smile
    p "7\%."(**comicboxtop("left",0,4))
    a "I can do 13\%."(**comicboxtop("right",0,3))
    p "9\%, maybe."(**comicboxtop("left",0,2))
    a "11\%."(**comicboxtop("right",0,1))
    show Pat normal
    p "10\%."(**comicboxtop("left",0,0))
    stop music
    call nextpage

    show Ashley frown down midclose
    nvl clear

    "..." # Make sure there's no sound in this part
    show Ashley at middef:
        xanchor 0.65 xpos 1.0
        xoffset 5
        pause 0.1
        xoffset -5
        pause 0.1
        repeat
    extend "\n... Crap, my facial muscles are twitching!{w} This was such a textbook negotiation example, that I didn't think he'd go for it."
    play music "audio/Peace_bgm_maoudamashii_acoustic38.ogg"
    show Ashley open at bounce:
        xanchor 0.65 xpos 1.0
    "Keep steady, Ashley, don't let him know that the offer is more than enough."

    show Pat up smile open
    p "Eh? What's that I see? Come onnnnn, your resistance is fading!" (380,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=4)
    show Ashley lookaway
    n"I crossed my arms and looked away, Feigning a pouting expression to not show him that the offer was acceptable, trying to hold out to see if he'll offer something more."(80,convo_ypos(200),show_tail="narr",show_xmax=750,show_retain=3)

    show Ashley closed down frown
    n"..." (80,convo_ypos(80),show_tail="narr",show_xmax=750,show_retain=2)
    n"........."(80,convo_ypos(10),show_tail="narr",show_xmax=750,show_retain=1)
    n"......................."(80,convo_ypos(10),show_tail="narr",show_xmax=750,show_retain=0)
    nvl clear
    call nextpage
    show Ashley open up
    a "Very well. 10\% is fair."(**comicboxtop("right",0,4))
    show Pat opensmile at bounce, middef:
        xanchor 0.02 xpos 0.0
    p "Awesome!"(**comicboxtop("left",0,3))
    show Pat smile
    p "I don't know why but I'm pretty excited about this!"(**comicboxtop("left",0,2))
    show Ashley smile
    a "I'm an adult, I care more about profit than fun."(**comicboxtop("right",0,1))
    p "We'll make that too!"(**comicboxtop("left",0,0))
    call nextpage
    p "Ah! I see that smile on your face, what're you thinking?"(**comicboxtop("left",-90,3))
    show Ashley midclose smile
    a "I'm thinking about whether I should throw you from the roof or see if I can fit you through that window."(**comicboxtop("right",0,2))
    p "That's cold, bro."(**comicboxtop("left",40,1))
    show Ashley down open
    a "I'm not your bro, Pat."(**comicboxtop("right",0,0))
    call nextpage
    p "Ah! You said it, you called me, Pat! So you don't totally hate my guts!"(**comicboxtop("left",0,2))
    show Ashley down midclose
    a "Like 90\%."(**comicboxtop("right",20,1))
    p "Good enough for me!"(**comicboxtop("left",0,0))
    call nextpage
    show Ashley closed frown
    pause
    show Ashley open
    a "Okay, this comedy routine aside,"(**comicboxtop("right",0,2))
    a "Before I shake your hand, I have one last thing to say."(**comicboxtop("right",0,1))
    a "I don't know anywhere near enough about you to say whether I want to be financially joined at the hip with you."(**comicboxtop("right",0,0))
    call nextpage

    show Ashley lookaway
    a "I don't have the time or patience to be chasing you around."(**comicboxtop("right",20,1))
    show Ashley open
    a "However, I'm not totally opposed to it."(**comicboxtop("right",0,0))
    call nextpage
    a "So, how about a compromise. We'll try this thing for about a month. If we're not compatible work partners, then you'll pick a new producer and I'll go back to my normal desk job."(700,convo_ypos(400),show_tail="righttop",show_xmax=720,show_retain=2)
    a "Simple as that."(700,convo_ypos(80),show_tail="righttop",show_xmax=720,show_retain=1)
    p "That works for me!" (380,convo_ypos(60),show_tail="baseleft",show_xmax=460,show_retain=0)
    call nextpage
    a "Furthermore, I'm not your mom, your wife, or one of your fan girls."(700,convo_ypos(400),show_tail="righttop",show_xmax=720,show_retain=2)
    a "We're business associates first and foremost. We will act like professionals and no more being late, agreed?"(780,convo_ypos(20),show_tail="righttop",show_xmax=840,show_retain=1)
    p "Agreed." (380,convo_ypos(100),show_tail="lefttop",show_xmax=460,show_retain=0)
    call nextpage
    hide Pat with dissolve
    show Ashley up lookaway
    a "And, I am aware that I can be a bit..."(700,convo_ypos(0),show_tail="rightbase",show_xmax=720,show_retain=4)

    # These are also coworkers
    # c2 "Overbearing?"
    # c3 "Cold?"
    # c4 "Tactless?"
    # c1 "Scary beyond all reason?"
    # call pan_Marie

    show coworker_2 frown with dissolve:
        xalign 0.22 yalign 0.8
    c2 "Overbearing?"(180,convo_ypos(0),show_tail="leftbase",show_xmax=720,show_retain=3)
    hide coworker_2 frown with dissolve
    show coworker_3 frown with dissolve:
        xalign 0.22 yalign 0.8
    c3 "Cold?"(180,convo_ypos(0),show_tail="leftbase",show_xmax=720,show_retain=2)
    hide coworker_3 with dissolve
    show coworker_4 frown with dissolve:
        xalign 0.22 yalign 0.8
    c4 "Tactless?"(180,convo_ypos(0),show_tail="leftbase",show_xmax=720,show_retain=1)
    hide coworker_4 with dissolve
    show coworker_1 frown with dissolve:
        xalign 0.22 yalign 0.8
    c1 "Scary beyond all reason?"(180,convo_ypos(0),show_tail="leftbase",show_xmax=720,show_retain=0)

    call nextpage
    call pan_Marie
    show Ashley at middef:
        xanchor 0.65 xpos 1.0

    show Marie open up frown at middef:
        xanchor 0.05 xpos 0.0 zoom 0.9
    a "...Marie, kindly remember the names of the people who just said something so I can get revenge later."(**comicboxtop("right",0,0))
    hide Marie with dissolve
    pause 1.0
    call nextpage
    show Pat up smile open at middef with dissolve:
        xanchor 0.05 xpos 0.0
    show Ashley closed smile
    a "But yes. You said that you have no patience for yes-men, well I would rather someone be open and upfront with me when I'm being unreasonable."(**comicboxtop("right",-50,4))
    show Ashley down open frown

    a" So, part two of this deal, we communicate openly. " (**comicboxtop("right",50,3))
    show Ashley up open smile
    a "Deal?"(**comicboxtop("right",0,2))
    p "Deal."(**comicboxtop("left",0,1))
    show Ashley closed
    a "Good."(**comicboxtop("right",-20,0))

    call nextpage
    scene officeBG with dissolve
    n"I look down at his outstretched hand, still hanging there like a limp branch."(80,convo_ypos(280),show_tail="narr",show_xmax=750,show_retain=4)
    n"A part of me  wonders if I'm making the right decision."(60,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=3)
    n"But what did he say earlier? About trusting his instincts?"(120,convo_ypos(16),show_tail="narr",show_xmax=750,show_retain=2)
    n"I guess I could try it once."(150,convo_ypos(16),show_tail="narr",show_xmax=750,show_retain=1)
    n"I firmly grasp his hand, making a decision that I felt could impact the rest of my life."(80,convo_ypos(40),show_tail="narr",show_xmax=750,show_retain=0)

    pa "So, let's start over fresh."#(**comicboxtop("left",0,0))
    stop music
    # Hand-shaking CG would go here
    scene black with dissolve
    play music "audio/Chill_bgm_maoudamashii_acoustic06.ogg"
    show screen CG_handshake
    # show handshake
    pause

    call nextpage
    p "Hello, I'm Victor J Patrick, my friends call me Pat, and I look forward to working with you."(180,convo_ypos(130),show_tail="baseleft",show_xmax=540,show_retain=5)
    a "Ashley Santiago, new hire, and I'll be your producer for the time being."(640,convo_ypos(60),show_tail="baseright",show_xmax=420,show_retain=4)
    a" If we treat each other with professional courtesy, then we should have no problems."(640,convo_ypos(-86),show_tail="righttop",show_xmax=620,show_retain=3)
    p "Agreed. Ya know, you have a really strong grip for someone so short-{cps=50} {b}owowowowowowow!{/b}{/cps}"(180,convo_ypos(180),show_tail="lefttop",show_xmax=540,show_retain=2)
    c1 "Please don't damage the talent, Ms Santiago! At least not until he's signed the other forms!"(80,600,show_tail="yell",show_xmax=750,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=30)
    p "It's okay, I'm ambidextrous!"(**comicboxtop("left",80,0))
    hide screen CG_handshake
    call nextpage
    scene black

    show Ashley open down frown at middef with dissolve:
        yoffset 500
    n"I am instantly regretting this already."(80,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=2)
    n "..." (80,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=1)
    show Ashley closed up smile with dissolve
    n"Well, only about 70\% regret."(80,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=0)
    scene black with Dissolve(2.0)
    call nextpage

    # Fade to black to end the scene
#
#     [End of epilogue]
    $ persistent.unlocked_gallery=True
    n"Thank you for Playing Monochrome Valentine!"(80,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=1)
    n"YOU HAVE UNLOCKED THE GALLERY MENU! Check it out!" (68,convo_ypos(20),show_tail="narr",show_xmax=750,show_retain=0)
    return
