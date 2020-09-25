import sys
import random
from libs_t3 import character

class soul ():
    def __init__(self,name,hp,dfn,mana):
        self.name = name
        self.hp = hp
        self.dfn = dfn
        self.mana = mana
        
class human(soul,object):  
    print()
    
def success():
    rand = random.randrange(0,100) 
    if rand > 50:
        return True
    else:
        return False  
    
class warrior(human,object):
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a warrior and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a warrior and have two options of attack")
        print ('The first attack option is the ax, have a power of 15 and the second one is the catapult, have a power of 20')
        n = int(input('Which attack do you want to use?'))
        print("------------------------------------------------------------------------------------------------------------")
        if self.hp <= 0:
            print(f'{self.name} has already dead')
        else:
            if success():
                if self.hp <= 0:
                    print(f'{self.name} is dead')
                    sys.exit()
                else:
                    if obj.hp <= 0:
                        print(f'{obj.name} is dead') 
                        sys.exit()
                    else:
                        if self.mana == 0:
                            print("you don't have mana, lost turn")
                        else:
                            if n == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an ax that inflicts damage of 15')
                                self.mana = self.mana - cm
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{self.name} actual Mana: {self.mana}")
                                print(f"{obj.name} actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an catapult that inflicts damage of 20')
                                self.mana = self.mana - cm
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{self.name} actual Mana: {self.mana}")
                                print(f"{obj.name} actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack ")
                    
class mage(human,object):
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a mage and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a mage and have two options of attack")
        print ('The first attack option is the fire, have a power of 20 and the second one is the ice, have a power of 15')
        n = int(input('Which attack do you want to use?'))
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
                            if n == 1:
                                cm = 14
                                print(f'{self.name} attack to {obj.name} with fire')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with ice')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack to {obj.name}")
                    
                
class elf(human,object): 
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a elf and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a elf and have two options of attack")
        print ('The first attack option is throw carnivorous plants, have a power of 25 and the second one is the power beam, have a power of 16')
        n = int(input('Which attack do you want to use?'))
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
                            if n == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an carnivorous plants')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 25
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an power beam')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 16
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack to {obj.name}")
                
                
class warrior_elf(human,object): 
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a warrior elf and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a warrior elf and have two options of attack")
        print ('The first attack option is the ax, have a power of 15 and the second one is the catapult, have a power of 20')
        print ('The third attack option is throw carnivorous plants, have a power of 25 and the fourt one is the power beam, have a power of 16')
        n = int(input('Which attack do you want to use?'))
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
                            if n == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an ax')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an catapult')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n == 3:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an carnivorous plants')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 25
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==4:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an power beam')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 16
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack to {obj.name}")
                
                
class warrior_mage(human,object):  
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a warrior mage and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a warrior mage and have four options of attack")
        print ('The first attack option is the ax, have a power of 15 and the second one is the catapult, have a power of 20')
        print ('The third attack option is the fire, have a power of 20 and the fourt is the ice, have a power of 15')
        n = int(input('Which attack do you want to use?'))
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
                            if n == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an ax')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an catapult')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n == 3:
                                cm = 14
                                print(f'{self.name} attack to {obj.name} with fire')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==4:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with ice')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack to {obj.name}")


class elf_mage(human,object):    
    def say_he(self):
        print("-----------------------------------")
        print (f"Hi i'm a elf mage and my name is {self.name}")
        print (f"HP {self.hp}")
        print (f"Defensa {self.dfn}")
        print (f"Mana {self.mana}")
    def attack(self,obj):
        print("--------------------------------------------Choose your attack---------------------------------------------")
        print ("I'm a elf mage and have four options of attack")
        print ('The first attack option is throw carnivorous plants, have a power of 25 and the second one is the power beam, have a power of 16')
        print ('The third attack option is the fire, have a power of 20 and the fourt is the ice, have a power of 15')
        n = int(input('Which attack do you want to use?'))
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
                            if n == 1:
                                cm = 15
                                print(f'{self.name} attack to {obj.name} with an carnivorous plants')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 25
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==2:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with an power beam')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 16
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n == 3:
                                cm = 14
                                print(f'{self.name} attack to {obj.name} with fire')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 20
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            elif n==4:
                                cm = 10
                                print(f'{self.name} attack to {obj.name} with ice')
                                self.mana = self.mana - cm
                                print(f"{self.name} actual Mana: {self.mana}")
                                obj.hp = (obj.hp + obj.dfn) - 15
                                print(f"{obj.name}  actual HP: {obj.hp}")
                            else:
                                print("This option attack doesn't exist")
            else:
                print(f"miss attack to {obj.name}")

                
