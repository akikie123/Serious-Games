### gonna have to find some backgrounds 
### (Dorm Room - Scenario1)
### (Stucen - Scenario2)
### Room Door - Scenario 3
### Crecine Courtyard - Scenario 4
### Dorm couch - Scenario 5

label rapid_fire:
    ###define scenario_numbers = ["0", "1", "2", "3", "4"]
    ###define maxIterations = 4
    $ random_scene = renpy.random.choice(scenario_numbers)
    ### $ num_string = str(random_num)
    if random_scene == "0":
        $ scenario_numbers.remove(random_scene)
        jump ss0
    elif random_scene == "1":
        $ scenario_numbers.remove(random_scene)
        jump ss1
    elif random_scene == "2":
        $ scenario_numbers.remove(random_scene)
        jump ss2
    elif random_scene == "3":
        $ scenario_numbers.remove(random_scene)
        jump ss3
    elif random_scene == "4":
        $ scenario_numbers.remove(random_scene)
        jump ss4

label next_scenario:
    ### $ num_string = str(random_num)
    ### $ scenario_numbers = [item for item in scenario_numbers if item != num_string]
    $ maxIterations -= 1
    ### if maxIndex == 0:
    ### jump last_one
    if maxIterations == -1:
        jump complete
    ### $ scenario_numbers = [item for item in scenario_numbers if item != num_string]
    ### $ random_num = renpy.random.randint(0,maxIndex)
    #### $ num_string = str(random_num)
    $ random_scene = renpy.random.choice(scenario_numbers)
    if random_scene == "0":
        $ scenario_numbers.remove(random_scene)
        jump ss0
    elif random_scene == "1":
        $ scenario_numbers.remove(random_scene)
        jump ss1
    elif random_scene == "2":
        $ scenario_numbers.remove(random_scene)
        jump ss2
    elif random_scene == "3":
        $ scenario_numbers.remove(random_scene)
        jump ss3
    elif random_scene == "4":
        $ scenario_numbers.remove(random_scene)
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
    with Dissolve(.5)
    pause 0.5
    scene ss1
    pause 1.0
    show nauseousbuzzsprite:
        zoom 0.5
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
            hide nauseousbuzzsprite
            show verynauseousbuzzsprite:
                zoom 0.40
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
            hide nauseousbuzzsprite
            show normalbuzzsprite:
                zoom 0.40
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
            hide normalbuzzsprite
            with Dissolve(.5)
            pause 0.5
            scene GRAYBG1
            pause 1.0

            """
            Answer: FALSE
            Congrats, you got it right!
            """
            """
            Explanation: Illness can trigger stress responses that increase the cortisol level (a stress hormone) in the body. 
            """
            """
            The sudden fluctuation of cortisol levels can affect how your diabetic friend’s body processes their insulin, 
            """
            """
            leading them to process less insulin and therefore increasing their risk of ketoacidosis. 
            """
            """
            Make sure that your friend is still properly following their insulin treatment care and tell/help them to take it easy to prevent more stress 
            """
            """
            within their body. This helps prevent the negative effects of cortisol.
            """
            """
            Source: https://my.clevelandclinic.org/health/diseases/21945-diabetic-ketoacidosis-dka
            """

            menu:
                "Play again?":
                    jump ss0

                "Continue to next":
                    jump next_scenario
    return

label ss1:
    with Dissolve(.5)
    pause 0.5
    scene ss2
    pause 1.0
    show normalbuzzsprite:
        zoom 0.40
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
            hide normalbuzzsprite
            show verynauseousbuzzsprite:
                zoom 0.40
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
            hide normalbuzzsprite
            with Dissolve(.5)
            pause 0.5
            scene GRAYBG2
            pause 1.0

            """
            Answer: "Did he make sure to take them before we left?"
            Congrats! You got it right!
            """
            """
            Explanation: Better safe than sorry! Lend a helping hand to your friend as literary
             review reveals that many factors could lead to a person forgetting to take their insulin. 
            """
            """
            Reasons include embarrassment, depression, and general lack of attention. 
            """
            """
            However, it is proven that both missed insulin dosages AND mistimed dosages lead to low insulin levels 
            so watch out for your friend! 
            """
            """
            According to studies, this causes higher blood sugar levels 
            but also can force their liver to break down fat for energy, causing ketoacidosis. 
            """
            """
            Both effects cause nausea and faintness.
            """
            """
            Source: 
            Susan Robinson, Rachel S. Newson, Birong Liao, Tessa Kennedy-Martin, and Tadej Battelino. Missed and Mistimed Insulin Doses in People with Diabetes: A Systematic Literature Review. 
            Diabetes Technology & Therapeutics.Dec 2021.844-856.http://doi.org/10.1089/dia.2021.0164
            """
            menu:
                "Play again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario
    return

