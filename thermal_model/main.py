# This is a project designed to combine my practical
# knowledge in mechanical engineering, with the software engineering 
# experience I've gathered so far and continue to learn about
# I don't think I've learned any new things in mech-e theory in a while
# as my focus has been heavily in the swe side. However, I should
# remind myself that I have amassed a wealth of practical production
# and design skills with 3D printing and CAD, and that I've read a handful of
# journals/publications in this space as well 

# Now I have a great opportunity and more accurately a necessity to 
# combine these skillsets and build something really cool alhamdulillah, I could have
# been doing this all along, and it may have accelerated my growth, as it
# did when I started working on simulations back when covid first hit.
# However, as my favorite saying goes, the best time is now.

# Mechanical Theory Topics
# - Thermal and material properties
# - Vector Dynamics and motion
# - System Dynamics, oscillatioms, damping, harmonics
# - Stress/Strain material stress
# - Heat transfer and phase change

# Software Development Topics
# - Object-Oriented Class Structure
# -- Classes, Libraries, Modules, Methods
# - Collaborative development via git
# - Optimized Algorithm Complexity
# - Passing data across multiple layers
# -- Application Layer, Framework Layer, Memory Layer
# - Unit Testing and Integration Testing

# Let's start with something really simple, like boiling water, which is actually
# a complex phenomenon


class substances:
    


def water():
    mass = 1 # kg
    temp_initial = 0 # C
    specific_heat = 4186 # kJ/(kg K)
    return mass, temp_initial, specific_heat

water_state = [0,0,0]
water_state[0], water_state[1], water_state[2] = water()

print('Initial State')
print(f'Water Mass: {water_state[0]}, Water Temp: {water_state[1]}')

def heater(substance,temp, duration): 
    # at first just add temp
    # next, add Joules or Watts of heat
    #substance[1] += 20 #adds 20C of temp

    requested_temp_increase=temp
    heat_required=substance[2]*substance[0]*requested_temp_increase
    substance[1] += 20
    power=heat_required/duration
    return substance, heat_required, power

for i in range(4):
    if water_state[1] >100:
        print('The water has boiled!')
        break
    water_state,heatreq,powerreq=heater(water_state,20, 10)
    print('Intermediate State')
    print(f'Water Mass: {water_state[0]}, Water Temp: {water_state[1]}')

print(f'Heat required: {heatreq} kJ')
print(f'Power required: {powerreq} kW')
print(f'Cost: ${heatreq*0.38/3600}')
print('end of run')
