class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting…"
        return "no bullets left"

#Test code
weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)