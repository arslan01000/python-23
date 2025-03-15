import random

# Initial stats
robot = {
    'hp': 1300,
    'defence': 120,
    'gun': 300
}

hero = {
    'hp': 2000,
    'defence': 100,
    'gun': 250,
    'protective_field': 150,
    'has_shield': False
}

def display_robot_info():
    print(f"Здоровье робота: {robot['hp']} ед.")

def display_hero_info():
    print(f"Здоровье героя: {hero['hp']} ед.")

def modify_health(character, amount):
    character['hp'] += amount
    if character['hp'] < 0:
        character['hp'] = 0

def calculate_damage(attacker, defender, extra_damage=0):
    damage = attacker['gun'] + extra_damage - defender['defence']
    return max(damage, 0)  # No negative healing!

def hero_turn():
    hit_probability = random.randint(1, 100)
    if hit_probability <= 75:  # 75% chance to hit
        damage = calculate_damage(hero, robot)
        modify_health(robot, -damage)
        print(f"Герой попал! Робот получил {damage} ед. урона.")
    else:
        print("Герой промахнулся.")

    display_robot_info()
    print("=" * 30)

def robot_turn():
    if robot['hp'] <= 0:
        return

    action = random.choice(["missile", "regular", "jammed"])
    
    if action == "missile":
        damage = calculate_damage(robot, hero, extra_damage=int(0.3 * robot['gun']))
        modify_health(hero, -damage)
        print(f"Робот использовал самонаводящуюся ракету! Герой получил {damage} ед. урона.")
    
    elif action == "regular":
        hit_probability = random.randint(1, 100)
        if hit_probability <= 50:  # 50% chance to hit
            damage = calculate_damage(robot, hero)
            modify_health(hero, -damage)
            print(f"Робот попал обычными патронами! Герой получил {damage} ед. урона.")
        else:
            print("Робот промахнулся обычными патронами.")
    
    else:
        print("Робот заклинило и он пропустил ход.")

    display_hero_info()
    print("=" * 30)

def main():
    print("Межгалактическая битва начинается!")
    print("=" * 30)

    while True:
        hero_turn()
        if robot['hp'] <= 0:
            print("Герой победил! Робот уничтожен.")
            break

        robot_turn()
        if hero['hp'] <= 0:
            print("Герой пал в бою! Робот победил.")
            break

if __name__ == "__main__":
    main()
