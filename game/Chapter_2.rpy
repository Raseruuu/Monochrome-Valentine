image s_ext_truck = "images/bg/selena_house_truck.webp"
image s_ext = "images/bg/selena_house.webp"
image s_int = "images/bg/selena_room_with_box.webp"
image sky_morning="images/bg/sky_morning.webp"
define c = Character("(Neighbour)",
            screen ="bubble_say")
image emblem="images/TKU_middle_school_emblem.webp"
image young_selena:
    "images/cg/young_selena.webp"
image CG6:
    "images/cg/CG6.webp"


screen yearbook():
    zorder 120
    add "images/cg/TKU_Middle_School_yearbook.webp" at yearbookanim
transform yearbookanim:
    yalign 0.75 xalign 0.1 yoffset 0 alpha 0.0
    ease .5 yoffset -80 alpha 1.0

label chapter2_1:
    stop music fadeout 3.0

    scene black with Dissolve(3.0)
    pause
    play music "audio/Interlude #5.ogg" noloop
    call screen chap("2", "Request")
    call nextpage
    play music "audio/Natsu no Owari.ogg"
    scene s_ext with dissolve
    n "A common saying is, life is often stranger than fiction." (220,50,show_tail="narr",show_xmax=600,show_retain=4)
    n "Today, I would agree with that." (550,250,show_tail="narr",show_xmax=330,show_retain=3)
    scene black with dissolve
    show Selena at middef
    show black as black2:
        alpha 0.5
    with dissolve
    n """A girl I just met, who seems really nice, and cute, and funny,
        and cute. Did I say cute twice?""" (100,650,show_tail="narr",show_xmax=550,show_retain=2)
    n "Anyways, this girl,\n her name is {b}Selena{b}."(350,880,show_tail="narr",show_xmax=520,show_retain=1)
    n " I don’t know what she finds so special about me, but despite knowing me for less than 20 minutes, she invited me back to her place." (350,1040,show_tail="narr",show_xmax=520,show_retain=0)
    btr "{size=50}{cps=5}. . . . .{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)

    call nextpage
    n """Not for anything lewd! She just wants me to help her pack and move some stuff in her house,
        to a moving truck outside, so she can then drive it to her parent’s place.""" (100,20,show_tail="narr",show_xmax=720,show_retain=2)
    btr "{size=50}{cps=5}.\n\n.\n\n.\n\n.\n\n.{/cps}{/size}" (890,50, show_tail="btr",show_xmax=800)
    n """Okay, I know that sounds suspicious. I had the exact same look which I imagine that any sane,
        rational person would have at being propositioned to return to a complete stranger’s home; but I swear it’s real."""(200,650,show_tail="narr",show_xmax=600)
    pause

    scene sky_morning with dissolve

    pause
    scene s_ext_truck with dissolve
    call nextpage

    pause 1

    n "There’s the moving truck, after all." (200,350,show_tail="narr",show_xmax=450,show_retain=2)
    n "Believe it or not, I did point out how weird it was to invite a complete stranger to your house to handle your stuff.
        What if I was a murderer, or a thief, or an alien?" (300,550,show_tail="narr",show_xmax=450,show_retain=1)
    n "Seriously, who would trust someone this much so quickly?" (450,900,show_tail="narr",show_xmax=450)

    show Selena midclose smug with dissolve:
        alpha 0.8 zoom 0.8 xalign 1.0
    call nextpage
    n """Her response was… to look at me for several seconds, and then smugly smirk at,
        what I assumed, was the idea of me being threatening."""  (20,50,show_tail="narr",show_xmax=550,show_retain=2)
    n "...I don’t know if I should feel flattered or insulted." (50,550,show_tail="narr",show_xmax=450,show_retain=1)
    n "So why didn’t I say no, if I know how weird this whole situation is?" (100,950,show_tail="narr",show_xmax=450)

    hide Selena
    call nextpage
    n "Well… she can be surprisingly persuasive." (50,100,show_tail="narr",show_xmax=500,show_retain=4)
    n "If this were an RPG, she’d have dumped all her points into charisma and could convince the final boss to give up his 1000 year plan to bring about eternal darkness and instead to close down shop, buy a suit, get a new house, and go back to school while working weekends at a local diner or-" (70,300,show_tail="narr",show_xmax=750,show_retain=3)
    s "Hey Blake, you there?" (-20,750,show_tail="lefttop",show_xmax=350,show_retain=2)
    b "Huh?" (400,1250,show_tail="baseright",show_xmax=250,show_retain=1)
    n "I must’ve been just standing in front of the truck for a while, in a trance. To the outside observer, I probably looked-" (420, 820,show_tail="narr",show_xmax=450)

    call nextpage
    show Selena at middef with dissolve
    s "Anyone ever tell you that you space out a lot?" (440,250,show_tail="baseleft",show_xmax=450,show_retain=3)
    b "...Maybe." (900,550,show_tail="rightbase",show_xmax=450,show_retain=2)
    show Selena opensmile
    s "So, this is my moving truck. What do you think?" (450,750,show_tail="topleft",show_xmax=450,show_retain=1)
    b "It’s… big? Seems like it’d haul a lot? Um… it smells very… much like a car?" (900,1250,show_tail="baseright",show_xmax=450)

    call nextpage
    nv "Continuing off the RPG analogy, that would’ve been a pretty low deception roll.\n Okay, I admit it, I’m not a car guy. I’m a failure of a man."
    nv "\n\nOh crap, how long have I been standing here without saying anything?"
    nv "\n\nQuick, say something so it seems like you were paying attention."
    nvl clear
    nvl hide
    b "{size=50}Apples!!!{/size}" (950,450,show_tail="rightbase",show_xmax=450,show_retain=3)
    show Selena frown up
    s "!?" (550,630,show_tail="topleft",show_xmax=450,show_retain=2)
    show Selena midclose squiggly
    s "...you think the truck’s manufacturer is… apples?" (450,750,show_tail="topleft",show_xmax=450,show_retain=1)
    n "That look of pity in her eyes hurt my soul." (350,1050,show_tail="narr",show_xmax=450)

    call nextpage
    b "Uhhhhhhhhhh….." (680,200,show_tail="rightbase",show_xmax=400,show_retain=3)
    n "Quick, change the subject! {nw}" (100,550,show_tail="narr",show_xmax=450,show_retain=2)
    b "So! This seems like a pretty nice neighborhood, how long have you lived here?" (790,800,show_tail="rightbase",show_xmax=520,show_retain=1)
    n "Nailed it."(600,1150,show_tail="narr",show_xmax=250)

    call nextpage
    show Selena smile open with ease:
        xpos 0.65
    s "Oh, well, I moved here a few months ago from my old place. It was a bit closer to my job, but…" (450,350,show_tail="baseright",show_xmax=450,show_retain=4)
    show Selena lookaway concerned
    extend " guess that’s not really an issue anymore." (450,350,show_tail="baseright",show_xmax=450,show_retain=3)
    show Selena open
    b "You only moved here a few months ago?" (-20,500,show_tail="leftbase",show_xmax=450,show_retain=2)
    show Selena lookaway
    s "Yep. Guess it was just time for a change." (600,650,show_tail="topright",show_xmax=450,show_retain=1)
    n "She streches as she said this, and I had that feeling again." (400,1050,show_tail="narr",show_xmax=500)

    call nextpage
    n "Like, there was something she didn’t want to talk about. Perhaps I should be more suspicious considering how little I kno-" (40,100,show_tail="narr",show_xmax=500,show_retain=2)
    hide Selena with dissolve
    s "You coming??" (420,630,show_tail="leftbase",show_xmax=450,show_retain=1)
    n "She’d already unlocked her front door and was standing in the hallway." (200,750,show_tail="narr",show_xmax=450)

    show Selena at middef with dissolve
    call nextpage
    b "Oh, yeah! Sorry, just admiring this… door frame? What’s this dent here?" (20,250,show_tail="leftbase",show_xmax=450,show_retain=4)
    s "Oh thanks, yeah, a pizza guy once slipped on his shoelaces and bashed his head in the frame." (520,570,show_tail="lefttop",show_xmax=350,show_retain=3)
    b "...really?"(50,700,show_tail="narr",show_xmax=450,show_retain=2)
    s "No, I’m just messing with you." (540,850,show_tail="lefttop",show_xmax=450,show_retain=1)
    n "I should really stop zoning out and narrating to myse-" (230,1050,show_tail="narr",show_xmax=580)

    call nextpage
    show Selena with dissolve:
        zoom 0.3 xpos 0.33 ypos 0.5 yanchor 0.0
    s "Blake?{p=0.2}" (300,810,show_tail="baseleft",show_xmax=450,show_retain=1)
    b "Coming!" (700,950,show_tail="rightbase",show_xmax=450)

    scene black with dissolve
    pause 2

