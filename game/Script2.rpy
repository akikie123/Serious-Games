label scenario2:
### need to put ESE or fitten lobby photo here as scene!!!!!!
with Dissolve(.5)
pause 0.5
scene rsz_lobby
with Dissolve(.5)
"""
It's another great day at Georgia Tech, sir yes sir! 
"""
"""
The birds are singing, the bees are buzzing, and you’re once again buried under a mountain of homework.
"""
"""
But that's fine. You and Buzz are about to head over to Willage to study and desperately grind away on work. 
"""
"""
{i}You are currently waiting for Buzz to come down to the lobby.{/i}
"""
buzz "Yo!"
"""
Buzz appears from around the corner.
"""
player "Hey Buzz, there you are! Make it down the stairs okay with your old bones?"
buzz "We are literally the same age."
player "Sure sure, whatever you say gramps. You got everything?"
buzz "Yeah!"

### now walking to willage - picture needed outside ESE lobby stairs (facing crecine) as scene!!!!!
with Dissolve(.5)
pause 0.5
scene wut
buzz "Ugh the sunlight hurts. Spent too many days holed up working."
player "uh oh, what’s been keeping you hostage?"
buzz "We have our exams soon yet 3 of my classes have a project due within the next week or 2."
buzz "No joke, my legs feel so weak right now. You think spending nearly 40 hours straight at a desk does something to you?"
"""
You’re not sure if you should be concerned for Buzz at this point, or if this is just normal Gatech student behavior.
"""
menu:
    "Have you excercised even a little bit?":
        jump askToWillage
    "Too relatable.":
        jump csMajorMoment

label askToWillage:
    buzz "Not really. Been glued to my computer screen."
    player "You good? Wanna go for a short walk before going to study?"
    buzz "Nah, I’m all good. Maybe later we can take that walk! We gotta get through this study guide first though."
    jump intoWillage

label csMajorMoment:
    player "What a cs major moment. Please tell me you at least showered."
    buzz "Of course I did! Did you?!"
    jump intoWillage

