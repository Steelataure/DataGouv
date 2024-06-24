import pandas as pd

chemin_fichier_partie_rapide = 'archive/ow2_quickplay_heroes_stats__2023-05-06.csv'
chemin_fichier_saison_1 = 'archive/ow2_season_01_FINAL_heroes_stats__2023-05-06.csv' 
chemin_fichier_saison_2 = 'archive/ow2_season_02_FINAL_heroes_stats_2023-05-06.csv'
chemin_fichier_saison_3 = 'archive/ow2_season_03_FINAL_heroes_stats_2023-05-06.csv'
chemin_fichier_saison_4 = 'archive/ow2_season_04_FINAL_heroes_stats_2023-05-06.csv'

def meilleur_composition_par_saison(chemin_fichier):
    df = pd.read_csv(chemin_fichier)

    df_grandmaster = df[df['Skill Tier'] == 'Grandmaster']

    selection_victoire = df_grandmaster[['Hero', 'Role', 'Pick Rate, %', 'Win Rate, %']]

    meilleur_tank = selection_victoire[selection_victoire['Role'] == 'Tank'].nlargest(1, 'Pick Rate, %')

    meilleur_dps = selection_victoire[selection_victoire['Role'] == 'Damage'].nlargest(2, 'Pick Rate, %')

    selection_victoire_sans_dps = selection_victoire[~selection_victoire['Hero'].isin(meilleur_dps['Hero'])]
    meilleur_supp = selection_victoire_sans_dps[selection_victoire_sans_dps['Role'] == 'Support'].nlargest(2, 'Pick Rate, %')
    
    best_comp = pd.concat([meilleur_tank, meilleur_dps, meilleur_supp])

    return best_comp

print(meilleur_composition_par_saison(chemin_fichier_saison_1))
