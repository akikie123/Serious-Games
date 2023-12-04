### gonna have to find some backgrounds 
### (Dorm Room - Scenario1)
### (Stucen - Scenario2)
### Room Door - Scenario 3
### Crecine Courtyard - Scenario 4
### Dorm couch - Scenario 5

label rapid_fire:
    define scenario_numbers = ["0", "1", "2", "3", "4"]
    define maxIndex = 4
    define visited = []
    $ random_num = renpy.random.randint(0,maxIndex)
    $ num_string = str(random_num)
    if scenario_numbers[random_num] == "0":
        jump ss0
    elif scenario_numbers[random_num] == "1":
        jump ss1
    elif scenario_numbers[random_num] == "2":
        jump ss2
    elif scenario_numbers[random_num] == "3":
        jump ss3
    elif scenario_numbers[random_num] == "4":
        jump ss4

label next_scenario:
    $ num_string = str(random_num)
    $ scenario_numbers = [item for item in scenario_numbers if item != num_string]
    $ maxIndex -= 1
    if maxIndex == 0:
        jump last_one
    elif maxIndex == -1:
        jump complete
    $ scenario_numbers = [item for item in scenario_numbers if item != num_string]
    $ random_num = renpy.random.randint(0,maxIndex)
    $ num_string = str(random_num)
    if scenario_numbers[random_num] == "0":
        jump ss0
    elif scenario_numbers[random_num] == "1":
        jump ss1
    elif scenario_numbers[random_num] == "2":
        jump ss2
    elif scenario_numbers[random_num] == "3":
        jump ss3
    elif scenario_numbers[random_num] == "4":
        jump ss4

label last_one:
    if scenario_numbers[0] == "0":
        jump ss0
    elif scenario_numbers[0] == "1":
        jump ss1
    elif scenario_numbers[0] == "2":
        jump ss2
    elif scenario_numbers[0] == "3":
        jump ss3
    elif scenario_numbers[0] == "4":
        jump ss4
label ss0:
    """
    Our dear Buzz here has diabetes! He was only quite recently diagnosed with diabetes and has been trying his best to keep up with his treatment. 
    """
    """
    Lately, he’s been under the weather and hasn’t been keeping up with his daily routines of checking his blood sugar and taking his insulin. 
    """
    buzz "Oh that’s right. Ugh, I just want to lay in bed for the rest of the day."

    player "Not so fast! You still gotta make sure your blood glucose levels are in check."

    buzz "I’ll be fine! I checked it yesterday morning, and everything’s good."

    """
    {i}{b}True or false?{/b}{/i}
    A person with Type I diabetes is likely to have blood sugar levels consistently stay in the same  elevated range, even when experiencing illness.
    """

    menu:
        "True":
            player "Yeah, if you say so…"

            """
            Buzz’s blood sugar levels dramatically increased overnight and his health continued to worsen because he neglected to take his medicine. 
            It got so bad that Buzz underwent diabetic ketoacidosis later that evening.

            He barely managed to come out of a critical state.

            Maybe try again...

            """

            menu:
                "Retry":
                    jump ss0

                "Continue to next":
                    jump next_scenario

        "False":
            player "Yes, but your blood sugar levels can fluctuate unpredictably, especcially when you’re sick. Better safe than sorry."
            buzz "Yeah. Yeah."

            """ 
            buzz checks his blood sugar and notices it is unusually high at 142 mg/dl.
            """ 
            buzz "Oh well dang. 142. That’s definitely high."
            player "Did you take your insulin this morning?" 
            buzz "I knew I was forgetting something this morning." 
            player "Buzz!"
            buzz "Already on it."

            """
            Buzz takes his insulin and his blood sugar readings slowly return to their normal range.
            You reminded him in enough time to not risk a potentially fatal situation in the future.
            """
            menu:
                "Play again?":
                    jump ss0

                "Continue to next":
                    jump next_scenario
    return

