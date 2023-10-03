image selena_room_box= "images/bg/selena_room_with_box.webp"
image selena_room_box_night= "images/bg/selena_room_with_box_night.webp"
image house_hallway= "images/bg/house_hallway.webp"
image rain="images/bg/rain.webp"
image nightsky="images/bg/Sky_night1.webp"
image lake2 :
    "images/bg/lakefull.webp"
    zoom 2.0
screen Selena_bed():
    zorder 120
    add "images/cg/CG4.webp" at bedcganim
screen Laptop():
    zorder 120
    add "images/cg/Laptop.webp" at laptopanim
transform bedcganim:
    alpha 0.0 yoffset 0 xalign 0.5 yalign 0.4
    ease 0.4 yoffset 40 alpha 1.0
transform laptopanim:
    alpha 0.0 zoom 0.8 yoffset 0 xalign 0.9 yalign 0.8
    ease 0.4 yoffset 40 alpha 1.0
image Sky1="images/bg/sky1.webp"
screen Vampire_n_Boxer():
    zorder 120
    add "images/cg/Vampire_n_Boxer.webp":
        xalign 0.8 yalign 0.05 zoom 0.9

image selena_house_truck= "images/bg/selena_house_truck.webp"

init python:
    def convo_ypos(add=0):
        global convo_y
        new_ypos = convo_y+add
        convo_y= convo_y+150+add
        return (new_ypos)