label intoWillage:
    with Dissolve(.5)
    pause 0.5
    scene willage_out
    """
    You finally arrive at Willage.
    """
    with Dissolve(.5)
    pause 0.5
    scene willage_bf
    """
    Even though you are on the bottom floor, there is a sweet scent in the air.
    """
    buzz "Whatever that is, it smells good."
    buzz "I gotta say though, it has to be because exams are coming up that I’m literally stress eating more snacks than ever."
    player " I know right. It’s like all of the energy I get from eating seeps away into my papers."
    buzz "Seriously, I have just had a craving for candies and practically inhaled so many cups of coffee and energy drinks too."
    
    menu:
        "You need to go eat something healthier":
            jump worryStudy
        "Felt":
            jump study
    
    label worryStudy:
        buzz "I will in a bit"
        player "You sure you don't want to nap?"
        player "Being on coffee, sugar and energy drinks is no good. We can always study later."
        buzz " Nahhhh, it’s alright. My vision is only a little blurry right now from trying to wake up."
        buzz "Thanks for the concern though."
        jump studyingIntensifies

    label study:
        player "Sleep is a myth. We better start the grind or this will never end."
        jump studyingIntensifies
    
    label studyingIntensifies:
        """
        Some time passes, with the only sounds interrupting you both being the clacking of keys and rustles of papers.
        """
        buzz "Time to crack open a cold one."
        player "Huh?!"
        """
        Buzz pulls out a familiar white can.
        """
        buzz "Gotta keep the white monsters stocked. Favorite energy drink right here."
        player "Was coffee not enough this morning?"
        buzz "Didn't get coffee, but I have my monsters. I have been oddly thirsty after grinding these past 2 days."
        player "{i}Didn't sleep, has an odd sugar addiction, and god knows when his last meal was.{/i}"
        menu: 
            "Let him be, he is gonna need it for today.":
                jump bathroomRuns
            "Take the drink":
                jump askingSugar

    label bathroomRuns:
        """
        Buzz quickly opens the can and takes a few sips.
        """
        """
        Within a few minutes he has downed the entire can.
        """
        """
        The study session continues...
        """
        buzz "But that algorithm can't run in O of n time, iterating over is too long."
        buzz "I'll explain once I get back."
        player "Bathroom again? This is like the 4th time already!"
        buzz "Maybe it was the monster?"
        """
        Buzz walks off to the restroom.
        """
        """
        When he returns you notice him pull out another monster can.
        """
        menu:
            "Stop him":
                jump askingSugar
            "Another can?":
                jump sleepyTime

    label askingSugar:
        """
        You grab the can and place it to the side.
        """
        player "How much sugar have you had today?"
        buzz "Well the snacks had uhhh, some amount?"
        player "And how many monsters have you had?"
        buzz "uhhhhhhh"
        player "I thought you learned your lesson with your hypoglycemia moment last semester."
        buzz "I did!"
        player "When was your last real meal?"
        buzz "uhhh-"
        player "Vision blurry, extremely thirsty, craving sugar. Sound familiar?"
        buzz "Hyperglycemia-- ugggghhh."
        buzz "I may or may not have also missed some insulin doses. Assignments have had me stressed."
        player "Is there anything I can do to help?"
        buzz "You feel like going for that walk?"
        player "I'm down, but only after you get water and some real food."
        jump good_scenario2_end
    
    label sleepyTime:
        buzz "That last one did not hit how it should have."
        player "Only you"
        """
        As you’re mid way through the practice, you notice Buzz is slowly nodding off.
        """
        player "Buzz? You alright?"
        buzz "What? Huh? Oh yeah I’m good sorry. Could you explain that again?"
        buzz "Sorry, I’m just super tired, and feel a bit dizzy rn."
        menu:  
            "Think you should check your blood sugar?":
                jump check_sugar 
            "If you say so":
                jump studypt3
    
    label check_sugar:
        buzz "Huh- I don't think I have checked it in a bit. "
        """
        Buzz takes a glance at his CGM (continusou glucose monitor), and blinks a couple times trying to clear his vision.
        """
        buzz "WOW. Uhhhhh- I am at 150mg/dL. I can't even remember if I took my insulin."
        player "Is there anything I can do to help?"
        buzz "I should be fine. I am going to pack up and head home and rest a bit before going to workout at CRC."
        buzz "I also need some water."
        player "I'll go with you to the CRC later, just text me when."
        jump middle_scenario2_end
    
    label studypt3:
        """
        You continue explaining the problems and finish the study session.
        """
        """
        You both start working on individual assignments. After some time you realize Buzz has been quiet and notice he has gone to sleep.
        """
        menu:
            "check his condition":
                jump callAmbulanceSigns
            "check his CGM":
                jump callAmbulanceMonitor

    label good_scenario2_end: 
        """
        You and Buzz head upstairs and have lunch in Willage. You then walk around west before returning to your dorms.
        """
        """
        After a while, you got confirmation from Buzz's roommate that he got some rest and took his insulin.
        """
        """
        Buzz felt better the next day.
        """
        jump info_end_scenario2
    label middle_scenario2_end:
        """
        After Buzz drinks some water, he says his goodbyes and heads home.

        A few hours later he texts you on his way to the CRC. 

        He feels a bit better by nighttime and fully recovers in a few days.
        """
        jump info_end_scenario2
    label callAmbulanceSigns:
        """
        You look over at Buzz's face and lightly tap his forehead.
        """
        player "No fever at least."
        """
        You notice how severely dry and cracked his lips are. 

        Upon further inspection you notice that Buzz looks thinner too. You try to shake him awake to only get drowsy replies.

        You quickly call the ambulance and within the hour medical professionals arrive and take Buzz away.
        """
        jump info_end_scenario2
    label callAmbulanceMonitor:
        """
        You carefully grab Buzz's CGM from his bag and look at the number.

        It reads 150mg/dL!

        You immediately call for help and within the hour an ambulance arrives taking a still unconcious Buzz away.
        """
        jump info_end_scenario2
    label info_end_scenario2:
        """
        What you just saw in this scenario was a case of hyperglycemia! The further you progressed into the scenario, the more severe the case became!

        Hyperglycemia is a condition in which your blood sugar (glucose) level is higher than the standard range, and it can happen for a large number of reasons. 

        Some causes can include skipping insulin dosages, stress, and drinking alcohol.

        Some of the symptoms include shakiness, headaches, blurred vision, confusion, unexplained weight loss, and many more.

        At a non-professional level, some of the best treatment for someone that is suffering from hyperglycemia, especially a diabetic, is to give them plenty of water and make sure they take their insulin.
        
        Once the person loses consciousness or there appear to be other abnormal or worrying symptoms, please call a professional or take them to the hospital.

        (Please note that we are not medical professionals)
        """
return