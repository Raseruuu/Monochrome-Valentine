# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character..

screen middlespeechbubble(text):
    frame:
        xalign 0.5 yalign 0.5
        add Text(text, slow_cps=60) xalign 0.5 yalign 0.5
    key "dismiss" action Return()
label centersay(text):
    # hide window
    call screen middlespeechbubble(text)
    return
init python:
    persistent.read_prologue=False
    persistent.read_Chapter1=False
    persistent.read_Chapter2=False
    persistent.read_Chapter3=False
    persistent.read_Chapter4=False
    persistent.read_Chapter5=False
    persistent.read_Epilogue=False
# The game starts here.
label chapterselect:
    menu:
        # n"Select A Chapter." (50,650,show_tail="narr",show_xmax=800)
        "{color=000}Prologue":
            jump prologue
        "{color=000}Chapter1 : Encounter" if persistent.read_Chapter1:
            jump chapter1
        "{color=000}Chapter2 : Request" if persistent.read_Chapter2:
            jump chapter2_1
        "{color=000}Chapter3 : Stranger" if persistent.read_Chapter3:
            jump chapter3_1
        "{color=000}Chapter4: " if persistent.read_Chapter4:
            jump Chapter_4
        "{color=000}Chapter5: " if persistent.read_Chapter5:
            jump chapter5_1
        "{color=000}Credits: ":
            jump credits

        "{color=000}Epilogue: " if persistent.read_Epilogue:
            jump chapter5_4
        "{color=000}Back":
            pass
    return



label start:
    label startchapterp:
        call prologue
    $ persistent.read_prologue=True
    label startchapter1:
        $ pagenum = 7
        call chapter1
    $ persistent.read_Chapter1=True
    label startchapter2:
        call chapter2_1
    $ persistent.read_Chapter2=True
    label startchapter3:
        $ pagenum = 120
        call chapter3_1
        $ persistent.read_Chapter3=True
    label startchapter4:
        call Chapter_4
        $ persistent.read_Chapter4=True
    label startchapter5:
        call chapter5_1
        $ persistent.read_Chapter5=True
    call credits
    label startchaptere:
        call chapter5_4
        $persistent.read_Epilogue=True
    call credits
    # This ends the game.

    return
image mvlogo = "gui/MVLogo.png"

label credits:
    $ convo_y=10
    play music "audio/Sweet_bgm_maoudamashii_piano34.ogg"

    scene flashback
    show mvlogo at truecenter with dissolve

    pause
    hide mvlogo with dissolve
    n"{size=40}{b}Monochrome Valentine{/b}{/size}"(100,convo_ypos(20),show_tail="narr",show_xmax=900,show_retain=1)
    # show
    n"""{cps=0}Made in Ren'Py Visual Novel Engine
            \n\n{b}A submission to Valentine's Game Jam 2021{/b}
            \n\n{b}Credits:{/b}
            \n\n  {b}{u}Raseruuu{/b}{/u}\n Lead Dev, Sprite, CG and Item Art
            \n\n  {b}{u}Dusk-Spark{/b}{/u} \n Outline, Story, Script
            \n\n  {b}{u}Jmac857{/b}{/u} \n 1st story concept, and Characters
            ​\n\n  {b}{u}Alcaknight{/u}, and {u}Maoudamashii{/b}{/u} \n  Music
            \n\n  {b}{u}Kathana-DA{/b}{/u} \n  Assistant CG Artist/Dusk-wrangler
            \n\n  {b}{u}Jeroz{/b}{/u} \n Programming, UI and Speech Bubbles Layout
            \n\n  {b}{u}Remix{/b}{/u} \n Comic-style Speech Bubble UI Code
            \n\n  {b}{u}Zon Dantes{/b}{/u} \nProofreading
            \n\n  {b}{u}Mangoku418{/b}{/u} \n Some speech bubble assets
            \n\n  {b}{u}Konett, Studio Senpai, Kimagure After, and Noraneko Games{/b}{/u} \nBackground Art{/cps}"""(0,convo_ypos(-40),show_tail="narr",show_xmax=1080,show_retain=0)
    scene flashback with dissolve
    call nextpage
    show Selena closed opensmile at middef with dissolve:
        zoom 1.1
    s"Thank You For Playing!"(400,convo_ypos(100),show_tail="baseright",show_xmax=900,show_retain=0)
    pause
    hide Selena with Dissolve(1.5)
    return
