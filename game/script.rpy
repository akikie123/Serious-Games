# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jack", color=(66, 221, 241, 255))
define m = Character("Buzz", color=(221, 15, 176, 255))


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene uhm

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sprite0001

    # These display lines of dialogue.

    e "Welcome! I am Jack. Jack Ehts, and this is the Serious Games project."

    """
    what is going on?
    """

    e "Well- this game will be about helping people with diabetes? When you're up for it, press start okay??"

    menu:

        "This is Choice A!":
            jump choice1_yes

        "This is Choice B!":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        e "Choice A Reached"

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        e "Choice B Reached"

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

 
    ## show buzz

    ## e ""

    # This ends the game.

    return
