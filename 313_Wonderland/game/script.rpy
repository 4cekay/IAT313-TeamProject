# Initialization 
init python:
    princess_name = "Posh Voice"
    doll_name = "Childish Voice"
    cat_name = "Alley Cat"

    charlie_bad_1 = False
    charlie_bad_2 = False
    charlie_bad_3 = False

    # Flash Transition
    flash = Fade(0.1, 0.0, 0.25, color="#fff")
    flash_princess = Fade(0.05, 0.0, 0.25, color="#fffad556")
    flash_teddy = Fade(0.05, 0.0, 0.15, color="#93e8ff56")
    flash_charlie = Fade(0.05, 0.0, 0.15, color="#ff989856")

    # Flashback Fade
    flashback_princess = Fade(0.25, 0.0, 0.5, color="#fffad5ff")
    flashback_charlie = Fade(0.25, 0.0, 0.5, color="#ff9898ff")
    flashback_teddy = Fade(0.25, 0.0, 0.5, color="#93e8ffff")

    # Transition Credits: https://lemmasoft.renai.us/forums/viewtopic.php?t=69087
    eyesopen = ImageDissolve("irismask", 0.25)
    eyesclose = ImageDissolve("irismask", 0.1, reverse=True)

    # Filter Modes
    sepia_mode = False
    princess_mode = False

# Player Character Setup
define mc = Character("[player_name]")

# Story Characters Setup
define pr = Character("[princess_name]")
define td = Character ("[doll_name]")
define ch = Character ("[cat_name]")

# Assets Setup
image shot cat_food = Transform("/beginning_scenes/shot cat_food.png", xsize=1920, ysize=1080)
image bg street_blurry = Transform("/backgrounds/bg street_blurry.png", xsize=1920, ysize=1080)

image bg blue_wonderland_dark = Transform("/backgrounds/bg blue_wonderland_dark.png", xsize=1920, ysize=1080)
image bg blue_wonderland_twisted_dark = Transform("/backgrounds/bg blue_wonderland_twisted_dark.png", xsize=1920, ysize=1080)
image bg pink_wonderland_dark = Transform("/backgrounds/bg pink_wonderland_dark.png", xsize=1920, ysize=1080)
image bg green_wonderland = Transform("/backgrounds/bg green_wonderland.png", xsize=1920, ysize=1080)
image bg green_wonderland_dark = Transform("/backgrounds/bg green_wonderland_dark.png", xsize=1920, ysize=1080)
image bg green_wonderland_twisted_dark = Transform("/backgrounds/bg green_wonderland_twisted_dark.png", xsize=1920, ysize=1080)

