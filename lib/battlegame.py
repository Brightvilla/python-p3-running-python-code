# Battlegame Group work
# Task 1: Setting up the game
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

# Task 3: Character Selection loop
while True:
    print("Choose your character:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Exit")
    character_choice = input("Choose your character (1-4): ").lower()
    
    if character_choice in ['1', 'wizard']:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice in ['2', 'elf']:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice in ['3', 'human']:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character_choice in ['4', 'exit']:
        print("Goodbye!")
        exit()
    else:
        print("Unknown character")

print(f"You chose: {character}")

# Task 4: Battle with the Dragon
while True:
    # Player's Turn
    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!")
    
    # Check for Dragon's defeat
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    
    # Dragon's Turn
    my_hp = my_hp - dragon_damage
    print(f"The Dragon damaged the {character}!")
    
    # Check for Character's defeat
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break