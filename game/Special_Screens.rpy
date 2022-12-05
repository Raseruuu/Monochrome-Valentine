## Manga border ###########################
screen manga_border():
    zorder 100
    add "gui/mborder.webp"

screen black_border():
    zorder 110 #so to cover the existing border
    add "white" at alpha05
    add "blackborder"

# screen button_overlay():
#     zorder 150
#     # mousearea:
#     #     area (400, 0, 680, 100)
#     #     if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
#     #         hovered Show("navigation", transition=wipedown)
#     #         unhovered Hide("navigation", transition=dissolve)
#     if renpy.variant("small"):
#         use navigation


init python:
     config.overlay_screens.append("manga_border")
     config.overlay_screens.append("navigation")
default manga_border = True
default button_overlay = True

## CG
screen CG_1():
    zorder 120
    add "CG1"


## Page Number ############################
init -1 python:
    pagenum=0
    convo_y=0
label nextpage:
    $ pagenum+=1
    show screen pageno(str(pagenum))
    $ convo_y=150
    return

screen pageno(text):
    zorder 130
    frame id "pageno":
        xalign 0.965
        yalign 0.98
        if renpy.get_screen("black_border"):
            style "pgtextw"
        else:
            style "pgtext"
        text text size 35

style pgtext:
    background None

style pgtextw:
    background None
style pgtext_text:
    color "#000"
style pgtextw_text:
    color "#FFFFFF"


## MISC ######################################
screen panel_1():
    # use panel_tr_white
    # frame:
    #     add "calem":
    #         pos (329,100)
    #         xmaximum 657
    #         ymaximum 429
    use panel_tr_page

screen panel_tr_white():
    zorder 90
    add "p_tr_white"

screen panel_tr_page():
    zorder 101
    add "gui/SpeechBubbles_UI/toprightpanel_page.webp"

screen chap(num, text):
    zorder 140
    add "black"
    frame:
        background None
        xalign 1.0 yalign 0.5
        vbox:
            text "Chapter [num]" size 120 color "#808080" xalign 1.0
            null height 25
            text text size 50 color "#808080" xalign 0.8
    key "dismiss" action Return()

screen middlespeechbubble(text):
    frame:
        xalign 0.5 yalign 0.5
        text text xalign 0.5 yalign 0.5
    key "dismiss" action Return()

screen bottomtext(text):
    zorder 150
    frame id "outertext":
        style "btext"
        text text color "#000" size 30
    key "dismiss" action Return()
style btext:
    background None
    xanchor 0.0
    yanchor 0.0
    xpos 0.1
    ypos 0.95








## discarded main menu screen ############
    # frame:
    #     at mm_boxmove
    #     style "mm_box"
    #     hbox:
    #         xalign 0.4
    #         yalign 0.5
    #         spacing 100
    #         textbutton _("New") action Start() style "mm_tb" at mm_tb_move(0.6)
    #         textbutton _("Load") action ShowMenu("load") style "mm_tb" at mm_tb_move(0.8)
    #         textbutton _("Options") action ShowMenu("preferences") style "mm_tb" at mm_tb_move(1)
