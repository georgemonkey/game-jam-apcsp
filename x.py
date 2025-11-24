import os
import time
import random
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_dots(count=3):
    for _ in range(count):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def draw_intro_scene():
    clear_screen()
    intro = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                        ██████╗ ██████╗  ██████╗ ██████╗                     ║
║                        ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗                    ║
║                        ██║  ██║██████╔╝██║   ██║██████╔╝                    ║
║                        ██║  ██║██╔══██╗██║   ██║██╔═══╝                     ║
║                        ██████╔╝██║  ██║╚██████╔╝██║                         ║
║                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                         ║
║                                                                              ║
║                              🎮 ESCAPE FROM PARTH 🎮                         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(intro)
    time.sleep(0.8)
    slow_print("    You picked up a strange glowing textbook...")
    time.sleep(0.5)
    slow_print("    And got sucked into a homework dimension!")
    time.sleep(0.8)
    
    print("\n")
    parth_intro = """
                        ___________________
                       /                   \\
                      |      ◉     ◉       |
                      |         ◡           |
                      |      \\_______/      |
                       \\_________________/
                            |__|
                           |____|  <- Goatee
"""
    print(parth_intro)
    time.sleep(0.5)
    slow_print("\n    A teenage boy appears - it's PARTH!")
    time.sleep(0.5)
    slow_print("    He's obsessed with homework and sports a magnificent goatee.")
    time.sleep(0.8)
    
    print("\n")
    slow_print("    Parth: \"Welcome to MY domain!\"")
    time.sleep(0.5)
    slow_print("    Parth: \"To escape, you must pass through 5 STAGES.\"")
    time.sleep(0.5)
    slow_print("    Parth: \"Each stage has a riddle and three doors.\"")
    time.sleep(0.5)
    slow_print("    Parth: \"Answer correctly to reveal the safe door.\"")
    time.sleep(0.5)
    slow_print("    Parth: \"Choose wrong and face BATTLE or be trapped FOREVER!\"")
    time.sleep(0.5)
    slow_print("    Parth: \"MUHAHAHA!\"")
    time.sleep(1)
    input("\n    Press ENTER to begin your escape...")

def draw_stage_scene(stage):
    clear_screen()
    
    stage_names = [
        "THE LIBRARY OF INFINITE HOMEWORK",
        "THE CLASSROOM OF ETERNAL TESTS",
        "THE LABORATORY OF FORMULAS",
        "THE GYMNASIUM OF PE WORKSHEETS",
        "PARTH'S HOMEWORK THRONE ROOM"
    ]
    
    stage_art = [
        "📚 📚 📚 📚 📚 📚 📚 📚",
        "🪑 📝 🪑 📝 🪑 📝 🪑 📝",
        "🧪 🧬 ⚗️ 🔬 📊 📈 🧪",
        "🏀 📋 ⚽ 📋 🏈 📋 🎾",
        "👑 📚📚📚 📚📚📚📚 👑"
    ]
    
    scene = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          STAGE {stage + 1} OF 5                                         ║
║                   {stage_names[stage]:^60}      ║
║                                                                              ║
║          {stage_art[stage]:^68}║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(scene)

def draw_parth_riddle(stage, riddle):
    parth = """
                        ___________________
                       /                   \\
                      |      ◉     ◉       |
                      |         <           |
                      |      \\_____/        |
                       \\_________________/
                            |__|
                           |____|  <- Goatee
    """
    print(parth)
    
    taunts = [
        "\"This riddle separates the geniuses from the mediocre!\"",
        "\"I solved this in 3 seconds. How long will YOU take?\"",
        "\"Most students fail this one. Will you?\"",
        "\"Careful now... think VERY carefully!\"",
        "\"This is my FAVORITE riddle! MUHAHAHA!\"",
    ]
    
    print(f"\n    Parth: {taunts[stage]}\n")
    
    speech_bubble = f"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║  {riddle['question']:^69} ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """
    print(speech_bubble)
    
    print(f"\n    💡 Hint: {riddle['hint']}\n")

def draw_riddle_options(riddle):
    print("    Your options are:")
    print(f"    {riddle['options'][0]}")
    print(f"    {riddle['options'][1]}")
    print()

