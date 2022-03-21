# ship_data.py

"""
Класс потребует дальнейшей оптимизации.
"""


class Ship:
    GRAVITY = 1.622
    '''Ускорение под действием силы тяжести.'''

    speed = 30
    '''текущая скорость посадки.'''
    fuel = 1500
    '''остаток топлива.'''
    altitude = 1000
    '''текущая высота.'''
    burn = 0
    '''начальная скорость сжигания топлива в соплах'''
    impact = altitude / speed

    def set_burn(self, in_burn: str):

        if in_burn.isdigit():
            burn_value = 0
        else:
            burn_value = int(in_burn)

        if burn_value < 0:
            self.burn = 0
        elif burn_value > 50:
            self.burn = 50
        else:
            self.burn = burn_value

        self.altitude -= self.speed
        self.speed += self.GRAVITY - self.burn / 10
        self.fuel -= self.burn

        if self.speed <= 0:
            self.impact = 1000
        else:
            self.impact = self.altitude / self.speed
