# The script of the game goes in this file.
init python:
    selena_outfit=""
# Declare characters used by this game. The color argument colorizes the
# name of the character..
# init python:
#     speaking = None
#     def while_speaking(name, speak_d, done_d, st, at):
#         if speaking == name:
#             return speak_d, .1
#         else:
#             return done_d, None
#
#     curried_while_speaking = renpy.curry(while_speaking)
#
#     def WhileSpeaking(name, speaking_d, done_d=Null()):
#         return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
#     def speaker_callback(name, event, **kwargs):
#         global speaking
#         if event == "begin":
#             speaking = name
#         elif (event == "slow_done" or event == "end"):
#             speaking = None
#     speaker = renpy.curry(speaker_callback)
# define bn = Character("Blake", callback=speaker("Blake"), screen ="bubble_say", show_tail=False)
# define sn = Character("Selena",callback=speaker("Selena") ,screen ="bubble_say")
# define an = Character("Ashley",callback=speaker("Ashley") ,screen ="bubble_say")
# define pn = Character("Pat",callback=speaker("Pat"), screen ="bubble_say")
# define b = Character("Blake", callback=speaker("Blake"))
# define s = Character("Selena",callback=speaker("Selena"))
# define a = Character("Ashley",callback=speaker("Ashley"))
# define p = Character("Pat",callback=speaker("Pat"))
image Ashley_eyes_blink:
    choice:
        "Characters/Ashley/Ashley_eyes.webp"
        pause 4.0
    choice:
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.1
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes.webp"
        pause 2.0
    choice:
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes.webp"
        pause 0.1
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes.webp"
        pause 2.0
    repeat
image Ashley_eyes_midclose:
    choice:
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 4.0
    choice:
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.1
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 2.0
    choice:
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_midclose.webp"
        pause 2.05
    repeat
image Ashley_eyes_lookaway:
    choice:
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 4.0
    choice:
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.1
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 2.0
    choice:
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 0.05
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_closed.webp"
        pause 0.07
        "Characters/Ashley/Ashley_eyes_lookaway.webp"
        pause 2.05
    repeat
image Ashley_mouth_frown_speaking:
    "Characters/Ashley/Ashley_mouth_open2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_open.webp"
    pause 0.1
    "Characters/Ashley/Ashley_mouth_open2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_frown.webp"
    pause 0.08
    repeat
image Ashley_mouth_smile_speaking:
    "Characters/Ashley/Ashley_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_opensmile.webp"
    pause 0.1
    "Characters/Ashley/Ashley_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_smile.webp"
    pause 0.1
    "Characters/Ashley/Ashley_mouth_open2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_open.webp"
    pause 0.1
    "Characters/Ashley/Ashley_mouth_open2.webp"
    pause 0.08
    "Characters/Ashley/Ashley_mouth_smile.webp"
    pause 0.08
    repeat

layeredimage Ashley:
    always:
        "Characters/Ashley/Ashley_base.webp"
    group eyes:
        attribute open default:
            "Ashley_eyes_blink"
        attribute oneclose:
            "Characters/Ashley/Ashley_eyes2.webp"
        attribute midclose:
            "Ashley_eyes_midclose"
        attribute lookaway:
            "Ashley_eyes_lookaway"
        attribute closed:
            "Characters/Ashley/Ashley_eyes_closed.webp"
    group eyebrows:
        attribute up default:
            "Characters/Ashley/Ashley_eyebrows_normal.webp"
        attribute concerned:
            "Characters/Ashley/Ashley_eyebrows_concerned.webp"

        attribute down:
            "Characters/Ashley/Ashley_eyebrows_angry.webp"

    group mouth:
        attribute frown:
            WhileSpeaking("Ashley","Ashley_mouth_frown_speaking","Characters/Ashley/Ashley_mouth_frown.webp")
        attribute openmouth:
            WhileSpeaking("Ashley","Ashley_mouth_frown_speaking","Characters/Ashley/Ashley_mouth_open.webp")
        attribute openmouth2:
            WhileSpeaking("Ashley","Ashley_mouth_frown_speaking","Characters/Ashley/Ashley_mouth_open2.webp")
        attribute smile default:
            WhileSpeaking("Ashley","Ashley_mouth_smile_speaking","Characters/Ashley/Ashley_mouth_smile.webp")
        attribute opensmile:
            WhileSpeaking("Ashley","Ashley_mouth_smile_speaking","Characters/Ashley/Ashley_mouth_opensmile.webp")
        attribute opensmile2:
            WhileSpeaking("Ashley","Ashley_mouth_smile_speaking","Characters/Ashley/Ashley_mouth_opensmile2.webp")

image Selena_eyes_blink:
    choice:
        "Characters/Selena/Selena_eyes.webp"
        pause 4.0
    choice:
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes.webp"
        pause 2.0
    choice:
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes.webp"
        pause 2.0
    repeat