label Chapter2_2: #Inside Selena’s apartment, packing her stuff*
    #- A vague shapeless pile of stuff
    #- Some boxes on the interior BG image, the boxes should be their own separate layer that can be hidden for scene 4
    #- Cut-in image of Blake’s smartphone
    #- cut-in image of the school uniform neckerchief thingy
    # Example floor plan: https://liveatone.com/wp-content/uploads/2019/03/ONE_1BED1BATH_1A_1_900x900_022519.jpg

    scene s_int with dissolve
    call nextpage
    n "What I see the moment I walk in is a sparse-looking apartment with several boxes stacked together off to the side. On each box is a label telling someone the contents of the box. I can’t help but wonder what her apartment looked like before she started packing?" (50,20,show_tail="narr",show_xmax=800,show_retain=3)
    b "So, how much stuff do you have left to pack?" (-20,650,show_tail="leftbase",show_xmax=350,show_retain=2)
    show Selena at middef
    s "Not much." (500,700,show_tail="lefttop",show_xmax=450,show_retain=1)
    n "She retrieved a cushion from the closet and put it on the ground where, I imagine, she wanted me to sit?" (250,950,show_tail="narr",show_xmax=500)

    call nextpage
    show Selena #with 1 bounce
    s "Well, here we are. This place used to be much cuter buuuut, now it’s back to… well, its base form."(430,250,show_tail="baseright",show_xmax=450,show_retain=1)
    s "Wait right here, I’ll be back in a sec."(570,500,show_tail="topleft",show_xmax=300)
    hide Selena with moveoutleft
    n "At which point, she disappears into the other room. Leaving me alone in her living room." (180,900,show_tail="narr",show_xmax=550,show_retain=1)
    btr "{size=50}{cps=5}. . . . .{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)

    call nextpage
    n "Seemed nice. One-room. Surprisingly spacious?" (150,200,show_tail="narr",show_xmax=550,show_retain=4)
    btr "{cps=0}What? I was in {b}I.T.{/b}, not Interior Design.{/cps}" (150,1330, show_tail="btr",show_xmax=800)
    n "Honestly, there wasn't much to describe." (40,400,show_tail="narr",show_xmax=450,show_retain=2)
    n "Guess I could check my phone?" (40,600,show_tail="narr",show_xmax=450,show_retain=1)
    show phone:
        zoom 0.5
        yanchor 0.0 xanchor 0.5 xpos 0.65
        ypos 1.0
        linear 0.3 ypos 0.4
    n "Damn, battery died. It hasn’t been that long, has it? Wait, how old is this phone? Maybe it’s time for an upgrade?" (100,1100,show_tail="narr",show_xmax=700)

    s "Okay, so…" (800,200,show_tail="rightbase",show_xmax=450,show_retain=3)
    n "Oh thank god, something to do." (150,350,show_tail="narr",show_xmax=450,show_retain=2)
    # hide phone with moveoutleft
    show Selena at middef behind phone:
        xpos 0.8
        # ypos -0.5
        # zoom 0.20
    s "Here’s what we’re gonna do!" (800,600,show_tail="righttop",show_xmax=700,show_retain=1)

    n "Selena returned from, what I assume was her bedroom, with an armful of… uh… various stuff?"(50,1100,show_tail="narr",show_xmax=700)

    call nextpage
    hide Selena
    hide phone with moveoutright
    with dissolve
    n "Honestly, it’s a bit difficult to describe exactly what I’m looking at, since there’s just a random selection of stuff in her arms. I can see a pink towel with a cute character on it, a scarf, a beret, several stuffed animals, an assortment of pins, and-" (150,250,show_tail="narr",show_xmax=700,show_retain=2)
    n "She dropped it all on the floor in front of me, then went over to the corner where boxes of varying sizes were stacked up precariously like a messed-up parody of… uh… what was that one game called with the stacking blocks?" (180,550,show_tail="narr",show_xmax=650,show_retain=1)
    n "J… something?" (150,950,show_tail="narr",show_xmax=700) #find placeholder brand name sometime.

    call nextpage
    show Selena at middef:
        xpos 0.0
    s "So, we take one of these things," (20,250,show_tail="leftbase",show_xmax=700,show_retain=4)
    # show towel:
        # zoom 0.5 yanchor 0.0 ypos 1.0 xalign 0.5
        # linear 0.8 ypos 0.2
    # "She lifts up a towel."
    s "And then put them in a box with a corresponding label. Like so." (20,450,show_tail="lefttop",show_xmax=700,show_retain=3)
    n "She places the towel in the box marked as, bathroom stuff." (400,650,show_tail="narr",show_xmax=450,show_retain=2)
    b "Alright. Seems pretty straightforward." (850,1100,show_tail="baseright",show_xmax=400,show_retain=1)
    s "Oh yeah, totally. Trust me, with the two of us, time should just soar right by!" (20,1180,show_tail="lefttop",show_xmax=700)

    scene white
    n "45 minutes later" (20,450,show_tail="narr",show_xmax=700)
    scene s_int with dissolve
    n "So the pile seemed deceptively smaller than it originally looked. Yet, why does it seem like the pile got bigger?"(100,100,show_tail="narr",show_xmax=710,show_retain=3)
    n "is this some uncaring god’s idea of a sick joke? Am I just tired and hallucinating? I didn’t get much sleep last night. Or ever, actually. At least, not for the past few weeks ever since…" (120,400,show_tail="narr",show_xmax=500,show_retain=2)
    n "Ah. Right. With Selena’s…. let’s call it, nature, it’s pretty hard to focus on the rift between me and Ashley. Is that a good thing?"(100,750,show_tail="narr",show_xmax=650,show_retain=1)
    n "Well, when I woke up this morning, I started out as an 8 on the sad scale. But now I’m a 5. So, whatever this busywork is, it at least seems therapeutic." (300,1000,show_tail="narr",show_xmax=500)

    n "I pick up what looks like… a ribbon? A neckerchief? What is this this thing and why does it seem familiar?" (80,40,show_tail="narr",show_xmax=750,show_retain=3)
    show neckerchief:
        zoom 0.4 yanchor 0.0 ypos 1.0 xalign 0.8
        linear 0.8 ypos 0.4
    pause 1
    show Selena at middef behind neckerchief:
        xpos -1.0
        linear 0.7 xpos 0.25
    show Selena #with 1 bounce
    pause 1
    s "Oh hey, I know that! Can’t believe I brought that with me from home." (380,400,show_tail="leftbase",show_xmax=500,show_retain=2)
    b "What is it?" (800,1100,show_tail="baseright",show_xmax=650,show_retain=1)
    s "Turn it over." (380,1150,show_tail="lefttop",show_xmax=650)

    call nextpage
    hide Selena
    hide neckerchief
    with dissolve
    show emblem with dissolve:
        align (0.8,0.35) zoom 0.5
    n "Turning it over, I see what seems like an emblem printed on the fabric?"(60,100,show_tail="narr",show_xmax=650,show_retain=3)
    n "But I don’t see what that has to-" (60,500,show_tail="narr",show_xmax=500,show_retain=2)
    n "Wait a minute." (60,750,show_tail="narr",show_xmax=650,show_retain=1)
    n "This emblem looks familiar." (60,950,show_tail="narr",show_xmax=650)

    n "A bird, flying through a crescent moon. It’s unnecessarily fancy for-" (110,200,show_tail="narr",show_xmax=650,show_retain=2)
    b "Oh, this is the crest of {b}T.K.U.{/b} Middle School!!" (180,750,show_tail="leftbase",show_xmax=650,show_retain=1)
    s "Ding ding ding! That’s right!" (880,800,show_tail="righttop",show_xmax=650)
    hide emblem

    call nextpage
    show neckerchief:
        zoom 0.4 yanchor 0.0 ypos 1.0 xalign 0.4
        linear 0.4 ypos 0.3
    b "Hey, what’s this mark on the bottom here? On the tips?"(30,300,show_tail="leftbase",show_xmax=650,show_retain=3)
    s "Ah, I was going through my fashionista phase so I didn’t feel right wearing the same exact thing everyone else was wearing. So, I colored in the tips with some dye."(850,900,show_tail="righttop",show_xmax=650,show_retain=2)
    b "The teachers didn’t notice?"(200,1200,show_tail="leftbase",show_xmax=350,show_retain=1)
    s "I’m honestly as surprised as you are."(870,350,show_tail="righttop",show_xmax=350)

    call nextpage
    hide neckerchief
    show Selena at middef #at pop up
    b "I see, though why do you have it?" (100,900,show_tail="leftbase",show_xmax=500,show_retain=4)
    s "...." (450,500,show_tail="lefttop",show_xmax=400,show_retain=2)
    show Selena closed
    extend "I like to steal the neckerchiefs off pre-teen girls because I’m jealous of their youth."
    b "...really?" (200,1000,show_tail="leftbase",show_xmax=500,show_retain=1)
    show Selena open opensmile
    s "Oh my god, no! I went there when I was a kid! Geez, what kinda weirdo do you think I am?" (500,1000,show_tail="lefttop",show_xmax=370)

    call nextpage
    show Selena smile
    s "...." (380,180,show_tail="baseright",show_xmax=500,show_retain=5)
    show Selena opensmile oneclose
    s "Actually, don’t answer that question, I need to preserve my image as a cool beauty with a megawatt smile!" (430,300,show_tail="baseleft",show_xmax=500,show_retain=4)
    show Selena openmouth open
    s "Ah, but how’d you know about it?" (550,500,show_tail="lefttop",show_xmax=300,show_retain=3)

    b "Oh well, I went there too." (40,800,show_tail="baseleft",show_xmax=500,show_retain=2)
    n "Though I wouldn’t exactly call my experience a pleasant one. Not that I could remember much,
        but it seems that whenever I think of my time there, I feel more annoyance than joy."  (100,790,show_tail="narr",show_xmax=700,show_retain=1)
    n "Of course, that might just be because everybody hates middle school." (200,1100,show_tail="narr",show_xmax=500)

    call nextpage

    s "You’re kidding? That's such a coincide-" (360,500,show_tail="rightbase",show_xmax=400,show_retain=5)
    show Selena horizontal lookaway
    s "Wait." (620,600,show_tail="baseleft",show_xmax=500,show_retain=4)
    nv "\n\n\n\n\nShe paused in the middle of folding that towel, and looked right at me."
    show Selena midclose frown
    s "Remember when I said that you seemed familiar to me?" (400,500,show_tail="topright",show_xmax=400,show_retain=3)
    b "Yeah, that was like… an hour ago, right?" (-20,880,show_tail="leftbase",show_xmax=400,show_retain=2)
    show Selena opensmile open
    s "Yeah, so, hear me out. You know the symbol, I know the symbol." (480,650,show_tail="topleft",show_xmax=350,show_retain=1)
    show Selena smile
    s "What if… the reason we seem so familiar to each other, is because we’ve met before, over a decade ago, back in middle school?" (500,1000,show_tail="lefttop",show_xmax=380)

    call nextpage
    b "...that’d be a heck of a coincidence." (-20,200,show_tail="leftbase",show_xmax=500,show_retain=3)
    show Selena opensmile up #new excited expression
    s "I know right! But what if it’s true?"  (450,600,show_tail="topright",show_xmax=400,show_retain=2)
    b "Hm, you do speak fluent Japanese. Sorry, I overheard you earlier." (20,1000,show_tail="leftbase",show_xmax=350,show_retain=1)
    show Selena bounce smile at bounce
    s "I do, yes!" (600,900,show_tail="topleft",show_xmax=500)
    
    call nextpage
    s "My mother is a Japanese citizen, so I spent a lot of my childhood in Japan!" (400,250,show_tail="baseright",show_xmax=380,show_retain=4)
    b "Oh yeah? When I was starting middle school, my dad took us with him when he was stationed in Japan." (-20,750,show_tail="leftbase",show_xmax=450,show_retain=3)
    s "Well the timeline sure adds up! Ooh, do you remember what class you were in?" (450,650,show_tail="lefttop",show_xmax=430,show_retain=2)
    b "Sorry, I was going through some stuff at the time, so I can’t really remember a lot of the finer details. I can barely remember what my homeroom teacher’s name was." (10,1080,show_tail="leftbase",show_xmax=700,show_retain=1)
    show Selena stand squiggly
    s "Aw, that sucks." (550,1150,show_tail="topleft",show_xmax=500)

    call nextpage
    n "She seemed genuinely disappointed by-" (10,60,show_tail="narr",show_xmax=500,show_retain=4)
    show Selena bounce smile at bounce
    s "Ooh! Ya know what?" (420,300,show_tail="leftbase",show_xmax=500,show_retain=3)
    n "Nevermind, she’s back." (20,600,show_tail="narr",show_xmax=500,show_retain=2)
    show Selena stand opensmile
    s "I think I have a yearbook in here somewhere. If I find it then we can figure out if we were in the same class!" (480,850,show_tail="topleft",show_xmax=400,show_retain=1)
    b "Well alright, could be fun." (-30,1200,show_tail="baseleft",show_xmax=350)

    call nextpage
    show Selena horizontal:
        ease 0.5 yoffset 50
    s "Great! So, I’m gonna check in the boxes, cause I know it’s in here somewhere." (450,300,show_tail="baseleft",show_xmax=400,show_retain=2)
    b "Wait, should we be unpacking stuff that we just packed? Doesn’t that seem-" (40,820,show_tail="leftbase",show_xmax=500,show_retain=1)
    show Selena closed smile:
        ease 0.5 yoffset 150
    s "Sorry, can’t hear you, digging!" (550,780,show_tail="lefttop",show_xmax=330)

    call nextpage
    n "Something told me that Selena was the type of person who was not easily deterred once she decides on something. It’s not a bad trait in and of itself, actually it’s kinda cute." (50,50,show_tail="narr",show_xmax=800,show_retain=3)
    n "And, I can’t really say that I’m not curious. She did seem familiar, maybe we were friends in the past? Though, it’s weird that I don’t remember her. Selena isn’t exactly a common name in Japan, maybe she used a nickname or a middle name?" (200,300,show_tail="narr",show_xmax=630,show_retain=2)
    n "Then again, it’s been about a decade since middle school. People forget things all the time." (150,750,show_tail="narr",show_xmax=650,show_retain=1)
    n "The mystery of our prior meeting aside, we should probably finish packing these boxes. I can’t imagine she’ll be able to rent that truck forever." (320,1000,show_tail="narr",show_xmax=530)

    call nextpage
    hide Selena with dissolve
    n "Reaching into the pile, I picked up what looked like… an old camera? With the advent of digital cameras and phones, I don’t really see these a lot anymore." (40,20,show_tail="narr",show_xmax=650,show_retain=3)
    show camera with dissolve:
        xalign 0.35
        ypos 0.4
    n "Unfortunately I didn’t know enough about whether this was a professional camera used even today or at least a few years ago, or if it’s more of a vintage camera?" (500,500,show_tail="narr",show_xmax=470,show_retain=2)
    n "Not that there’s anything wrong with vintage gear, Old stuff can still be just as good or useful as top of the line-" (40,900,show_tail="narr",show_xmax=500,show_retain=1)
    s "Oh hey, I remember that! It’s Tsukuyomi!" (800,1100,show_tail="righttop",show_xmax=400)

    call nextpage
    hide camera with dissolve
    show Selena at middef
    b "Tsukuyomi?" (40,100,show_tail="leftbase",show_xmax=500,show_retain=3)
    s "Yeah, that’s the name of my camera. Well, that’s not the name of its model, I named it. Was really into this one show at the time where-" (420,300,show_tail="leftbase",show_xmax=460,show_retain=2)
    show Selena lookaway smug
    s "Nevermind!" (600,500,show_tail="lefttop",show_xmax=470,show_retain=1)
    n "She takes the old camera carefully in her hands, as if it were a precious treasure that could break if handled poorly." (40,1100,show_tail="narr",show_xmax=700)

    call nextpage
    show camera with dissolve:
        xalign 0.35
        ypos 0.4
    show Selena lookaway
    show Selena opensmile open
    s """When I started middle school, my dad came back from one of his business trips and gave me this.
        According to him, he won it by freeing a genie from a bottle under the pale moonlight in a game of chance.""" (350,300,show_tail="leftbase",show_xmax=620,show_retain=4)
    b "Really?" (-20,500,show_tail="leftbase",show_xmax=500,show_retain=3)
    show Selena lookaway smile
    s "No, he was obviously lying. I think he just saw it in a display window for a discount and bought it for cheap." (510,600,show_tail="lefttop",show_xmax=360,show_retain=2)
    show Selena open opensmile
    s "Ooh, the memory stick is still in here." (480,960,show_tail="lefttop",show_xmax=380,show_retain=1)
    n "She ushered me over to sit next to her to look into the imager… reader… thingy..." (20,1120,show_tail="narr",show_xmax=650) ## find Proper name?

    call nextpage
    show Selena midclose
    s "See here, my brother’s birthday." (500,300,show_tail="rightbase",show_xmax=500,show_retain=5)
    b "Why do you have him in a headlock?" (-25,700,show_tail="leftbase",show_xmax=500,show_retain=4)
    show Selena down smile
    s "Eh, when you grow up in a house of brothers, you learn to be tough or they snap the heads off all your dolls." (520,800,show_tail="leftbase",show_xmax=350,show_retain=3)
    b "Did that really happen?" (20,1000,show_tail="leftbase",show_xmax=500,show_retain=2)
    show Selena opensmile open
    s "Next pic!" (480,1050,show_tail="lefttop",show_xmax=500,show_retain=1)
    n "Wait no, seriously, did that actually happen?" (530,1200,show_tail="narr",show_xmax=400)

    call nextpage
    show Selena crying opensmile concerned
    s "Ooh, and here’s the dress I made for the school play!" (400,300,show_tail="baseright",show_xmax=350,show_retain=3)
    b "Oh hey, I think I remember that one. Yeah, the teachers let the students write the story because they were sick of putting on the same performance every year and wanted something new and fresh." (-10,930,show_tail="leftbase",show_xmax=350,show_retain=2)
    show Selena open squiggly horizontal
    s "Yeah! Though in retrospect, putting a bunch of hormonal pre-teens in charge of writing was… not the best idea." (500,800,show_tail="lefttop",show_xmax=370,show_retain=1)
    show Selena smile up
    s "At least the dresses were good." (520,1150,show_tail="lefttop",show_xmax=350)

    call nextpage
    show Selena open opensmile
    s "Next pic!" (320,420,show_tail="rightbase",show_xmax=380,show_retain=3)
    show Selena midclose openmouth
    s" Oh hey, this was from my High-school graduation trip. Huh, weird. Did I not use this camera for a while or something?" (400,600,show_tail="righttop",show_xmax=380,show_retain=2)
    b "Maybe you placed different photos on different memory sticks and left this one in the camera?" (900,900,show_tail="rightbase",show_xmax=420,show_retain=1)
    show Selena open frown
    s "I think so."(450,1000,show_tail="righttop",show_xmax=450,show_retain=0)
    show Selena midclose frown
    s" I wonder what else is{nw}{w=.5}" (320,300,show_tail="rightbase",show_xmax=400,show_retain=1)
    show Selena open openmouth
    extend " on he--{nw}{w=.5}"
    show Selena openmouth #embarrassed
    show CG6 at truecenter with Dissolve(0.3):
        alpha 1.0
        zoom 0.35
        pause 1.0
        linear 0.2 alpha 0.0
    hide camera with dissolve
    n "I saw a flash of pink and she immediately turned the camera away." (250,1150,show_tail="narr",show_xmax=650)
    # (This is not a lewd pic, it’s just a mirror selfie of herself trying on a new swimsuit)

    call nextpage
    b "Um…" (20,50,show_tail="lefttop",show_xmax=450,show_retain=8)
    show Selena crying squiggly blush
    s "......" (520,270,show_tail="leftbase",show_xmax=350,show_retain=7)
    b "Was that-" (40,450,show_tail="lefttop",show_xmax=450,show_retain=6)
    show Selena frown
    s "Did you see?" (560,650,show_tail="lefttop",show_xmax=300,show_retain=5)
    b "Well-" (20,850,show_tail="lefttop",show_xmax=450,show_retain=4)
    show Selena down
    s "Did. {p=0.2}You. {p=0.2}See?" (520,1050,show_tail="lefttop",show_xmax=350,show_retain=1)
    n "I saw everything." (420,1200,show_tail="narr",show_xmax=450)

    call nextpage
    b "Did I see what?" (20,50,show_tail="lefttop",show_xmax=350,show_retain=2)
    n "In this situation, it’s better to just lie." (570,300,show_tail="narr",show_xmax=300,show_retain=1)
    show Selena lookaway opensmile #new expression
    s "Oh hey! I think I left something in the other room! I’ll be right back!" (520,650,show_tail="lefttop",show_xmax=350)
    hide Selena with moveoutright
    b "Oh, well, alright. I’ll just put the rest of this stuff away then?" (50,950,show_tail="leftbase",show_xmax=650,show_retain=1)
    n "She pauses midway through the door frame, then quickly turns around." (220,1150,show_tail="narr",show_xmax=600)

    call nextpage
    show Selena at middef with moveinright:
        yalign 0.0
        xpos 1.0
        linear 3 xpos 0.9
    s "Actually, could you load the packed boxes into the moving truck?" (620,150,show_tail="rightbase",show_xmax=550,show_retain=3)
    n "That’s what she was saying, but what she actually meant was probably…" (120,450,show_tail="narr",show_xmax=450,show_retain=2)
    n "\"I think I might have some other embarrassing things in the pile, so can you take the boxes into the truck so I can quickly check and hide that stuff?\"" (120,850,show_tail="narr",show_xmax=650,show_retain=1)
    b "Uh, sure thing." (320, 1350,show_tail="leftbase",show_xmax=450)

    call nextpage
    show Selena closed smile#with close eye smile expresssion
    s "Thanks, you’ve been a real help. Hang on, lemme just get the key." (650,420,show_tail="rightbase",show_xmax=550,show_retain=2)
    n "......" (80,480,show_tail="narr",show_xmax=350,show_retain=1)
    n "Though I’ll never forget what I saw, I will take that knowledge to my grave." (100,700,show_tail="narr",show_xmax=520)


