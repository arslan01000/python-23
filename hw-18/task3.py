import random

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
    shield = hero['protective_field'] if hero['has_shield'] else 0
    print(f"Здоровье героя: {hero['hp']} ед., Защита: {hero['defence']} (+{shield} при щите)")

def modify_health(character, amount):
    character['hp'] += amount
    if character['hp'] < 0:
        character['hp'] = 0

def calculate_damage(attacker, defender):
    damage = attacker['gun'] - defender['defence']
    return max(damage, 0)

def equip_shield():
    if not hero['has_shield']:
        hero['defence'] += hero['protective_field']
        hero['has_shield'] = True
        print("Герой активировал защитное поле!")

def remove_shield():
    if hero['has_shield']:
        hero['defence'] -= hero['protective_field']
        hero['has_shield'] = False
        print("Защитное поле героя отключено.")

def hero_turn():
    action = input("Ход героя: выберите действие (attack, defence, pass): ").strip().lower()

    if action == "attack":
        hit_probability = random.randint(1, 100)
        if hit_probability <= 75:
            damage = calculate_damage(hero, robot)
            modify_health(robot, -damage)
            print(f"Герой попал! Робот получил {damage} ед. урона.")
        else:
            print("Герой промахнулся.")
    
    elif action == "defence":
        equip_shield()

    elif action == "pass":
        print("Герой пропустил ход.")

    else:
        print("Неизвестная команда. Герой пропустил ход.")

    display_robot_info()
    display_hero_info()
    print("=" * 30)

def robot_turn():
    if robot['hp'] <= 0:
        return

    action = random.choice(["missile", "regular", "jammed"])

    if action == "missile":
        damage = robot['gun'] + int(0.3 * robot['gun']) - hero['defence']
        damage = max(damage, 0)
        modify_health(hero, -damage)
        print(f"Робот использовал ракету! Герой получил {damage} ед. урона.")

    elif action == "regular":
        hit_probability = random.randint(1, 100)
        if hit_probability <= 50:
            damage = calculate_damage(robot, hero)
            modify_health(hero, -damage)
            print(f"Робот попал! Герой получил {damage} ед. урона.")
        else:
            print("Робот промахнулся.")

    else:
        print("Робот заклинило и он пропустил ход.")

    display_hero_info()
    print("=" * 30)

    remove_shield()

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