image Selena_eyes_crying:
    choice:
        "Characters/Selena/Selena_eyes_crying.webp"
        pause 4.0
    choice:
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_crying.webp"
        pause 2.0
    choice:
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_crying.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_crying_midclose.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_crying.webp"
        pause 2.0
    repeat
image Selena_eyes_midclose:
    choice:
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 4.0
    choice:
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.2
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 2.0
    choice:
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_midclose.webp"
        pause 2.05

    repeat
image Selena_eyes_lookaway:
    choice:
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 8.0
    choice:
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.1
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 3.0

    choice:
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 0.05
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_closed.webp"
        pause 0.07
        "Characters/Selena/Selena_eyes_lookaway.webp"
        pause 3.0

    repeat
image Selena_mouth_frown_speaking:
    "Characters/Selena/Selena_mouth_open2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_open.webp"
    pause 0.1
    "Characters/Selena/Selena_mouth_open2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_frown.webp"
    pause 0.08
    repeat
image Selena_mouth_smile_speaking:
    "Characters/Selena/Selena_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_opensmile.webp"
    pause 0.1
    "Characters/Selena/Selena_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_smile.webp"
    pause 0.1
    "Characters/Selena/Selena_mouth_open2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_open.webp"
    pause 0.1
    "Characters/Selena/Selena_mouth_open2.webp"
    pause 0.08
    "Characters/Selena/Selena_mouth_smile.webp"
    pause 0.08
    repeat
layeredimage Selena:
    always:
        "Characters/Selena/Selena_base_[selena_outfit].png"
    group eyes:
        attribute open default:
            "Selena_eyes_blink"
        attribute oneclose:
            "Characters/Selena/Selena_eyes2.webp"
        attribute midclose:
            "Selena_eyes_midclose"
        attribute closed:
            "Characters/Selena/Selena_eyes_closed.webp"
        attribute lookaway:
            "Selena_eyes_lookaway"
        attribute crying:
            "Selena_eyes_crying"
    group eyebrows:
        attribute up default:
            "Characters/Selena/Selena_eyebrows_up.webp"
        attribute concerned:
            "Characters/Selena/Selena_eyebrows_concerned.webp"
        attribute down:
            "Characters/Selena/Selena_eyebrows_angry.webp"
        attribute horizontal:
            "Characters/Selena/Selena_eyebrows_horizontal.webp"
    group mouth:
        attribute frown:
            WhileSpeaking("Selena","Selena_mouth_frown_speaking","Characters/Selena/Selena_mouth_frown.webp")
        attribute squiggly:
            WhileSpeaking("Selena","Selena_mouth_frown_speaking","Characters/Selena/Selena_mouth_squiggly.webp")
        attribute smile default:
            WhileSpeaking("Selena","Selena_mouth_smile_speaking","Characters/Selena/Selena_mouth_smile.webp")
        attribute openmouth:
            WhileSpeaking("Selena","Selena_mouth_frown_speaking","Characters/Selena/Selena_mouth_open.webp")
        attribute opensmile:
            WhileSpeaking("Selena","Selena_mouth_smile_speaking","Characters/Selena/Selena_mouth_opensmile.webp")
        attribute smug:
            WhileSpeaking("Selena","Selena_mouth_smile_speaking","Characters/Selena/Selena_mouth_smug.webp")
    group blush:
        attribute noblush default:
            Null()
        attribute blush:
            "Characters/Selena/Selena_blush.png"
            alpha 0.7
image Pat_eyes_blink:
    choice:
        "Characters/Pat/Pat_eyes.webp"
        pause 4.0
    choice:
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.1
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes.webp"
        pause 2.0
    choice:
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.05
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.05
        "Characters/Pat/Pat_eyes.webp"
        pause 0.1
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.05
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.05
        "Characters/Pat/Pat_eyes.webp"
        pause 2.0
    repeat
image Pat_eyes_midclose:
    choice:
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 4.0
    choice:
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.2
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 2.0
    choice:
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.05
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_closed.webp"
        pause 0.07
        "Characters/Pat/Pat_eyes_midclose.webp"
        pause 2.05

    repeat
# image Pat_eyes_lookaway:
#     choice:
#         "Pat_eyes_lookaway.webp"
#         pause 4.0
#     choice:
#         "Pat_eyes_lookaway.webp"
#         pause 0.07
#         "Pat_eyes_closed.webp"
#         pause 0.1
#         "Pat_eyes_lookaway.webp"
#         pause 2.1
#
#     choice:
#         "Pat_eyes_lookaway.webp"
#         pause 0.05
#         "Pat_eyes_closed.webp"
#         pause 0.07
#         "Pat_eyes_lookaway.webp"
#         pause 0.07
#         "Pat_eyes_closed.webp"
#         pause 0.07
#         "Pat_eyes_lookaway.webp"
#         pause 2.05
#
#     repeat
image Pat_mouth_frown_speaking:
    "Characters/Pat/Pat_mouth_open2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_open.webp"
    pause 0.1
    "Characters/Pat/Pat_mouth_open2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_frown.webp"
    pause 0.08
    repeat
