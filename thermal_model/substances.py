class Water:
    def __init__(self):
        self.__mass = ''

    def getmass(self):
        if self.derived_mass:
            self.__mass = self.volume * self.density
        return self.__mass

    def setmass(self, mass):
        self.__mass = mass
        print(f'new mass is set to: {mass}')
        self.derived_mass = False

    name = 'Water'  # class attribute
    specificHeat = 4.816  # KJ/(kg K) Specific Heat
    liquid_vapor_temp = 100
    heat_of_vaporization = 2256  # kJ/kg
    density = 1.000  # kg/L
    volume = 0  # L
    temp = 0
    derived_mass = True
    mass = property(getmass, setmass)


class Milk:
    def __init__(self):
        self.__mass = ''

    def getmass(self):
        if self.derived_mass:
            self.__mass = self.volume * self.density
        return self.__mass

    def setmass(self, mass):
        self.__mass = mass
        print(f'new mass is set to: {mass}')
        self.derived_mass = False

    name = 'Milk'  # class attribute
    specificHeat = 3.77  # KJ/(kg K) Specific Heat
    liquid_vapor_temp = 100.5
    heat_of_vaporization = 2256  # kJ/kg
    density = 1.035  # kg/L
    volume = 0  # L
    derived_mass = True
    mass = property(getmass, setmass)
    temp = 0