label Chapter2_3: ##Moving the stuff into the truck *
#     #- Canned drink from scene 1
#     #- Truck interior, it’s full of boxes *

    scene white with dissolve
    #play sound "dooropen.ogg"
    play sound "audio/sfx-dooropens.ogg" volume 0.25
    scene s_ext_truck with dissolve
#     # Note to self: "FInd the yearbook here"

    call nextpage
    n "And…{p=1.0} heave… {p=2.5}ho!" (70,40,show_tail="narr",show_xmax=650,show_retain=4)
    n "And with that last bit of exertion, the last box was in the truck." (80,320,show_tail="narr",show_xmax=550,show_retain=3)
    n "Well, sorta."(80,480,show_tail="narr",show_xmax=350,show_retain=2)
    n "She had sequestered herself in her room, carefully going over what was left herself." (140,860,show_tail="narr",show_xmax=650,show_retain=1)
    n "I guess she didn’t want me to see another example of <classified.> " (80,1080,show_tail="narr",show_xmax=450)

    call nextpage
    n "So, with nothing to do, I guess I’ll just… sit here, in the back of the truck." (90,80,show_tail="narr",show_xmax=650,show_retain=4)
    n "..." (270,280,show_tail="narr",show_xmax=650,show_retain=3)
    n "Pretty nice outside." (170,540,show_tail="narr",show_xmax=650,show_retain=2)
    n "Wonder if Ashley’s awake now? Is she worried about me? Maybe I should call?" (80,840,show_tail="narr",show_xmax=650,show_retain=1)
    btr "{cps=50}.  .  .  .  .{/cps}" (420,1330, show_tail="btr",show_xmax=800)

    call nextpage
    n "Wait, no, phone’s dead. Why didn’t I bring a charger?" (40,80,show_tail="narr",show_xmax=600,show_retain=3)
    n "What’s this in my pocket?" (80,280,show_tail="narr",show_xmax=600,show_retain=2)
    show can:
        zoom 0.5
        align (0.5, 0.5)
    n "It’s the drink Selena bought for me earlier? Guess I forgot to drink it." (470,840,show_tail="narr",show_xmax=400,show_retain=1)
    btr "{cps=50}.  .  .  .  .{/cps}" (420,1330, show_tail="btr",show_xmax=800)

    call nextpage
    n "Well, might as well." (240,80,show_tail="narr",show_xmax=600,show_retain=4)
    # (screenshake)
    hide can

    n "As soon as I open the can, it suddenly makes an unexpected noise, which causes me to jolt backwards. Causing me to tilt one of the boxes." (140,380,show_tail="narr",show_xmax=600,show_retain=3) with Shake((0, 0, 0, 0), 0.5, dist=10)
    n "Operating on instinct, I manage to catch the box just before the contents fell."(80,680,show_tail="narr",show_xmax=600,show_retain=2)
    n "That was close." (540,980,show_tail="narr",show_xmax=600,show_retain=1)
    n "Or at least, that’s what I thought, until I noticed the box was upside down, and some of the objects had already spilled out." (40,1130,show_tail="narr",show_xmax=600)

    call nextpage
    show Blake lookaway openmouth at middef:
        xpos 0.35
    b "Ah crap, better clean this up." (430,280,show_tail="leftbase",show_xmax=350,show_retain=3)
    show Blake midclose frown
    n "First I put the box right-side-up, next I started picking up the items that fell out: books." (480,450,show_tail="narr",show_xmax=380,show_retain=2)
    n "Printed on the books were years and artistically designed covers along with the names of schools. Obviously, yearbooks." (40,980,show_tail="narr",show_xmax=600,show_retain=1)
    btr "{cps=50}.  .  .  .  .{/cps}" (420,1330, show_tail="btr",show_xmax=800)

    call nextpage
    show Blake open frown
    n "I shouldn’t look, maybe it’s an invasion of privacy." (40,80,show_tail="narr",show_xmax=550,show_retain=4)
    n "I begin to put them back in the box when I see one of the books labeled {b}T.K.U.{/b} Middle School. It should be a pretty familiar book because I had the same one, though it’s back at my parent’s house." (400,350,show_tail="narr",show_xmax=550,show_retain=3)
    n "Oh yeah, we probably went to the same middle school." (440,680,show_tail="narr",show_xmax=550,show_retain=2)
    btr "{cps=50}.  .  .  .  .{/cps}" (360,1330, show_tail="btr",show_xmax=800)
    n "Come to think of it, she was curious about our school past, even tried looking for this specific yearbook." (140,930,show_tail="narr",show_xmax=590)

    call nextpage
    show screen yearbook
    show Blake lookaway
    n "Guess a quick peek won’t hurt." (640,80,show_tail="narr",show_xmax=230,show_retain=2)
    n "I dispense with the cautious approach, and immediately open up the yearbook." (440,350,show_tail="narr",show_xmax=390,show_retain=1)
    show Blake smile midclose
    b "Now let’s see... where am I…" (240,730,show_tail="narr",show_xmax=550)

    call nextpage
    #hide blake
    #show yearbook?
    show Blake closed
    n "It didn’t take long to find me. Class 2B, back corner row in the class photo." (40,120,show_tail="narr",show_xmax=550,show_retain=3)
    n "Heh, even in the past, I still had an introvert’s streak." (500,380,show_tail="narr",show_xmax=350,show_retain=2)
    n "I Guess the more things change, the more things stay the same." (420,760,show_tail="narr",show_xmax=550,show_retain=1)
    show Blake open frown

    n "Now, let’s stop wasting time. Where’s Selena?" (460,1000,show_tail="narr",show_xmax=450)

    call nextpage
    n "Looking into the class list yielded no results. No one named Selena in the bunch, and no one who looked like her." (60,50,show_tail="narr",show_xmax=750,show_retain=4)
    n "Guess she wasn’t in my class then?" (120,270,show_tail="narr",show_xmax=750,show_retain=3)
    n "A quick scan of the other class lists yielded no results either." (520,500,show_tail="narr",show_xmax=350,show_retain=2)
    n "Her name’s Selena, right? Was I spelling it wrong? Did she maybe go by a different name?" (40,920,show_tail="narr",show_xmax=550,show_retain=1)
    n "There’s gotta be a hint, some way to tell her apart..." (60,1140,show_tail="narr",show_xmax=750)

    call nextpage
    # hide yearbook
    hide screen yearbook
    scene flashback
    show screen black_border
    show neckerchief:
        zoom 0.4 yanchor 0.0
        ypos 1.0 xpos 0.2
        linear 0.2 ypos 0.3
    b "Hey, what’s this mark on the bottom here? On the tips?" (60,70,show_tail="lefttop",show_xmax=750,show_retain=1)
    s "\"Ah, I was going through my fashionista phase so I didn’t feel right wearing the same exact thing everyone else was wearing. So, I colored in the tips with some dye.\"" (860,1170,show_tail="rightbase",show_xmax=750)
    hide neckerchief
    hide screen black_border

    call nextpage
    scene s_ext_truck with dissolve
    #show yearbook
    b "Marks on the tips..." (-20,70,show_tail="lefttop",show_xmax=750,show_retain=2)
    n "I went back to my class, scanned for a girl with marked tips. Nothing." (60,470,show_tail="narr",show_xmax=750,show_retain=1)
    n "Next class… there she was!" (90,870,show_tail="narr",show_xmax=750)

    call nextpage

    # CG of young Selena in a class photo, no reason to draw the others, just zoom in on her, this could also function as a cut-in image
    show young_selena:
        yalign 0.60 xalign 0.5 yoffset 0 alpha 0.0 zoom 0.6
        ease .5 yoffset -80 alpha 1.0
    n "Just to be sure, I looked in the other class photos of all the girls in our year, she was the only one with dyed tips." (350,30,show_tail="narr",show_xmax=520,show_retain=3)
    n "Thank god I found her, because I really didn’t want to go looking through the other years or in other books." (-80,370,show_tail="narr",show_xmax=350,show_retain=2)
    n "Still, heck of a coincidence that I found the exact yearbook I needed." (320,930,show_tail="narr",show_xmax=550,show_retain=1)
    n "So that was young Selena, eh?" (560,1150,show_tail="narr",show_xmax=300)

    call nextpage
    nvl clear
    nv "Honestly, she looked pretty different from how she is now."
    nv "I think our school had a strict dress-code, where girls had to keep their hair a particular length, no makeup, no decorations of any sort. Boys had similar rules but it was mostly to keep our hair trimmed. I hated it."
    nv "Looks like Selena had a bit of a rebellious streak."
    nvl clear
    nv "While her uniform was fine at a glance, she found subtle ways to silently rebel against the dress code."
    nv "The dye-tipped neckerchief was just one part of it."
    nvl clear
    nvl hide
    hide young_selena
    call nextpage
    n "Huh." (50,50,show_tail="narr",show_xmax=650,show_retain=5)
    n "When I looked at this photo, I expected some memories to appear. But I guess it doesn’t just work the way it does in the movies, eh?" (150,250,show_tail="narr",show_xmax=650,show_retain=4)
    n "I didn’t feel nothing though." (150,500,show_tail="narr",show_xmax=650,show_retain=3)
    n "When I looked at her photo, I felt… sadness?" (150,750,show_tail="narr",show_xmax=650,show_retain=2)
    n "Something in my memories seemed to be stirring." (150,1000,show_tail="narr",show_xmax=650,show_retain=1)
    n "But what could it-"(450,1200,show_tail="narr",show_xmax=650)

    call nextpage
    c "Excuse me." (20,50,show_tail="lefttop",show_xmax=650,show_retain=5)
    b "Huh?" (150,200,show_tail="narr",show_xmax=650,show_retain=4)
    # hide yearbook
    # n "I poked my head out from above the book cover."
    n "..." (650,450,show_tail="narr",show_xmax=650,show_retain=3)
    n "Then I hastily scrambled to put it back in the box, not realizing until later that I didn’t need to do that." (150,600,show_tail="narr",show_xmax=600,show_retain=2)
    b "Ahem- uh, hello, hi, um, how’s it going? I mean…" (680,1050,show_tail="rightbase",show_xmax=450,show_retain=1)
    b "What can I do for you?"(680,1270,show_tail="rightbase",show_xmax=350)

    call nextpage
    show Blake frown at middef with dissolve
    c "Do you work for the movers?" (150,-20,show_tail="topleft",show_xmax=650,show_retain=5)
    b "No?" (270,290,show_tail="rightbase",show_xmax=650,show_retain=4)
    c "Do you know where Selena is?" (500,200,show_tail="topleft",show_xmax=430,show_retain=3)
    show Blake smile
    b "She’s inside doing-" (550,700,show_tail="lefttop",show_xmax=350,show_retain=2)
    play sound "audio/sfx-damage.ogg"
    y"{size=45}Crash!!{/size}"(40,720,show_tail="yell",show_xmax=450,show_retain=1) with Shake((0, 0, 0, 0), 0.5, dist=20)
    # playCRASHING SOUND
    show Blake midclose up
    b "-That." (550,790,show_tail="lefttop",show_xmax=350)

    call nextpage
    show Blake up smile open #new expression
    b "Do you need some help? I can go get her if you want." (340,300,show_tail="baseright",show_xmax=300,show_retain=3)
    c "No, what I really need is for this truck to be moved. I need to pull out my car, but I can’t." (910,220,show_tail="righttop",show_xmax=550,show_retain=2)
    show Blake:
        ease 0.5 xoffset -100
    b "Oh, yeah, of course, lemme just... um, pull the truck out of the driveway." (550,600,show_tail="lefttop",show_xmax=300,show_retain=1)
    n "I awkwardly stammered as I made my way to the front of the truck, hoping that this person wouldn’t know that I’ve never driven a truck before." (250,900,show_tail="narr",show_xmax=600)

    call nextpage
    scene s_ext_truck with dissolve
