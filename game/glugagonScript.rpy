label glucagon_scenario:

with Dissolve(.5)
pause 0.5
scene # next to nav sand courts
with Dissolve(.5)

"""
You and Buzz decided to join intramurals volleyball together!
"""
"""
You two have been practicing together non-stop for the past few weeks in preparation for the first game, which is now!
"""
"""
{i}*Whistle Noise*{/i}
"""
player "We're next! Ready Buzz?"
# insert drowsy buzz
buzz "Yea. I don’t know why but I feel a little shakey…"

menu:
    "Probably just nerves! Just shake ‘em out. I get jittery before games too.":
        jump askingShakey
    "Hm… Maybe check your blood sugar? Just in case ya’ know?":
        jump askingShakey

label askingShakey:
    buzz "The game is about to start though…"
    player "Just. In. Case."
    buzz "Okay. Okay."
    """
    {i}Buzz laughs and goes to check his blood{/i}
    """
    # insert blood sugar monitor screen
    buzz "It’s not ideal, but I feel fine right now!"
    """
    {i}*Whistle Noise*{/i}
    """
    buzz "It should be okay. Let’s go play!"
    player "If you say so..."

with Dissolve(.5)
pause 0.5
scene # on nav sand courts
with Dissolve(.5)

# background volleyball game noize
buzz "*huff huff*"
# insert more tired buzz sprite
player "Yo! Buzz, are you alright??"
buzz "*huff huff* *mumbling*"
"""
{i}You signal to the referee to pause the game and run to Buzz.{/i}
"""
player "Hey Buzz? You doing alright?"
"""
{i}Buzz takes a couple of seconds to catch his breath.{/i}
"""
buzz "I-I don’t t-think so. I-It feels like my h-heart is jumping a mile every s-second."

menu:
    "We practiced too long for you to go down now! Just hold on till the end of the set! We got this!":
        jump continueFaint
    "Oh shoot. Hey, lets go sit down.":
        jump stopFaint

label continueFaint:
    buzz "Yea… We… got this…"
    """
    {i}You motion to the ref to continue the game. After a few unsuccessful rounds, there is a thud. Buzz has fainted! The referee immediately stops the game and everyone runs to help Buzz.{/i}
    """

label stopFaint:
    """
    {i}You offer an arm as support for Buzz and slowly walk over to a nearby bench.{/i}
    """
    """
    {i}Before you two could make it, you feel Buzz slump over. Oh no, Buzz has fainted! You immediately check if he is breathing. {/i}
    """
    """
    {i}He is! You breathe a sigh of relief and gently lay Buzz down. {/i}
    """

player "His blood sugar is way too low! Can someone call 911?"
coach "Already on it!"
"""
{i}Your coach hands over the phone.{/i}
"""
emergencyOperator "Your coach has informed me that your friend has fainted due to hypoglycemia. Could you tell me his current blood sugar?"
    """
    Buzz briefly explained how he checks his blood sugar with a glucometer, but that was a while ago.
    """

    # the player has a choice to check Buzz's blood sugar with or without instructions
    menu:
        "I can do it without help!":
            jump to bloodSugarUnassisted
        "Can you walk me through how?":
            jump to bloodSugarAssisted

label bloodSugarAssisted:
    # TODO: implement assisted blood sugar simulation here...
    jump checkedBloodSugar

label bloodSugarUnassisted:
    # TODO: implement unassisted blood sugar simulation here...
    jump checkedBloodSugar

label checkedBloodSugar:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: choose scene
    with Dissolve(.5)

    player "It reads 35 mg/dL."
    emergencyOperator "Your friend's blood sugar is way too low.  If we don't administer glucagon right now, there is a risk of permanent damage!"
    emergencyOperator "Does your friend carry a glucagon kit with them?"
    """
    You remember an old conversation with Buzz where he told you that he always carried a glucagon kit at the bottom of his bookbag. You immediately grab the kit.
    """
    player "Yes, I have the kit on me right now."
    emergencyOperator "Okay, would you like step by step instructions for administering the glucagon or are you able to administer it unassisted?"

    # the player has a choice to administer glucagon with or without instructions
    menu:
        "I can do it unassisted.":
            jump glucagonUnassisted
        "Please walk me through it!":
            jump glucagonAssisted

label glucagonUnassisted:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: choose scene
    with Dissolve(.5)

    # TODO: implement unassisted glucagon simulation here...
    jump buzzWakesUp

label glucagonAssisted:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: choose scene
    with Dissolve(.5)

    # TODO: implement assisted glucagon simulation here...
    jump buzzWakesUp

label buzzWakesUp:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: choose scene
    with Dissolve(.5)

    """
    Buzz seems to be regaining his consciousness!
    """
    show tiredbuzzsprite:
        zoom 0.40
    buzz "Wha- Why am I on the ground?"
    player "Well uh… you might have fainted because your blood sugar was too low."
    player "Are you feeling alright?"
    buzz "Yeah, just a bit nauseous and tired. Thanks for looking out for me."
    player "Well, lets just get you checked out to make sure no damage was done."
    buzz "Sounds like a plan!"

    # the epilogue...
    """
    You just witnessed Buzz having a hypoglycemic episode.

    Hypoglycemia, or low blood sugar, can occur in individuals with conditions like Type 1 diabetes.

    Symptoms may include shaking, lightheadedness, rapid heartbeat, and even fainting, as you saw with Buzz.

    In such situations, it's crucial to act quickly. If someone exhibits symptoms of hypoglycemia, check their blood sugar levels if possible.

    If it's dangerously low, like Buzz's was at 35 mg/dl, immediate action is needed to prevent permanent damage.

    Administering glucagon, a hormone that raises blood sugar levels, can be life-saving. It's good practice to be educated on how to administer it.

    Remember to always carry a glucagon kit if you have diabetes, and educate those around you on how to use it in case of emergencies.

    Additionally, if someone experiences a hypoglycemic episode, ensure they receive medical attention promptly to assess any potential complications and provide proper care.
    """

return