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

def kda_global_per_champion():
    print("Calcul du KDA global par champion et par rang...")
    files = [f'archive/ow2_season_0{i}_FINAL_heroes_stats__2023-05-06.csv' for i in range(1, 5)]
    all_data = []

    for file_path in files:
        df = pd.read_csv(file_path)
        if 'Eliminations / 10min' in df.columns and 'Deaths / 10min' in df.columns:
            df['Season'] = file_path.split('_')[2]
            all_data.append(df[['Hero', 'Skill Tier', 'Season', 'Eliminations / 10min', 'Deaths / 10min']])

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df['KDA'] = combined_df['Eliminations / 10min'] / combined_df['Deaths / 10min']
        kda_selection = combined_df[['Hero', 'Skill Tier', 'KDA']].groupby(['Hero', 'Skill Tier']).mean().reset_index()
        kda_selection.to_json('KDA_Global.json', orient='records', indent=4)
        print("Le fichier KDA_Global.json a été créé avec succès.")
    else:
        print("Aucune donnée n'a été trouvée pour calculer le KDA.")
        
def create_headshot_accuracy_json():
    files = [f'archive/ow2_season_0{i}_FINAL_heroes_stats__2023-05-06.csv' for i in range(1, 5)]

    all_data = []

    for file in files:
        df = pd.read_csv(file)
        if 'Crit Accuracy, %' in df.columns:
            df_filtered = df[['Hero', 'Skill Tier', 'Crit Accuracy, %']]
            all_data.append(df_filtered)
        else:
            print(f"Column 'Headshot Accuracy, %' not found in {file}")

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df.to_json('Headshot_Accuracy.json', orient='records', indent=4)
        print("Le fichier Headshot_Accuracy.json a été créé avec succès.")
    else:
        print("Aucune donnée d'accuracy de headshot trouvée dans les fichiers.")

    
def main():
    Comp_selon_saison()
    WinRate_PickRate()
    kda_global_per_champion()
    create_headshot_accuracy_json()


if __name__ == "__main__":
    main()
