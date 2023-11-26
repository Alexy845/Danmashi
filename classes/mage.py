from character import Character
from dice import Dice

class Mage(Character):
    playerMove = [
        "Attack",
        "Attack spe"
        ]
    
    def __init__(self, name:str) -> None:
        super().__init__(name, "Mage")
        self._max_health = 50
        self._health = self._max_health
        self._attack_value = 6
        self._attack_type_value = 10
        self._defense_value = 3
        self._dice = Dice(4)
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} le mage 🧙"

    def compute_damages(self, roll, target):
        print(f"🪓 {self._name} lance l'attaque déferlement sur {target.get_name()}.")
        return super().compute_damages(roll, target) + roll
    
    def compute_damages_type(self, roll, target):
        print(f" {self._name} lance le sort maîtrise de soi...")
        return super().compute_damages_type(roll, target) + roll
