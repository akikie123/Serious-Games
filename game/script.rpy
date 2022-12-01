# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jack", color=(66, 221, 241, 255))
define m = Character("Buzz", color=(221, 15, 176, 255))
define y = Character("You", color=(222, 34, 213, 255))


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

    """
      You and Buzz are meeting up one day before class! Buzz is a known diabetic, and but recently his mind has been occupied by school and responsibilities.
    """
    
    y "Hey Buzz! How’s it going? Are you ready for CS 2200 to steamroll us again?"
    
    m "Hey! I’m going as well as I can, didn’t get much sleep last night, but at least I managed to work out a lot today! Pretty hungry though, maybe I’ll eat again later."

    
    y "Let’s head down to class then!"
    
    #somehow change slides here
   # e "Well- this game will be about helping people with diabetes? When you're up for it, press start okay??"

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
