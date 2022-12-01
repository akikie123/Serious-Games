# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jack", color=(66, 221, 241, 255))
define m = Character("Buzz", color=(255, 251, 21, 255))
define player = Character("You", color=(222, 34, 213, 255))


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene uhm

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    """
    You and Buzz are meeting up one day before class! Buzz is a known diabetic, and but recently his mind has been occupied by school and responsibilities.
    """
    
    player "Hey Buzz! How’s it going? Are you ready for CS 2200 to steamroll us again?"
    
    m "Hey! I’m going as well as I can, didn’t get much sleep last night, but at least I managed to work out a lot today! Pretty hungry though, maybe I’ll eat again later."

    "Buzz seems to be shaking a little bit as he talks."
    "You’re not sure if it’s just because it’s cold outside or because of something else."

    menu:

        "Ignore it":
            jump choice1_bad

        "Ask if he's ok":
            jump choice1_good

    label choice1_bad:

        $ menu_flag = True

        "He's probably just tired. He did say he hardly slept."
        player "Let's head down to class then!"

        jump choice1_done

    label choice1_good:

        $ menu_flag = False
        player "You sure you wanna go? You're shaking a bit."
        m "uhh-"

        jump choice1_done

    
    #somehow change slides here

    label choice1_done:

        # ... the game continues here.

 
    ## show buzz

    ## e ""

    # This ends the game.

    return
