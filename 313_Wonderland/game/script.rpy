# Initialization 
init python:
    princess_name = "Princess"
    doll_name = "Doll Kid"
    cat_name = "Alley Cat"

    met_all = False
    met_pr = False
    met_td = False
    met_ch = False



# Player Character Setup
define mc = Character("[player_name]")

# Story Characters Setup
define pr = Character("[princess_name]")

define td = Character ("[doll_name]")

define ch = Character ("[cat_name]")

# Effects Setup
define flash = Fade(0.1, 0.0, 0.25, color="#fff")

# Assets Setup
image shot cat_food = Transform("/beginning_scenes/shot cat_food.png", xsize=1920, ysize=1080)


# Startup Sequence
label start:

    $ player_name = renpy.input("Who are you?", default="Gwen", length=12)
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Gwen"

    "Always a pleasure, [player_name]."
    "Now…"
    "Rise and shine!"

    jump morning_rush_1


    
label morning_rush_1:
    # 1: Morning Rush

    scene bg bedroom
    with fade

    mc "Ughhh…"

    "Your eyes feel even heavier after a night’s sleep."

    mc "(Psh, if you could even call it that…)"

    "Rays of the early morning sun spill through the blinds, starting the day off with its first pesky chore."

    "You bat an arm in the direction of the window, but the comfort of your bed refuses to release you."

    # [BZZZZZZT] + [OBNOXIOUS RINGTONE]

    mc "(Lord!)"

    "Your phone vibrates violently from the edge of the dresser, buzzing itself down onto the floor where it now lays blaring what may possibly be the worst sound on Earth."

    # [RUSTLING/SHUFFLING]

    mc "One of these days, I’ll change that to something that doesn’t put out my will to live before I get out of bed."

    # [RUSTLING/SHUFFLING]

    mc "What time even is it...?"


    show black
    with flash

    menu: 
        "{w=0.1}6:49"
        "WHAT?":
            pass

        "THAT HAS TO BE A TYPO?":
            pass
            
        "You take that back.":
            pass
    

    mc "Dammit, I’m gonna be late! I’ll have to go for a simpler look—"
    # [DRAMATIC SUSPENSE SOUND EFFECT]
    # [GASP]
    mc "...!"

    show shot bedroom_mirror
    with dissolve

    mc "(I look like a banshee!)"
    mc "(Why does my face look like it lost a fight?)"
    mc "(Not to mention the bush on my head, ew.)"

    scene black
    with fade

    # [ROUGH HAIR BRUSHING]
    show text "SFX: ROUGH HAIR BRUSHING" with fade
    mc "{w=0.35}Cooperate for ONCE…!"

    # [RUMMAGING]
    show text "SFX: RUMMAGING" with fade

    menu:
        mc "(Where did I put my ID?)"
        "{w=0.3}Right, over there!":
            pass

    # [RUMMAGING]
    show text "SFX: MORE RUMMAGING" with fade

    menu:
        mc "(I swear I left that report on the desk.)"
        "That was not there yesterday.":
            pass

    # [THUD + CLASP + ZIP]
    show text "SFX: THUD, CLASP, ZIIIIP" with fade

    menu:
        "That should be everything.": 
            pass

    mc "–Oh!"
    mc "I almost forgot your breakfast, sorry Char–"

    # filler
    show shot cat_food
    with fade

    mc "{w=1.0}–lie."
    mc "..."
    mc "Right."

    menu:
        mc "..."
        "One less chore, I guess.": 
            pass

    scene black
    with fade

    # [DEEP BREATH]
    show text "SFX: DEEP BREATH" with fade
    mc "(Well.)"

    # [DOOR SHUT]
    show text "SFX: DOOR SHUTS" with fade
    # [SPRINTING DOWN THE HALL]
    show text "SFX: SPRINTING DOWN THE HALL" with fade
    mc "(At least I’ll be on time!)"

    jump dead_sprint_2



