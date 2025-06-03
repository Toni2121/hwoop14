from basic_spaceship import BasicSpaceship
from shield_decorator import ShieldDecorator
from weapon_decorator import WeaponDecorator


def main():
    spaceship = BasicSpaceship()
    spaceship = ShieldDecorator(spaceship)
    spaceship = WeaponDecorator(spaceship, weapon_name="Advanced Laser", attack_bonus=25, weight_bonus=20)

    print("Spaceship Stats:")
    print(f"Attack Points: {spaceship.attack_get()}")
    print(f"Defense Points: {spaceship.defense_get()}")
    print(f"Weight: {spaceship.weight_get()}")
    print(f"Details: {spaceship.details_get()}")


if __name__ == "__main__":
    main()
