#!/usr/bin/env python
import pandas as pd
from matplotlib import pyplot as plt


pokemon = pd.read_csv('csv_files/pokemon.csv')

"""
############################################################################################
   Practicing new column creation, .apply(lambda), column selection with and without logic.
############################################################################################
"""

# Changing the values of 'is_legendary' from 0/1's to True/False for the entire dataframe:
pokemon['is_legendary'] = pokemon['is_legendary'].apply(lambda x: True \
        if x == 1 \
        else False)


# Determing type of pokemon based on attack, defense, or balanced attack/defense based off numbers and creating new column
# This was kinda complicated since you CANNOT use 'elif' statements in lambda functions, you have to
# nest if..else statements. That's why the second 'else' statement is inside the parenthesis of the
# first else statement, basically you have to repeat the if statement within the else statement.
pokemon['battle_type'] = pokemon.apply(lambda x: 'attack type' \
        if x.attack > x.defense \
        else ('balanced' if x.attack == x.defense \
        else 'defense type'), \
        axis=1)


# Plotting the new column as a bar chart:
plt.figure()
pokemon['battle_type'].value_counts().plot.bar(figsize=(10, 15))
plt.xlabel('Battle types')
plt.ylabel('Number of pokemon')
plt.title('Number of pokemon who belong to Attack/Defense/Balanced types')
plt.savefig('pokemon_dataframes/bar_test.png')

# Selecting all of the legendary pokemon: 
legendaries = pokemon[pokemon['is_legendary'] == True]
legendaries.to_csv('pokemon_dataframes/legendary_pokemon.csv')

print('')

# Finding the total count of legendary pokemon and printing just the name, generation, and is_legendary columns
legendary_count = pokemon['is_legendary'].value_counts()
legendary_gen3 = pokemon.loc[((pokemon['is_legendary'] == True) & (pokemon['generation'] == 3)), ['name', 'generation', 'is_legendary']]
print('Counting the total number of legendary pokemon, True == legendary')
print(legendary_count)
print('')
print('Printing only the name of gen 3 legendary pokemon')
print(legendary_gen3)

print('')
print('')


# Finding all of the flying type pokemon and saving it to an CSV
flying = pokemon.loc[(pokemon['type1'] == 'flying') | (pokemon['type2'] == 'flying'), ['name', 'attack', 'defense', 'pokedex_number', 'type1', 'type2', \
        'generation', 'is_legendary', 'battle_type']]
flying = flying.reset_index(drop=True)
print('All flying types')
print(flying.head(10))
flying.to_csv('pokemon_dataframes/flying_types.csv')

print('')
print('')


# Finding all the ice and flying type pokemon.
# If we wanted too, we could have narrowed down the above dataframe 'flying' and kept the same column configuration since
# the 'flying' dataframe has already narrowed down all of the flying pokemon
ice_fly = pokemon[((pokemon['type1'] == 'ice') & (pokemon['type2'] == 'flying')) | ((pokemon['type1'] == 'flying') & (pokemon['type2'] == 'ice'))]
ice_fly = ice_fly.reset_index(drop=True)
print(ice_fly.head())
ice_fly.to_csv('pokemon_dataframes/ice_flying.csv')



print('')
print('')
print('')


"""
#######################################################################################
   Practicing using groupby and pivoting
#######################################################################################
"""

# Counting the total number of pokemon for each generation
gen_count = pokemon.groupby('generation').pokedex_number.count()
print('Printing the total number of pokemon in each generation:')
print(gen_count)



print('')
print('')


# Calculating the average height of each classification of pokemon:
#NOTE: 'classification' is spelled INCORRECTLY ON PURPOSE! the CSV has the column name as 'classficiation'
avg_height = pokemon.groupby('classfication').height_m.mean()
avg_height_round = avg_height.round(2)
classfication_count = pokemon.groupby('classfication').classfication.count()
print('Printing the total number of pokemon in each classification:')
print(classfication_count)
print('')
print('Calculating the average height for each classification of pokemon in meters')
print(avg_height)
avg_height.to_csv('pokemon_dataframes/pokemon_classification_heights_meters.csv')


print('')
print('')


# Further calculating the min and max attack for each generation
attack_min_max = pokemon.groupby('generation').attack.agg(['min', 'max', 'median', 'mean'])
print('Further calculating the min/max of every attack by generation:')
print(attack_min_max)


print('')
print('')


# attack of generation, type1. Further building up on the calculationa above
gen_type_rate = pokemon.groupby(['type1', 'generation']).attack.mean().reset_index()
gen_type_rate = gen_type_rate.round(2)
gen_type_rate = gen_type_rate.pivot(
        columns='generation',
        index='type1',
        values='attack')
print('attack of type1/generation:')
print(gen_type_rate)
gen_type_rate.to_csv('pokemon_dataframes/pivot_example.csv')


"""
############################################################################################
   Practicing using Pandas to plot basic figures.
############################################################################################
"""
# The 'attack' column has a nice spread of values, histograph of it. Using 
# 'plt.close('all') since we have a figure plotted at the beginning and trying
# to keep it clean
plt.close('all')
plt.figure()
ax = plt.subplot()
pokemon['attack'].plot.hist()
plt.title('Spread of attack values')
plt.xlabel('Attack value')
plt.ylabel('Number of pokemon')
ax.set_yticks(range(0, 250, 25))
ax.set_yticklabels(range(0, 250, 25))
plt.savefig('pokemon_dataframes/histogram_test.png')


# The 'base_egg_steps' has a pretty huge spread, plotting line chart:
plt.close('all')
plt.figure()
pokemon['base_egg_steps'].value_counts().sort_index().plot.area()
plt.xlabel('Base number of steps required to hatch egg')
plt.ylabel('Number of Pokemon')
plt.title('Number of pokemon and frequency of base steps needed to hatch an egg')
plt.savefig('pokemon_dataframes/line_test.png')


# Plotting pie chart of split of Legendary and non-legendary pokemon
# NOTE: the line 'plt.ylabel('')' is used to remove the column name displayed
### on the pie chart. For some reason it just automatically prints it 
### on the y-axis. Setting it as blank.
plt.close('all')
plt.figure()
pie_labels = ['Non-legendary', 'Legendary']
pokemon['is_legendary'].value_counts().plot.pie(labels=pie_labels, autopct='%0.2f%%')
plt.title('Percentage of legendary pokemon from entire pokemon population')
plt.ylabel('')
plt.legend()
plt.savefig('pokemon_dataframes/pie_test.png')


