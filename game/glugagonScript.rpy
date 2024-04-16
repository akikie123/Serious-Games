init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drops[0].drag_name
        store.droppable = drop.drag_name

        return True

label glucagon_scenario:

with Dissolve(.5)
pause 0.5
scene byVolleyballCourt
with Dissolve(.5)

"""
You and Buzz decided to join intramurals volleyball together!
"""
"""
You two have been practicing together non-stop for the past few weeks in preparation for the first game, which is now!
"""
"""
{i}*Whistle*{/i}
"""
player "We're next! Ready Buzz?"
show tiredbuzzsprite: # change to tired buzz sprite
    zoom 0.40
buzz "Yea. I don’t know why but I feel a little shakey…"

menu:
    "Probably just nerves! Just shake ‘em out. I get jittery before games too.":
        jump notWorried
    "Hm… Maybe check your blood sugar? Just in case ya’ know?":
        jump askingShakey

label askingShakey:
    buzz "The game is about to start though…"
    player "Just. In. Case."
    buzz "Okay. Okay."
    """
    {i}Buzz laughs and goes to check his blood sugar{/i}
    """

    show expression "checkBloodSugarImage.png" at right
    buzz "It’s not ideal, but I feel fine right now!"
    """
    {i}*Whistle Noise*{/i}
    """
    hide expression "checkBloodSugarImage.png"
    jump afterConvo

label notWorried:
    scene byVolleyballCourt
    show tiredbuzzsprite:
        zoom 0.40
    buzz "It should be okay. Let’s go play!"
    player "If you say so..."

label afterConvo:
with Dissolve(.5)
pause 0.5
scene volleyballCourt
with Dissolve(.5)

# background volleyball game noize
show verytiredbuzzsprite:
    zoom 0.40
buzz "*huff huff*"
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
    jump afterFaint

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

label afterFaint:

player "His blood sugar is way too low! Can someone call 911?"
coach "Already on it!"
"""
{i}Your coach hands over the phone.{/i}
"""

hide verytiredbuzzsprite
show phone_talking:
    zoom 0.40
emergencyOperator "Your coach has informed me that your friend has fainted due to hypoglycemia. Could you tell me his current blood sugar?"
"""
Buzz briefly explained how he checks his blood sugar with a glucometer, but that was a while ago.
"""

# the player has a choice to check Buzz's blood sugar with or without instructions
menu:
    "I can do it without help!":
        jump bloodSugarUnassisted

    "Can you walk me through how?":
        jump bloodSugarAssisted

# define a screen to handle the drag-and-drop interaction
python:
    def drag_placed(drags, drop):
        if not drop:
            return
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        return True

label bloodSugarAssisted:
    with Dissolve(.5)
    pause 0.5
    scene byVolleyballCourt
    with Dissolve(.5)

    # TODO: implement assisted blood sugar simulation here...
    jump checkedBloodSugar

label bloodSugarUnassisted:
    with Dissolve(.5)
    pause 0.5
    scene byVolleyballCourt
    with Dissolve(.5)

    # TODO: implement assisted blood sugar simulation here...
    jump checkedBloodSugar
    

label checkedBloodSugar:
    with Dissolve(.5)
    pause 0.5
    scene byVolleyballCourt
    with Dissolve(.5)

    show phone_talking:
        zoom 0.40
    player "It reads 35 mg/dL."
    emergencyOperator "Your friend's blood sugar is way too low.  If we don't administer glucagon right now, there is a risk of permanent damage!"
    emergencyOperator "Does your friend carry a glucagon kit with them?"
    """
    You remember an old conversation with Buzz where he told you that he always carried a glucagon kit at the bottom of his bookbag. You immediately grab the kit.
    """
    player "Yes, I have the kit on me right now."
    emergencyOperator "Okay, would you be able to administer the glucagon to Buzz?"

    menu:
        "I can do it!":
            jump glucagonSim

label glucagonSim:
    with Dissolve(.5)
    pause 0.5
    scene byVolleyballCourt
    with Dissolve(.5)

    hide phone_talking

    show buzz_outerthigh at left:
        zoom 0.3

    # HANDLE UNCAPPING SYRINGE...
    default btn_selected = False
    screen uncapSyringe:
        imagebutton:
            idle "syringe2_capped.png"
            hover "syringe2_capped.png"
            selected_idle "syringe3.png"
            selected_hover "syringe3.png"
            focus_mask True
            action ToggleVariable("btn_selected", True)  # Toggle only if btn_selected is False
            selected (btn_selected)

    show screen uncapSyringe

    while btn_selected == False:
        "Click the syringe to uncap it."

    # HANDLE DRAGGING SYRINGE ON TOP OF VIAL...
    # create draggroups with a draggable uncapped syringe and the glucagon vial

    hide screen uncapSyringe
    default draggedSyringe = False
    screen dragSyringeToVial:
        fixed:
            draggroup:
                drag:
                    drag_name "uncappedVial"
                    xpos 100
                    ypos 100
                    child "bottle_front.png"
                    draggable True
                    droppable True
                drag:
                    drag_name "waterSyringe"
                    xpos 100
                    ypos 100
                    child "syringe3.png"
                    draggable True
                    droppable True
    
    show screen dragSyringeToVial
    while draggedSyringe == False:
        "Drag the syringe to the vial to push the pre-filled syringe liquid into the glucagon vial."

    pause 10000

    # syringe3.png is uncapped syringe
    # syringe2_capped.png is capped syringe pre-filled with water

    # STEPS:
    # click the syringe to uncap it (go from syringe2_capped to syringe3)
    # drag the syringe on top of the vial to fill the vial with the water (go from bottle_front to bottle_water)
    # turn syringe into syringe2 (empty syringe now)
    # shake powder until it is mixed -> change image to bottle_mixed.png
    # drag syringe on top of vial to turn into syringe3 again
    # drag syringe onto buzz thigh to administer glucagon and exit the activity




    pause 1000
    jump buzzWakesUp

label buzzWakesUp:
    with Dissolve(.5)
    pause 0.5
    scene byVolleyballCourt
    with Dissolve(.5)

    """
    Buzz seems to be regaining his consciousness!
    """
    show nauseousbuzzsprite:
        zoom 0.40
    buzz "Wha- Why am I on the ground?"
    player "Well uh… you might have fainted because your blood sugar was too low."
    player "Are you feeling alright?"
    buzz "Yeah, just a bit nauseous and tired. Thanks for looking out for me."
    player "Well, lets just get you checked out to make sure no damage was done."
    show tiredbuzzsprite:
        zoom 0.40
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