def draw_three_doors(safe_revealed, safe_door_name):
    print("\n    Three mysterious doors appear before you...\n")
    
    if safe_revealed:
        print(f"    💡 You know the SAFE door is: {safe_door_name}\n")
    
    door_art = """
        🚪 DOOR 1              🚪 DOOR 2              🚪 DOOR 3
         [LEFT]                [MIDDLE]                [RIGHT]
      
      _____________          _____________          _____________
     |  _______  |          |  _______  |          |  _______  |
     | |       | |          | |       | |          | |       | |
     | |   1   | |          | |   2   | |          | |   3   | |
     | |_______| |          | |_______| |          | |_______| |
     |    ___    |          |    ___    |          |    ___    |
     |   |___|   |          |   |___|   |          |   |___|   |
     |___________|          |___________|          |___________|
    """
    print(door_art)

def timing_battle(stage):
    clear_screen()
    print("="*80)
    print(" "*25 + "⚔️  BATTLE MODE ACTIVATED! ⚔️")
    print("="*80)
    
    battle_scene = """
                        YOU                              PARTH
                    ___________                      ___________________
                   /           \\                    /                   \\
                  |  O     O   |                  |      ◉     ◉       |
                  |      ^     |       VS         |         <           |
                  |   \\_____/  |                  |      \\_____/        |
                   \\_________/                     \\_________________/
                                                        |__|
                                                       |____|
    """
    print(battle_scene)
    
    challenges = [
        "\"SOLVE THIS CALCULUS PROBLEM... IN YOUR HEAD!\"",
        "\"RECITE THE PERIODIC TABLE... BACKWARDS!\"",
        "\"FACTOR THIS POLYNOMIAL... WHILE DOING JUMPING JACKS!\"",
        "\"PROVE THE PYTHAGOREAN THEOREM... USING ONLY EMOJIS!\"",
        "\"COMPLETE MY ULTIMATE HOMEWORK CHALLENGE!\"",
    ]
    
    slow_print(f"\n    Parth: {challenges[stage % len(challenges)]}")
    print("\n" + "="*80)
    print(" "*20 + ">>> TIMING MINI-GAME <<<")
    print("="*80)
    print("""
    INSTRUCTIONS:
    Watch the X move across the bar. Press ENTER when X is in the TARGET ZONE!
    
    Target Zone: [░░░X░░░]
    """)
    
    input("    Press ENTER when ready...")
    print("\n    Get ready")
    animate_dots()
    
    bar_length = 21
    target_start = 9
    target_end = 12
    
    position = random.randint(0, bar_length - 1)
    direction = random.choice([-1, 1])
    speed = 0.12
    
    print("\n    ⚡ THE X IS MOVING! ⚡\n")
    
    import threading
    hit_pressed = threading.Event()
    final_position = [position]
    
    def wait_for_enter():
        input()
        hit_pressed.set()
    
    input_thread = threading.Thread(target=wait_for_enter, daemon=True)
    input_thread.start()
    
    moves = random.randint(15, 25)
    for i in range(moves):
        if hit_pressed.is_set():
            break
            
        bar = ['═'] * bar_length
        
        if target_start <= position <= target_end:
            for j in range(target_start, target_end + 1):
                if j != position:
                    bar[j] = '░'
        
        bar[position] = 'X'
        
        bar_str = ''.join(bar)
        print(f'\r    [{bar_str}]', end='', flush=True)
        time.sleep(speed)
        
        position += direction
        if position >= bar_length:
            position = bar_length - 1
            direction = -1
        elif position < 0:
            position = 0
            direction = 1
        
        final_position[0] = position
    
    if not hit_pressed.is_set():
        print("\n\n    >>> PRESS ENTER NOW! <<<")
        hit_pressed.wait()
    
    success = target_start <= final_position[0] <= target_end
    
    print("\n")
    if success:
        print("    " + "="*70)
        print("    " + " "*25 + "✅ PERFECT HIT! ✅")
        print("    " + "="*70)
        slow_print("\n    You defeated Parth's challenge!")
        slow_print("    Parth: \"Impossible! Fine, you may pass...\"")
        input("\n    Press ENTER to continue...")
        return True
    else:
        print("    " + "="*70)
        print("    " + " "*25 + "❌ MISSED! ❌")
        print("    " + "="*70)
        slow_print("\n    You missed the target zone!")
        slow_print("    Parth: \"FAILURE! You're trapped forever!\"")
        return False