label ss1:
    """
    Our dear Buzz here has diabetes! He was only quite recently diagnosed with diabetes, and has been trying his best to keep up with his treatment. 
    """
    """
    Lately, he’s been forgetting his insulin every now and then, but does his best to keep up with it. 
    """
    player "Excited for the buffet tonight?"
    buzz "Absolutely! I’m ready gorge myself on every single dish there!"
    player "No same honestly, after this semester we deserve it so much."
    buzz "I’m so ready to completely forget everything and just eat!"

    """
    As you sit down at the table, you notice that Buzz still has a full vial dose of insulin in his bag.

    What do you wonder?
    """

    menu:
        "Must be a spare dose. Always good to have extra":
            buzz "That meal was delicious, thanks for dragging me there I really enjoyed it!"

            player "{i}hmm? Buzz smells kinda like fruits? I swear I only saw him eat some small apple tarts. Guess he had more before we left{/i}"

            """
            The next day, Buzz felt very dizzy and sick. He has a headache as well and decided to go to the hospital. 
            Turns out, he has ketones in his blood due to his low levels of insulin and is further helped by the doctors there.
            The isulin vial was indeed- not a spare.

            Maybe try again?
            """
            menu:
                "Retry":
                    jump ss1

                "Continue to next":
                    jump next_scenario

        "Did he make sure to take them before we left?":
            player "Buzz, did you take your insulin before we left?"
            buzz "Oh my god. I completely mixed up my alarms. I had one set for meds but confused it for leaving today."
            """ Buzz quickly takes out the vial and takes it"""
            buzz "Imma check my levels soon and then eat."
            
            """
            Buzz and you end up enjoying a nice evening dinner and go home feeling well fed and well rested!
            """
            menu:
                "Play again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario
    return

label ss2:
    """ 
    Our dear Buzz here has diabetes! He was only quite recently diagnosed with diabetes, and has been trying his best to keep up with his treatment. 
    """
    """
    {i}Trying{/i} being the keyword. Lately, he’s been unsure about how to adjust his insulin levels, but now that he’s sick he hasn’t put that much thought into it and hasn’t been eating well.
    """
    player "Hey Buzz, I heard you weren’t doing or eating so well last I checked. Anything I can do?"

    player "Hey, [playerName], thanks for checking in on me. I’m doing as well as I can for someone with such a bad cold. It’s mostly been coughing and chills so far, do you mind grabbing me a bag of the Hall’s cough drops?"

    player "I gotchu, hopefully, you can get to bed and just rest up. I hope you feel better soon! I’ll be back with the cough drops after class."

    buzz "Sounds good, let me know when you get back!"

    """Later that afternoon, you return to Buzz’s apartment."""

    player "Hey Buzz, how are you feeling?"

    buzz "Not great. I have no appetite, but I’ve been drinking water at least. Definitely a little dizzy, and definitely a lot of coughing, unfortunately. I’ve been throwing up too. Hopefully, it goes away soon."

    menu:
        "You should really eat something":

            player "I don't care how small it is, you need to eat."
            player "And oh! Buzz, I know your head hurts but check in with your doctor."

            buzz "That might actually be a good idea. They mentioned that I should probably take my insulin more often since my body isn’t able to utilize it as much. Thanks."

            player "You should really eat, it’ll at least put some calories back into your body so that you don’t end up burning fat and releasing ketones into your bloodstream." 
            player "Besides, it wasn't really an option"
            
            """
            Buzz calls his doctor and they luckily pick up. They recommend he takes an at home ketone test, which he send you to go grab.
            """
            """
            Buzz ends up checking his urine for ketones with and over the counter strip test, and adjusts his insulin, replaces his fluids and eats more to account for his illness! 
            """
            """
            Buzz ends up recovering well and goes back to the GT grind!
            """
            menu:
                "Play Again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario

        "Dang. Oh! I got the cough drops!":
            buzz "Thanks! You should probably go before I get you sick as well."
            player "I’ll head out then, I hope you feel better soon!
            Call me if you need anything!"

            """
            By the next day, Buzz is feeling very dizzy and sick. He has a headache as well and asks you to drive him to the hospital.
            Turns out, his insulin levels dropped so low and his blood sugar levels skyrocketed from his illness that the ketones in his blood stream and is further helped by the doctors there.
            
            Maybe try again...
            """
            menu:
                "Retry":
                    jump ss1

                "Continue to next":
                    jump next_scenario

    return
