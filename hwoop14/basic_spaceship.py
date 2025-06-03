from spaceship_interface import ISpaceship


class BasicSpaceship(ISpaceship):
    def __init__(self):
        self._attack = 10
        self._defense = 50
        self._weight = 100

    def attack_get(self) -> int:
        return self._attack

    def defense_get(self) -> int:
        return self._defense

    def weight_get(self) -> int:
        return self._weight

    def details_get(self) -> str:
        return "Basic Spaceship"
