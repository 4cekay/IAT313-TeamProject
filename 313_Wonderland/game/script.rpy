init python:
    princess_name = "Princess"
    doll_name = "Doll Kid"
    cat_name = "Catboy"

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



label start:

    $ player_name = renpy.input("Enter your name.", default="Gwen", length=12)
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Gwen"


    scene bg bedroom
    with fade

    "This is your room."

    mc "Oh girl, ew."

    "Yeah. Clean up while we meet the rest of the cast, why don't you?"

    mc "Hold on now--"

    "No time, we only got 4 weeks for this."

    show bg shot_bedroom_mirror
    with dissolve

    mc "This? What's this? What cast? Wait--"

    "All in due time, [player_name]. Enjoy~!"

    mc "WAIT COME BA-"

    show bg shot_wonderland_transition
    with dissolve

    mc "AHHHHHHHHHHHHHHHHHHHHHHHH-"

    scene bg blue_wonderland
    with dissolve

    mc "Ow."
    
    "Moment of truth, [player_name]."
    
    menu:
        "Who do you want to meet first?"

        "The Perfect Me.":
            jump meet_princess

        "The friend in my most precious memories.":
            jump meet_teddy
        
        "My best buddy that I miss every day.":
            jump meet_charlie


    label meet_princess:
        scene bg pink_wonderland
        with fade

        mc "Goddamn, this place is bright."

        show princess smile_onehand
        pr "Oh? And who might this cutie be?"

        mc "H-Huh?"
        
        show princess neutral_onehand
        pr "It's been a while since anyone's dropped by my land."

        show princess smile_bothhands
        pr "Must be my lucky day!"

        mc "(A princess?! A real live princess?)"
        mc "(I must be dreaming...)"

        mc "I'm sorry, miss. I just..."

        "You scratch your head awkwardly, taking in your surroundings."
        "It looks straight out of a storybook. You've never seen anything like it."

        mc "...have no idea how I got here, actually."

        show princess surprise
        pr "Haha! And you're funny too!"

        show princess neutral
        "She extends one dainty, perfectly manicured hand."

        pr "Well, come on, darling-- Don't just stay there on the ground."

        mc "R-Right. Sorry."

        "As you take her hand and let her pull you up, you catch a closer look at her face."
        show princess smile_onehand
        mc "(She feels... familiar, somehow.)"
        "You cock your head, squinting up at her as you try to remember."

        show princess neutral
        mc "This might sound crazy, but..."
        mc "Have we met before?"
        mc "I feel like I know you."

        show princess surprise_onehand
        pr "My! You're quite the flatterer, aren't you?"
        mc "That's not what I meant-"

        show princess smile_onehand
        pr "Don't you worry, darling."
        show princess neutral
        pr "I could never forget a face like yours."
        show princess smile
        pr "So this must be our first time meeting!"

        "The longer she speaks, the fewer words you hear, her voice getting lost with the fogginess in your mind."
        show princess neutral
        "She stares so intently at you that you can almost see your own reflection through her eyes."
        "That's when it hits you."

        mc "(Hold on-!)"

        show princess smile_onehand
        pr "Though, I suppose you could say..."

        mc "(She kinda looks just like-)"

        show princess surprise
        $ princess_name = "P-Prin-"
        pr "...that here in Wonderland..."

        scene bg shot_tight_alley
        with dissolve
        show princess closeup
        with fade
        $ princess_name = "Princess Gwen?"
        pr "We're all one and the same."

        mc "NO-"

        






    

    return