image Pat_mouth_smile_speaking:
    "Characters/Pat/Pat_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_opensmile.webp"
    pause 0.1
    "Characters/Pat/Pat_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_smile.webp"
    pause 0.1
    "Characters/Pat/Pat_mouth_open2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_open.webp"
    pause 0.1
    "Characters/Pat/Pat_mouth_open2.webp"
    pause 0.08
    "Characters/Pat/Pat_mouth_smile.webp"
    pause 0.08
    repeat
layeredimage Pat:
    always:
        "Characters/Pat/Pat_base.webp"
    group eyes:
        attribute open default:
            "Pat_eyes_blink"
        attribute oneclose:
            "Characters/Pat/Pat_eyes2.webp"
        attribute midclose:
            "Pat_eyes_midclose"
        attribute closed:
            "Characters/Pat/Pat_eyes_closed.webp"
        # attribute lookaway:
        #     "Pat_eyes_lookaway"
    group eyebrows:
        attribute normal default:
            "Characters/Pat/Pat_eyebrows_normal.webp"
        attribute down:
            "Characters/Pat/Pat_eyebrows_angry.webp"
        attribute up:
            "Characters/Pat/Pat_eyebrows_up.webp"
    group mouth:
        attribute frown:
            WhileSpeaking("Pat","Pat_mouth_frown_speaking","Characters/Pat/Pat_mouth_frown.webp")
        attribute openmouth:
            WhileSpeaking("Pat","Pat_mouth_frown_speaking","Characters/Pat/Pat_mouth_open2.webp")
        attribute openmouth2:
            WhileSpeaking("Pat","Pat_mouth_frown_speaking","Characters/Pat/Pat_mouth_open.webp")
        attribute opensmile:
            WhileSpeaking("Pat","Pat_mouth_smile_speaking","Characters/Pat/Pat_mouth_opensmile.webp")

        attribute smile default:
            WhileSpeaking("Pat","Pat_mouth_smile_speaking","Characters/Pat/Pat_mouth_smile.webp")
    zoom 0.95
image Blake_eyes_blink:
    choice:
        "Characters/Blake/Blake_eyes.webp"
        pause 4.0
    choice:
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.1
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes.webp"
        pause 2.0
    choice:
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes.webp"
        pause 0.1
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes.webp"
        pause 2.0
    repeat
image Blake_eyes_midclose:
    choice:
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 4.0
    choice:
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.2
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 2.0
    choice:
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_midclose.webp"
        pause 2.05

    repeat
image Blake_eyes_lookaway:
    choice:
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 4.0
    choice:
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.2
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 2.0
    choice:
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 0.05
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_closed.webp"
        pause 0.07
        "Characters/Blake/Blake_eyes_lookaway.webp"
        pause 2.05

    repeat
image Blake_mouth_frown_speaking:
    "Characters/Blake/Blake_mouth_open2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_open.webp"
    pause 0.1
    "Characters/Blake/Blake_mouth_open2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_frown.webp"
    pause 0.08
    repeat
image Blake_mouth_smile_speaking:
    "Characters/Blake/Blake_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_opensmile.webp"
    pause 0.1
    "Characters/Blake/Blake_mouth_opensmile2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_smile.webp"
    pause 0.1
    "Characters/Blake/Blake_mouth_open2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_open.webp"
    pause 0.1
    "Characters/Blake/Blake_mouth_open2.webp"
    pause 0.08
    "Characters/Blake/Blake_mouth_smile.webp"
    pause 0.08
    repeat
image side Blake_side:
    LiveCrop((200,0, 550,800), "Blake")
    zoom 0.4

layeredimage Blake:
    always:
        "Characters/Blake/Blake_base.webp"
    group eyes:
        attribute open default:
            "Blake_eyes_blink"
        attribute oneclose:
            "Characters/Blake/Blake_eyes2.webp"
        attribute midclose:
            "Blake_eyes_midclose"
        attribute closed:
            "Characters/Blake/Blake_eyes_closed.webp"
        attribute lookaway:
            "Blake_eyes_lookaway"

    group eyebrows:
        attribute down default:
            "Characters/Blake/Blake_eyebrows_normal.webp"

        attribute up:
            "Characters/Blake/Blake_eyebrows_up.webp"

    group mouth:
        attribute frown:
            WhileSpeaking("Blake","Blake_mouth_frown_speaking","Characters/Blake/Blake_mouth_frown.webp")
        attribute openmouth:
            WhileSpeaking("Blake","Blake_mouth_frown_speaking","Characters/Blake/Blake_mouth_open.webp")

        attribute smile default:
            WhileSpeaking("Blake","Blake_mouth_smile_speaking","Characters/Blake/Blake_mouth_smile.webp")
        attribute opensmile:
            WhileSpeaking("Blake","Blake_mouth_smile_speaking","Characters/Blake/Blake_mouth_opensmile.webp")