label Chapter_4:
    # call nextpage
    # $ selena_outfit="_bedtime"
    scene black
    call screen chap("4", "Stay")
    scene house_hallway with dissolve: #with blinking
    call nextpage
    show Blake closed frown with dissolve:
        xalign 0.9 yanchor 0.0 ypos 0.3
    n "My arm was getting tired." (120,50,show_tail="narr",show_xmax=500,show_retain=2)
    n "This was cute and wholesome for a while, but now I think my arm’s gonna be stuck in this position."(130,250,show_tail="narr",show_xmax=530,show_retain=1)
    n "I really shouldn’t, but my mind was already trying to think of a way to still emphasize that I was still here but that my arm was about to fall off."(320,980,show_tail="narr",show_xmax=500)
    call nextpage
    show Blake open frown with dissolve:
        xalign 0.1
    play music "audio/Beside_bgm_maoudamashii_acoustic29.ogg" volume 0.3
    s "O-Oh, hey, you!" (800,250,show_tail="baseright",show_xmax=345,show_retain=3)
    s "There’s a um… an alien in here… who’s holding people’s hands. Don’t worry, I’ll rescue you!" (800,550,show_tail="baseright",show_xmax=345,show_retain=2)
    n "She lets go of my hand, though I can’t tell if it’s because her arm was getting tired or if she sensed that mine were."(500,620,show_tail="narr",show_xmax=380,show_retain=1)
    n "Although, it’s equally possible that she just got embarrassed when she realized how long she’d been holding my hand."(320,980,show_tail="narr",show_xmax=500)
    hide Blake
    call nextpage
    scene selena_room_box with dissolve
    show Selena crying frown at middef with dissolve
    s "So… um… do you… have the snacks?" (350,250,show_tail="baseright",show_xmax=345,show_retain=3)
    b "Oh, yeah, right here. I’ve got your change too."(930,680,show_tail="rightbase",show_xmax=400,show_retain=2)
    show Selena smile
    s "Oh, you can keep that." (350,650,show_tail="topright",show_xmax=345,show_retain=1)
    n "As a bribe?"(320,980,show_tail="narr",show_xmax=500)
    call nextpage
    show Selena smile
    s "Took you a little while to get back, eh?" (350,250,show_tail="baseright",show_xmax=345,show_retain=1)
    b "Oh yeah, you wouldn’t believe what happened. So, I get there and..."(930,680,show_tail="rightbase",show_xmax=400)
    # [ one story later ] <- This should probably be centered after a fade to black or something
    scene flashback with dissolve
    call centersay("{size=50}{cps=20}One Story Later...{/cps}{/size}")
    nvl clear
    nvl hide
    scene selena_room_box
    show Selena horizontal at middef
    with dissolve
    call nextpage
    s "..." (300,convo_ypos(),show_tail="baseright",show_xmax=345,show_retain=3)
    b "...."(850,convo_ypos(),show_tail="rightbase",show_xmax=400,show_retain=2)
    s "....Hey…" (300,convo_ypos(),show_tail="baseright",show_xmax=345,show_retain=1)
    b "Yeah?"(850,convo_ypos(),show_tail="rightbase",show_xmax=400,show_retain=0)
    call nextpage
    show Selena squiggly concerned :
        ease 1.0 yoffset 40
    s "You should probably cut back on the drugs." (350,250,show_tail="baseright",show_xmax=345,show_retain=2)
    n "Of course she didn’t believe me!"(320,680,show_tail="narr",show_xmax=500,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=10)
    b "It’s true though!"(850,980,show_tail="rightbase",show_xmax=400,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=10)
    show Selena closed opensmile up:
            rotate 0
            rotate 0.
    call nextpage
    s "A story that weird, who knows." (300,convo_ypos(),show_tail="baseright",show_xmax=345,show_retain=1)
    show Selena lookaway opensmile down
    s "Story… story… ah right!"(320,convo_ypos(),show_tail="rightbase",show_xmax=400,show_retain=0)
    scene house_hallway
    show Selena:
        xpos 1.0 xanchor 0.0
        rotate -45
        linear 0.5 xpos 0.1 xanchor 0.0 yanchor 0.0 ypos 0.1 zoom 0.7
    n "Suddenly, she poked her head out the door, with the box set in hand."(200,120,show_tail="narr",show_xmax=500,show_retain=3)
    s "Since we’re all done packing and I fixed the truck, and you brought snacks… do you…" (300,convo_ypos(),show_tail="topright",show_xmax=345,show_retain=2)
    s "Want to watch this with me?"(300,convo_ypos(250),show_tail="topright",show_xmax=345,show_retain=1)
    b "..."(850,convo_ypos(200),show_tail="rightbase",show_xmax=400,show_retain=0)
    call nextpage
    scene house_hallway
    show Selena concerned at middef:
        ease 1.0 yoffset 50
    with dissolve
    s "I mean, you don’t have to if you want, I’ve taken up a lot of your time already so-" (300,convo_ypos(40),show_tail="baseright",show_xmax=345,show_retain=6)
    b "I’ll do it."(800,convo_ypos(),show_tail="rightbase",show_xmax=400,show_retain=5)
    s "Really? You know you don’t have to force yourself to." (300,convo_ypos(),show_tail="baseright",show_xmax=345,show_retain=4)
    b "Trust me, I’ve got plenty of time."(850,convo_ypos(),show_tail="rightbase",show_xmax=400,show_retain=3)
    show Selena up
    s "Promise?"(300,convo_ypos(-40),show_tail="topright",show_xmax=345,show_retain=2)
    b "Promise."(850,convo_ypos(50),show_tail="rightbase",show_xmax=400,show_retain=1)
    show Selena down opensmile at bounce
    s "Great!"(300,convo_ypos(),show_tail="topright",show_xmax=345,show_retain=0)
    call nextpage
    n "Her mood seemed to have perked up."(200,980,show_tail="narr",show_xmax=500)
    scene selena_room_box with dissolve
    n "I’m glad, she’s cuter when she’s happy." (-30,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=4)
    n "Cuter?" (50,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=3)
    n "Is that a weird sentence?"(100,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=2)

    s "Lemme just go set everything up, trust me, you’re gonna love this series!" (900,convo_ypos(-100),show_tail="topright",show_xmax=345,show_retain=1)
    n "Well, whatever. I’m happy to have been of use."(150,convo_ypos(120),show_tail="narr",show_xmax=500)
    call nextpage
    scene sky_bright
    show screen Vampire_n_Boxer

    n"{b}Of Vampires and Boxers.{/b}" (-80,convo_ypos(170),show_tail="narr",show_xmax=500,show_retain=5)
    n"As Selena described it…"(-40,convo_ypos(100),show_tail="narr",show_xmax=500,show_retain=4)
    n"It’s the story about a human boxer, down on his luck, who ends up renting out the spare room to a vampire girl. The narrative follows their various supernatural misadventures, ranging from getting into a boxing match with a werewolf."(-80,convo_ypos(20),show_tail="narr",show_xmax=550,show_retain=3)
    n"Trying to throw the scent off a vampire hunter.\n"(480,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=2)
    extend"Meeting her adopted vampire progenitor."(480,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=1)
    n"And then one deleted episode concept involved going back in time to the age of vikings and fighting against viking raiders. Which created its own spinoff."(20,convo_ypos(-20),show_tail="narr",show_xmax=1000,show_retain=0)
    hide screen Vampire_n_Boxer
    call nextpage

    n"It’s apparently highly-rated due to its expertly handled character development, story, and art direction."(40,convo_ypos(-80),show_tail="narr",show_xmax=800,show_retain=5)
    n"But, tragically, it suffered from seasonal rot after the network heads kicked out the original creative team and started trying to chase trends and social movements."(40,convo_ypos(50),show_tail="narr",show_xmax=700,show_retain=4)
    n"While there were good episodes in that era, most of the fandom consider it to be non-canon because it deviated so far from the original vision."(-40,convo_ypos(120),show_tail="narr",show_xmax=1000,show_retain=3)
    n"Then it had a revival when the original creator came back from a long sabbatical who managed to reacquire the license from the network who were trying to release a bunch of unnecessary, horrible spinoffs."(90,convo_ypos(50),show_tail="narr",show_xmax=850,show_retain=2)
    n"The original creator then started a kickstarter to recreate the series, better than it ever was, and do it properly this time."(300,convo_ypos(70),show_tail="narr",show_xmax=520,show_retain=1)
    n"...." (700,convo_ypos(70),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    show screen Vampire_n_Boxer
    n"That’s what Selena says at least."(4,convo_ypos(500),show_tail="narr",show_xmax=800,show_retain=2)
    n"Short version: it’s a story about a human boy and a vampire girl, sharing an apartment, hijinks ensue."(50,convo_ypos(20),show_tail="narr",show_xmax=800,show_retain=1)
    s "Alright, snacks are ready!" (840,convo_ypos(220),show_tail="baseright",show_xmax=345,show_retain=0)
    call nextpage
    hide screen Vampire_n_Boxer

    scene selena_room_box with dissolve
    show Selena smile at middef with dissolve

    show screen Laptop
    s "We’ll first watch the original version, " (580,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=2)
    show Selena closed
    s"because you can’t appreciate the remake without seeing the original."(580,convo_ypos(-100),show_tail="topleft",show_xmax=345,show_retain=4)
    b "...the whole thing?" (40,convo_ypos(180),show_tail="baseleft",show_xmax=345,show_retain=3)
    show Selena opensmile open

    s "We’ve got plenty of time!"(580,convo_ypos(-150),show_tail="topleft",show_xmax=345,show_retain=2)
    b "I mean, I guess but…"(40,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=1)
    n"The size of that complete box set just radiated intimidation."(450,convo_ypos(-200),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    b "Do… do we also have to watch the spinoffs?"(40,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=4)
    show Selena frown lookaway down
    s "......"(580,convo_ypos(-50),show_tail="topleft",show_xmax=345,show_retain=3)
    # Yandere/ dead-eye stare from Selena
    show Selena frown midclose down
    s "Do you normally start a story and skip chapters, Blake?"(580,convo_ypos(50),show_tail="topleft",show_xmax=345,show_retain=2)
    b "..."(40,convo_ypos(),show_tail="baseleft",show_xmax=345,show_retain=1)
    show Selena horizontal squiggly open
    b "{size=40}Wow, these are some great snacks!{/size}"(40,convo_ypos(150),show_tail="baseleft",show_xmax=345,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=10)
    call nextpage
    hide screen Laptop
    scene selena_house_truck with Fade(0.5, 1.5, 0.5)
    pause
    call nextpage
    scene selena_room_box with fade:
        xalign 0.0 zoom 1.5
    show Blake smile down open with dissolve:
        xalign 0.1 yanchor 0.0 ypos 0.3
    pause
    scene selena_room_box with fade:
        xalign 1.0 zoom 1.5
    show Selena smile closed with dissolve:
        xalign 0.9 yanchor 0.0 ypos 0.3

    pause
    call nextpage
    stop music
    scene Sky1 with dissolve
    play sound "audio/Interlude #7.ogg"

    pause
    call nextpage
    # Image of Selena smiling
    # (This one’s a bit weird, since we need to show the passage of time and there’s a few ways to do that so I’ll leave it up to whoever’s coding to decide which way works best. There’s gonna be about 2-3 of these short sequences)
    # Method 1: Show the same BG image, but show the passage of time by changing the shadows on the room or show it in the sky outside
    # Method 2: Show a timer somewhere: this could be a watch, someone’s phone, or the timer on the laptop that they’re watching this on
    # Method 3: Show the scene transition image after each time skip
    # Method 4: Use a single CG to show the passage of time
    # Method 5: Just cut to the sky changing colors then cut back to the room
    # Time-skip transition here
    # Maybe put a short jingle here, as if it’s the end of an episode, doesn’t need to be long… just something that lasts for like 2-3 seconds
    play music "audio/Meeting.ogg"

    n"Huh, so that was the first season..." (-20,convo_ypos(),show_tail="narr",show_xmax=800,show_retain=4)
    n"Seemed a bit rough around the edges, but there’s something appealing about it that makes me want to watch the rest of the episode." (40,convo_ypos(),show_tail="narr",show_xmax=800,show_retain=3)
    n"Also, I didn’t expect the fight scene at the end to be so cool."(100,convo_ypos(100),show_tail="narr",show_xmax=800,show_retain=2)
    n"Come to think of it, Selena’s been pretty quiet for a while."(160,convo_ypos(),show_tail="narr",show_xmax=800,show_retain=1)
    n"Wonder if she’s okay?" (160,convo_ypos(220),show_tail="narr",show_xmax=800,show_retain=0)
# Slight pan to show Selena’s sprite, who is sobbing
    scene selena_room_box with dissolve
    call nextpage
    show Selena crying concerned squiggly at middef with dissolve
    s "It was even better than I remembered!" (580,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=3)

    n"She’s sobbing?!"(450,convo_ypos(),show_tail="narr",show_xmax=500,show_retain=2)
    show Selena opensmile
    s "She begun the process of learning the true meaning of friendship!" (580,convo_ypos(80),show_tail="topleft",show_xmax=345,show_retain=1)
    show Selena up at bounce
    s "Next episode!"(580,convo_ypos(120),show_tail="topleft",show_xmax=345,show_retain=0)
# Time-skip transition here
    scene selena_house_truck with Fade(0.5, 1.5, 0.5)
    pause
    call nextpage
    n"According to Selena, after the end of season 1, the network executives pushed the original showrunner out of the picture to exert more creative control over the franchise."(40,convo_ypos(-120),show_tail="narr",show_xmax=800,show_retain=6)
    n"Over the years, everyone who originally worked on the show would be replaced."(40,convo_ypos(80),show_tail="narr",show_xmax=800,show_retain=5)
    n"Midway through season 2, even I could tell how different the writing was."(40,convo_ypos(80),show_tail="narr",show_xmax=800,show_retain=4)
    n"For a few episodes leading to the end of season 2, they changed the writing format to an 11-minute format, which was better suited to slapstick comedy shows rather than the deep emotional drama that was this show."(40,convo_ypos(),show_tail="narr",show_xmax=800,show_retain=3)
    n"...."(600,convo_ypos(115),show_tail="narr",show_xmax=800,show_retain=2)
    n"I didn’t know what any of that meant, but that’s what Selena said."(40,convo_ypos(-40),show_tail="narr",show_xmax=800,show_retain=1)
    n"Either way, the show was going downhill."(120,convo_ypos(0),show_tail="narr",show_xmax=800,show_retain=0)
# Time-skip transition here
    call nextpage
    scene selena_room_box with dissolve
    show Blake openmouth up at middef:
        xalign 0.9 zoom 0.6
    b "And so they’re just gonna end like that?!" (700,convo_ypos(),show_tail="baseright",show_xmax=345,show_retain=10)
    show Selena at middef:
        xalign 0.1 zoom 0.6
    s "Yep!"  (250,convo_ypos(-120),show_tail="baseleft",show_xmax=345,show_retain=9)
    show Blake frown
    b "But what about-"(640,convo_ypos(-100),show_tail="baseright",show_xmax=345,show_retain=8)
    show Selena closed
    s "Doesn’t matter."(260,convo_ypos(-160),show_tail="lefttop",show_xmax=345,show_retain=7)
    show Blake midclose
    b "But what happened to the count?"(620,convo_ypos(-80),show_tail="topright",show_xmax=345,show_retain=6)
    show Selena oneclose
    s "Resolved off-screen."(260,convo_ypos(),show_tail="topleft",show_xmax=345,show_retain=5)
    show Blake openmouth open
    b "And what about Christa-"(640,convo_ypos(-40),show_tail="topright",show_xmax=345,show_retain=4)
    show Selena opensmile
    s "I guess she died!"(240,convo_ypos(-20),show_tail="topleft",show_xmax=345,show_retain=3)
    show Blake down frown midclose
    b "What the shit kind of ending was that?!"(640,convo_ypos(-40),show_tail="topright",show_xmax=345,show_retain=2)
    show Selena openmouth open down
    s "I know right! Social media blasted them for years! It’s still going on now! It had such a great start too, but the network was way more concerned with merchandising than quality!"(260,convo_ypos(),show_tail="topleft",show_xmax=600,show_retain=1)
    show Selena frown horizontal midclose
    s "Such squandered potential."(200,convo_ypos(150),show_tail="lefttop",show_xmax=345,show_retain=0)
    call nextpage
    with fade
    n"....."(300,convo_ypos(-100),show_tail="narr",show_xmax=345,show_retain=2)
    show Selena down open opensmile at bounce
    s "Fortunately, that’s what the remake solves!"(290,convo_ypos(140),show_tail="baseleft",show_xmax=345,show_retain=1)
    show Blake open opensmile at bounce
    b "Alright, let’s start watching immediately!"(640,convo_ypos(100),show_tail="righttop",show_xmax=345,show_retain=0)
    # Note that it might be better for them to not finish the series yet, actually ya know what, since I don’t wanna write that anymore, I’m just gonna cap it there. As of this section, the bg should indicate that it’s night time
    hide Selena
    hide Blake
    with fade
    call nextpage
    show screen Laptop
    n"Selena quickly reaches over to the remake’s box set and I can practically feel the excitement in the air as we get ready to watch the next-"(40,convo_ypos(80),show_tail="narr",show_xmax=600,show_retain=1)
    scene black
    hide screen Laptop
    stop music
    n"Suddenly the power went out."(380,convo_ypos(40),show_tail="narr",show_xmax=345,show_retain=0)
    # ^ Alternatively, just show the screen blacking out
    # Loud crashing noise, as the sudden blackout caused Blake to trip. I was gonna say he banged his shin on the table, but then I remembered there is no table
    call nextpage
    show Selena_eyes_blink:
        xalign 0.1 yalign 0.3 zoom 0.5
    play sound"audio/2_Minute_Thunderstorm-Mike_Koenig.ogg" loop fadein 1.0
    s "Eh? Eh? What happened?" (250,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=6)
    s "Are we dead?" (350,convo_ypos(-50),show_tail="baseleft",show_xmax=345,show_retain=5)
    s "Did we die?"(400,convo_ypos(-40),show_tail="baseleft",show_xmax=345,show_retain=4)
    s "Blake, are you there?"(280,convo_ypos(),show_tail="baseleft",show_xmax=345,show_retain=3)
    show Blake_eyes_blink:
        xalign 0.80 yalign 0.65 zoom 0.5
    b "Yeah, sorry, I’m right here! I think the sudden darkness just made me slip."(700,convo_ypos(50),show_tail="baseright",show_xmax=345,show_retain=2)
    s "Well, keep talking, lemme help you up."(250,convo_ypos(-140),show_tail="lefttop",show_xmax=345,show_retain=1)
    b "Okay, I’m right over here.."(610,convo_ypos(150),show_tail="rightbase",show_xmax=345,show_retain=0)
    # Sudden thunder noise!
    show Selena_eyes_blink at bounce
    y"{size=80}Crash!!{/size}"(500,120,show_tail="yell",show_xmax=800,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=10)
    show Blake_eyes_blink at bounce
    y"{size=80}Crash!!{/size}"(40,720,show_tail="yell",show_xmax=800,show_retain=0) with Shake((0, 0, 0, 0), 0.5, dist=10)
    # Another crash!
    call nextpage
    s "...I nearly had a heart attack."(250,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=3)
    b "Are you okay?"(700,convo_ypos(50),show_tail="baseright",show_xmax=345,show_retain=2)
    s "I’m good, but listen."(250,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=1)
    n"...?"(380,convo_ypos(40),show_tail="narr",show_xmax=345,show_retain=0)
    # Rain sounds
    call nextpage
    play music "audio/The Sleeping City.ogg" fadein 1.0
    scene rain with dissolve
    n"Ah. When did it start raining? I don’t remember the weather app mentioning-"(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=3)
    n"Oh right. Phone’s still dead. Maybe I should’ve charged the phone while the power was up."(200,convo_ypos(100),show_tail="narr",show_xmax=500,show_retain=2)
    s "Ah, that reminds me, we’ve been binging this series all day but how are you gonna get home in this storm?"(150,convo_ypos(420),show_tail="baseleft",show_xmax=345,show_retain=1)
    b "That… is an excellent question."(700,convo_ypos(50),show_tail="baseright",show_xmax=345,show_retain=0)
    call nextpage
    n "At this time of night, would there be a {b}dRuver{/b} around?"(100,convo_ypos(-200),show_tail="narr",show_xmax=500,show_retain=10)
    s "It’s coming down pretty hard. You might catch a cold if you go out there."(50,convo_ypos(280),show_tail="baseleft",show_xmax=345,show_retain=9)
    n "Nah, probably too expensive."(450,convo_ypos(-350),show_tail="narr",show_xmax=500,show_retain=8)
    s "Hm… if you want, you could stay here for the night."(120,convo_ypos(230),show_tail="baseleft",show_xmax=345,show_retain=7)
    n "I don’t live that far, I could just walk it." (450,convo_ypos(-350),show_tail="narr",show_xmax=500,show_retain=6)
    s "I think you’re a trustworthy person, so I don’t really mind."(50,convo_ypos(300),show_tail="baseleft",show_xmax=345,show_retain=5)
    n"And risk being stabbed in the face? Forget it."(440,convo_ypos(-380),show_tail="narr",show_xmax=500,show_retain=4)
    s "Blake, are you there?"(200,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=3)
    n"Maybe there’s a-"(550,convo_ypos(-250),show_tail="narr",show_xmax=500,show_retain=2)
    s "{size=40}Blake N Lawrence!{/size}"(220,convo_ypos(150),show_tail="baseleft",show_xmax=400,show_retain=1)
    y "{size=45}Present!{/size}"(500,convo_ypos(-350),show_tail="yell",show_xmax=500,show_retain=0)
    call nextpage
    n"I instinctively reacted as if I was in a classroom, I hadn’t done that in so long that I just moved on autopilot."(200,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=8)
    b "I mean... yes?"(700,convo_ypos(210),show_tail="baseright",show_xmax=345,show_retain=7)
    s "I was saying… if you want, you can stay the night."(50,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=6)
    b "...."(700,convo_ypos(-100),show_tail="baseright",show_xmax=345,show_retain=5)
    s "....."(50,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=4)
    b "......"(700,convo_ypos(-100),show_tail="baseright",show_xmax=345,show_retain=3)
    s "..Ya know, this is kinda embarrassing for me too, so can you please say something?"(180,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=2)
    b "...."(700,convo_ypos(-100),show_tail="baseright",show_xmax=345,show_retain=1)
    s "...Blake?"(50,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=0)
# Thud noise
    call nextpage
    scene black
    play sound "audio/sfx-thud.ogg" volume 0.25
    s "Blake! Did you seriously just faint?"(100,convo_ypos(380),show_tail="baseleft",show_xmax=345,show_retain=0)
    stop sound
# [ End scene]


    call nextpage
    scene selena_room_box_night
    show black:
        alpha 0.7
    with dissolve
    # Scene transition
    n "...."(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=4)
    n "...The ceiling seems taller than I remember?"(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=3)
    n "Oh right. I’m laying down."(100,convo_ypos(40),show_tail="narr",show_xmax=500,show_retain=2)
    n "In a sleeping bag."(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=1)
    n "....."(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=0)

    call nextpage
    scene flashback
    # flashback line, but with lewd music attached to it to imply that it’s lewder than it seemed
    $ selena_outfit="bedtime"
    show Selena blush smile concerned midclose at middef,sway:
        yoffset 200
    show black:
        alpha 0.7
    s "\"W-Would you like to... stay the night?\"" (580,convo_ypos(200),show_tail="baseleft",show_xmax=345)

    scene selena_room_box_night
    call nextpage
    n "It definitely didn’t happen like that!"(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=4) with Shake((0, 0, 0, 0), 0.5, dist=20)
    n "Were my cheeks red? I felt like they were red."(100,convo_ypos(50),show_tail="narr",show_xmax=500,show_retain=3)
    n "Calm down! This isn’t that sort of situation, it’s just a kind gesture to a friend."(100,convo_ypos(50),show_tail="narr",show_xmax=500,show_retain=2)
    n "...That you recently met."(100,convo_ypos(100),show_tail="narr",show_xmax=500,show_retain=1)
    n "Don’t overthink it dammit!"(100,convo_ypos(0),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    scene nightsky with dissolve

    s "Blake, are you awake?"(50,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=6)
    b "Uh, yeah! Still awake!"(700,convo_ypos(0),show_tail="baseright",show_xmax=345,show_retain=5)
    s "Okay."(50,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=4)
    n "Her voice sounded different."(240,convo_ypos(-120),show_tail="narr",show_xmax=500,show_retain=3)
    n "Before she was like, how do I describe it, a ball of positive energy that could power the gloomiest of cities for years."(100,convo_ypos(0),show_tail="narr",show_xmax=700,show_retain=2)
    n "Now she seemed uncharacteristically shy."(240,convo_ypos(80),show_tail="narr",show_xmax=500,show_retain=1)
    s "Well, I’m just going to scoot in next to you."(50,convo_ypos(190),show_tail="baseleft",show_xmax=345,show_retain=0)
    # Shuffling sound, as if there’s a second sleeping bag
    play sound "audio/sfx-shoomp.ogg" volume 0.15
    call nextpage
    s "There we go, nice and comfy."(50,convo_ypos(350),show_tail="baseleft",show_xmax=345,show_retain=3)
    n "I can’t see her, my back is turned to the side. I can’t look at her, because I feel like I really shouldn’t."(150,convo_ypos(-140),show_tail="narr",show_xmax=500,show_retain=2)
    n "..."(160,convo_ypos(180),show_tail="narr",show_xmax=500,show_retain=1)
    n "Things are getting pretty awkward. Say something, dumbass!"(340,convo_ypos(-150),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    scene lake2 with dissolve:
        xalign 0.0
        ease 50 xalign 1.0
    show black:
        alpha 0.7
    b "So uh, did you ever see something like this happening when the memento I threw away accidentally landed on your head?"(700,convo_ypos(200),show_tail="baseright",show_xmax=500,show_retain=5)
    s "...No."(50,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=4)
    b "Ah. Yeah. Me neither. Sorry about that, by the way. I don’t know if I apologized for that, but it just kinda slipped out of my hand and sorta veered off course like it was fa-"(790,convo_ypos(120),show_tail="baseright",show_xmax=500,show_retain=3)
    n "I stopped myself before saying something supremely creepy."(60,convo_ypos(40),show_tail="narr",show_xmax=500,show_retain=2)
    n " \"Like it was fate.\""(500,convo_ypos(-180),show_tail="narr",show_xmax=500,show_retain=1)
    n "Who says that outside of shojo manga?!"(340,convo_ypos(40),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    s "It’s okay."(50,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=6)
    n "Her voice is so quiet I almost missed it."(340,convo_ypos(-80),show_tail="narr",show_xmax=500,show_retain=5)
    # s "It’s okay."(50,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=5)
    s "The truth is, I didn’t think I was gonna go home today.."(50,convo_ypos(200),show_tail="baseleft",show_xmax=345,show_retain=4)
    b "Eh?"(700,convo_ypos(-100),show_tail="baseright",show_xmax=500,show_retain=3)
    s "I was just taking a walk to clear my head of everything. So much of my life was changing, so many things that I’d dreamed of were falling apart, and I felt lost."(50,convo_ypos(170),show_tail="baseleft",show_xmax=500,show_retain=2)
    s "It’s just that, I sacrificed so much, tried so hard, did everything right. Or at least, I thought I was doing everything right."(100,convo_ypos(70),show_tail="baseleft",show_xmax=800,show_retain=1)
    s "But I guess it wasn’t enough."(250,convo_ypos(0),show_tail="baseleft",show_xmax=345,show_retain=0)
    call nextpage

    s "A person can do everything right and still fail."(50,convo_ypos(50),show_tail="baseleft",show_xmax=500,show_retain=4)
    s "At one point, my mind went to some dark places. I kept thinking about what the point of everything was, and if the hole in my heart would ever close."(50,convo_ypos(100),show_tail="baseleft",show_xmax=945,show_retain=3)
    s "Then a small object hit me in the back of my head."(200,convo_ypos(180),show_tail="baseleft",show_xmax=645,show_retain=2)
    s "Sorta snapped me back to reality."(50,convo_ypos(140),show_tail="baseleft",show_xmax=345,show_retain=1)
    s "Is that weird? I think it sounds pretty weird."(250,convo_ypos(40),show_tail="baseleft",show_xmax=345,show_retain=0)
    call nextpage
    s "I expected to see some jerk tossing garbage or something, and instead I saw you."(50,convo_ypos(300),show_tail="baseleft",show_xmax=700,show_retain=2)
    s "Someone who looked like he was in pain too."(450,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=1)
    s "The same kind of pain as me."(250,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=0)
    call nextpage
    s "I don’t know what I was expecting today, certainly not this."(50,convo_ypos(140),show_tail="baseleft",show_xmax=500,show_retain=4)
    s "But… I’ve been told that I’m a sort of look before you leap person, and now look at me. I’m sleeping next to a total stranger, in my empty apartment, with the power out."(50,convo_ypos(80),show_tail="baseleft",show_xmax=900,show_retain=3)
    s "I mean, this is crazy, isn’t it?"(50,convo_ypos(20),show_tail="baseleft",show_xmax=345,show_retain=2)
    s "What if you were like, a scammer, or a murderer? I just invited you into my house at my most vulnerable moment, and now I’m whining about my life. What’s wrong with me?"(50,convo_ypos(80),show_tail="baseleft",show_xmax=900,show_retain=1)
    b "..."(700,convo_ypos(20),show_tail="baseright",show_xmax=345,show_retain=0)
    call nextpage
    scene nightsky with dissolve
    n "With the edge of my palm, I tap hers. I’m not good with words. Not at all."(340,convo_ypos(-170),show_tail="narr",show_xmax=500,show_retain=7)
    n "I work with computers, systems, data sets. These are things that make sense to me."(-40,convo_ypos(80),show_tail="narr",show_xmax=450,show_retain=6)
    n "I don’t really know what to say to help her."(450,convo_ypos(-120),show_tail="narr",show_xmax=500,show_retain=5)
    n "So I do the only thing I can."(380,convo_ypos(80),show_tail="narr",show_xmax=500,show_retain=4)
    n "She takes the cue and softly interlocks her fingers with mine."(240,convo_ypos(10),show_tail="narr",show_xmax=650,show_retain=3)
    n "......"(100,convo_ypos(40),show_tail="narr",show_xmax=500,show_retain=2)
    n "We stayed in complete silence for while, neither of us needing to exchange any words. Just this simple gesture was enough. Was she asleep by now? Has she calmed down a little bit? Did I mess up?"(290,convo_ypos(-140),show_tail="narr",show_xmax=700,show_retain=1)
    n "My mind was spinning again."(340,convo_ypos(180),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    # shuffling noise in the bed
    play sound "audio/sfx-shoomp.ogg" volume 0.15
    n "I heard her shift her body in the sleeping bag next to mine, and could feel her eyes on my back."(340,convo_ypos(40),show_tail="narr",show_xmax=500,show_retain=0)
    call nextpage
    scene black with dissolve
    s "..." (50,convo_ypos(0),show_tail="baseleft",show_xmax=700,show_retain=10)
    s "Blake, are you awake?" (50,convo_ypos(-20),show_tail="baseleft",show_xmax=700,show_retain=9)
    b "..."(700,convo_ypos(-80),show_tail="baseright",show_xmax=345,show_retain=8)
    n "I hesitated to answer."(340,convo_ypos(-100),show_tail="narr",show_xmax=500,show_retain=7)
    s "..."(50,convo_ypos(0),show_tail="baseleft",show_xmax=700,show_retain=6)
    s "{cps=20}Do you… wanna do it?{/cps}"(90,convo_ypos(-40),show_tail="baseleft",show_xmax=700,show_retain=5)
    n "...."(480,convo_ypos(-160),show_tail="narr",show_xmax=500,show_retain=4)
    s "...I wouldn’t mind if you want to."(50,convo_ypos(100),show_tail="baseleft",show_xmax=700,show_retain=3)
    n "..."(450,convo_ypos(-120),show_tail="narr",show_xmax=500,show_retain=2)
    s "Blake? Look at me, please?"(90,convo_ypos(100),show_tail="baseleft",show_xmax=700,show_retain=1)
    b "...okay."(700,convo_ypos(0),show_tail="baseright",show_xmax=345,show_retain=0)
    call nextpage
    # shuffling sound, then see Selena’s pajama CG
    play music "audio/Just for a While.ogg" fadein 1.0
    show screen Selena_bed
    n "......" (-50,convo_ypos(-100),show_tail="narr",show_xmax=500,show_retain=9)
    b "You’re very pretty."(300,convo_ypos(160),show_tail=False,show_xmax=345,show_retain=8)
    s "Thanks."(350,convo_ypos(-80),show_tail="baseright",show_xmax=700,show_retain=7)
    s "Then do you-"(450,convo_ypos(),show_tail="baseright",show_xmax=700,show_retain=6)
    b "I don’t know."(300,convo_ypos(-80),show_tail=False,show_xmax=345,show_retain=5)
    s "Eh?"(450,convo_ypos(-160),show_tail="righttop",show_xmax=700,show_retain=4)
    b "The truth is, I don’t dislike the idea."(300,convo_ypos(80),show_tail=False,show_xmax=345,show_retain=3)
    s "..."(450,convo_ypos(-200),show_tail="righttop",show_xmax=700,show_retain=2)
    s "But, you’re unsure if we should cross that line?"(700,convo_ypos(),show_tail="topright",show_xmax=700,show_retain=1)
    b "Yeah. A lot of things could change if we do."(780,convo_ypos(150),show_tail=False,show_xmax=345,show_retain=0)

    call nextpage
    s "Is it me?"(490,convo_ypos(-80),show_tail="baseright",show_xmax=700,show_retain=5)
    s "Do I really not have any appeal?"(490,convo_ypos(20),show_tail="baseright",show_xmax=350,show_retain=4)
    b "Of course you do! You’re so cute that any guy would love to spend even an hour in your presence! Just to talk about the weather!"(300,convo_ypos(200),show_tail=False,show_xmax=400,show_retain=3)
    b "You’re… the type of girl who’d look at a sad loser like me and do your best to cheer him up even when she’s feeling like her world is coming down around her. Before yourself, you put me and my feelings ahead. You didn’t even know me."(580,convo_ypos(220),show_tail=False,show_xmax=600,show_retain=2)
    b "It’s just that… in our current mental states, I’m unsure if we should… do that."(550,convo_ypos(0),show_tail=False,show_xmax=600,show_retain=1)
    b "It’s not that I don’t want to! Take my word for it, I really do."(700,convo_ypos(0),show_tail=False,show_xmax=600,show_retain=0)
    call nextpage
    hide screen Selena_bed
    # close up of her lips
    scene CG4 with dissolve:
        zoom 3.0 xalign 0.75 yalign 0.6
    b "I just… \ngimme a…"(300,convo_ypos(750),show_tail=False,show_xmax=345,show_retain=3)
    # chest
    scene CG4 with dissolve:
        zoom 2.0 xalign 0.6 yalign 0.5
    b "a um…"(350,convo_ypos(-80),show_tail=False,show_xmax=600,show_retain=2)
    # waist
    scene CG4 with dissolve:
        zoom 2.0 xalign 0.2 yalign 0.5
    b "a m-minute to…"(400,convo_ypos(-80),show_tail=False,show_xmax=600,show_retain=1)

    # eyes
    scene CG4 with dissolve:
        zoom 3.0 xalign 0.8 yalign 0.3
    b "um… to think about… things."(550,convo_ypos(-80),show_tail=False,show_xmax=600,show_retain=0)
    call nextpage
    scene CG4 with fade:
        zoom 1.6 xalign 1.0 yalign 0.5
    s "...okay."(490,convo_ypos(80),show_tail="baseright",show_xmax=700,show_retain=6)
    n "Another minute or two passes as we just stare at each other, illuminated by the small specks of moonlight peeking through the rainclouds." (-80,convo_ypos(-100),show_tail="narr",show_xmax=430,show_retain=5)
    s "Blake?"(490,convo_ypos(160),show_tail="righttop",show_xmax=700,show_retain=4)

    b "Yeah?"(300,convo_ypos(80),show_tail=False,show_xmax=600,show_retain=3)
    s "Have you thought about it yet?"(600,convo_ypos(-160),show_tail="righttop",show_xmax=700,show_retain=2)
    b "...maybe."(300,convo_ypos(80),show_tail=False,show_xmax=600,show_retain=1)
    s "...can I come closer to you then?"(680,convo_ypos(-160),show_tail="righttop",show_xmax=700,show_retain=0)
    call nextpage
    scene black with Dissolve(2.0)
    b "....."(700,convo_ypos(200),show_tail=False,show_xmax=600,show_retain=0)

    scene white with Dissolve(0.25)
    scene nightsky with Dissolve(1.5)
    pause
    ""

    return
