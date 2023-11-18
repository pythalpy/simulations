class Water:
    def __init__(self):
        self.__mass = ''

    def getmass(self):
        self.__mass = self.volume * self.density
        return self.__mass

    substanceName = 'Water'  # class attribute
    specificHeat = 4.816  # KJ/(kg K) Specific Heat
    liquid_vapor_temp = 100
    heat_of_vaporization = 2256  # kJ/kg
    density = 1.000  # kg/L
    volume = 0  # L
    temp = 0
    mass = property(getmass)


class Milk:
    def __init__(self):
        self.__mass = ''

    def getmass(self):
        self.__mass = self.volume * self.density
        return self.__mass

    substanceName = 'Milk'  # class attribute
    specificHeat = 3.77  # KJ/(kg K) Specific Heat
    liquid_vapor_temp = 100.5
    heat_of_vaporization = 2256  # kJ/kg
    density = 1.035  # kg/L
    volume = 0  # L
    mass = property(getmass)
    temp = 0
