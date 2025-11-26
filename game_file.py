import os
import sys
import time
import random
import threading

# --- Terminal UI helpers ---

def clear_screen():
    """Clears the terminal screen depending on OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

class Col:
    """ANSI colors for chill text effects"""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"

def slow_print(text, delay=0.02):
    """Prints text char by char for that dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_dots(count=3, delay=0.35):
    """Simple loading dots animation"""
    for _ in range(count):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def boxed(text):
    """Prints text in a neat ASCII box"""
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    top = '╔' + '═' * width + '╗'
    bot = '╚' + '═' * width + '╝'
    out = [top] + [f'║ {line.ljust(width - 2)} ║' for line in lines] + [bot]
    return '\n'.join(out)

# --- Game Data ---

riddles = [
    {"question":"I speak without a mouth, and hear without ears. I have no body, but I come alive with movement of air.",
     "options":["A) Echo","B) Ghost"], "answer":"A", "hint":"You only hear it after you make noise."},
    {"question":"I can be cracked, made, told, and played. I can break tension but never bones.",
     "options":["A) A Joke","B) A Code"], "answer":"B", "hint":"Some people are terrible at these."},
    {"question":"The more you take, the more you leave behind. What am I?",
     "options":["A) Footsteps","B) Memories"], "answer":"A", "hint":"Sherlock Holmes would follow these."},
    {"question":"I am always hungry and must be fed. The finger I touch will soon turn red. What am I?",
     "options":["A) Fire","B) Rust"], "answer":"B", "hint":"Too close and your hand becomes medium-rare."},
    {"question":"I have cities but no houses, forests but no trees, and water but no fish. What am I?",
     "options":["A) A Map","B) A Painting"], "answer":"A", "hint":"Flat version of the world."}
]

stages = [
    {"name":"Library of Infinite Homework","art":"📚 📚 📚 📚"},
    {"name":"Classroom of Eternal Tests","art":"🪑 📝"},
    {"name":"Laboratory of Formulas","art":"🧪 🔬"},
    {"name":"Gymnasium of PE Worksheets","art":"🏀 📋"},
    {"name":"Parth's Homework Throne Room","art":"👑 📚"}
]

# --- Game State ---
state = {
    "inventory": [],   # hold lucky charms
    "courage": 3,      # not really used but could be for extensions
    "stage_safe_doors": {}  # maps stage index -> door outcomes
}

# --- Setup Functions ---

def assign_doors(seed=None):
    """Randomize each stage's doors (safe / battle / trap)"""
    rng = random.Random(seed)
    for i in range(len(stages)):
        doors = ['safe','battle','trap']
        rng.shuffle(doors)
        state['stage_safe_doors'][i] = {'1': doors[0], '2': doors[1], '3': doors[2]}

# --- Title / Help Screens ---

def title_screen():
    clear_screen()
    print(Col.CYAN + boxed("ESCAPE FROM PARTH - TEXT ADVENTURE") + Col.RESET)
    print('  ' + Col.BOLD + 'A short adventure with riddles, doors, and battles.' + Col.RESET)
    print('\n  Options:\n   1) Start Game\n   2) How to play\n   3) Quit')
    choice = input('\nChoose (1-3): ').strip()
    if choice == '1':
        assign_doors()
        main_game()
    elif choice == '2':
        how_to_play()
    else:
        print('\nGoodbye!')

def how_to_play():
    clear_screen()
    help_text = """How to play:
- 5 stages, each with a riddle and 3 doors
- Correct answer reveals safe door (sometimes Parth lies!)
- Items (Lucky Charms) help peek behind doors
- Multiple endings depend on choices
Controls:
- Type A/B or full word for riddles
- Type 1,2,3 to choose doors"""
    print(boxed(help_text))
    input("\nPress ENTER to return to title...")
    title_screen()

# --- Stage / Riddle / Doors ---

def print_stage_header(stage):
    """Show stage name and ASCII art"""
    clear_screen()
    s = stages[stage]
    print(boxed(f"STAGE {stage+1} - {s['name']}"))
    print('\n   ' + s['art'] + '\n')

