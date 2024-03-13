# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character(_("Uno"), color="#ffd9c8")
define m = Character(_("Madis"), color="#fff0c8")
define s = Character(_("Simon"), color="#c8ffc8")
define t = Character(_("Theodore"), color="#c8ffe3")
define a = Character(_("Alvin"), color="#c8ebff")
define ss = Character(_("Sonia"), color="#ffd9c8")

default book = False

# The game starts here.
label start:
    #Start by playing music
    play music "illurock.opus"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg forist
    with fade

    "A girl is crying and walking in the forest thinking about what has happened in the past 4 month"
    "And if she can get a second chance she would take it without caring"
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
