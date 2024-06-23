import pandas as pd
import numpy as np

chemin_fichier_partie_rapide = 'archive/ow2_quickplay_heroes_stats__2023-05-06.csv'
chemin_fichier_saison_1 = 'archive/ow2_season_01_FINAL_heroes_stats__2023-05-06.csv' 
chemin_fichier_saison_2 = 'archive/ow2_season_02_FINAL_heroes_stats__2023-05-06.csv'
chemin_fichier_saison_3 = 'archive/ow2_season_03_FINAL_heroes_stats__2023-05-06.csv'
chemin_fichier_saison_4 = 'archive/ow2_season_04_FINAL_heroes_stats__2023-05-06.csv'

def WinRate_PickRate():
    df = pd.read_csv(chemin_fichier_partie_rapide)

    selection_victoire = df[['Hero', 'Skill Tier', 'Pick Rate, %', 'Win Rate, %']]

    moyennes_selection_victoire = selection_victoire.groupby(['Hero', 'Skill Tier']).mean().reset_index()

    moyennes_selection_victoire.to_json('WinRate_PickRate.json', orient='records', indent=4)

    print(moyennes_selection_victoire)

def meilleur_composition_par_saison(chemin_fichier):
    df = pd.read_csv(chemin_fichier)

    df = df.loc[df['Skill Tier'] == 'Grandmaster']

    selection_victoire = df[['Hero', 'Role', 'Pick Rate, %']]

    meilleur_tank = selection_victoire[selection_victoire['Role'] == 'Tank'].nlargest(1, 'Pick Rate, %')
    meilleur_dps = selection_victoire[selection_victoire['Role'] == 'Damage'].nlargest(2, 'Pick Rate, %')
    meilleur_supp = selection_victoire[selection_victoire['Role'] == 'Support'].nlargest(2, 'Pick Rate, %')

    best_comp = pd.concat([meilleur_tank, meilleur_supp, meilleur_dps])

    return best_comp

def Comp_selon_saison():
    for i in range(1, 5):
        chemin_fichier = f'archive/ow2_season_0{i}_FINAL_heroes_stats__2023-05-06.csv'
        best_comp = meilleur_composition_par_saison(chemin_fichier)

        best_comp.to_json(f'Best_Comp_Saison_{i}.json', orient='records', indent=4)

def main():
        Comp_selon_saison()
        WinRate_PickRate()

if __name__ == "__main__":
    main()

