import substances


# Unit Converters
def F2C(temp_Fahrenheit):
    temp_Celsius = 5/9*(temp_Fahrenheit - 32)  # (5/9) * (degF - 32) = C
    return temp_Celsius


def cup2L(volume_cups):
    volume_L = volume_cups/4.22675  # (cups) * (1 L / 4.22675 cups) = L
    return volume_L


water = substances.Water()  # Instantiate substance class object
water.temp = F2C(55)        # Set Initial Temperature in F (converted to C)
water.volume = cup2L(0.5)   # Set Volume in cups (converted to L)

milk = substances.Milk()
milk.temp = F2C(55)
milk.volume = cup2L(0.5)

print('-% start of run %-')
print(f'Initial State: Water Mass: {round(water.mass,3)} kg, Water Temp: {round(water.temp, 2)} C' )
print(f'Initial State: Milk Mass: {round(milk.mass, 3)} kg, Milk Temp: {round(milk.temp, 2)} C' )


def heater(substance,target_temp):
    required_temp_increase = target_temp - substance.temp
    heat_required = substance.specificHeat * substance.mass * required_temp_increase
    if target_temp > substance.liquid_vapor_temp:
        heat_required += substance.heat_of_vaporization

    print(f'delta-T: {round(required_temp_increase, 2)} C')
    return heat_required


heatreq_water = heater(water, 104)
heatreq_milk = heater(water, 99.7)
utilcost = 0.38
energy_cost = utilcost*(heatreq_water + heatreq_milk)/3600
energy_cost = "${:,.2f}".format(energy_cost)


print(f'Heat required: {round((heatreq_water + heatreq_milk),2)} kJ')
print(f'Heat required: {round((heatreq_water + heatreq_milk)/3600,2)} kilowatt-hour')
# print(f'Power required: {powerreq} kW')
print(f'Cost at ${utilcost}/kW-hr: {energy_cost}')
print('-% end of run %-')


