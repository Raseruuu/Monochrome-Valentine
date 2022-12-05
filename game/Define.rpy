init python:
    speaking = None
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
    curried_while_speaking = renpy.curry(while_speaking)

    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "begin" or event == "show":
            speaking = name
        elif (event == "slow_done" or event == "end"):
            speaking = None
    speaker = renpy.curry(speaker_callback)
## Shake the Screen by adding.. with Shake((0, 0, 0, 0), 0.5, dist=20)
init python:
    bedtime=""
    import math
    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)
transform sway:
    transform_anchor True
    linear 0.25 rotate 5
    linear 0.5 rotate -5
    linear 0.20 rotate 1
    linear 0.05 rotate 0

## Character Define ##
define bt = Character(None,
            what_style="btext_what",
            window_style="btext_window")

define nv = nvl_narrator
define n = Character(None, screen ="bubble_say", show_tail="narr",what_text_align=0.5)
define y = Character(None, screen ="bubble_say", show_tail="yell",what_text_align=0.5)

#ADV
define aa = Character("Ashley",
            callback=speaker("Ashley"),
            image="Ashley_side"
            )
define pa = Character("Pat",
            callback=speaker("Pat"))

define b = Character("Blake",
            callback=speaker("Blake"),
            screen ="bubble_say",
            what_text_align=0.5
            )
define a = Character("Ashley",
            callback=speaker("Ashley"),
            screen ="bubble_say",
            what_text_align=0.5
            )
define s = Character("Selena",
            callback=speaker("Selena"),
            screen ="bubble_say",
            what_text_align=0.5)
define p = Character("Pat",
            callback=speaker("Pat"),
            screen ="bubble_say",
            what_text_align=0.5)
define c1 = Character("Co-worker1",
            callback=speaker("Co-worker1"),
            screen ="bubble_say",
            what_text_align=0.5)
define c2 = Character("Co-worker2",
            callback=speaker("Co-worker2"),
            screen ="bubble_say",
            what_text_align=0.5)
define c3 = Character("Co-worker3",
            callback=speaker("Co-worker3"),
            screen ="bubble_say",
            what_text_align=0.5)
define m = Character("Marie",
            callback=speaker("Marie"),
            screen ="bubble_say",
            what_text_align=0.5)
define btr = Character(None,
            screen ="bubble_say", show_tail="btr")

############################################################
####             IMAGES                                 ####
############################################################

## BG Definition ########################################
image city = "images/bg/city.webp"
image city2 = "images/bg/city2.webp"
image sky_bright = "images/bg/Sky_bright.webp"
image street = "street_by_konett"
image park = "images/bg/park.webp"
image park2 = "images/bg/park2.webp"
# image


image white = "#fff"
image grey = "#808080"
image black = "#000"
image flashback = "images/bg/flashback.webp"
image blackborder = im.MatrixColor("gui/mborder.webp", im.matrix.brightness(-1))

image p_tr_white = "toprightpanel_white"
image p_tr_page = "toprightpanel_page"
image p_tr_solo = "toprightpanel_solo"

#####     CG     #####
image CG1 = "images/CG/CG1.webp"
image CG2 = "images/CG/CG2.webp"
image CG3 = "images/CG/CG3.webp"
image CG4 = "images/CG/CG4.webp"


#####     Cut-in     #####
image memento = "images/cg/Memento_Ring.webp"
image can = "images/cg/Helios_Can.webp"
#MOVE ALL CUTINS HERE
## Transforms ##############################################
transform slidebottom:
    yanchor 0.0
    ypos 1.0
    ease 0.3 ypos 0.4
transform alpha05:
    alpha 0.4

transform vflip:
    yzoom -1.0
transform hflip:
    xzoom -1.0

transform shadow(child): #all black
        im.MatrixColor(Image(child), im.matrix.brightness(-1))

transform cutup(child): #x,y,width,height
        im.Crop(Image(child), (0,0,2200,2000))
        zoom 0.17

transform bounce:
    yoffset 0
    linear 0.1 yoffset -100
    linear 0.1 yoffset 0
image blake_head = "blake frown"
############################################################
####               LOCATION                             ####
############################################################
transform middef:
    yanchor 0.0 ypos 0.15 xalign 0.5 zoom 0.7

transform starein:
    zoom 1.2
    yalign 0.65





###    MISC    ###
image cityblur:
        contains:
            "city"
            alpha 0.5 xoffset -3
        contains:
            "city"
            alpha 0.5 xoffset +3
        contains:
            "city"
            alpha 0.5 yoffset -3
        contains:
            "city"
            alpha 0.5 yoffset +3