#     # Change scene to the truck instead of the back, no idea how to depict that though
    b "Alright, so, I just need to drive the truck to let you out?" (680,320,show_tail="rightbase",show_xmax=400,show_retain=3)
    c "...yes, that’s… exactly what I said." (40,700,show_tail="leftbase",show_xmax=650,show_retain=2)
    n "Don’t tell them you’ve never driven a car, let alone a truck." (80,900,show_tail="narr",show_xmax=650,show_retain=1)
    n "Maybe I should get Selena?" (250,1150,show_tail="narr",show_xmax=650)

    call nextpage
    scene sky_morning with dissolve
    n "The tapping of their foot impatiently on the ground was almost like a maxed-rank taunting spell." (20,50,show_tail="narr",show_xmax=650,show_retain=7)
    n "I’ll show you!" (250,270,show_tail="narr",show_xmax=650,show_retain=6)
    n "I’m just going to be moving the truck forward slightly. How hard can that be?" (20,420,show_tail="narr",show_xmax=350,show_retain=5)
    n "After hopping up to the driver’s seat, I put the key in the ignition… after fumbling with it." (450,650,show_tail="narr",show_xmax=430,show_retain=4)
    n "Then I turn the key, expecting to hear the engine or something turn on." (270,930,show_tail="narr",show_xmax=600,show_retain=3)
    n "Instead, there’s like this… stalling sound. And the car refuses to start." (30,1120,show_tail="narr",show_xmax=650,show_retain=2)
    #play sound "stalling.ogg"
    n "...{p}Crap." (690,1180,show_tail="narr",show_xmax=650)


