from spaceship_interface import ISpaceship


class SpaceshipDecorator(ISpaceship):
    def __init__(self, spaceship: ISpaceship):
        self._spaceship = spaceship

    def attack_get(self) -> int:
        return self._spaceship.attack_get()

    def defense_get(self) -> int:
        return self._spaceship.defense_get()

    def weight_get(self) -> int:
        return self._spaceship.weight_get()

    def details_get(self) -> str:
        return self._spaceship.details_get()
