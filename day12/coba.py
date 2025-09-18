game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


if game_level < 8 :
    show_enemy = enemies[1]

print(show_enemy)



enemie = 1

def increase_enemies():
    global enemie
    enemie += 1
    print(f"enemies outside funciton {enemie}")


increase_enemies()
print(f"enemies outside fucntion: {enemie}")