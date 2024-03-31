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