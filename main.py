import pandas as pd
import numpy as np

chemin_fichier_partie_rapide = 'archive/ow2_quickplay_heroes_stats__2023-05-06.csv'
chemin_fichier_saison_1 = 'archive/ow2_season_01_FINAL_heroes_stats_2023-05-06.csv' 
chemin_fichier_saison_2 = 'archive/ow2_season_02_FINAL_heroes_stats_2023-05-06.csv'
chemin_fichier_saison_3 = 'archive/ow2_season_03_FINAL_heroes_stats_2023-05-06.csv'
chemin_fichier_saison_4 = 'archive/ow2_season_04_FINAL_heroes_stats_2023-05-06.csv'

df = pd.read_csv(chemin_fichier_partie_rapide)

selection_victoire = df[['Hero', 'Skill Tier', 'Pick Rate, %', 'Win Rate, %']]

moyennes_selection_victoire = selection_victoire.groupby(['Hero', 'Skill Tier']).mean().reset_index()

moyennes_selection_victoire.to_json('test.json', orient='records', indent=4)

print(moyennes_selection_victoire)