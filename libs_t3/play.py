from libs_t3 import character
from libs_t3 import human
  
def characters(): 
    name = input('What name do you want to choose? ')
    print("-----------------Character------------------")
    print('choose your character')
    print ('1. Warrior')
    print ('2. Mage')
    print ('3. Elf')
    print ('4. Warrior Elf')
    print ('5. Warrior Mage')
    print ('6. Elf Mage')
    player = int(input('which character do you want to be? '))
    character.monster.def_monster()
    if player == 1 and character.monster.def_monster() == 1:
        p = human.warrior(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h() 
        while p.hp > 0 and m.hp > 0:
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 1 and character.monster.def_monster() == 2:
        p = human.warrior(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 1 and character.monster.def_monster() == 3:
        p = human.warrior(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 2 and character.monster.def_monster() == 1:
        p = human.mage(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 2 and character.monster.def_monster() == 2:
        p = human.mage(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 2 and character.monster.def_monster() == 3:
        p = human.mage(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 3 and character.monster.def_monster() == 1:
        p = human.elf(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 3 and character.monster.def_monster() == 2:
        p = human.elf(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 3 and character.monster.def_monster() == 3:
        p = human.elf(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 4 and character.monster.def_monster() == 1:
        p = human.warrior.elf(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 4 and character.monster.def_monster() == 2:
        p = human.warrior_elf(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 4 and character.monster.def_monster() == 3:
        p = human.warrior_elf(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 5 and character.monster.def_monster() == 1:
        p = human.warrior_mage(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 5 and character.monster.def_monster() == 2:
        p = human.warrior_mage(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 5 and character.monster.def_monster() == 3:
        p = human.warrior_mage(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 6 and character.monster.def_monster() == 1:
        p = human.elf_mage(name,100,10,100)
        p.say_he()
        m = character.skeleton('Chingiru',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 6 and character.monster.def_monster() == 2:
        p = human.elf_mage(name,100,10,100)
        p.say_he()
        m = character.centaur('Quiron',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
    elif player == 6 and character.monster.def_monster() == 3:
        p = human.elf_mage(name,100,10,100)
        p.say_he()
        m = character.slime('Glossy',100,10,100)
        m.say_h()
        while p.hp > 0 and m.hp > 0: 
            p.attack(m)
            m.attack(p)
            yield
            print()
            break
            

def start():
    characters()
    next(characters())
    