label dead_sprint_2:
    # 2: Dead Sprint

    scene black

    # [RUNNING DOWN THE STAIRS]
    show text "SFX: RUNNING DOWN THE STAIRS" with fade

    "You fling yourself out the front door, right past the elevator to sprint down the back stairwell and out of the building."
    
    # [BUILDING DOOR OPENING]
    show text "SFX: BUILDING DOOR OPENING" with fade
    # [MORNING RUSH HOUR TRAFFIC, fade in]
    show text "SFX: MORNING RUSH HOUR TRAFFIC, fade in" with fade

    "Just like yesterday, and the day before that."

    scene bg street_blurry
    with fade

    mc "(You know what they say—)"
    mc "(\"Better to be ugly and employed, than pretty and jobless.\")"

    # [CAR HONKS]
    show text "SFX: CAR HONKS" with flash

    menu: 
        mc "(..!)"
        "Flip him off.":
            mc "YEAH, stick it to the pedestrian who's already running, asshole!"

            # [CAR HONKS AGAIN]
            show text "SFX: CAR HONKS AGAIN" with flash

            mc "I'M GOING, JEEZ."
            pass

        "Cross the street faster.":
            mc "Sorry..."
            mc "(This crosswalk has no right being this long at 6 A.M.)"
            pass
            
        "Take your time crossing the street.":
            # [CAR HONKS AGAIN]
            show text "SFX: CAR HONKS AGAIN" with flash

            "You whistle as you reach the other side of the street with a petty spring in your step."
            pass


    # [SPRINTING DOWN THE SIDEWALK]
    "You continue in a dead sprint down to the bus stop."

    scene black
    with flash
    mc "GAH–!!"
    # [SPRINTING COMES TO A SUDDEN STOP.]

    "...until a dark little creature zooms past your feet, nearly tripping you over."

    mc "Hey! Watch it, little guy…"

    scene shot cat
    with fade

    "You regain your balance, glancing up in the direction of the creature, and your eyes meet a sight that freezes every bone in your body still."

    menu:
        "Charlie?": 
            pass
    
    ch "Meow."

    mc "You've really lost it now, [player_name]..."
    mc "No."
    mc "That's impossible."

    menu:
        mc "You're not..."
        "Slowly approach for a closer look.":
            mc "God, you look just like him when he was a baby..."
            
            "The closer you get to the black-coloured kitten, the more you see your best pal in its stead."
            
            mc "Charlie... {w}\nI've missed you so much, bud."
            mc "I still haven't been able to get rid of your bowl, y'know? {w}\nI hate coming home to see your side of the couch empty."

            "You crouch down slowly, trying your best not to get too choked up and spook the cat."

            mc "Come here, buddy... {w}Let's get you home."
            pass

        "Get to work!":
            "You try to shake some sense back into your head, wiping furiously at your eyes."

            mc "I have to go. {w}\nI can't afford to be losing my mind this early on a Wednesday."

            "Taking one last glance at the alley cat, you take a step back, before freezing as its single, but intense gaze meets your own."

            mc "You really are the spitting image of him, though..."
            mc "If it really was you..."

            "Against the better judgement of the past 10 seconds, you step back towards the cat."

            mc "I'd get fired from this crappy job a thousand times. I don't care."
            pass

        "Convince yourself you're just seeing things.":
            "You rub furiously at your eyes, blinking repeatedly up at the morning sky as if it would leave your window to the world squeaky clean."

            mc "I really need to get more sleep, this is insane."

            "You shake your head, running one chilly hand over your face with a defeated chuckle."

            mc "This has gotta be a new low, even for you, [player_name]."
            mc "You see dead people now! {w}\nEr, cats. Dead cats, I guess."
            mc "Hah. {w}As if."
            mc "...Now you're talking to yourself."
            mc "(Let's just get going before this craziness leaks into my work day, god forbid.)"

            pass

    scene shot cat_chase
    with flash

    "Before you can make another move, the cat suddenly perks up and begins to sprint away from you."
            
    menu:
        "CHARLIE!":
            scene black
            with dissolve

            mc "WAIT! Come back!"
            "The cat takes off into the dark alleyway, leaving behind a trail of small pawprints."

            pass
        
    jump alley_chase_3

