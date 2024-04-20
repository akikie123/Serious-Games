init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True
    

label glucagon_scenario:

with Dissolve(.5)
pause 0.5
scene # TODO: scene here
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
    scene # TODO: scene here
    show tiredbuzzsprite:
        zoom 0.40
    buzz "It should be okay. Let’s go play!"
    player "If you say so..."

label afterConvo:
with Dissolve(.5)
pause 0.5
scene # TODO: scene here
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


label bloodSugarAssisted:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: scene here
    with Dissolve(.5)

    # TODO: implement assisted blood sugar simulation here...
    jump checkedBloodSugar

label bloodSugarUnassisted:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: scene here
    with Dissolve(.5)

    # TODO: implement assisted blood sugar simulation here...
    jump checkedBloodSugar
    

label checkedBloodSugar:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: scene here
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
        "I can do it without help!":
            jump glucagonSim
        "Yes, can you walk me through it?":
            jump glucagonSimAssisted

label glucagonSim:

    # STEPS:
    # drag the syringe on top of the vial to fill the vial with the water (go from bottle_front to bottle_water)
    # turn syringe into syringe2 (empty syringe now)
    # shake powder until it is mixed -> change image to bottle_mixed.png
    # drag syringe on top of vial to turn into syringe3 again
    # drag syringe onto buzz thigh to administer glucagon and exit the activity
    # syringe3.png is uncapped syringe
    # syringe2_capped.png is capped syringe pre-filled with glucagon solution

    emergencyOperator "Buzz should have a glucagon kit handy nearby. It should have a glucagon vial and a pre-filled syringe."
    hide phone_talking

    # HANDLE UNCAPPING SYRINGE...
    default btn_selected = False
    show screen uncapSyringe
    while btn_selected == False:
        "Click the syringe to uncap it."
    hide screen uncapSyringe

    # HANDLE DRAGGING SYRINGE ON TOP OF VIAL...
    call screen dragSyringeToVial
    if draggable == "waterSyringe":
        if droppable == "uncappedVial":
            hide screen dragSyringeToVial

    # HANDLE SHAKING VIAL TILL MIXED
    call screen shakeVial
    if draggable == "filledVial": # TODO: fix image here
        if droppable == "invisScreen":
            hide screen shakeVial

    # HANDLE DRAGGING SYRINGE ON TOP OF VIAL TO FILL IT AGAIN
    call screen dragSyringeToVial2
    if draggable == "emptySyringe":
        if droppable == "fullVial":
            hide screen dragSyringeToVial2

    # HANDLE DRAGGING SYRINGE ON BUZZ'S THIGH
    call screen injectBuzz
    if draggable == "filledSyringe":
        if droppable == "buzzThigh":
            hide screen injectBuzz

    jump buzzWakesUp

label glucagonSimAssisted:
    emergencyOperator "Buzz should have a glucagon kit handy nearby. It should have a glucagon vial and a pre-filled syringe."
    emergencyOperator "First, you'll need to uncap the pre-filled glucagon syringe."

    show screen uncapSyringe
    while btn_selected == False:
        "Click the syringe to uncap it."
    hide screen uncapSyringe

    emergencyOperator "Good. Now, you need to inject the pre-filled liquid into the glucagon vial."
    """
    Drag the syringe to the vial to push the pre-filled syringe liquid into the glucagon vial.
    """
    call screen dragSyringeToVial
    if draggable == "waterSyringe":
        if droppable == "uncappedVial":
            hide screen dragSyringeToVial
    
    emergencyOperator "Now that you've injected the contents of the syringe into the vial, shake the vial to mix the liquid and powder."
    call screen shakeVial
    if draggable == "filledVial": # TODO: fix image here
        if droppable == "invisScreen":
            hide screen shakeVial
    
    emergencyOperator "Perfect. Now that the powder and liquid are mixed, we can load the solution back into the syringe to inject."
    """
    Drag the syringe to the vial to load up the syringe with the new solution.
    """
    call screen dragSyringeToVial2
    if draggable == "emptySyringe":
        if droppable == "fullVial":
            hide screen dragSyringeToVial2

    emergencyOperator "Good. Now we're ready to inject. Glucagon should NEVER be injected into a muscle or vein. Let's inject into his thigh."
    """
    Drag the filled syringe to Buzz's thigh to administer the glucagon.
    """
    call screen injectBuzz
    if draggable == "filledSyringe":
        if droppable == "buzzThigh":
            hide screen injectBuzz

    jump buzzWakesUp

label buzzWakesUp:
    with Dissolve(.5)
    pause 0.5
    scene # TODO: add scene here
    with Dissolve(.5)

    show nauseousbuzzsprite:
        zoom 0.40
    """
    Buzz seems to be regaining his consciousness!
    """
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

screen dragSyringeToVial:
        draggroup:
            drag:
                drag_name "uncappedVial"
                child "bottle_front.png"
                xpos 675
                ypos 500
                draggable True
                droppable True
            drag:
                drag_name "waterSyringe"
                xpos 700
                ypos 350
                child "syringe3.png"
                drag_raise True
                draggable True
                droppable False 
                dragged drag_placed

screen uncapSyringe: # manually resize image
        imagebutton:
            xpos 700
            ypos 350
            idle "syringe2_capped.png"
            hover "syringe2_capped.png"
            selected_idle "syringe3.png"
            selected_hover "syringe3.png"
            focus_mask True
            action ToggleVariable("btn_selected", True)  # Toggle only if btn_selected is False
            selected (btn_selected)

screen shakeVial:
    draggroup:
        drag:
            drag_name "filledVial"
            child "bottle_filled.png"
            xpos 675
            ypos 500
            draggable True
            droppable False
            dragged drag_placed
        drag:
            drag_name "emptiedSyringe"
            xpos 700
            ypos 350 
            child "syringe2.png"
            draggable False
            droppable False
        drag:
            drag_name "invisScreen"
            child "invisScreen.png"
            xpos 400
            ypos 500
            draggable False
            droppable True

screen dragSyringeToVial2:
        draggroup:
            drag: 
                drag_name "fullVial"
                child "bottle_mixed.png"
                xpos 675
                ypos 500
                draggable True
                droppable True
            drag:
                drag_name "emptySyringe"
                xpos 700
                ypos 350
                child "syringe2.png" 
                drag_raise True
                draggable True
                droppable False
                dragged drag_placed

screen injectBuzz:
        draggroup:
            drag:
                drag_name "buzzThigh"
                child "buzz_outerthigh.png"
                xpos 0 
                ypos 300
                draggable True
                droppable True
            drag: 
                drag_name "filledSyringe"
                xpos 700
                ypos 350
                child "syringe3.png"
                drag_raise True
                draggable True
                droppable False
                dragged drag_placed