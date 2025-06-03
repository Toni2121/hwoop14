from spaceship_decorator import SpaceshipDecorator


class WeaponDecorator(SpaceshipDecorator):
    def __init__(self, spaceship, weapon_name="Laser Rifle", attack_bonus=15, weight_bonus=15):
        super().__init__(spaceship)
        self._weapon_name = weapon_name
        self._attack_bonus = attack_bonus
        self._weight_bonus = weight_bonus

    def attack_get(self) -> int:
        return self._spaceship.attack_get() + self._attack_bonus

    def weight_get(self) -> int:
        return self._spaceship.weight_get() + self._weight_bonus

    def details_get(self) -> str:
        return self._spaceship.details_get() + f", equipped with {self._weapon_name}"
