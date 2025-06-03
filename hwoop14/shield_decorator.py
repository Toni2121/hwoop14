from spaceship_decorator import SpaceshipDecorator


class ShieldDecorator(SpaceshipDecorator):
    def __init__(self, spaceship):
        super().__init__(spaceship)
        self._extra_defense = 10
        self._extra_weight = 20
        self._shield_desc = "Standard Shield"

    def defense_get(self) -> int:
        return self._spaceship.defense_get() + self._extra_defense

    def weight_get(self) -> int:
        return self._spaceship.weight_get() + self._extra_weight

    def details_get(self) -> str:
        return self._spaceship.details_get() + f", with {self._shield_desc}"