def present_riddle(stage):
    riddles = [
        {
            "question": "I have keys but no locks. I have space but no room. You can enter but can't go inside. What am I?",
            "options": ["A. Keyboard", "B. Piano"],
            "correct": "A",
            "hint": "You're using one right now to play this game...",
            "explanation": "A keyboard has keys, a space bar, and an enter key!"
        },
        {
            "question": "What has hands but cannot clap?",
            "options": ["A. Clock", "B. Statue"],
            "correct": "A",
            "hint": "It helps you tell when homework is due...",
            "explanation": "A clock has hands (hour and minute hands) but cannot clap!"
        },
        {
            "question": "I'm tall when I'm young and short when I'm old. What am I?",
            "options": ["A. Candle", "B. Tree"],
            "correct": "A",
            "hint": "I provide light and melt as I age...",
            "explanation": "A candle is tall when new and gets shorter as it burns!"
        },
        {
            "question": "What has a head and tail but no body?",
            "options": ["A. Coin", "B. Snake"],
            "correct": "A",
            "hint": "You flip it to make decisions...",
            "explanation": "A coin has heads and tails sides but no body!"
        },
        {
            "question": "What gets wetter the more it dries?",
            "options": ["A. Towel", "B. Sponge"],
            "correct": "A",
            "hint": "You use it after a shower...",
            "explanation": "A towel gets wetter as it dries you off!"
        }
    ]
    
    riddle = riddles[stage]
    
    # Randomize door assignments ONCE at the start and keep them fixed
    door_assignments = ["safe", "battle", "death"]
    random.shuffle(door_assignments)
    
    door_map = {
        "1": door_assignments[0],
        "2": door_assignments[1],
        "3": door_assignments[2]
    }
    
    safe_door_num = None
    for door_num, outcome in door_map.items():
        if outcome == "safe":
            safe_door_num = door_num
            break
    
    door_names = {
        "1": "Door 1 (Left)",
        "2": "Door 2 (Middle)",
        "3": "Door 3 (Right)"
    }
    
    safe_door_name = door_names[safe_door_num]
    
    draw_stage_scene(stage)
    time.sleep(0.5)
    slow_print("\n    Parth appears before you...")
    time.sleep(0.8)
    input("\n    Press ENTER to face Parth's challenge...")
    
    clear_screen()
    draw_stage_scene(stage)
    time.sleep(0.3)
    draw_parth_riddle(stage, riddle)
    time.sleep(0.5)
    draw_riddle_options(riddle)
    
    answer = ""
    while True:
        answer = input("    Your answer (type A or B): ").strip().upper()
        if answer in ["A", "B", "KEYBOARD", "PIANO", "CLOCK", "STATUE", "CANDLE", 
                      "TREE", "COIN", "SNAKE", "TOWEL", "SPONGE"]:
            word_to_letter = {
                "KEYBOARD": "A", "PIANO": "B",
                "CLOCK": "A", "STATUE": "B",
                "CANDLE": "A", "TREE": "B",
                "COIN": "A", "SNAKE": "B",
                "TOWEL": "A", "SPONGE": "B"
            }
            if answer in word_to_letter:
                answer = word_to_letter[answer]
            break
        else:
            print("    Invalid input! Please enter A or B, or type the full answer.")
    
    print()
    time.sleep(0.5)
    if answer == riddle["correct"]:
        slow_print("    ✓ CORRECT!")
        time.sleep(0.3)
        slow_print(f"    {riddle['explanation']}")
        time.sleep(0.5)
        slow_print(f"    The safe door is: {safe_door_name}")
        safe_revealed = True
    else:
        slow_print("    ✗ WRONG!")
        time.sleep(0.3)
        slow_print(f"    The correct answer was: {riddle['correct']}")
        time.sleep(0.5)
        slow_print("    Parth: \"WRONG! Now you must choose blindly!\"")
        safe_revealed = False
    
    time.sleep(0.8)
    input("\n    Press ENTER to approach the doors...")
    
    clear_screen()
    time.sleep(0.3)
    draw_three_doors(safe_revealed, safe_door_name)
    
    door_choice = ""
    while True:
        door_choice = input("\n    Which door do you choose? (type 1, 2, or 3): ").strip()
        if door_choice in ["1", "2", "3"]:
            break
        else:
            print("    Invalid input! Please enter 1, 2, or 3 only.")
    
    print()
    time.sleep(0.5)
    outcome = door_map[door_choice]
    
    if outcome == "safe":
        slow_print("    The door opens smoothly... Golden light shines through!")
        time.sleep(0.5)
        slow_print("    ✨ You pass through SAFELY to the next stage! ✨")
        time.sleep(0.8)
        input("\n    Press ENTER to continue...")
        return "safe"
    elif outcome == "battle":
        slow_print("    The door EXPLODES open! Parth appears!")
        time.sleep(0.5)
        slow_print("    📚💥 BATTLE MODE! 💥📚")
        time.sleep(0.8)
        input("\n    Press ENTER to battle...")
        if timing_battle(stage):
            return "safe"
        else:
            return "death"
    else:
        slow_print("    The door opens to INFINITE HOMEWORK!")
        time.sleep(0.5)
        slow_print("    Papers swirl around you! You're being pulled in!")
        time.sleep(0.5)
        slow_print("    💀 TRAPPED IN THE HOMEWORK VOID! 💀")
        time.sleep(1)
        return "death"

