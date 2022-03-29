from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(mylist):
  return_list = []
  for item in mylist:
    if item == "Damages not recorded":
      return_list.append(item)
      continue
    last_letter = item[-1]
    multiply_by = conversion[last_letter]
    number = float(item[:-1])
    return_list.append(number*multiply_by)
  return return_list

# test function by updating damages
#print(damages)
#print(update_damages(damages))
damages = update_damages(damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary

def create_hurridict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  my_dict = {}
  for i in range(len(names)):
    name = names[i]
    my_dict[name] = {
      "Name": name, 
      "Month": months[i], 
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i], 
      "Areas Affected": areas_affected[i], 
      "Damage": damages[i], 
      "Deaths": deaths[i]
    }
  return my_dict

hurricanes_dict = create_hurridict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

#print(hurricanes_dict["Cuba I"])

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def organize_by_year(hurridict):
  new_dict = {}
  for record in hurridict.values(): 
    year = record['Year']
    try:
      new_dict[year].append(record)
    except KeyError:
      new_dict[year] = [record]
  return new_dict

hurricanes_dict_year = organize_by_year(hurricanes_dict)
#print(hurricanes_dict_year[1932])

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def num_hurricanes(hurricanes_dict):
  new_dict = {}
  for hurr in hurricanes_dict.values():
    list_areas = hurr['Areas Affected']
    for area in list_areas:
      try:
        new_dict[area] += 1
      except KeyError:
        new_dict[area] = 1
  return new_dict

#print(num_hurricanes(hurricanes_dict))

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected(hurricanes_dict):
  stats = num_hurricanes(hurricanes_dict)
  max_hits = max(stats, key=stats.get)
  return (max_hits, stats[max_hits])

#print(most_affected(hurricanes_dict))

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest(hurricanes_dict):
  max_deaths = 0
  for hurr in hurricanes_dict:
    if hurricanes_dict[hurr]["Deaths"] > max_deaths:
      max_deaths = hurricanes_dict[hurr]["Deaths"]
      name = hurr
  return (name, max_deaths)

#print(deadliest(hurricanes_dict))

# 7
# Rating Hurricanes by Mortality

# categorize hurricanes in new dictionary with mortality severity as key
def mortality_dict(hurricanes_dict):
  d = defaultdict(list)
  for hurr in hurricanes_dict.values():
    deaths = hurr["Deaths"]
    if deaths > 10000:
      scale = 5
    elif deaths > 1000:
      scale = 4
    elif deaths > 500:
      scale = 3
    elif deaths > 100:
      scale = 2
    elif deaths > 0:
      scale = 1
    else:
      scale = 0
    d[scale].append(hurr)
  return d

#print(mortality_dict(hurricanes_dict)[5])

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def greatest_damage(hurricanes_dict):
  max_damage = 0
  for hurr in hurricanes_dict.values():
    damage = hurr["Damage"]
    if isinstance(damage, str):
      continue
    if damage > max_damage:
      max_damage = damage
      name = hurr["Name"]
  return (name, max_damage)

#print(greatest_damage(hurricanes_dict))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_scale_dict(hurricanes_dict, damage_scale):
  d = defaultdict(list)
  for hurr in hurricanes_dict.values():
    damage = hurr["Damage"]
    if isinstance(damage, str):
      continue
    for i in range(4,-1,-1):
      if damage > damage_scale[i]:
        d[i+1].append(hurr)
        break
    else:  # Executed because no break
      d[0].append(hurr)
  return d

#print(damage_scale_dict(hurricanes_dict, damage_scale)[3])