label ss2:
    with Dissolve(.5)
    pause 0.5
    scene ss3a1
    pause 1.0
    show nauseousbuzzsprite:
        zoom 0.45
    """ 
    Our dear Buzz here has diabetes! He was only quite recently diagnosed with diabetes, and has been trying his best to keep up with his treatment. 
    """
    """
    {i}Trying{/i} being the keyword. Lately, he’s been unsure about how to adjust his insulin levels, but now that he’s sick he hasn’t put that much thought into it and hasn’t been eating well.
    """
    player "Hey Buzz, I heard you weren’t doing or eating so well last I checked. Anything I can do?"

    buzz "Hey, [playerName], thanks for checking in on me. I’m doing as well as I can for someone with such a bad cold. It’s mostly been coughing and chills so far, do you mind grabbing me a bag of the Hall’s cough drops?"

    player "I gotchu, hopefully, you can get to bed and just rest up. I hope you feel better soon! I’ll be back with the cough drops after class."

    buzz "Sounds good, let me know when you get back!"

    """Later that afternoon, you return to Buzz’s apartment."""

    player "Hey Buzz, how are you feeling?"

    buzz "Not great. I have no appetite, but I’ve been drinking water at least. Definitely a little dizzy, and definitely a lot of coughing, unfortunately. I’ve been throwing up too. Hopefully, it goes away soon."

    menu:
        "You should really eat something":
            with Dissolve(.5)
            pause 0.5
            scene ss3a2
            pause 1.0
            hide nauseousbuzzsprite
            show normalbuzzsprite:
                zoom 0.45

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
            hide normalbuzzsprite
            with Dissolve(.5)
            pause 0.5
            scene GRAYBG3
            pause 1.0

            """
            Answer: "I don't care how small it is, you need to eat."
            Congrats, you got it right!
            """
            """
            Explanation: These are all common symptoms of Ketoacidosis and can be resolved by general blood sugar management such as eating. 
            """
            """
            Source: Shahid, W., Khan, F., Makda, A., Kumar, V., Memon, S., & Rizwan, A. (2020). Diabetic Ketoacidosis: Clinical Characteristics and Precipitating Factors.
            """
            """
            Cureus, 12(10), e10792. https://doi.org/10.7759/cureus.10792
            """
            menu:
                "Play Again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario

        "Dang. Oh! I got the cough drops!":
            with Dissolve(.5)
            pause 0.5
            scene ss3a2
            pause 1.0
            hide nauseousbuzzsprite
            show verynauseousbuzzsprite:
                zoom 0.45

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
    with Dissolve(.5)
    pause 0.5
    scene ss4
    pause 1.0
    show normalbuzzsprite:
        zoom 0.40
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
            hide normalbuzzsprite
            with Dissolve(.5)
            pause 0.5
            scene GRAYBG4
            pause 1.0
            """
            Answer: TRUE
            Congrats you got it right!
            Explanation: Moderate exercise has been found to help maintain blood sugar levels. 
            """
            """
            However, excessive exercise can put your Type 1 diabetic friend at risk of hypoglycemia which prevents proper maintenance of blood sugar levels. 
            """
            """
            This is because their body starts reducing the amount of glycogen within their muscles and hepatic system. 
            """
            """
            This can cause their body to intake glucose too quickly and lead to hypoglycemia or hyperglycemia. Additionally, if they have some comorbidities such as macrovascular disease, excessive exercise is not recommended as it can cause further difficulties. 
            """
            """
            Overall, it is recommended for your friend to check with a doctor and see if they are predisposed to any of these effects. 
            """
            """
            Source: Lu, X., Zhao, C. (2020). Exercise and Type 1 Diabetes. In: Xiao, J. (eds) Physical Exercise for Human Health. Advances in Experimental Medicine and Biology, vol 1228. Springer, Singapore. https://doi.org/10.1007/978-981-15-1792-1_7
            """
            menu:
                "Play Again?":
                    jump ss1

                "Continue to next":
                    jump next_scenario



        "False":
            player "It’s just a couple weeks, let me know if you want any pointers in volleyball!"
            buzz "Course! Thank you so much for the help!"
            hide normalbuzzsprite
            show nauseousbuzzsprite:
                zoom 0.40
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
    with Dissolve(.5)
    pause 0.5
    scene ss5
    pause 1.0
    show tiredbuzzsprite:
        zoom 0.40
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
    $scenario_numbers.append("0")
    $scenario_numbers.append("1")
    $scenario_numbers.append("2")
    $scenario_numbers.append("3")
    $scenario_numbers.append("4")
    $maxIterations += 5
    """
    Congrats! You have finished all of the short scripts! 
    """
    """
    All of these mini scenarios have shown different situations which could result in {i}diabetic ketoacidosis{/i} sometimes called {i}DKA{/i}.
    """
    




return