def game_over_win():
    clear_screen()
    time.sleep(0.5)
    win_screen = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊  VICTORY!  🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉                    ║
║                                                                              ║
║                                                                              ║
║                        ___________________                                   ║
║                       /                   \\                                 ║
║                      |      O     O       |     <- YOU WIN!                 ║
║                      |         ^          |                                 ║
║                      |      \\_____/       |                                 ║
║                       \\_________________/                                   ║
║                             \\|/                                             ║
║                              |                                               ║
║                             / \\                                             ║
║                                                                              ║
║                        YOU ESCAPED PARTH!                                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(win_screen)
    time.sleep(0.8)
    slow_print("    You solved all 5 riddles and made it through every door!")
    time.sleep(0.5)
    slow_print("    The homework dimension releases you back to reality.")
    time.sleep(0.8)
    
    print("\n")
    parth_defeated = """
                        ___________________
                       /                   \\
                      |      -     -       |     <- Parth (defeated)
                      |         o          |
                      |      \\_____/       |
                       \\_________________/
                            |__|
                           |____|
"""
    print(parth_defeated)
    time.sleep(0.5)
    slow_print("\n    Parth: \"You... you actually did it. Fine. You're free to go.\"")
    time.sleep(0.5)
    slow_print("    Parth: \"But remember... homework is ETERNAL! MUHAHAHA!\"")
    time.sleep(0.8)
    
    print("\n")
    slow_print("    You tumble back onto the sidewalk. The glowing book is gone.")
    time.sleep(0.5)
    slow_print("    Freedom at last! No more Parth! No more homework dimension!")
    time.sleep(0.8)
    
    print("\n")
    print("                        🏆 CONGRATULATIONS! 🏆")
    print()

def game_over_lose():
    clear_screen()
    time.sleep(0.5)
    lose_screen = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                          💀 GAME OVER 💀                                     ║
║                                                                              ║
║                                                                              ║
║                        ___________________                                   ║
║                       /                   \\                                 ║
║                      |      X     X       |     <- YOU (trapped)            ║
║                      |         o          |                                 ║
║                      |      \\_____/       |                                 ║
║                       \\_________________/                                   ║
║                                                                              ║
║                   YOU ARE TRAPPED FOREVER                                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(lose_screen)
    time.sleep(0.8)
    slow_print("    Papers swirl endlessly. Textbooks pile to infinity.")
    time.sleep(0.5)
    slow_print("    The sound of pencils scratching echoes eternally.")
    time.sleep(0.8)
    
    print("\n")
    parth_victory = """
                        ___________________
                       /                   \\
                      |      ◉     ◉       |     <- Parth (victorious)
                      |         <          |
                      |      \\_____/       |
                       \\_________________/
                            |__|
                           |____|
"""
    print(parth_victory)
    time.sleep(0.5)
    slow_print("\n    Parth: \"MUHAHAHA! Another student trapped in my realm!\"")
    time.sleep(0.5)
    slow_print("    Parth: \"You'll do homework FOREVER! Calculus! Essays!\"")
    time.sleep(0.5)
    slow_print("    Parth: \"Chemistry! History! ALL OF IT! ETERNALLY!\"")
    time.sleep(0.8)
    
    print("\n")
    slow_print("    He hands you a stack of worksheets that reaches the ceiling.")
    time.sleep(0.8)
    
    print("\n")
    slow_print("    Your fate is sealed. The homework dimension claims you.")
    time.sleep(0.5)
    slow_print("    Forever solving problems. Forever writing essays.")
    time.sleep(0.5)
    slow_print("    Forever trapped with Parth and his magnificent goatee.")
    time.sleep(0.8)
    
    print("\n")
    print("                        📚 TRAPPED FOREVER 📚")
    print()

def main():
    draw_intro_scene()
    
    for stage in range(5):
        result = present_riddle(stage)
        if result == "death":
            game_over_lose()
            play_again = input("\n    💀 Try again? (yes/no): ").strip().lower()
            if play_again == "yes":
                main()
            return
    
    game_over_win()
    play_again = input("\n    🎮 Play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()

if __name__ == "__main__":
    main()