label Chapter2_4: ##Vehicle troubles
#     #Setting: Selena apartment - exterior - daylight - next to the truck
    call nextpage
    scene s_ext_truck with fade
    show Blake frown at middef
    c "So, um.. do you know what you’re doing?" (-50,270,show_tail="leftbase",show_xmax=650,show_retain=2)
    b "Sorry, uh… looks like there might be a little problem." (320,720,show_tail="rightbase",show_xmax=350,show_retain=1)
    c "I see…" (-50,1100,show_tail="leftbase",show_xmax=650)

    call nextpage
    n "The neighbor pulls out their phone and swipes it on." (200,40,show_tail="narr",show_xmax=650,show_retain=4)
    c "Hm, well, I’m gonna go back inside and make some coffee. See ya." (-50,200,show_tail="lefttop",show_xmax=650,show_retain=3)
    n "And I was alone again."(50,700,show_tail="narr",show_xmax=650,show_retain=2)
    show Blake up lookaway
    b "Well, what’s wrong with it?" (500,850,show_tail="lefttop",show_xmax=350,show_retain=1)
    n "Honestly, I couldn’t even begin to figure out what was wrong with the truck. As I have no doubt mentioned before, I work with computers. Software, mostly. Those skills don’t exactly translate to vehicle maintenance." (150,1020,show_tail="narr",show_xmax=700)

    call nextpage
    n "How do I even determine the problem?" (30,110,show_tail="narr",show_xmax=650,show_retain=3)
    n "I just turn on the engine, it makes this weird noise." (570,350,show_tail="narr",show_xmax=300,show_retain=2)
    n "And then it just doesn’t turn on. What does that even mean?" (30,770,show_tail="narr",show_xmax=650,show_retain=1)
    b "Maybe the tires are flat?" (550,950,show_tail="topleft",show_xmax=380)

    call nextpage

    n "I quickly hop out of the car, and do a quick tire check… by kicking the tires to see if it feels like they’re out of air." (440,80,show_tail="narr",show_xmax=420,show_retain=4)
    n "Does that even make sense?" (50,480,show_tail="narr",show_xmax=650,show_retain=3)
    n "Upon confirming (ish) that the tires are fine, I move onto the next thing." (250,710,show_tail="narr",show_xmax=650,show_retain=2)
    show Blake open
    b "What if I didn’t turn the key right?" (50,1010,show_tail="narr",show_xmax=650,show_retain=1)
    #play sound stalling.ogg
    btr "{size=50}{cps=5}. . . . .{/cps}{/size}" (650,1330, show_tail="btr",show_xmax=800)

    call nextpage
    b "It felt wrong the moment it came out." (330,410,show_tail="rightbase",show_xmax=320,show_retain=3)
    b "Okay, if it’s a sound issue… let’s um, pop the hood?" (570,410,show_tail="leftbase",show_xmax=320,show_retain=2)
    n "....how do I pop the hood?" (50,760,show_tail="narr",show_xmax=650,show_retain=1)
    n "I thought it would be right next to the same place where I opened up the backdoor hatch thing, but that didn’t work." (200,960,show_tail="narr",show_xmax=650)

    call nextpage
    hide blake
    n "Hey wait, do I even need to do that? Maybe that’s just a bakckdoor thing?" (350,180,show_tail="narr",show_xmax=550,show_retain=3)
    n "What if I just tried opening the hood myself?" (50,410,show_tail="narr",show_xmax=650,show_retain=2)
    s "...honestly, this is a little embarrassing." (580,810,show_tail="righttop",show_xmax=650,show_retain=1)
    n "I was startled by Selena’s sudden presence." (500,1010,show_tail="narr",show_xmax=350)
    hide Blake
    call nextpage

    show Selena bounce at middef, bounce#pop up animation
    b "Oh, hey. Um, how’s it going?" (-50,120,show_tail="leftbase",show_xmax=400,show_retain=3)
    s """Well, I found a box set of one of my favorite series of all time hidden in the pile,
        so I was coming out here to get my spare laptop charger from the truck.""" (520,400,show_tail="leftbase",show_xmax=370,show_retain=2)
    show Selena stand midclose
    s "But then I saw you here and had to watch what you were doing and…" (550,520,show_tail="lefttop",show_xmax=320,show_retain=1)
    show Selena frown
    n "She looked at me with the same pity you’d show to a child playing basketball who didn’t even get close to sinking a shot in the hoop." (550,950,show_tail="narr",show_xmax=420)

    call nextpage
    b "{size=25}...I’m a software guy.{/size}" (-50,210,show_tail="leftbase",show_xmax=650,show_retain=4)
    n "I mumbled under my breath, mostly for my own ego more than anything." (50,310,show_tail="narr",show_xmax=300,show_retain=3)
    s "What was that?" (550,620,show_tail="lefttop",show_xmax=650,show_retain=2)
    b "Nothing." (50,750,show_tail="lefttop",show_xmax=650,show_retain=1)
    n "I just casually scooted over so Selena can get into the driver’s seat." (150,1010,show_tail="narr",show_xmax=650)

    call nextpage
    show Selena lookaway smile
    s "Oh, yeah, that shouldn’t be difficult to fix." (520,210,show_tail="baseleft",show_xmax=350,show_retain=3)
    b "You know how to fix cars?" (-50,340,show_tail="leftbase",show_xmax=400,show_retain=2)
    s "I grew up in a house with enough brothers to start my own baseball team, remember?" (540,510,show_tail="lefttop",show_xmax=330,show_retain=1)
    show Selena open down
    s "In that kind of household, you learn a few things here and there." (540,910,show_tail="lefttop",show_xmax=330)

    call nextpage
    show Selena horizontal#sigh expression
    s "I’m gonna head in the back and get my toolbox, in the meantime…" (500,280,show_tail="leftbase",show_xmax=350,show_retain=4)
    n "She produced a slip of paper and pressed it into my hand, along with a 50$ bill." (20,550,show_tail="narr",show_xmax=350,show_retain=3)
    show Selena up
    s "Remember that convenience store we passed on the way here?" (520,710,show_tail="lefttop",show_xmax=350,show_retain=2)
    show Selena lookaway smile
    s "While I fix the truck and help Rob, so they can go to their mistresses’ house, can you pick us up some snacks? You can buy some stuff for yourself as well and keep the change." (410,960,show_tail="lefttop",show_xmax=460,show_retain=1)
    b "Uh, sure." (20,1310,show_tail="leftbase",show_xmax=350)

    call nextpage
    show Selena bounce opensmile at bounce# new joyous expression at bounce
    s "Great, thanks! Oh, one more thing! If they have Helio-Zen in stock, can you pick me up some?" (350,250,show_tail="leftbase",show_xmax=550,show_retain=3)
    show Selena stand smile
    s "Actually, more than the snacks, I want that drink." (550,350,show_tail="lefttop",show_xmax=350,show_retain=2)
    s "They only sell them in that specific store." (520,650,show_tail="lefttop",show_xmax=350,show_retain=1)
    b "Okay, that seems doable." (50,950,show_tail="leftbase",show_xmax=550)

    b "Well, I’m off then." (20,150,show_tail="leftbase",show_xmax=550,show_retain=4)
    show Selena closed at middef with dissolve
    s "Take care, come back soon!" (500,250,show_tail="leftbase",show_xmax=350,show_retain=3)
    show Selena open opensmile
    s "Ah, after we’re done moving, if you want to stay and watch the series with me, I’d be happy to have you join me!" (550,650,show_tail="leftbase",show_xmax=320,show_retain=2)
    b "Well-" (50,600,show_tail="topleft",show_xmax=550,show_retain=1)
    show Selena closed at sway:
        yanchor 0.585 xanchor 0.5 ypos 1.0 xpos 0.5
    s "Okay, good luck! Bye!" (450,800,show_tail="lefttop",show_xmax=450)
    show black:
        alpha 0.5
    n "Barrier up."  (350,150,show_tail="narr",show_xmax=550,show_retain=3)
    n "She seems like the bossy type of person, sorta reminds me of someone in a way. I don’t hate that though." (200,650,show_tail="narr",show_xmax=550,show_retain=2)
    n "....."  (600,850,show_tail="narr",show_xmax=200,show_retain=1)
    n "Do I have a type?" (600,1000,show_tail="narr",show_xmax=250)


    return
