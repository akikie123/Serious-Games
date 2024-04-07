#hi this is Lily
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define buzz = Character("Buzz", color=(196, 196, 11, 255))
define player = Character("[playerName]", color=(222, 34, 213, 255))
define coach = Character("Coach", color=(255, 255, 255, 255))
define emergencyOperator = Character("911 Operator", color=(255, 255, 255, 255))

# The game starts here.
label splashscreen:
    scene black
    with Pause(1)

    show text "{i}{b}VIP: Serious Games presents....{/b}{/i}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bluesky
    define scenario_numbers = ["0", "1", "2", "3", "4"]
    define maxIterations = 4

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ playerName = renpy.input("What is your name?", length = 15)
    $ playerName = playerName.strip()
    $ if not playerName: playerName = "Techie"
    # These display lines of dialogue.

    menu:
        "Begin scenario 1":
            jump scenario1

        "Begin scenario 2":
            jump scenario2

        "Begin Short Scripts":
            jump rapid_fire

        "Begin Glucagon Scenario":
            jump glucagon_scenario

    

    label scenario1:

    with Dissolve(.5)
    pause 0.5
    scene plz
    ### with Dissolve(.5)
    """
    You and Buzz are meeting up one day before class! 
    Buzz is a known diabetic, but recently he has been preoccupied with school and responsibilities.
    """
    
    show normalbuzzsprite:
        zoom 0.5
    with moveinleft
    player "Hey Buzz! How’s it going? Are you ready for CS 2200 to steamroll us again?"
    
    buzz "Ugh. Don't even {b}mention{/b} it. I didn’t get much sleep grinding the homework, but at least I still managed to go work out this morning!"
    buzz "I'm hungry though, weird since my breakfast was kinda big."

    #player "Maybe grab a snack from the vending machine?"
    #player "We should head to class though or we are gonna be late!"

    #buzz "Pretty hungry though, maybe I’ll eat again later.."
    
    ###somehow change slides here: the following is the scene swap psuedocode
    with Dissolve(.5)
    pause 0.5
    scene ferst
    pause 1.0
    show normalbuzzsprite:
    ##show tiredbuzzsprite:
        zoom 0.40
    ### with Dissolve(.5)

    """
    As you walk, you notice Buzz's voice shaking slightly as he talks, but you’re not sure if it’s just because it’s cold outside or not.
    """
    menu:

        "We can grab a quick snack from the vending machine right now, there's one near by!":
            jump outside_class

        "We should head to class or we are gonna be late, but we can try to get a snack after!":
            jump conversation_to_class


    label outside_class:
    
    with Dissolve(.5)
    pause 0.5
    scene outclass
    pause 1.0
    show normalbuzzsprite:
        zoom 0.40

    $ menu_flag = False

    buzz "Around 15 minutes before I eat, I always have to check a couple things: my current blood sugar, and the amount of carbs I’m about to eat."
    buzz "Carbs make everyone’s blood sugar levels rise, so I have to see how much insulin I need to balance it. Fats and proteins get in the way of this process"

    buzz "The equation can seem pretty complicated, but I promise you'll get the hang of it!"
    buzz "[((current blood sugar) - (target blood sugar)) / correction factor] + [(number of grams of carbs) / (insulin:carb ratio)]" 
    ## implement mini game around here to drag just variables 

    buzz "Many of these factors are set numbers that are unique just for me: Target blood sugar = 120 mg/dl, Correction factor = 35, and my Insulin to Carb Ratio = 10 (grams / unit of insulin)"
    ## *given a blank equation fill in these numbers into the correct blanks to get this result:
    #[(current blood sugar) - 120) / 35] + [(# of grams of carbs / 10]
    jump vending1

    label vending1:
    
    with Dissolve(.5)
    pause 0.5
    scene vending
    pause 1.0
    show normalbuzzsprite:
        zoom 0.40   

    ##start of vending machine 1 scenario where Buzz's blood sugar is normal

    buzz "Okay so my current blood sugar is reading 120mg/dl, perfect! I have to go to the bathroom real quick, do you mind getting a snack for me?"
    player "Of course!"

    ##dissolve to Demi's screen 

    """ 
    You stand at the vending maching looking at options...
    """
    
    ## message pops up informing user they can hover over options to see the nutritional values 

    menu:

            "Choose the yogurt drink": # (18g carbs, 10g protein,4g fat)
                jump thanks

            "Choose the protein bar": # (29g carbs, 20g protein, 11g fat)
                jump thanks

    label thanks:
        buzz "Thanks for the snack, I got you next time!"
        jump early_action


    label conversation_to_class:

        player "you okay there Buzz?"
        buzz "yeah. think I did too much with my workout. haaa."
        
        """
        You start walking to class, lightheartedly chatting about the next impossible project that the professors have decided was an amazing idea.
        """

        player "I’m telling you, there’s no way we’ll be able to finish it."

        """
        Buzz stops, staring blankly and breathing heavily, looking a little queasy.
        """

        #jump choice1_done

        menu:

            "Wait Quietly.":
                jump buzz_says_nothing

            "Ask “Are you alright?”":
                jump buzz_says_something

    label buzz_says_nothing:

        #  $ menu_flag = True
        """
        Buzz continues on like nothing happened.
        The two of you quickly walk to class.
        """
        jump outside_class2

    label buzz_says_something:
        #   $ menu_flag = False

        buzz "Oh yeah, I’m all good. Thanks for asking. Just tired after the workout and weirdly anxious about the project."

        jump outside_class2

        #jump outside_class

    label outside_class2:
        with Dissolve(.5)
        pause 0.5
        scene outclass
        pause 1.0
        show nauseousbuzzsprite:
            zoom 0.40

        $ menu_flag = False

        buzz "Barely made it. 5 minutes before it starts! Nice! My head hurts now, but that’s fine. Price we pay for basically sprinting here."

        """
        Buzz speaks in an upbeat tone...
        """
        """
        but he looks sickly.
        """
        player "{i}Headache, uneven walking, pale and clammy look. This is starting to be a lot of symptoms that aren’t just from a long workout or a bad night of sleep. What should I do?{/i}" 
        
        menu:

            "Usher the both of you into class. He just needs to sit a while.":
                jump in_class

            "Ask “Are you sure you’re okay?”":
                jump buzz_sits_down

            "Ask “Should you check your blood sugar?”":
                jump buzz_check_blood

        label buzz_check_blood:

        #  $ menu_flag = True
            buzz "I don’t actually know. I’m really not feeling great, so I could just be sick. But everything came pretty suddenly. I’ll check it once we’re in class, I don’t want to pull it out of my pocket right now."
            """
            The two of you head inside and settle down in class.
            """
            jump in_class

        label buzz_sits_down:

        #   $ menu_flag = False

            buzz "I should be. But since you're obviously worried- let’s just sit down in class first and I’ll solve it in there."

            jump in_class

        label in_class:

        #   $ menu_flag = False
            with Dissolve(.5)
            pause 0.5
            scene classroom
            with Dissolve(.5)
 
            """
            Both of you pull out your laptops and prepare to start taking notes.

            """

            buzz "I think I’m going to put my head down for a bit. It’s not doing to great with both the headache and the amount of trauma this room has given me from 2200 Tests."

            menu:

                "Let him rest":
                    jump class_continues

                "Ask if he can check his blood sugar.":
                    jump check_blood_sugar

            label check_blood_sugar:

            #  $ menu_flag = True
                """
                Buzz pulls out his CGM (Continuous Glucose Monitor) and notices that it’s way too low! It’s under 65 mg/dL!
                """
 
 
                "{i}This normally isn't a problem, but after eating breakfast, his average blood sugar should be closer to 140mg/dL{/i}"
                "{i}This blood sugar level is comparable to that of a non-diabetic person having not eaten for over 5 hours{/i}" 
                ## check these numbers with Maheen

                buzz "Oh. That explains CGM reading, could you run and grab me a snack?"

                player "You got it!"

                """
                You run to the vending machine
                """
                ##dissolve to Demi's screen 

                with Dissolve(.5)
                pause 0.5
                scene vending

                ## message pops up informing user they can hover over options to see the nutritional values 
                menu:

                    "Choose a pack of Jolly Ranchers": # (17g carbs)
                        jump hard_candy

                    "Choose a pack of peanuts": # (5g carbs, 14g fat, 7g protein)
                        jump peanuts

                    "Choose a pack of PopTarts": #(70g carb, 9g fat)
                        jump poptart

                    "Choose a pack of Oreos": #(25g carb, 7g fat, 1g protein)
                        jump oreo

                label hard_candy:

                #  $ menu_flag = True
                with Dissolve(.5)
                pause 0.5
                scene classroom
                with Dissolve(.5)
                """
                You come back to class holding a bag of Jolly Ranchers.
                """

                buzz "Sweet! Pun intended, that’s exactly what I needed! Thank you so much!"

                jump vending_machine_ending_screen
                
                label peanuts:

                """
                You come back to class holding a bag of peanuts.
                """
                with Dissolve(.5)
                pause 0.5
                scene classroom
                with Dissolve(.5)
                buzz "uhhhh- Not quite what I needed... but I'll take it"
                """
                Buzz munches on a few peanuts before putting his head back down.
                """
                jump class_continues

                label poptart: 

                """
                You come back to class holding a pack of PopTarts.
                """
                with Dissolve(.5)
                pause 0.5
                scene classroom
                with Dissolve(.5)
                buzz "Thanks this is just what I needed!"
                """
                Buzz takes a few bites and starts taking lecture notes.
                """
                jump vending_machine_ending_screen

                label oreo:

                """
                You come back to class holding a sleeve of Oreos.
                """
                with Dissolve(.5)
                pause 0.5
                scene classroom
                with Dissolve(.5)
                buzz "Ooo I love oreos, but I'm not sure if these will do the trick."
                """
                Buzz munches on a few cookies before putting his head back down.
                """
                jump class_continues

            label class_continues:

            #   $ menu_flag = False
                """
                You pay attention to class for sometime, diligently taking notes and notice that Buzz hasn’t lifted his head from the table in a while. 
                """
                menu: 
                    "Poke him to see if he wakes up":
                        jump found_sluggish

                    "Let him sleep":
                        jump found_unconcious_way_later

                label found_sluggish:
                    """
                    You decide to poke him a little bit, and find that he’s not responding at all! Not even a slap makes him react!
                    """

                    player "Buzz? Buzz! Are you there, we need to learn about network hopping!"

                    buzz ". . . huh? Sup? Is something wrong? Something is probably wrong, but something is always wrong."

                    player "Uh oh, this doesn’t look to good."

                    menu:
                        "Check his CGM for his blood sugar level":
                            jump you_check_CGM

                        "Leave him alone":
                            jump found_unconcious_way_later

                    label you_check_CGM:
                        """
                        You pull out his CGM from his pocket. It’s below 50 dl/mg! That’s not good, what do you do now?!                        
                        """
                        menu:
                            "Run to the Vending Machine":
                                jump vending_machine_pt2

                            "Panic silently":
                                jump found_unconcious_way_later

                        label vending_machine_pt2:
                            """
                            You run to the vending machine.
                            """
                            with Dissolve(.5)
                            pause 0.5
                            scene vending             #maybe start delete at the next line to zoom
                            pause 1.0             
                            show verytiredbuzzsprite: 
                                zoom 0.40             # maybe end delete
                            with Dissolve(.5)

                            ##dissolve to Demi's screen 
                            ##hover actions

                            """
                            Insulin won't help now, it will only lower Buzz's blood sugar levels even more!
                            """
                            menu:
                                "Choose Mountain Dew": ## (62g carbs)
                                    jump mountain_dew 

                                "Choose beef jerky": ## (4g carbs, 1g fat, 11g protein)
                                    jump beef_jerky

                                "Choose Diet Coke": ## (0g of fat protein and carbs)
                                    jump diet_coke 

                                "Choose a Snickers bar": ## (35g carbs, 14g fat, 4g protein)
                                    jump snickers
                                
                            label mountain_dew:
                                with Dissolve(.5)
                                pause 0.5
                                scene classroom
                                with Dissolve(.5)
                                """
                                You come back to class holding a Mountain Dew, and shake Buzz a little more to wake him up.
                                """
            
                                player "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple sips for now to get the blood sugar up?"

                                buzz "Hrgg? Oh yeah sure. Thanks for watching out for me, I’ll pay you back. Didn't think to check my sugars after my workout. Sorry"
                                
                                jump middle_ending_screen

                            label beef_jerky:
                                with Dissolve(.5)
                                pause 0.5
                                scene classroom
                                with Dissolve(.5)
                                """
                                You come back to class holding a bag of beef jerky.
                                """

                                player "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple bites for now to get the blood sugar up?"

                                buzz "Hmm? Oh yeah sure. Thanks for watching out for me, I’ll pay you back. Didn't think to check my sugars after my workout. Sorry"
                                
                                buzz "Wait a second, beef jerky? I don’t know how much this will help me. The amount of protein in this will make my blood sugar levels rise more slowly."

                                jump found_unconcious_way_later

                            label diet_coke:
                                with Dissolve(.5)
                                pause 0.5
                                scene classroom
                                with Dissolve(.5)
                                """ 
                                You come back to class holding a bottle of Diet Coke.
                                """
                                player "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple bites for now to get the blood sugar up?"

                                Buzz "Um… sure but you know this doesn’t have any sugar in it right…?"

                                jump found_unconcious_way_later

                            label snickers:
                                with Dissolve(.5)
                                pause 0.5
                                scene classroom
                                with Dissolve(.5)

                                """ 
                                You come back to class holding a Snickers bar.
                                """
                                player "Hey, just checked your CGM it doesn’t look too good. You mind taking a couple bites for now to get the blood sugar up?"

                                Buzz "Ooo yeah I love Snickers, they have a lot of nuts though which are high in protein."

                                jump found_unconcious_way_later


                label found_unconcious_way_later:
                    """
                    It’s now the end of class! And you two need to leave soon! So you poke Buzz to see if he wakes up.
                    """

                    player "Buzz, we have to go! Wake up!"

                    buzz ". . ."

                    player "Buzz? Buzz! Hello?!"

                    buzz ". . . . . . . . . ."

                    """
                    This doesn’t look good, what do you do??!!
                    """

                    menu:
                        "Call 911":
                            jump er_ending_screen

                        "Try to shake him awake":
                            jump someone_else_called_911

                    return
                   
    #jump vending_machine_ending_screen

    label early_action:
        "You made sure Buzz's blood sugar stayed in a healthy range, good job!"
        jump info_end


    label vending_machine_ending_screen:
        "You got his blood sugar to a normal range with that little sweet rush! Good job!!"
        "Buzz started feeling a bit better within the hour."
        jump info_end
        
    label middle_ending_screen:
        """
        Though a little late to notice, you got Buzz just what he needed. 
        He felt well enough within the hour and decided to go back to his dorm to rest. 
        """
        "nice save."
        jump info_end
    
    label bad_ending_screen:
        "Buzz quietly ate some peanuts before looking dazed."
        "The person behind you gives him some fruit from their bag and worridly looks after him the rest of class."
        "You seriously didn't know what to do huh?"

    label er_ending_screen:
        """
        On the down side, you did not get Buzz the extra sugar rush that he needed in time.
        On the bright side, at least you recognized when you needed to call a professional in.
        He's doing a lot better now! Just had a little bit of a scare, and is resting at home now.
        """
        jump info_end

    label someone_else_called_911:
        """
        On the very down side, neither did you realize that Buzz was unconscious earlier, but you also didn't quite know what to do.
        That's okay though! Someone else was able to swoop in and save the day! And now you know for next time what not to do!
        """

        jump info_end
        
    label info_end:
        """
        What you just saw in this scenario was a case of hypoglycemia! The further you progressed into the game, the more severe the case became!

        Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than the standard range, and it can happen for a large number of reasons. 

        Some causes can include skipping meals, increased exercise levels, and drinking alcohol.

        Some of the symptoms include shakiness, headaches, blurred vision, confusion, nervousness, and many more.

        At a non-professional level, some of the best treatment for someone that is suffering from hypoglycemia, especially a diabetic, is to give them something that is high in sugar content or carbohydrates. This could be candy, soda, juice.
        Especially things high in natural sugars such a raisins or other fruits.

        Once the person loses consciousness or there appear to be other abnormal or worrying symptoms, please call a professional or take them to the hospital.

        (Please note that we are not medical professionals)
        """
        return

    # This ends the game.

    return