label alley_chase_3: 
    # 3: Alley Chase

    "Despite the clock ticking closer to the start of your shift, you feel an inexplicable draw towards the creature that was before you moments ago."
    "Without a second thought, {w}\ncrazy as it may be, {w}\nyou find yourself unable to do anything but–"

    menu:
        "RUN AFTER HIM!":
            # [RUNNING INTO ALLEY]
            show text "SFX: RUNNING INTO ALLEY"
            
            "You take off after the cat, abandoning the path to your bus stop and launching into a clumsy pursuit through the dark corridor."
            pass
    
    "The alleyway narrows the further you go in, but like the responsibilities hanging above your head to wish you a lovely morning,"
    "your musty, dilapidated surroundings are out of sight, out of mind."
    "Your focus is trained on nothing but the pawprints ahead of you."
    
    mc "Charlie! Stop-"

    # [STUMBLING STEPS]
    show text "SFX: STUMBLING STEPS"
    # [PANTING]
    show text "SFX: PANTING"

    mc "You know my cardio sucks, Char–!"

    # [TRIP]
    show text "SFX: TRIP" with flash

    mc "WHOA!"

    scene shot gwen_dizzy
    with dissolve

    menu:
        "Ouch.":
            mc "Ugh, that really hurt."
            mc "I knew I shouldn't have worn these boots today..."

            "You get up slowly, hand firm on your now-pounding head."

            pass 
    
    scene black
    with dissolve

    # [DUSTING OFF CLOTHES]
    show text "SFX: DUSTING"

    mc "...Charlie?"

    "You squint back down at the little paw prints, their trail stopping at a wall."

    mc "Damn. A dead en-"

    scene shot tight_alley
    with dissolve

    mc "Oh!"

    "As you reach the wall, the dim light of the alley reveals a dangerously tight opening that offers little more than darkness at first glance."

    menu:
        mc "Uh..."
        "If there's a will, there's a way?":

            scene black with fade
            # [DEEP BREATH]
            show text "SFX: DEEP BREATH" with fade

            "You steel yourself with a shivering inhale, shedding your coat and letting the extra bulk fall onto the ground."
            
            mc "I swear, if my eyes have been playing tricks on me all morning..."
            
            pass
    
    "You begin to squeeze your frame through the gap."
    
    scene shot gwen_squeeze
    with dissolve

    # [SQUEEZING THROUGH TIGHT WALL]
    show text "SFX: SQUEEZING THROUGH TIGHT WALL" with fade

    menu:
        "Charlie!":
            mc "Where are you? {w}Please still be there..."
            pass
    
    menu:
        "Go further.":
            mc "Gah!"
            mc "Where does this even go?"

            "What little illumination the alley had to offer fades as you shuffle deeper into the gap."
            pass
    
    # [SQUEEZING THROUGH TIGHT WALL]
    show text "SFX: SQUEEZING THROUGH TIGHT WALL" 

    mc "You're really giving me a tough time here, huh, Charlie?"
    mc "(At least I'm no stranger to things going sideways...)"

    "You continue struggling towards what you hope is an end to this passageway."
    # glints of neon flash effect ?    

    menu: 
        "Almost!":
            menu:
                "There!":
                    pass
    
    mc "Hold on, Charlie!"

    scene black with flash

    # [SHOVE + FALLS TO THE GROUND THUD]
    show text "SFX: SHOVE + FALLS TO THE GROUND THUD" 

    "Your knees buckle as you reach the end and force yourself out with all your strength, barely catching yourself against the rough brick wall."
    

    "{w=0.5}Every inhale feels shallow, and you feel your eyelids growing heavy as you struggle to focus your vision once more."
    "As you stumble up, you feel the world begin to spin."

    mc "Great. A concussion on top of everyth-"
    
    "As your eyes finish adjusting, you finally notice the sparks and colours beginning to whirl around you."

    mc "Huh?"

    # [WHOOSH]
    show text "SFX: WHOOSH" with flash
    "Before you can take another step, the colourful vortex ramps up violently, seemingly sucking you in with no effort."

    menu:
        "HOLD ON-!":
            scene shot wonderland_transition
            with flash
            
            mc "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
            pass
    
    jump welcome_to_wonderland_4
    
    
label welcome_to_wonderland_4:
    # 4: Welcome to Wonderland
    return
