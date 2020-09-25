import sys
import random
from libs_t3 import human

class soul ():
    def __init__(self,name,hp,dfn,mana):
        self.name = name
        self.hp = hp
        self.dfn = dfn
        self.mana = mana

def success():
    rand = random.randrange(0,100) 
    if rand > 50:
        return True
    else:
        return False  
    
class monster(soul,object):  
    def def_monster():
        rand = random.randrange(1,4) 
        if rand == 1:
            return 1
        elif rand == 2:
             return 2
        elif rand == 3:
            return 3
    
    def monster_attack():
        rand = random.randrange(1,3) 
        if rand == 1:
            return 1
        elif rand == 2:
            return 2        
        
        
class skeleton(monster,object): 
        def say_h(self):
            print("-----------------------------------")
            print (f"Hi i'm a monster and my name is {self.name}")
            print (f"HP {self.hp}")
            print (f"Defensa {self.dfn}")
            print (f"Mana {self.mana}")
        def attack(self,obj):
            print("-------------------------------------------- Monster attack---------------------------------------------")
            print ("I'm a skeleton and have two options of attack")
            print ('The first attack option is the chigiriki, have a power of 20 and the second one is the ono, have a power of 22')
            print("------------------------------------------------------------------------------------------------------------")
            if self.hp <= 0:
                print(f'{self.name} has already dead')
                sys.exit()
            else:
                if success():
                    if obj.hp <= 0:
                        print(f'{obj.name} is dead')
                        sys.exit()
                    else:
                        if obj.hp <= 0:
                            print(f'{obj.name} is dead') 
                            sys.exit()
                        else:
                            if self.mana == 0:
                                print("you don't have mana, lost turn")
                                self.mana == 100
                            else:
                                if monster.monster_attack() == 1:
                                    cm = 15
                                    print(f'{self.name} attack to {obj.name} with an chigiriki')
                                    self.mana = self.mana - cm
                                    print(f"{self.name} actual Mana: {self.mana}")
                                    obj.hp = (obj.hp + obj.dfn) - 20
                                    print(f"{obj.name}  actual HP: {obj.hp}")
                                    if obj.hp <= 0:
                                        print(f'{obj.name} is dead')
                                        sys.exit()
                                    elif monster.monster_attack() == 2:
                                        cm = 10
                                        print(f'{self.name} attack to {obj.name} with an ono')
                                        self.mana = self.mana - cm
                                        print(f"{self.name} actual Mana: {self.mana}")
                                        obj.hp = (obj.hp + obj.dfn) - 15
                                        print(f"{obj.name}  actual HP: {obj.hp}")
                                        if obj.hp <= 0:
                                            print(f'{obj.name} is dead')
                                            sys.exit()
                else:
                    print(f"miss attack to {obj.name}")
                

        
class centaur(monster,object):
    def say_h(self):
            print("-----------------------------------")
            print (f"Hi i'm a monster and my name is {self.name}")
            print (f"HP {self.hp}")
            print (f"Defensa {self.dfn}")
            print (f"Mana {self.mana}")
    def attack(self,obj):
        print("-------------------------------------------- Monster attack---------------------------------------------")
        print ("I'm a centaur and have two options of attack")
        print ('The first attack option is the sword, have a power of 20 and the second one is a kick, have a power of 10')
        print("------------------------------------------------------------------------------------------------------------")
        
        if self.hp <= 0:
            print(f'{self.name} has already dead')
        else:
            if success():
                if obj.hp <= 0:
                    print(f'{obj.name} is dead')
                    sys.exit()
                else:
                    if obj.hp <= 0:
                        print(f'{obj.name} is dead') 
                        sys.exit()
                    else:
                        if self.mana == 0:
                            print("you don't have mana, lost turn")
                            self.mana == en
                        else:
                            if monster.monster_attack() == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an sword')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif monster.monster_attack() == 2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with a kick')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 10
                                print(f"{obj.name}  actual HP: {obj.hp}")
            else:
                print(f"miss attack to {obj.name}")
                
class slime(monster,object):  
    def say_h(self):
            print("-----------------------------------")
            print (f"Hi i'm a monster and my name is {self.name}")
            print (f"HP {self.hp}")
            print (f"Defensa {self.dfn}")
            print (f"Mana {self.mana}")
    def attack(self,obj):
        print("-------------------------------------------- Monster attack---------------------------------------------")
        print ("I'm a slime and have two options of attack")
        print ('The first attack option is a slime ball, have a power of 20 and the second one is the kanabo, have a power of 25')
        print("------------------------------------------------------------------------------------------------------------")
        if self.hp <= 0:
            print(f'{self.name} has already dead')
        else:
            if success():
                if obj.hp <= 0:
                    print(f'{obj.name} is dead')
                    sys.exit()
                else:
                    if obj.hp <= 0:
                        print(f'{obj.name} is dead') 
                        sys.exit()
                    else:
                        if self.mana == 0:
                            print("you don't have mana, lost turn")
                            self.mana == en
                        else:
                            if monster.monster_attack() == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an slime ball')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif monster.monster_attack() ==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an kanabo')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 22
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else: 
                                print('wee lo sabia')
            else:
                print(f"miss attack to {obj.name}")




