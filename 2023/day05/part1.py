almanac = ''

with open('input') as in_file:
    for line in in_file.readlines():
        almanac += line.strip() + '||'

almanac = almanac.split('||')
print(almanac)

seeds = almanac[0].split(': ')[1].split(' ')
print(seeds)

for i in range(0, len(almanac)):
    if 'seed-to-soil' in almanac[i]:
        seed_to_soil = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                seed_to_soil.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'soil-to-fertilizer' in almanac[i]:
        soil_to_fertilizer = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                soil_to_fertilizer.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'fertilizer-to-water' in almanac[i]:
        fertilizer_to_water = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                fertilizer_to_water.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'water-to-light' in almanac[i]:
        water_to_light = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                water_to_light.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'light-to-temperature' in almanac[i]:
        light_to_temperature = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                light_to_temperature.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'temperature-to-humidity' in almanac[i]:
        temperature_to_humidity = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                temperature_to_humidity.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1
    elif 'humidity-to-location' in almanac[i]:
        humidity_to_location = []
        offset = 1
        sets = []
        while True:
            if almanac[i + offset] == '':
                break
            else:
                destination, source, length = almanac[i + offset].split(' ')
                humidity_to_location.append({'destination': int(destination), 'source': int(source), 'length': int(length)})
            offset += 1

lowest_location = 999999999999999999999999999999

for seed in seeds:
    print('Seed', seed)
    soil = int(seed)
    temp_map = {}
    for lookup in seed_to_soil:
        if int(seed) >= lookup['source'] and int(seed) < (lookup['source'] + lookup['length']):
            soil = int(seed) - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == int(seed):
                    soil = lookup['destination'] + r'''
    print('Found soil')

    fertilizer = soil
    temp_map = {}
    for lookup in soil_to_fertilizer:
        if soil >= lookup['source'] and soil < (lookup['source'] + lookup['length']):
            fertilizer = soil - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == soil:
                    fertilizer = lookup['destination'] + r'''
    print('Found fertilizer')

    water = fertilizer
    temp_map = {}
    for lookup in fertilizer_to_water:
        if fertilizer >= lookup['source'] and fertilizer < (lookup['source'] + lookup['length']):
            water = fertilizer - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == fertilizer:
                    water = lookup['destination'] + r'''
    print('Found water')

    light = water
    temp_map = {}
    for lookup in water_to_light:
        if water >= lookup['source'] and water < (lookup['source'] + lookup['length']):
            light = water - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == water:
                    light = lookup['destination'] + r'''
    print('Found light')

    temperature = light
    temp_map = {}
    for lookup in light_to_temperature:
        if light >= lookup['source'] and light < (lookup['source'] + lookup['length']):
            temperature = light - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == light:
                    temperature = lookup['destination'] + r'''
    print('Found temperature')

    humidity = temperature
    temp_map = {}
    for lookup in temperature_to_humidity:
        if temperature >= lookup['source'] and temperature < (lookup['source'] + lookup['length']):
            humidity = temperature - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == temperature:
                    humidity = lookup['destination'] + r'''
    print('Found humidity')

    location = humidity
    temp_map = {}
    for lookup in humidity_to_location:
        if humidity >= lookup['source'] and humidity < (lookup['source'] + lookup['length']):
            location = humidity - lookup['source'] + lookup['destination']
            '''for r in range(0, lookup['length']):
                if lookup['source'] + r == humidity:
                    location = lookup['destination'] + r'''

    print("Seed", seed, "goes to location", location)
    if location < lowest_location:
        lowest_location = location

print(lowest_location)
