import json
from country_code import get_country_code
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# load the data into a list.
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f) # open the data as a list

#Build a dictionary of world population data.
cc_populations = { }

for x in pop_data:
    if x['Year'] == '2010':
        country = x['Country Name']
        population = int(float(x['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

#Group countries in three population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for key, value in cc_populations.items():
    if value < 10000000:
        cc_pops_1[key] = value
    elif value < 1000000000:
        cc_pops_2[key] = value
    else:
        cc_pops_3[key] = value

#Prints how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style = LCS)
wm = World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