# --- Battle minigame ---
def timing_fight(stage):
    """Timing-based X-in-bar battle minigame"""
    print('\n⚔️  BATTLE MODE ⚔️')
    print('Press ENTER when you think the X is in the target zone.')
    input('Press ENTER to start...')

    bar_length, target_start, target_end = 21, 8, 12
    position, direction = random.randint(0, bar_length-1), random.choice([-1,1])
    hit = [False]
    final_pos = [position]

    def waiter():
        input()
        hit[0] = True

    threading.Thread(target=waiter, daemon=True).start()
    moves = random.randint(20,32)

    for _ in range(moves):
        if hit[0]: break
        bar = ["═"]*bar_length
        for j in range(target_start,target_end+1): bar[j] = "░"
        position = max(0, min(bar_length-1, position))
        bar[position] = "X"
        print("\r["+"".join(bar)+"]", end="", flush=True)
        time.sleep(0.09 + random.uniform(-0.03,0.04))
        position += direction
        if position >= bar_length: position, direction = bar_length-1, -1
        if position < 0: position, direction = 0, 1
        final_pos[0] = position

    if not hit[0]:
        print("\nNOW! PRESS ENTER!!")
        input()
        hit[0] = True

    success = target_start <= final_pos[0] <= target_end
    print()
    slow_print("You landed it!" if success else "You missed. Parth smirks...")
    return success

# --- Play a stage ---
def play_stage(i):
    print_stage_header(i)
    r = riddles[i]

    print("\nParth approaches...\n o_o\n/| |\\\n | |\n_|_|_\n")
    slow_print(f"Parth: Alright genius, try this one.\n")
    slow_print(f"Riddle:\n  {r['question']}")
    for opt in r['options']: print("  "+opt)
    print("Hint:", r['hint'])

    # get answer
    mapping = {"KEYBOARD":"A","PIANO":"B","CLOCK":"A","STATUE":"B",
               "CANDLE":"A","TREE":"B","COIN":"A","SNAKE":"B",
               "TOWEL":"A","SPONGE":"B"}
    while True:
        ans = input("Your answer: ").strip().upper()
        if ans in ["A","B"]: break
        if ans in mapping: ans = mapping[ans]; break
        print("Try A or B.")

    correct = ans == r['answer']
    safe = [k for k,v in state['stage_safe_doors'][i].items() if v=="safe"][0]

    # Chance Parth lies about safe door
    lie_chance = 0.25
    shown_safe = safe
    if correct and random.random() < lie_chance:
        fake_safe = random.choice([k for k in ["1","2","3"] if k != safe])
        shown_safe = fake_safe
        slow_print(f"Parth: Safe door is Door {fake_safe} (might be lying...)")
    elif correct:
        slow_print(f"Parth: Safe door is Door {safe}")
    else:
        slow_print("Parth: Wrong! Choose blindly!")

    input("\nWalk to the doors (press Enter)...")
    print(" DOOR 1   |   DOOR 2   |   DOOR 3\n-----------------------------------")

    # lucky charm peek
    if "lucky" in state['inventory']:
        if input("Use Lucky Charm to peek? (y/n): ").lower().startswith("y"):
            peek = random.choice(["1","2","3"])
            slow_print(f"Charm glows near Door {peek}.")
            state['inventory'].remove("lucky")

    # pick a door
    pick = ""
    while pick not in ["1","2","3"]: pick = input("Choose (1-3): ").strip()
    actual_outcome = state['stage_safe_doors'][i][pick]

    # even safe door might trigger fight
    if actual_outcome == "safe" and random.random()<0.2:
        slow_print("...Parth jumps out! Forced fight!")
        return "safe" if timing_fight(i) else "death"
    elif actual_outcome == "safe":
        slow_print("Door swings open. Light ahead.")
        if random.random()<0.25: 
            slow_print("Found Lucky Charm! Yoink.")
            state['inventory'].append("lucky")
        return "safe"
    elif actual_outcome=="battle":
        slow_print("Parth attacks!")
        return "safe" if timing_fight(i) else "death"
    else:
        slow_print("Endless homework engulfs you. 😭")
        return "death"

# --- Endings ---
def ending_win():
    clear_screen()
    print(boxed("VICTORY! You escaped the homework dimension."))
    slow_print("Parth: You win... but homework never ends.")
    input("Press ENTER to return to title...")
    title_screen()

def ending_lose():
    clear_screen()
    print(boxed("GAME OVER - TRAPPED FOREVER"))
    slow_print("Parth: You'll do homework forever! 😈")
    input("Press ENTER to return to title...")
    title_screen()

def ending_truce():
    clear_screen()
    print(boxed("SECRET ENDING - PARTH'S TRUCE"))
    slow_print("Parth: You collected enough charms. Let's chill instead of fighting.")
    input("Press ENTER to return to title...")
    title_screen()

# --- Main game loop ---
def main_game():
    clear_screen()
    slow_print("You pick up a glowing textbook...")
    animate_dots()
    slow_print("Pulled into Parth's homework dimension...")
    input("Press ENTER to begin...")
    for stage in range(len(stages)):
        res = play_stage(stage)
        if res == "death": ending_lose(); return
    if state["inventory"].count("lucky") >= 2: ending_truce()
    else: ending_win()

# --- Start ---
if __name__ == "__main__":
    title_screen()