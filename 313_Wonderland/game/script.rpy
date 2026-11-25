# Initialization 
init python:
    princess_name = "Posh Voice"
    doll_name = "Doll Kid"
    cat_name = "Alley Cat"

    charlie_bad_1 = False
    charlie_bad_2 = False
    charlie_bad_3 = False


    # Transition Credits: https://lemmasoft.renai.us/forums/viewtopic.php?t=69087
    eyesopen = ImageDissolve("irismask", 0.25)
    eyesclose = ImageDissolve("irismask", 0.1, reverse=True)


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
image bg blue_wonderland_dark = Transform("/backgrounds/bg blue_wonderland_dark.png", xsize=1920, ysize=1080)


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
    show princess smile_both_hands with dissolve
    pause 1.0

    $ princess_name = "???"

    "Scrambling up, you're met with the sight of a princess—a real life princess—towering over you with her, looking down with a curious glint in her eye."
    "You do a double take, glancing behind you before realizing that by \"adorable thing\", she meant {i}you{/i}." 

    mc "(Poofy dress, {w=0.5}perfect hair, {w=0.5}shoes worth more than my apartment, probably.)"

    "You suddenly feel {i}very{/i} self-conscious.\nAnd a little starstruck."

    mc "...You're a princess. Like a {i}Princess{/i} princess."

    "She laughs at your astonishment, helping you up."
    show princess neutral with dissolve

    mc "(God, even her laugh is melodic.)"
    mc "(Do you think she can talk to birds? {w}Should I ask?)"

    "Dusting yourself off, you realize that your hand had slipped from Charlie's."

    mc "Oh, you mentioned a cat. Charlie, do you know—"

    "You turn back to Charlie, who may as well have vanished into thin air."

    mc "Charlie?"

    pr "Hm? Are you looking for someone?"

    mc "I— He was right here, I don't underst—"

    "The Princess chuckles and pats you on the head."

    pr "That's no matter, sweetie."
    pr "Lucky for you, you just met the only one you'll need from now on!" 

    "Her tone is so lighthearted, it's almost too easy to overlook how creepily those words could be taken."



    
    

[MC] is in awe, starstruck until the figure notices her and approaches. Upon closer inspection, the she finds her own face smiling down at her. 

[PRINCESS] passive-aggressively comments on [MC]’s appearance, saying she could make a fixer-upper out of her. 

    return
