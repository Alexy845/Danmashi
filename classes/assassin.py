from __future__ import annotations
from .character import Character
from .dice import Dice
from random import randint

class Assassin(Character):
    playerMove = [
        "Coup de dague",
        "hachettes des ombres"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Assassin | None:
        if (template=="default"):
            return Assassin(name=name, classe="Assassin", max_health=35, attack_value=6, defense_value=3, attack_type_value=10, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} l'assassin 🥷\n"
    
    def compute_damages(self, roll, target):
        print(f"{self._name} donne un coup de dague !\n")
        return super().compute_damages(roll, target)

    def compute_damages_type(self, roll, target):
        type_attack_damages = self._attack_value
        rand_num = randint(2, 6)
        print(f"{self._name} lance {rand_num} hachettes des ombres !\n")
        for _ in range(2, rand_num):
            type_attack_damages += 3
        return type_attack_damages
    
    def compute_damages_special(self, roll, target):
        print(f"{self._name} utilise son écran de fumée 🌫️ qui rend confus {target.get_name()}\n")
        self._touchable += 2
        return 0, False
    
    def defense(self, damages, attacker):
        if randint(1, 4) == 1:
            print(f"{self._name} a esquivé l'attaque avec habilité")
            self.decrease_health(0)
        else:
            return super().defense(damages, attacker)
            
    def add_special(self):
        self.playerMove.append("écran de fumée")
            