image bg castle_exterior = Transform("/backgrounds/bg castle_exterior.png", xsize=1920, ysize=1080)
image bg castle_exterior_dark = Transform("/backgrounds/bg castle_exterior_dark.png", xsize=1920, ysize=1080)
image bg castle_interior_nomirror = Transform("/backgrounds/bg castle_interior_nomirror.png", xsize=1920, ysize=1080)
image bg castle_interior_nomirror_dark = Transform("/backgrounds/bg castle_interior_nomirror_dark.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror = Transform("/backgrounds/bg castle_interior_coveredmirror.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror_dark = Transform("/backgrounds/bg castle_interior_coveredmirror_dark.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror_darker = Transform("/backgrounds/bg castle_interior_coveredmirror_darker.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror_evendarker = Transform("/backgrounds/bg castle_interior_coveredmirror_evendarker.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror_neardarkest = Transform("/backgrounds/bg castle_interior_coveredmirror_neardarkest.png", xsize=1920, ysize=1080)
image bg castle_interior_coveredmirror_darkest = Transform("/backgrounds/bg castle_interior_coveredmirror_darkest.png", xsize=1920, ysize=1080)

image mc princess_1 = Transform("/princess_route/mc princess_1.png", xsize=802, ysize=1080)
image princess lipstick = Transform("/princess_route/princess lipstick.png", xsize=1920, ysize=1080)
image princess lipstick_smear = Transform("/princess_route/princess lipstick_smear.png", xsize=1920, ysize=1080)

image teddy crying = Transform("/teddy_route/teddy crying.png", xsize=1920, ysize=1080)
image shot teddy_1 = Transform("/teddy_route/shot teddy_1.png", xsize=1920, ysize=1080)
image shot teddy_2 = Transform("/teddy_route/shot teddy_2.png", xsize=1920, ysize=1080)
image shot teddy_3 = Transform("/teddy_route/shot teddy_3.png", xsize=1920, ysize=1080)
image shot teddy_4 = Transform("/teddy_route/shot teddy_4.png", xsize=1920, ysize=1080)

image bg end_frame_crack = Transform("bg end_frame_crack.png", xsize=1920, ysize=1080)
image bg end_frame_nocrack = Transform("bg end_frame_nocrack.png", xsize=1920, ysize=1080)


# Filters / Effects
transform sepia_filter:
    matrixcolor (TintMatrix("#a98869") * SaturationMatrix(0.25) if sepia_mode else IdentityMatrix())

transform princess_filter:
    #matrixcolor (TintMatrix("#e5b4ebd2") * SaturationMatrix(0) if princess_mode else IdentityMatrix())
    xanchor 0.5
    xpos 0.50
    yalign 0.5
    zoom 0.6

# Three-Sprite Positioning
transform split_left:
    xanchor 0.5
    xpos 0.20
    yalign 1.0
    zoom 0.9  

transform split_center:
    xanchor 0.5
    xpos 0.50
    yalign 1.0
    zoom 0.9

transform split_right:
    xanchor 0.5
    xpos 0.80
    yalign 1.0
    zoom 0.9

transform zoom:
    yalign 2
    zoom 1.5

transform zoom_out:
    xpos 0.25
    ypos 0
    zoom 0.5

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
    mc "(\"Better to be ugly {i}and{/i} employed, than pretty and {i}jobless.{/i}\")"

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
    
    scene black with dissolve

    
    # [LOUD PLOP ONTO GROUND]
    show text "SFX: LOUD PLOP ONTO GROUND" with flash

    menu:
        "OW!":
            pass
    
    mc "Oughhh..."
    mc "That's gonna leave a mark."

    "While waiting for the pounding in your head to quell, you realize the world has gone quiet."
    "..."
    "{i}Too quiet.{/i}"

    mc "(There's no way it's this quiet outside at 7 A.M. on a weekday.)"

    "As you begin to lift your head to investigate the lack of noise, you realize the rest of you needs lifting too."
    "All at once, your senses zone back in, making you very aware of your current face-down, flat-as-a-pancake position on the ground."

    menu:
        "Get UP, loser!":
            scene bg wonderland_dark with eyesopen
            "You scramble up to your feet, dusting yourself off."
            pass

    scene black with eyesclose
    mc "{i}Ohmygosh{/i}, this is so embarrassing."
    mc "I really hope nobody saw that. {w}NOT my finest moment."

    scene bg wonderland_dark with eyesopen
    mc "Where even {i}are{/i} you, Charl-"
    
    scene bg wonderland with dissolve

    mc "{w=1.0}... {w=0.5}\n...{w=0.5}\n..."

    menu: 
        mc "WHERE THE HELL AM I?"
        "The alley..?":
            mc "(No...)"
            mc "(Not unless that alleyway was being used as a front by Willy Wonka.){w}\n(Or maybe the Lorax?)"
            mc "(Oh my {i}god{/i}, [player_name]. Does it really matter right now?!)"
            pass

        "I'm getting punked.":
            mc "Someone's gotta be playing a trick on me right now."
            mc "(But who...?)"

            "You start carefully down the path before you, eyes suspiciously narrowed as you examine your surroundings for signs of danger."

            mc "...{w=0.5}Who am I kidding?"
            mc "I have no friends to punk me!"
            
            "You laugh mockingly at yourself."
            "Perhaps a little too loudly—A bird or two get startled out of the trees nearby."
            "Either that, or they couldn't tell if you were laughing or crying and wanted to give you a moment."
            pass

        "I died.":
            mc "{w=1.5}(My god...)"
            mc "(I'm dead... aren't I?)"
            mc "(It's the only reasonable explanation:){w}\n(I've died and gotten reincarnated in a 5-year-old's colouring book.)"
            mc "(As PUNISHMENT for a life of mediocrity!)"
            pass
        
    "You continue down the road, left with little options outside of marvelling at the mirage of colours making up the world around you."
    mc "Seriously, what {i}is{/i} this place?"

    jump meeting_charlie_5

label meeting_charlie_5:

    $ cat_name = "???"

    ch "{i}[player_name!u]{/i}?!"

    "You whip around in the voice's direction immediately."

    mc "Who's there?!"
    mc "I-I've gotta warn you, you don't wanna mess with me!"
    mc "{w=0.75}(Real convincing, [player_name]. {w=0.35}Now we're really gonna die.)"

    "Nevertheless, you commit to it. What have you got to lose but your life at this point?"
    mc " Don't come closer! I have a yellow belt in Karate!"
    "You get into a flimsy stance, hands ready to chop at any threat."

    "A nearby shuffle clues you in, and you squint as a scraggly cat-like person slowly emerges from behind cover."

    mc "What the—"

    "You drop the stance, taking a cautious step closer to the cloaked figure."

    show charlie shy with dissolve

    $ cat_name = "Cat?"
    ch "What are you doing here, [player_name]?"

    $ cat_name = "Person?"
    ch "How did you even get here?"

    mc "What—"
    mc "Who are you?"
    mc "How do you know my name?"

    "Sensing fear in the creature instead, you slowly continue towards it for a closer look."

    mc "Are those ears... real?"
    mc "What even are you?"

    "The creature winces and begans to back off."
    "Its voice is uncharacteristically timid for a black-cloaked figure emerging from the shadows of Candyland."

    $ cat_name = "Cat-Person?"
    ch "We don't have time for all these questions, [player_name]. \nYou can't be here!"
    ch "You have to go back from where you came!"

    mc "And where is that?"

    show charlie neutral with dissolve
    "You back off from the creature and stomp back to the path, exaggeratedly looking around for a nonexistent exit before hollering back at it."

    mc "As you can see, there aren't exactly any emergency exits around here!"
    mc "I sorta just...{w=0.75} fell from the sky!"

    "The cat-person groans and leaves its station to join you on the path."

    show charlie angry
    $ cat_name = "Annoyed Cat Person"
    ch "You've gotta remember {i}something{/i}.\nPeople don't just end up in a place like this!"

    mc "Well, I do, apparently!"
    
    show charlie neutral with dissolve
    
    "You can't tell whether you're laugh or crying anymore, either."

    mc "I shouldn't even be here!\nI've definitely missed my bus now, dammit!"

    "With no regard for the cat-like person behind you, you begin staggering down the path as your frustrations boil over."

    $ cat_name = "Cat Person"
    ch "W-Wait up!"

    "You don't even turn around when you hear another pair of footsteps start following after yours."

    mc "I don't even know if I {i}can{/i} get to work at this rate!"
    mc "All I did was follow my cat into an alley—"

    ch "{i}[player_name]{/i}..."
    "The creature's voice softens in a way you've heard far too often from the people in your life this year."
    "It feels sorry for you."

    mc "(Right.)"
    
    "You slump down onto ground, right in the middle of the path."

    $ eyesclose = ImageDissolve("irismask", 0.5, reverse=True)
    scene black with eyesclose

    mc "I followed my cat.{w}\nMy {i}dead{/i} cat.{w}\nInto a dark, creepy alleyway!"
    mc "I'm crazy, cat-dude!"
    mc "I don't know what I'm doing or why I'm even here!"

    "You bury your face in your hands, trying very hard not to have a total meltdown in the most colourful place on earth."
    "You hear some soft steps around you, and when you open your eyes..."

    $ eyesopen = ImageDissolve("irismask", 0.75)
    scene bg wonderland_dark with eyesopen
    show charlie neutral_one_hand with dissolve

    "The cloaked creature is crouched down with you, one clawed hand outstretched."

    ch "Come on, [player_name]."

    "You could almost laugh at how incredulous it all feels as you take the creature's hand."

    mc "How do you even know my name again—?"

    "The creature hesitates, averting its single-eyed gaze away for a second as a thought creeps up on you."

    show shot cat_flashback with flash
    pause 1.5
    show shot cat_chase_flashback with flash
    pause 1.5
    show shot gwen_squeeze_flashback with flash
    pause 1.5
    show shot wonderland_transition_flashback with flash
    pause 1.5 

    scene bg wonderland_dark with dissolve
    show charlie neutral_hood

    menu:
        "Charlie?":
            mc "Could it really be you?"
            pass
    
    $ cat_name = "Charlie?"

    show charlie shy with dissolve
    ch "[player_name]..."

    "You take in the creature's appearance in its entirety for a second."
    "Its posture."
    "Its ears."
    "Those claws."
    mc "(That collar...)"

    mc "{w=1.25}It's really you, isn't it?"
    mc "You're my Charlie."

    $ cat_name = "Charlie"

    show charlie neutral with dissolve

    ch "..."
    ch "[player_name], I know this is a lot to take in."

    mc "Your eye."

    ch "...!"

    mc "You got that scar from a nasty stray, right before we rescued you."

    "A flood of emotions begin to fill you, and your hand trembles in Charlie's clawed, yet soft grip."

    mc "(I can't believe it.)"

    "You finally stand up, not letting go of Charlie's hand."
    "You can barely resist the urge to wrap the scruffy little one before you in the biggest hug; if only it wouldn't risk scaring him away."

    mc "How is this even possible? I feel like I'm dreaming..."
    "Your voice is audibly watery now, but you don't care."

    mc "(Does it even matter right now?)"

    menu:
        "I have Charlie back.":
            mc "I've missed you so much, did you know that?"
            mc "I never thought I'd get to tell you that again."
            
            "Despite the tears now spilling from your eyes, you break into the realest smile you've worn in months."
            pass

    ch "[player_name], I'm so sorry."

    mc "No! Nothing was your fault, buddy, not ever."
    mc "I'm just glad to be here with you again."

    scene bg wonderland with dissolve
    "You finally notice the colourful world surrounding you both once more."

    mc "Wherever {i}here{/i} even is, haha."

    "Charlie averts his gaze, looking down at his feet as he gently takes his hand out of your grasp." 
    show charlie neutral_one_hand with dissolve
    "His expression is somber in a way you had yet to see."

    ch "That's just the thing."
    ch "You can't be here with me, [player_name]."

    "You shake your head, shooting down his negativity right away."

    mc "I'm literally right here, Charlie."
    mc "And now that we're together again, I'm not leaving your side if I can help it!"

    show charlie neutral

    ch "Huh? No, I—"

    "You take his hand before he can say another word, a watery laugh escaping you as you pull him along the path, past rows upon rows of luminscent flora."
    
    mc "Loosen up, buddy!"
    mc "You're here with me again, and now we have this entire world to explore together!"
    mc "Totally beats the morning rush, if you ask me."

    ch "[player_name], you're not listening to me."
    show charlie angry with dissolve 
    ch "You can't stay here!"

    mc "Yes, I can! There isn't even a way out!"
    mc "{w=1.0}Maybe this was meant to be."
    mc "Like the universe wanted to give us some more time together."

    show charlie neutral_one_hand with dissolve

    ch "[player_name]..."
    ch "...{w=0.75}You know that's impossible. You don't belong he—"

    show charlie neutral

    "You cut him off before he can say the words you don't want to hear right now. You steel yourself as you march on forward, taking Charlie in the direction of a rainbow mushroom cluster."
    "You look back to him over your shoulder as you walk, forcing a grin in an effort to lift his mood."

    jump meeting_princess_6

label meeting_princess_6:

    scene bg blue_wonderland with dissolve
    mc "Look at those things! Are they native to this place?"

    "The only reply you hear is a startled gasp before you feel yourself collide with something {i}poofy{/i}," 
    show black with flash
    
    "...Sending yourself back to the ground in an inelegant tumble."
    
    pr "Oh my—!"

    mc "{w=1}...{w=1}Urgh."
    mc "(Not again...)"

    pr "Now, what adorable thing has the cat dragged in this time~?"

    "An almost sing-songy voice rings above you, and before you can even look up, you feel a shadow looming over you."

    scene bg blue_wonderland_dark with eyesopen
    pause 1.0
    show princess surprise_both_hands with dissolve
    pause 1.0

    $ princess_name = "???"

    $ princess_name = "Princess"
    "She laughs at your astonishment, helping you up."
    show princess neutral with dissolve

    "Looking up, your eyes get lost in a golden-crowned whirlwind of flouncy pink standing above you."

    mc "(Is that really a princess?)"
    mc "(Even her laugh was melodic.)"
    mc "(Do you think she can talk to birds?){w}\n(Should I ask?)"

    $ princess_name = "Princess"

    show princess surprise_one_hand with dissolve

    pr "It isn’t often I find a poor, unfortunate, lost soul just lying on the ground so close to my castle!"

    show princess smile_one_hand
    pr "What brings you here then?"

    "You do a double take, glancing behind before realizing that she's been talking about {i}you{/i}." 

    mc "Me? Uh, I..."
    mc "Oh, wow. You’re really pretty."
    
    pr "Naturally! Anything less than perfection is hardly worth the effort, no?"

    pr "However did you make it here in such a state anyway? You'd never have been permitted past my gates, you poor thing."
    
    show princess neutral
    scene bg castle_exterior_dark with dissolve
    
    "Suddenly feeling even more out of place, you scramble up, dusting yourself off. You eye the massive pink doors looming above you."

    scene bg castle_exterior with dissolve

    pause 1.0
    
    mc "I don’t really know myself, I was just with a friend and—"

    "You finally realize that your hand had slipped from Charlie's and turn back."

    # show bg 

    "He may as well have vanished into thin air."

    mc "I— He was right here, I don't underst—"

    show princess surprise_one_hand
    pr "A friend! My, how quaint!" 

    show princess surprise_both_hands with dissolve
    pr "Who might that be? Everyone who resides here is, of course, acquainted with me, so I daresay I'll have met them."
    
    show princess smile_one_hand with dissolve
    "The princess leans down, very close, head tilted as she smiles and waves a graceful hand."

    mc "It's alright. I'm sure they're fine."
    mc "{w=1.0}(Okay, she’s a little close.)"
    
    show bg castle_exterior_dark with dissolve
    show princess neutral
    pause 0.75
    mc "(Her smile though... From here, it feels almost familiar...)"
    
    show princess smile with dissolve
    pr "If you say so~"

    show bg castle_exterior with dissolve
    show princess smile_both_hands
    pr "Well anyhow, no need to dwell on that insignificant nonsense now that you’ve met the only one you'll ever need around here!"

    show princess surprise_one_hand with dissolve
    pr "Now, first order of business, we must get you out of those rags!"
    
    mc "({i}Rags?{/i})"

    "You look down at yourself."

    show princess neutral_one_hand with dissolve
    mc "(I guess I must seem like a beggar in comparison, huh? Her shoes alone are probably worth more than my entire lifestyle.)"
    mc "I didn’t bring a change of clothes."
    
    show princess surprise_both_hands with dissolve
    "The princess gives a high, tinkling laugh in response."
    
    pr "Aren't you lucky to have run into me, then!"

    show princess smile_one_hand with dissolve 
    pr "No need to worry your little self about that."
    pr "You'll be coming to join me in the castle. We'll get you fixed up right away."
    
    show princess neutral with dissolve
    mc "(Is there really time for this? I need to find Charlie.)"
    mc "That's very kind of you, but I really should go check on my friend."

    "You pull your gaze away from hers as you move to leave."

    hide princess with dissolve
    show bg castle_exterior_dark with dissolve
    pause 1.5

    show bg castle_exterior with flash_princess
    # SFX : SUDDEN FOOTSTEP
    pr "Oh, there's no need to concern yourself with all that!"

    show princess smile_both_hands with dissolve
    pr "I can handle it all. After all, I do know everyone who knows everyone around here!"

    show princess surprise_one_hand with dissolve
    pr "Aaaaand I'm an exceptionally generous host! You'll be fed, watered, and dressed in something far more suitable, with a touch of sparkle to finish."
    show princess smile_both_hands 
    pr "I’ve a lovely ensemble and jewelry that would suit you perfectly!"

    show bg castle_exterior_dark with dissolve
    mc "(I don’t even remember the last time I was given a gift...)"

    show princess neutral with dissolve
    mc "(But she’s so pink and sparkly. I could never pull off her kind of clothing.)"
    mc "{w=1}(...Would be nice to see what she means though, maybe.)"

    show bg castle_exterior with dissolve
    mc "That sounds lovely, but maybe after I—"

    show princess angry with dissolve
    "The Princess' face darkens slightly before she huffs and begins to turn away."
    pause 0.75 

    show bg castle_exterior_dark with dissolve
    pr "Honestly, turning down royalty?"
    pr "How unbecoming."

    # SFX: A COUPLE FOOTSTEPS, AWAY FROM YOU
    pause 1.0
    show princess neutral_one_hand with dissolve
    pr "But because I'm true to my word, as your {i}gracious{/i} host,{w=0.75}\nand only friend in sight, really,{w=1}\nI'll get everything ready for when you get tired of walking around in {i}all that{/i} and come knocking."
    
    show princess surprise with dissolve
    pr "You best make up your mind quickly, though!"

    hide princess with dissolve
    show bg castle_exterior with flash_princess
    "She swivels toward the castle entrance, not even sparing another glance over her shoulder."
    
    pr "Use the door knocker once you've come to your senses and someone will come fetch you."
    pr "Ta ta~!"

    # SFX: CASTLE DOORS SLAM SHUT
    "The princess saunters back into the castle, humming as the doors slam shut behind her."

    mc "{w=1.0}(...Rich people.)"

    jump meeting_teddy_7

label meeting_teddy_7:

    scene bg blue_wonderland_dark with fade
    "After that unsolicited encounter with the land's reigning primadonna, you find yourself back on one of the paths, picking some lint off of your clothes."

    # SFX: FOOSTEPS

    mc "(Fine, maybe I haven't done laundry in a while, but surely these are a step above {i}rags{/i}...)"

    "You shake your head away from useless thoughts, bringing your attention back up to the scenery before you."
    show bg blue_wonderland with dissolve

    mc "(If I was a magical spirit cat, where would I go to hide from a sparkly princess?)"

    mc "Charlie?"

    # SFX: FURTHER FOOTSTEPS

    mc "CHAR{w=0.5}-LIEEEEEE!"

    "You give a few sheepish looks to a couple toffee-looking squirrels that startle at your hollering."

    mc "Sorry. I'm just looking for my friend, you see."
    mc "Maybe you know him?"
    mc "About yay high, {w}\nmay or may not be cloaked, {w}\nprobably skulking about in the shadows?"

    "In your futile attempts at gathering clues from the nearby fauna, you don't notice the next unlucky obstacle until it's too late."

    show black with flash
    mc "Oof!"

    "It sends you stumbling back, though luckily whatever {i}it{/i} was happened to be soft and squishy enough to keep you on your feet this time."
    show bg blue_wonderland_dark
    hide black with dissolve

    mc "(I swear that wasn't there before.)"
    mc "(...Wait, what did I just bump into?)"
    mc "I don't feel a bruise forming so it couldn't have been one of those lollipop trees-"

    show teddy sprite with flash_teddy
    td "Sorry ma'am!"

    $ doll_name = "Floating Doll Kid?!"
    mc "AHHHHH!"

    show teddy frown_tilt with flash_teddy
    td "AHHHHH!"

    "You nearly trip over your own feet backing away from the {i}armed and floating doll{/i}, who in fairness, seems equally frightened by your scream."

    show bg blue_wonderland with dissolve

    mc "Floating! You—"
    mc "Why are you floating?!"

    show teddy frown with dissolve
    td "Hey! It's not nice to ask why someone's floating!"
    td "It's not like I ask why you're {i}walking!{/i}"

    "You stammer, wracking your headd for a retort, but find yourself too astonished by the bizarre boy before you."

    show teddy smile with dissolve
    td "But it's okay! Everyone makes mistakes, and I'd rather make a new friend today!"

    show bg blue_wonderland with dissolve
    td "I'm Teddy! What's your name?"

    $ doll_name = "Teddy"

    show teddy neutral_tilt with dissolve
    "He examines you with two unmistakeably button eyes."

    td "You know, you kinda look like this other lady I see around sometimes."
    td "But she's always wearing these big, poofy clothes so I don't think she even sees me most days."

    "Though he doesn't give a name, you have an inkling you know precisely who he's referring to."

    mc "I doubt she'd agree, but thanks, I guess."
    mc "I'm uh—"

    "You awkwardly withdraw what was supposed to be a handshake, settling for a little wave instead."

    mc "I'm [player_name]."

    show teddy smile with dissolve
    "The doll boy brightens instantly at your name, floating to your side to join you down the paths."

    # SFX: CONTINUE WALKING

    show bg wonderland with dissolve
    td "Wow! I had a friend named [player_name] too!"

    show teddy frown with dissolve
    td "I haven't seen her in so long, though. I wonder if she even remembers me..."

    "Just as animatedly, he deflates, floating ever-so-slightly slower beside you."

    show bg wonderland_dark with dissolve
    show teddy frown_tilt with dissolve
    mc "It's almost funny, his little frown looks just like..."

    "You chuckle to yourself, squinting at Teddy and his stitched pout."
    
    mc "You remind me a lot of a friend I used to have, too."
    mc "His name was Theodore, but everyone also called him Teddy."
    mc "He was my next-door neighbour, and my best friend."

    show bg wonderland with dissolve 
    show teddy smile with dissolve
    td "No way, me too!"
    show teddy frown
    td "But I like \"Teddy\" way better. \"Theodore\" sounds like it's for grown-ups, yuck!"

    "You can't help but giggle at his childish response."

    show teddy neutral with dissolve
    mc "(Teddy used to say the exact same thing, what are the odds?)"
    
    "You shake your head fondly at the memory of teasing your childhood friend relentlessly."
    "It would be too easy to get lost in nostalgia if it wasn't for this Teddy."

    show teddy frown_tilt 
    td "Don't laugh at me! You're just like my friend, Gwen!"

    scene bg wonderland_dark with flash_teddy
    "Something about his whiny tone rings more than a few bells."

    mc "(For a second there, I swear I heard...)"

    show teddy frown with dissolve

    "You stop walking, cocking your head and squinting at the Teddy floating in place."

    mc "(Y'know... Teddy also had ginger hair.)"
    mc "(And blue eyes.)"
    mc "(And that exact same pout.)"
    
    show teddy neutral with dissolve
    "You take a single step towards him, trying to connect the dots."

    mc "You couldn't be... right?"

    show teddy neutral_tilt with dissolve
    mc "...{w=1}Teddy?"

    td "[player_name]?"

    mc "(If it's possible for Charlie to be here, then what are the odds that—)"

    show teddy neutral with dissolve
    mc "Do you still remember me? [player_name]?"
    mc "I think I might be the [player_name] you knew before too."

    mc "It's just been so long... I haven't seen my Teddy since we were 8, when he moved away."
    mc "Which is why you might not recognize me now, hah!"

    "A familiar ache builds up in your throat as you continue with a slight quiver."

    mc "I grew up!"
    show teddy frown with dissolve
    mc "But I'm still the same [player_name], I promise."
    mc "And I'd never forget you, Teddy."

    show teddy frown_tilt with dissolve
    "You wait for the recognition to arrive on Teddy's face as he peers down at you from where he floats."
    
    "After some grueling moments, his face lights up with the same childlike wonder as earlier."

    show bg wonderland with dissolve
    show teddy smile with dissolve

    td "No way! [player_name]! It really is you!"

    "You smile away the tears beginning to form in your eyes."

    mc "So you recognize me?"
    mc "It's really you?"

    show teddy smile_tilt with dissolve
    td "Of course I do, and of course it is!"

    "He begans to float ahead of you in excitement, looking around from side-to-side."

    show teddy neutral_tilt
    td "Do you see any other \"me\"'s around here, huh?"

    show teddy smile with dissolve
    td "I missed you so much!"

    mc "I missed you more!"
    
    "You can't help the childlike huff that escapes you."

    mc "You promised to write me! I never heard from you again!"
    
    show teddy frown with dissolve
    td "I'm sorry, [player_name]. I guess things got in the way, huh..."

    "Something about that line tugs at your chest, but you shove it aside."

    show teddy smile
    td "But not anymore!"

    mc "What do you mean?"

    td "Now that you're here, we can make up for all that lost time!"

    show teddy neutral with dissolve
    "Teddy develops a mischievous grin that dispels any lingering doubt you may have had."

    td "Starting..."
    pause 1.25

    show teddy candy_hands with flash_teddy
    td "Now!"

    hide teddy with dissolve
    "And just like when you were kids, Teddy takes off without warning, leaving you to catch up with him."

    mc "H-Hey! No fair, you got a headstart, cheater!"

    "You chase after him without a second thought."

    scene bg green_wonderland with fade

    mc "(Finally...)"

    menu: 
        "Gotcha!":
            show bg green_wonderland_dark
            show teddy frown_tilt with flash_teddy
            pause 0.75

            show teddy smile with dissolve
            "Teddy yelps as you tag him, before dissolving into deeply contagious laughter."
            mc "(I haven't laughed like this in forever...)"

    show bg green_wonderland with dissolve
    td "Aw, man! You win!" 
    td "I demand a rematch!"

    "Still catching your breath, you smile up at him with a sorry expression."

    mc "I don't know about that one, Teddy."
    show teddy frown with dissolve

    mc "This was fun, but I still have to go find Charlie, then get to work somehow."
    mc "(If I still have a job after this...)"

    td "Oh, work shmwork! You're such a grown-up now, what happened to my fun friend, [player_name]?"

    show teddy frown_tilt with dissolve
    td "Remember when you'd come over and play? It would always cheer you up!"
    td "You look so tired now...{w}and I missed you!"
    td "So just one more game? {w=0.75}{i}Pleeeeease?{/i}"

    "You take a deep breath, willing yourself not to give in to Teddy's pleading eyes, before a shuffling in your periphery catches your attention."

    jump point_of_no_return
    
label point_of_no_return:
    
    scene bg blue_wonderland_dark with fade

    show charlie neutral_hood with flash_charlie
    ch "...!"

    pause 0.75
    show charlie shy with dissolve
    pause 0.5
    hide charlie with flash_charlie

    mc "(Charlie!)"

    show bg blue_wonderland with dissolve
    "Before you can bolt after him, Charlie disappears into a small forest of candied flora in the distance."

    show bg green_wonderland_dark with dissolve
    show teddy frown with dissolve
    "You turn to Teddy, suppressing a few obscenities in the face of the little boy, and force out what you hope is a cheeky grin."

    mc "Why don't you warm up, Teddy?"
    mc "I'll catch up with ya later, after I go check on something!"

    show teddy frown_tilt
    td "You promise?"

    "He holds out stitched-up pinky."
    "You link your littlest finger with his..."

    mc "Promise."

    "...then take off in Charlie's direction."

    scene bg wonderland with fade

    mc "CHARLIE!"

    show bg wonderland_dark with dissolve 

    mc "Dammit..."
    mc "I lost him."

    "You find yourself atop a hill overlooking the rest of this wondrous, vibrant land."
    show bg wonderland with dissolve

    "Time had flown, but it doesn't hit you until now just how {i}exhausting{/i} all the running around has been."
    "You can't help but chuckle as you hunch over to catch your breath."

    mc "What the hell kind of day has this been, seriously..."

    "You glance up, finding your eyes wandering to the right."

    show bg blue_wonderland with dissolve 
    "They follow the cascade of cotton candy-hued hills..."
    pause 0.5
    show bg blue_wonderland_dark with dissolve
    "...that hold the time last spent with a precious pal."
    pause 0.5
    
    $ sepia_mode = True
    show bg blue_wonderland_twisted_dark at sepia_filter with flashback_charlie
    show charlie neutral_one_hand at sepia_filter with dissolve

    ch "..."
    ch "[player_name], I know this is a lot to take in."

    mc "Your eye."

    ch "...!"

    mc "You got that scar from a nasty stray, right before we rescued you."
    pause 0.75

    hide charlie with dissolve
    $ sepia_mode = False
    show bg wonderland at sepia_filter with flashback_charlie

    pause 0.75
    
    show bg pink_wonderland with dissolve
    "Your eyes trail up the pink-stained land gleaming with crystals..."
    pause 0.75
    show bg castle_exterior with dissolve
    "...all the way up to a magnificent castle that towers above all."

    pause 0.75
    $ sepia_mode = True
    show bg pink_wonderland_dark at sepia_filter with flashback_princess
    show princess smile_both_hands at sepia_filter with dissolve
    pr "Well anyhow, no need to dwell on that insignificant nonsense now that you’ve met the only one you'll ever need around here!"

    show princess surprise at sepia_filter with dissolve
    pr "You best make up your mind quickly, though!"

    $ sepia_mode = False
    hide princess with dissolve 
    show bg wonderland at sepia_filter with flashback_princess

    "Finally, you gaze upon fresh green fields of youth..."
    show bg green_wonderland with dissolve
    pause 1
    show bg green_wonderland_dark with dissolve
    "...where happier times live, with the friend you'd never forgotten."
    pause 0.75

    $ sepia_mode = True
    show bg green_wonderland_twisted_dark at sepia_filter with flashback_teddy

    show teddy frown_tilt at sepia_filter with dissolve
    td "Remember when you'd come over and play? It would always cheer you up!"
    td "You look so tired now...{w}and I missed you!"
    td "So just one more game? {w=0.75}{i}Pleeeeease?{/i}"

    hide teddy with dissolve
    $ sepia_mode = False
    show bg wonderland at sepia_filter with flashback_teddy

    "Emotions well up in your chest as you look upon the horizon and recall the unforgettable encounters you've had in this peculiar land."

    show bg wonderland_dark with dissolve
    
    show charlie smile with dissolve
    "A lost companion, found once more..."
    hide charlie with dissolve

    show princess smile with dissolve
    "Wildest dreams made reality..."
    hide princess with dissolve

    show teddy smile with dissolve
    "The gateway to better times living only in memory..."
    hide teddy with dissolve

    jump final_choice

label final_choice: 
    show charlie neutral at split_left
    show princess neutral at split_center
    show teddy neutral at split_right
    with dissolve

    "The inexplicable draw in your heart has become impossible to ignore."
    "For the first time, you are certain of where the road before you leads."

    menu: 
        "To the forest, reuniting with Charlie at last.":
            hide princess
            hide teddy
            with dissolve

            show charlie neutral_hood at center with dissolve
            pause 1.5

            menu:
                "Are you sure?"
                "Yes.":
                    "Your ending has been written."
                    jump charlie_route_8

                "NO WAIT GO BACK!":
                    "PLEASE click carefully, we don't have all day."
                    jump final_choice


        "To the castle, where the Princess awaits your presence.":
            hide charlie
            hide teddy
            with dissolve

            show princess smile_both_hands at center with dissolve
            pause 1.5

            menu:
                "Are you sure?"
                "Yes.":
                    "Your ending has been written."
                    jump princess_route_8

                "NO WAIT GO BACK!":
                    "PLEASE click carefully, we don't have all day."
                    jump final_choice
            

        "To the greener grass, for sunnier days with Teddy.":
            hide charlie
            hide princess
            with dissolve

            show teddy candy_hands at center with dissolve
            pause 1.5

            menu:
                "Are you sure?"
                "Yes.":
                    "Your ending has been written."
                    jump teddy_route_8

                "NO WAIT GO BACK!":
                    "PLEASE click carefully, we don't have all day."
                    jump final_choice        

label princess_route_8:
    scene bg castle_exterior with fade

    "You arrive at the castle entrance. Even looking up at the tall doors fills you with a strong sense of inadequacy."

    mc "(Do I just knock? This place is {i}way{/i} too fancy for me.)"

    show bg castle_exterior_dark with dissolve
    "One firm thump of the door-knocker is enough to echo through the gates."
    "Almost instantly, there's a scramble of panicked rustling from within. You're ushered inside not even a moment after the doors open."

    scene bg castle_interior_coveredmirror with fade

    "...And find yourself left alone in a very, very bright pink room."

    mc "(Funny, I almost miss the colourful eyesore of the world outside.)"
    pause 1.0

    show bg castle_interior_coveredmirror_dark with dissolve
    # SFX: HEELS CLICK-CLACK DOWN THE HALLWAY
    show text "SFX: HEELS CLICK-CLACK DOWN THE HALLWAY" with dissolve
    pause 0.75

    # SFX: DOOR SLAMS OPEN
    show text "SFX: DOOR SLAMS OPEN" with flash

    mc "...!"

    show princess smile_one_hand with dissolve
    "The Princess makes her grand entrance, still issuing orders to one of her many staff."
    pr "—and set that table, promptly."

    show princess neutral with dissolve
    "When her eyes land on you, one could only describe her as inexplicably pleased with herself."

    show princess neutral_both_hands with dissolve
    pr "Welcome [player_name]!"
    pr "I knew you had a little smarts in that head of yours!"

    mc "Thanks again for the invite." 
    mc "This room is very... {w}pink!"
    
    show bg castle_interior_coveredmirror with dissolve
    show princess surprise_both_hands
    pr "I know, isn't it lovely?"
    pr "And you will have your very own room here! How exciting."
    
    "You blink in confusion."

    mc "Oh, I’m just visiting for the day."

    show princess smile with dissolve
    "The princess laughs, stepping into a closet and rummaging around."
    pause 0.75
    hide princess with dissolve

    pr "Don’t be silly." 
    pr "How could you leave? Anything you could ever want is right here."

    show bg castle_interior_coveredmirror_dark with dissolve
    mc "..."
    mc "(I guess she isn’t wrong?)"

    show princess surprise_both_hands with dissolve
    "The princess emerges from the closet moments later, shoving a pink dress into your hands with a dazzling grin."

    show bg castle_interior_coveredmirror with dissolve

    pr "Well? Go on and change!"

    show princess smile_both_hands
    pr "It’s pink, just like me. We’ll match!"

    mc  "Wait, for me? No no, I couldn't—"

    show princess smile with dissolve
    pr "Of course it's for you, silly."

    show princess smile at zoom with dissolve  
    "The Princess leans in closer, her gaze unsettling."
    show princess neutral at zoom with dissolve

    show bg castle_interior_coveredmirror_dark with dissolve
    pr "All of it is for you."
    pr "Anything, and everything, {w}\nthat you could ever possibly want..."
    pr "{w=0.75}...[player_name]."

    hide princess with dissolve

    show bg castle_interior_coveredmirror with dissolve
    "With a flick of her wrist, the princess whisks the sheet away from the mirror."
    pause 0.35
    show bg castle_interior_nomirror with dissolve
    pause 0.25
    show mirror sprite at zoom_out with flash_princess
    pause 0.75
    
    "There you stand beside her, the two of you framed in gilded glass."

    hide mirror with dissolve
    "She holds the dress over your body, sizing you up in the mirror."
    pause 0.75

    show princess neutral at left with dissolve

    pr "It's perfect, isn't it?"

    "The princess smiles at your reflection, her lips tilting up in a familiar way."
    "For the first time, you notice how similar some of your features are."

    show mc princess_1 at right with dissolve
    "Studying her expression, you try to mimic her smile."
    
    pause 1.0
    hide mc
    show princess smile_both_hands 
    with dissolve

    pr "Well, put it on then!"

    "She leaves the dress in your hands, strolling over to the door."

    hide princess with dissolve

    pr "Don’t keep me waiting too long~"

    "With a rustle of silk, the door closes with a gentle click—"
    "and she's gone."

    "You meet your own gaze back in the glass, and the difference is striking now that you're alone:" 
    show bg castle_interior_nomirror_dark with dissolve
    "The polished appearance you lack; the poise you couldn't fake if you tried."

    mc "(Can I really wear something so pink and eye-catching?)"
    mc "(Even if I put it on, it won’t look as good on me.)"

    "You glance over at the closed door, knowing the Princess waits behind it."
    
    mc "Just hurry up, [player_name]. Stop overthinking."
    mc "(She wouldn't think twice about this.)"

    pause 1.5
    # SFX: GETTING DRESSED FABRIC 

    "You examine your appearance in the mirror, running your hands over the new outfit."

    mc "This is kind of pretty, I think. Maybe I should put a little more effort in the mornings."

    "A dainty knock sounds on the other side of the door."

    pr "Are you finished? I’m coming in!"

    show bg castle_interior_nomirror with dissolve
    show princess neutral with dissolve
    "Stepping back inside, the Princess looks you over, before humming with half-hearted satisfaction."

    show princess neutral_one_hand with dissolve
    pr "Well... {w=1}it’s certainly a {i}start!{/i}" 

    show princess surprise_both_hands with dissolve
    pr "But don’t you just feel so much better already?"

    show bg castle_interior_nomirror_dark with dissolve
    hide princess with dissolve
    "She steps in front of you, blocking your view of the mirror while throwing the cover back on."

    show bg castle_interior_coveredmirror_dark with dissolve

    mc "(Oh, okay.)"
    mc "(I wasn’t really done looking, but I guess it {i}is{/i} her mirror?)"
    
    pause 0.75

    show princess smile_both_hands with dissolve
    pr "No need for that thing anymore!"
    show princess smile_one_hand with dissolve
    pr "At least not while I'm here to give your lucky little self allll the tips you could possibly need!"

    show princess neutral_one_hand
    mc "Ah, alright then."
    mc "I’m just not sure if stuff like this really suits me."

    show princess surprise_both_hands with dissolve
    pr "Not {i}yet{/i}, it doesn't!"
    pr "But just you wait, the makeover has yet to be completed."
    
    show bg castle_interior_coveredmirror_darker with dissolve
    hide princess with dissolve

    pause 1.5
    #SFX: MAKEUP BRUSHING AND STUFF

    pr "We’ll just have to give you a little makeup, {w=0.85}fill in those gaunt cheeks."

    $ princess_mode =  True
    show mc princess_filtered_1 at princess_filter with dissolve

    pr "Isn’t this just so. {w=0.5}Much. {w=0.5}Better!"

    mc "Really? Do I look pretty now?"

    hide mc with dissolve

    show princess smile_both_hands with dissolve
    "The Princess laughs, a hand flying up to cover her mouth."
    "Your eyes catch on her nails: perfectly groomed and lacquered."

    pr "Are you seriously doubting me?"

    show princess surprise_one_hand with dissolve
    pr "Why, we could almost be twins!"

    show princess smile_one_hand
    pr "We’ll have your nails done of course—there’s absolutely no room for sloppiness."

    show bg castle_interior_coveredmirror_evendarker with dissolve
    hide princess with dissolve

    pause 2.0
    #SFX: INCREASINGLY CONCERNING TINKERING NOISE
    
    show mc princess_2 at princess_filter with dissolve

    "You admire your nails, freshly painted with a coat of bubblegum pink."

    mc "(I wonder why I was so hesitant before.)"
    mc "(I look so much better~!)"

    hide mc with dissolve

    show princess smile_one_hand with dissolve
    pr "That’s more like it!" 

    show princess surprise_one_hand
    pr "Now, for a finishing touch:"

    show bg castle_interior_coveredmirror_neardarkest with dissolve
    hide princess with dissolve

    pause 2.0
    #SFX: LIPSTICK CAP, FOOTSTEPS GETTING CLOSER
    
    pr "Every princess needs a signature look, and it’s never complete without lipstick!"
    pr "Lucky for you, I’ve got just the thing!"

    "She pulls out a lipstick bullet from the nearby vanity—one that matches the shade on her lips perfectly."
    pause 0.85

    show princess lipstick with dissolve

    mc "Isn’t this {i}your{/i} colour? Are you sure it matches me?"

    "The Princess' lips twist into a wicked smile."

    pr "{i}Ours{/i} now."

    pause 0.85
    show princess lipstick_smear with dissolve

    #SFX: PUTTING ON LIPSTICK

    pr "Perfect." 
    pr "Aren’t you glad you decided to stay~?"
    pr "There’s absolutely no reason to be elsewhere!"

    hide princess
    show mc princess_3 at princess_filter 
    with dissolve

    mc "You’re right!"
    mc "It’s so nice here, I can’t imagine why I’d want to go back to that tiny, cramped apartment."

    hide mc
    show princess smile_both_hands with dissolve

    mc "Thank you so much, your Highness. I really appreciate everything!"
    mc "I hope my time here will let me grow to be just like you."
    mc "(Just like I always dreamed of.)"

    show princess surprise_both_hands
    "You smile at the Princess, watching your own smile reflected back in her face."
    mc "(No wonder the mirror wasn't necessary anymore!)"

    mc "What’s next then?"

    show bg castle_interior_coveredmirror_darkest with dissolve
    hide princess with dissolve

    pr "Oh, we still have much left to do!"
    pr "Let’s make sure we fix those pesky, sad, and gray eyebags you have." 
    pr "Maybe sharpen those cheekbones!"

    #SFX: VERY CONCERNING SOUND EFFECTS LIKE GO CRAZY PUT CONSTRUCTION SOUNDS FOR ALL I CARE PUT A BUZZSAW
    show text "SFX: VERY CONCERNING SOUND EFFECTS LIKE GO CRAZY PUT CONSTRUCTION SOUNDS FOR ALL I CARE PUT A BUZZSAW" with flash_princess

    pause 2.0
    show princess surprise_one_hand with dissolve
    pr "Anything less than perfection is not acceptable!"
    pause 1.0
    show princess neutral with dissolve
    pause 1.5

    show mc princess_4 at princess_filter with dissolve

    mc "Whatever you say!" 
    mc "We have all the time in the world here now."

    pause 2.5
    
    scene bg end_frame_nocrack with fade
    pause 0.85
    show bg end_frame_crack with flash_princess
    show text "\"THE FAIREST OF THEM ALL\""

    "The End{w=1.5}...?"

    return

label teddy_route_8:
    scene bg green_wonderland with fade

    mc "(Shoot, where did he go?)"
    mc "TEDDY?"
    mc "Teddy! I'm back, let's play!"

    "You spot him at the bottom of one of the hills, slumped down on the grass."
    show bg green_wonderland_dark with dissolve
    mc "Huh? Is he... {w=0.5}crying?"

    "You take a careful step in his direction, careful not to startle him, and hear his sobs grow clearer."
    show teddy frown_tilt with dissolve

    td "[player_name] is taking so long..."
    td "I bet she's not even coming back, is she?"

    "Unsure of what to say, you stay back and let him cry it out for a second."
    "Unfortunately, the longer you wait, the more upset he seems to become."

    show bg green_wonderland_twisted_dark
    show teddy crying
    with dissolve

    td "WAAAA! Where are youuuu, [player_name]?!?"
    td "Did you leave me again?"

    "He lets out a loud sniffle, batting at the grass with his lollipop."

    td "You can have anything here! Why won’t you stay with me?!"
    td "Look—!"
    td "{i}SNIFFLE{/i}"
    td "Even my tears turn into candy when I'm sad, \nso nothing stays forever bad!"

    td "So why didn't you come baaaaaack, [player_name]?!?! {w=0.85}WAAAAAA"

    "Teddy’s high-pitched cries cut through the air, accompanied by the soft clinks of candy falling to the ground."
    
    hide teddy with dissolve
    show bg green_wonderland_dark with dissolve
    mc "Teddy..."
    
    "You watch your old friend with an almost fond exasperation, shaking your head as you slowly make your way closer to him."

    mc "(Some things never change, huh? You're still a total crybaby.)"

    show bg green_wonderland with dissolve

    mc "Hey! Teddy!"
    "You wave wildly in the air as you jog over to his side."

    "Teddy immediately perks up, his frown turning upside-down as he floats up from his spot on the grass."

    show teddy smile_tilt with dissolve
    td "[player_name]?!"

    "Both memories of your old friend and Teddy's infectious excitement in this moment tug at your heartstrings."
    "The scent of sweetness draws you closer and closer, and you can feel your own smile grow childlike alongside Teddy's." 

    td "Yippee!"
    td "You finally came back! I knew you would!"

    mc "(...Right.)"
    mc "Of course I did! I pinky-promised, didn't I?"

    show teddy smile with dissolve
    td "That's right!"
    td "Now we can play together forever and ever!!!"

    "You laugh, patting him on his soft, plush head."
    mc "Forever's a pretty long time, Teddy, but I suppose I can stay a bit longer."

    show teddy neutral
    td "Yeah, yeah, but you've gotta stick around for a long while."
    td "You can have anything here! It's always so bright and beautiful!"
    td "Plus, you'll never grow old with all this—"

    show teddy candy_hands with flash_teddy
    pause 0.5
    td "CANDY!"
    
    hide teddy
    show bg green_wonderland_dark 
    with dissolve
    "You watch in astonishment as Teddy tosses heaps of candy in your direction, watching them land at your feet."
    
    mc "That's... {w=0.75}real candy...!"

    show teddy neutral with dissolve
    td "Duh. Obviously it's real candy, [player_name]."
    td "What's the point of fake candy?"

    "You bite back the urge to ask him if he can even eat candy."
    "Instead, you pick catch a piece, unwrapping it and plopping it into your mouth."

    mc "...!"

    "The taste of citrus and sugar greet your tastebuds, and you turn to Teddy with wide eyes."

    show bg green_wonderland
    mc "This is the best orange candy I've ever had!"

    show teddy smile with dissolve
    td "I know right?!"
    td "And the best part is: {w}I never run out, it's an endless supply!"

    "You quirk an eyebrow up at him as you unwrap another piece."
    show teddy neutral

    mc "For free?"
    mc "How does that even work?"

    show teddy neutral_tilt with dissolve
    "He shrugs, not even sparing a first thought, let alone a second."

    td "I dunno. But does it matter?"

    show bg green_wonderland_dark 
    show teddy neutral 
    with dissolve
    "The simplicity with which he says that has you pondering on it for a second."

    mc "(Well, it's not like there are shops or credit card debt here anyway.)"
    mc  "(And if Teddy has an endless candy supply, who am I to deny the magic, right?)"

    show bg green_wonderland with dissolve
    mc "Huh. I guess not."

    show teddy smile with dissolve
    td "That's right! You don't have to worry about any of that boring adult stuff here with me."
    show teddy smile_tilt with dissolve
    td "So just come play with me for a bit longer!"

    show teddy neutral_tilt
    show bg green_wonderland_dark with dissolve 
    "You feel the grin forming on your lips as you watch Teddy's expectant expression."
    mc "(You've always been impossible to say no to, huh, Teddy?)"

    show bg green_wonderland with dissolve
    mc "Oh, alright, fine! I'll play hooky with you today."
    mc "They probably won't even miss me at work today. I mean, I sure aren't!"
    
    show teddy smile with dissolve
    "You laugh with Teddy as you spit out those words, your shoulders feeling lighter than you have in years."

    mc "Yeah... {w}screw work!"
    mc "I hate that place anyway! Screw taxes and all that!"

    td "Yeah, screw it! Who cares?!"
    "His laughter rises as he copies you, throwing adult responsibilities he probably does not have to the wind."
    "You can't help but simply laugh along with him, letting the wind carry your worries away in the sweet, sweet air."
  
    scene shot teddy_1 with fade
    "Time flies when you're with Teddy, lively days blending into beautiful nights."

    td "Even the sky changes whenever you want!"
    td "With some practice, I'm sure you'll be able to float just like me and reach for the stars."

    mc "I don't know about that one, Teddy."
    mc "I don't think I have the same powers you do. I'm not special, or anything."

    td "WRONG!"

    mc "Huh?"

    td "Not with {i}that{/i} attitude, you won't!"
    td "You just have to {i}believe{/i}, [player_name]."
    td "That's the magic of this place!"

    "He whirls around in the air, stopping to pose and point at the night sky."

    td "There's no real sun to tell you you're late, or make you feel tomorrow creeping up."
    td "Time never has to move forward again, if you don't want it to!"
    
    "He turns to you once more, taking your hand as he begins to float up higher."

    td "So if you wanna fly—"
    td "FLY!"

    "You let him whisk you off, laughing as you run alongside him."
    mc "(The way he speaks and the words he says...)"
    mc "(It's straight out of a storybook.)"

    "You allow yourself one last wistful breath before you let the moment sweep you light off your feet."

    scene shot teddy_2 with fade 

    # SFX:  CHILD LAUGHING SUBTLE
    show text "SFX: CHILD LAUGHING SUBTLE"

    td "Aren't they pretty, [player_name]?"
    td "All these flowers are ours too!"
    td "We can make flower crowns just like we used to, and eat candy until our bellies ache without a care in the world."
    
    mc "That sounds awesome, Teddy!"

    td "Yeah it does! Every day of the week, all the time!"

    mc "Yeah..."
    mc "Every day..."

    "And true to your promises, you do so."
    "Day after day."
    "After day."
    "{w=2}After... {w}\nday."

    #Boredom begins to seep into the crevices of your mind.

    scene shot teddy_3 with fade
    # SFX: CHILD LAUGHING MORE
    show text "SFX: CHILD LAUGHING MORE"

    td "What are you waiting for, [player_name]?!"
    td "Let's go to more places! The further we go, the more fun we have!" 
    td "You wouldn't wanna go back to all that stuff from outside, right? Like before?"
    td "Blegh!" 

    "You muster up a smile for Teddy, but it doesn't quite reach your eyes."
    "Or at least, you don't think it does."
    "It's been a while since you've fixed yourself up for work in front of the mirror."

    mc "Sorry, Teddy. I must've zoned out for a second there."

    "You follow him through the land as per usual, but find that your mind is elsewhere today."

    mc "(...When {i}is{/i} today?)"

    "You wonder how much time has passed as Teddy takes you across the peaks and valleys you've now grown used to."
    "It's uncertain whether the it's the day or the scenery itself that's lost its luster, but amidst the strange flatness of it all, you can't help but wonder..."

    mc "(What would happen if I told Teddy \"no\" for once?)"
    mc "(What would I even do if I'm not playing along with our game anymore?)"

    "Though you voice none of these concerns, Teddy remains as perceptive as ever."
    
    td "Hey, why'd you stop smiling, [player_name]?"
    
    mc "I'm sorry, Teddy. Head in the clouds today, I guess."

    "Teddy huffs, button eyes twisting with frustration."

    td "You're zoning out a lot today, [player_name]!"
    td "We're supposed to be playing together!"

    mc "I know, I'm so—"

    td "No, you're not! And it's not fair!"
    td "Who else is gonna play with you, huh?!"
    td "Your dead cat?!"

    "You're taken aback by his outburst, but its those words specifically that hit way too close for comfort, even with Teddy."

    mc "Hey! Don't you talk about Charlie like that!"

    td "Charlie this, Charlie that!"
    td "I'm so sick of that stupid cat, he's not even here!"
    td "Just forget about Charlie already, [player_name]!"

    "You feel your world slowly go white with anger as Teddy rattles on."

    mc "Teddy, that's ENOU—"

    td "No! You've been like this every day!"
    
    "He takes your hand and begins dragging you along the trail before you can react."

    td "So, y'know what? Come with me!"
    td "I'll find you a new Charlie."
    td "TEN new Charlies, if you want!"
    td "Then we can finally go back to playing together!"
    td "{w=1.5}Just like you promised."

    scene shot teddy_4 with fade

    "Day after day drones on."
    "You sincerely hope they do, at least."
    "Nowadays, it's impossible to tell if even the sunrise or sunset is real."
    "It's only the same games, in the same places, every single minute of every hour of every would-be day."

    td "Why don't you want to play with me anymore?!"
    td "I thought you wanted to forget all that stupid adult stuff and have fun all day long."

    mc "(...)"

    "You stare at Teddy, lips parted but unable to croak out a sound."
    "Talking to him has gotten harder and harder."
    "You watch him drone on and on, but it's as if you can't tell where you end and this world around you begins."

    td "I gave you everything so you wouldn't have to go back to your miserable, boring life, and you're still acting like a baby!"

    "You'd laugh at his temper tantrum, if you could."
    "But you feel nothing but {i}stuck{/i}."
    "In place.{w}\nIn time.{w}\nIn this world."

    "So you stay and listen."

    td "See! No one CARES."
    td "Look around you, [player_name]!"
    td "Nobody wants a washed-up grownup who can't keep up with life anymore just because you had no other friends but your cat."
    
    "Forever,"

    td "You're ruining everything just like you always do!"

    "and ever,"

    td "No wonder you have nobody."
    td "If I wasn't here with you, you'd be all alone again."

    "and ever."

    pause 2.5
    
    scene bg end_frame_nocrack with fade
    pause 0.85
    show bg end_frame_crack with flash_teddy
    show text "\"FOREVER IN EVERLAND\""

    "The End{w=1.5}...?"

    return



label charlie_route_8:
    "Are you sure?"


    return
