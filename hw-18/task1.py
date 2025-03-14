import random

robot = {
    'hp': 1300,
    'defence': 120
}

hero = {
    'gun': 300
}

def display_robot_info():
    print(f"Здоровье робота: {robot['hp']} ед.")

def modify_health(character, amount):
    character['hp'] += amount
    if character['hp'] < 0:
        character['hp'] = 0

def calculate_damage(hero, robot):
    damage = hero['gun'] - robot['defence']
    return max(damage, 0)

def hero_turn():
    hit_probability = random.randint(1, 100)
    if hit_probability <= 75:
        damage = calculate_damage(hero, robot)
        modify_health(robot, -damage)
        print(f"Герой попал! Робот получил {damage} ед. урона.")
    else:
        print("Герой промахнулся.")

    display_robot_info()
    print("=" * 30)

def main():
    print("Межгалактическая битва начинается!")
    print("=" * 30)

    while robot['hp'] > 0:
        hero_turn()
        if robot['hp'] <= 0:
            print("Герой победил! Робот уничтожен.")
            break

if __name__ == "__main__":
    main()
