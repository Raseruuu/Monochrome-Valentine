# screen gallery():
#     tag menu
#     frame:
#         imagebutton idle ".png"
transform halfsize:
    zoom 0.5

transform cg2size:
    zoom 0.4243

init python:

    g_cg = Gallery()
    g_bg = Gallery()

    # Backgrounds for the BG Gallery
    g_cg.button("CG1")
    g_cg.unlock_image("cg1")


    g_cg.button("CG2")
    g_cg.unlock_image("cg2")

    g_cg.button("CG3")
    g_cg.unlock_image("cg3")

    g_cg.button("CG4")
    g_cg.unlock_image("cg4")

    g_cg.button("CG5")
    g_cg.unlock_image("cg5")

    g_cg.button("CG6")
    g_cg.unlock_image("cg6")

    g_cg.button("CG7")
    g_cg.unlock_image("cg7")

    g_cg.button("CG8")
    g_cg.unlock_image("cg8")



screen bg_gallery():

    tag menu

    ## This use statement includes the extra_frame screen inside this one.
    # use extra_frame(_("Background Gallery")):

    #     grid 1 3:

    #         xfill True
    #         yfill True

    #         ## Call make_button to show a particular button.
    #         # add g_bg.make_button("background", "bg_button")

    #         add g_cg.make_button("room", "room_button", xalign=0.5, yalign=0.5)
    #         add g_bg.make_button("office", "office_button", xalign=0.5, yalign=0.5)
    #         add g_bg.make_button("beach", "beach_button", xalign=0.5, yalign=0.5)


screen extra_menu():
    tag menu

    add gui.game_menu_background

    # hbox:
    #     ysize 40
    #     xpos 75
    #     ypos 75
    #     imagebutton auto "gui/Icons/back-button_%s.png" xanchor 0.0 yanchor 0.5 yalign 0.5 action Return() alt _("Back")
    #     null width 55
    #     label _("Extras") xanchor 0.0 yanchor 0.5 yalign 0.5 text_font persistent.pref_text_font text_size 50 yoffset 5 text_color "#fff"

    vbox:
        spacing 20
        xpos 189 xanchor 0.0 ypos 203
        button:
            xsize 351 ysize 760
            background im.Grayscale("gui/Extras/Artworks.png")
            hover_background "gui/Extras/Artworks.png"
            text "{noalt}Artworks{/noalt}" ypos 710:
                style "Extras_text_button"
            action ShowMenu("Gallery")
            alt _("Artworks")
        button:
            xsize 351 ysize 760
            background im.Grayscale("gui/Extras/Soundtrack.png")
            hover_background "gui/Extras/Soundtrack.png"
            text "{noalt}Soundtrack{/noalt}" ypos 710:
                style "Extras_text_button"
            action ShowMenu("Soundtrack")
            alt _("Soundtrack")
        button:
            xsize 351 ysize 760
            background im.Grayscale("gui/Extras/Characters.png")
            hover_background "gui/Extras/Characters.png"
            text "{noalt}Characters{/noalt}" ypos 710:
                style "Extras_text_button"
            action ShowMenu("Characters")
            alt _("Characters")
        button:
            xsize 351 ysize 760
            background im.Grayscale("gui/Extras/Endings.png")
            hover_background "gui/Extras/Endings.png"
            text "{noalt}Endings{/noalt}" ypos 710:
                style "Extras_text_button"
            action ShowMenu("Endings")
            alt _("Endings")
    ## extra screen buttons go here: cg gallery, music room, endings, sprite viewer
screen Gallery():
    tag menu
    use extra_frame("Gallery"):
        # viewport:
        #     xpos 162 ypos 230
        #     scrollbars "horizontal"
        #     draggable True
        #     mousewheel True
        #     pagekeys True

            vpgrid:
                xpos 140 ypos 230
                xmaximum 1652
                cols 4
                spacing 20
                scrollbars "horizontal"

                draggable True
                mousewheel "horizontal"
                pagekeys True

                # if
                # add "images/CG/CG_1/cg_1_a.jpg" at resize(0.13)
                add g_cg.make_button("CG1", unlocked="cg1_a",locked= "cglock_button", xalign=0.5, yalign=0.5) xsize 538 ysize 302
                add g_cg.make_button("CG2", "cg2_a", xalign=0.5, yalign=0.5) xsize 538 ysize 302
                add g_cg.make_button("CG3", unlocked="cg3", xalign=0.5, yalign=0.5)  xsize 538 ysize 302
                # add "images/CG/CG_1/cg_1_a.jpg" at resize(0.13)


                add g_cg.make_button("CG4", "cg4", xalign=0.5, yalign=0.5)  xsize 538 ysize 302

                add g_cg.make_button("CG5", "cg5_a", xalign=0.5, yalign=0.5)  xsize 538 ysize 302
                add g_cg.make_button("CG6", "cg6_a", xalign=0.5, yalign=0.5)  xsize 538 ysize 302


                add g_cg.make_button("CG7", "cg7_a", xalign=0.5, yalign=0.5)  xsize 538 ysize 302
                add g_cg.make_button("CG8", "cg8_a", xalign=0.5, yalign=0.5)  xsize 538 ysize 302
            # # add g_cg.make_button("CG3", "cg_9_a", xalign=0.5, yalign=0.5) at resize(0.13)
            # null width 538 height 302
init python:
    character_list={
        "blake":["Blake N Lawrence","-"],
        "ashley":["Ashley Santiago","-"],
        "selena":["Selena ","-"],
        "pat":["Patrick","-"]}
    character_list2 = ["blake","ashley","selena","pat"]


default current_character="blake"
screen Characters():
    tag menu
    use extra_frame("Characters"):

        add "[current_character]" xpos 700 ypos 1.0 yanchor 1.0 at resize(0.35)
    vbox:
        xpos 172 ypos 230
        text character_list[current_character][0]:
            style "char_name_text"
        null height 30
        frame:
            background Null()
            xmaximum 500
            text character_list[current_character][1]
    grid 2 2:
        xpos 1470 ypos 297
        for character in character_list2:
            button:
                add "gui/Extras/[character]_icon.png" at resize(0.18)
                hover_foreground "gui/Extras/character_sprite_selected_border.png"
                action SetScreenVariable("current_character",character)
                alt character + _(" button")

## Extras frame screen ############################################################
##
## This is the same as the menu frame screen, but just for the extra menus

screen extra_frame(title):

    add gui.game_menu_background
    # hbox:
    #     ysize 40
    #     xpos 75
    #     ypos 75
    #     imagebutton auto "gui/Icons/back-button_%s.png" xanchor 0.0 yanchor 0.5 yalign 0.5 action ShowMenu("extra_menu") alt _("Back")
    #     null width 55
    #     label title xanchor 0.0 yanchor 0.5 yalign 0.5 text_font persistent.pref_text_font text_size 50 yoffset 5 text_color "#fff"

    vbox:
        transclude