image Marie_eyes_blink:
    choice:
        "Marie/Marie_eyes.png"
        pause 4.0
    choice:
        "Marie/Marie_eyes_midclose.png"
        pause 0.07
        "Marie/Marie_eyes_closed.png"
        pause 0.1
        "Marie/Marie_eyes_midclose.png"
        pause 0.07
        "Marie/Marie_eyes.png"
        pause 2.0
    choice:
        "Marie/Marie_eyes_midclose.png"
        pause 0.05
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_midclose.png"
        pause 0.05
        "Marie/Marie_eyes.png"
        pause 0.1
        "Marie/Marie_eyes_midclose.png"
        pause 0.05
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_midclose.png"
        pause 0.05
        "Marie/Marie_eyes.png"
        pause 2.0
    repeat
image Marie_eyes_midclose:
    choice:
        "Marie/Marie_eyes_midclose.png"
        pause 4.0
    choice:
        "Marie/Marie_eyes_midclose.png"
        pause 0.07
        "Marie/Marie_eyes_closed.png"
        pause 0.1
        "Marie/Marie_eyes_midclose.png"
        pause 0.07
        "Marie/Marie_eyes_midclose.png"
        pause 2.0
    choice:
        "Marie/Marie_eyes_midclose.png"
        pause 0.05
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_midclose.png"
        pause 0.07
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_midclose.png"
        pause 2.05
    repeat
image Marie_eyes_lookaway:
    choice:
        "Marie/Marie_eyes_lookaway.png"
        pause 4.0
    choice:
        "Marie/Marie_eyes_lookaway.png"
        pause 0.07
        "Marie/Marie_eyes_closed.png"
        pause 0.1
        "Marie/Marie_eyes_lookaway.png"
        pause 0.07
        "Marie/Marie_eyes_lookaway.png"
        pause 2.0
    choice:
        "Marie/Marie_eyes_lookaway.png"
        pause 0.05
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_lookaway.png"
        pause 0.07
        "Marie/Marie_eyes_closed.png"
        pause 0.07
        "Marie/Marie_eyes_lookaway.png"
        pause 2.05
    repeat
image Marie_mouth_frown_speaking:
    "Marie/Marie_mouth_open2.png"
    pause 0.08
    "Marie/Marie_mouth_open.png"
    pause 0.1
    "Marie/Marie_mouth_open2.png"
    pause 0.08
    "Marie/Marie_mouth_frown.png"
    pause 0.08
    repeat
image Marie_mouth_smile_speaking:
    "Marie/Marie_mouth_opensmile2.png"
    pause 0.08
    "Marie/Marie_mouth_opensmile.png"
    pause 0.1
    "Marie/Marie_mouth_opensmile2.png"
    pause 0.08
    "Marie/Marie_mouth_smile.png"
    pause 0.1
    "Marie/Marie_mouth_open2.png"
    pause 0.08
    "Marie/Marie_mouth_open.png"
    pause 0.1
    "Marie/Marie_mouth_open2.png"
    pause 0.08
    "Marie/Marie_mouth_smile.png"
    pause 0.08
    repeat

layeredimage Marie:
    always:
        "Marie/Marie_base.png"
    group eyes:
        attribute open default:
            "Marie_eyes_blink"
        attribute oneclose:
            "Marie/Marie_eyes2.png"
        attribute midclose:
            "Marie_eyes_midclose"
        attribute lookaway:
            "Marie_eyes_lookaway"
        attribute closed:
            "Marie/Marie_eyes_closed.png"
    always:
        "Marie/Marie_glasses.png"
    group eyebrows:
        attribute up default:
            "Marie/Marie_eyebrows_normal.png"
        attribute concerned:
            "Marie/Marie_eyebrows_concerned.png"

        attribute down:
            "Marie/Marie_eyebrows_angry.png"

    group mouth:
        attribute frown:
            WhileSpeaking("Marie","Marie_mouth_frown_speaking","Marie/Marie_mouth_frown.png")
        attribute openmouth:
            WhileSpeaking("Marie","Marie_mouth_frown_speaking","Marie/Marie_mouth_open.png")
        attribute open3:
            WhileSpeaking("Marie","Marie_mouth_frown_speaking","Marie/Marie_mouth_open3.png")
        attribute smile default:
            WhileSpeaking("Marie","Marie_mouth_smile_speaking","Marie/Marie_mouth_smile.png")
    zoom 0.98
