from pokemon_scarlet import violet_map
import random


print("Províncias disponíveis:")
for i, key in enumerate(violet_map.keys()):
    print(f"{i}: {key}")


provinces = list(violet_map.items())
position_province = int(input('Escolha a província: '))
key_province, value_province = provinces[position_province]


print("Áreas disponíveis:")
for i, key in enumerate(value_province.keys()):
    print(f"{i}: {key}")


areas = list(value_province.items())
position_area = int(input('Escolha a área: '))
key_area, value_area = areas[position_area]


random_position = random.randint(0, len(value_area) - 1)
pick_pokemon = value_area[random_position]
print(pick_pokemon)