label ss3:
    """
    Our dear Buzz here has diabetes! He was only quite recently diagnosed with diabetes, and has been trying his best to keep up with his treatment.  """
    """
    {i}Trying{/i} being the keyword. Lately, he’s been unsure about how to adjust his insulin levels, and has decided that this semester he’s going to change his lifestyle around and become more active.
    """
    buzz "Yo, I signed up for our dorm’s intramural volleyball tournament, you think I got this?"

    player "Buzz, you haven’t played a day in your life! Pop off I guess?? 
    Do you at least know the rules of the game?"

    buzz "Yeah I do! It’s going to be a lot more practice, so I think I’ll be in the CRC a lot more."

    player "How long are you going to be playing for?"

    buzz "Could be a couple weeks, could be a long time I really liked playing it the other day, weird because I’m not usually this physically active in anything in a while."

    """
    {i}{b}True or false{/b}{/i} There are health risks related to extrenous excercise and diabeties. 
    """

    menu:
        "True":
            player "It’s always a good idea to ask your doctor."
            buzz "You sure? I don’t want to bother the doctor with something as trivial as this."
            player "It’s your health, it’s not trivial, but it’s quite honestly something that can be answered with a phone call and you’ll either get a ‘You should be okay ’ or ‘Come in for an appointment’"
            buzz "Yeah, okay." 

            """
            Buzz calls the doctor and they set up a time for him to come in for a physical.
            They find that if he kept playing so vigorously his insulin levels would have been hard to maintain without checkups.
            """ 
            buzz "Just wanted to say, thanks for supporting me to go talk to the doctor, turns out exercising and changing lifestyles suddenly is really bad without adjusting the insulin levels. 
            I could have made a really bad mistake there."
            player "Of course! How was the game? It went well?"
            buzz  "It did! I only felt dizzy at the game because of nerves!"
            menu:
                "Play Again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario

        "False":
            player "It’s just a couple weeks, let me know if you want any pointers in volleyball!"
            buzz "Course! Thank you so much for the help!"

            """
            During the game BUZZ ends up feeling very dizzy at the intramural tournament both because he’s nervous and because his insulin is so low. He’s got muscle aches, and his stomach has been upset for a while.
            """
            
            """
            He decides to get checked out later that night after the pain doesn’t stop. Once they take him to the doctors, they realize that his blood sugar is staying at or above 300 mg/dL and decided to instantly treat him by giving him insulin and replacing his fluids.
            """

            """
            He decides to get checked out later that night after the pain doesn’t stop. Once they take him to the doctors, they realize that his blood sugar is staying at or above 300 mg/dL and decided to instantly treat him by giving him insulin and replacing his fluids.
            He is sent to the ER to stay under monitoring for the night.
            """

            """
            Maybe try again...
            """
            
            menu:
                "Retry":
                    jump ss1

                "Continue to next":
                    jump next_scenario
    return

label ss4:
    """
    Buzz was recently diagnosed with diabetes, and does his best to keep up with his treatment. 
    See how stress may affect Buzz and his condition.
    """

    ### INT. LIVING ROOM - DAY

    """You and Buzz are sitting on the couch, chatting."""

    buzz "You know, managing diabetes can be tricky sometimes."

    player "Oh? Like when you're stressed?"


    buzz "When stress hits, I try to tackle it head-on. It's crucial for managing my blood sugar levels."

    player "That makes sense. How do you do it?"

    buzz "First, I check my blood sugar. If it's high, I focus on deep breathing exercises to bring it down. 
    Then, I tackle the source of stress—whether it's work or personal issues."

    player "Smart move. How well does that usually work out?"

    buzz "It helps a lot. By addressing stress promptly, I can maintain better control over my diabetes, as I’m usually eating correctly, 
    I don’t have high levels of cortisol, and remember my insulin more often."

    buzz "Anytime it’s the end of the semester coming up, though, I always find it tempting to ignore the stress and hope it goes away on its own."

    player "What happens if you do?"

    buzz "A lot of maybes"
    buzz "Ignoring stress might lead to elevated blood sugar levels, but it's a choice some people make. It also ..."

    """
    Buzz trails off his sentence, looking hesitant.
    """

    player "And also?"

    buzz "Well, if I ignore it, my blood sugar can spike, and that's not good. Stress releases cortisol, and high levels of cortisol make it harder for my body to use Insulin.
    It's a gamble, really. But I gotta grind for this linear final."

    player "Looks like you have some tough decisions to make, Buzz."

    buzz "Yeah, managing diabetes is a daily adventure. But making the right choices keeps me in control."
    menu:
        "Replay":
            jump ss4

        "Continue to next":
            jump next_scenario

    return

label complete:
    """
    Congrats! You have finished all of the short scripts! 
    """
    """
    All of these mini scenarios have shown different situations which could result in {i}diabetic ketoacidosis{/i} sometimes called {i}DKA{/i}.
    """

return
