import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Graph_WinRate_PickRate():
    win_rate_par_rank_par_champ = pd.read_json('WinRate_PickRate.json')

    plt.figure(figsize=(14,10))
    sns.barplot(x='Pick Rate, %', y='Hero', hue='Skill Tier', data=win_rate_par_rank_par_champ)
    plt.title('Taux de séléction par Héros et par Rank')
    plt.legend(title='Skill Tier')
    plt.show()

    plt.figure(figsize=(14,10))
    sns.barplot(x='Win Rate, %', y='Hero', hue='Skill Tier', data=win_rate_par_rank_par_champ)
    plt.title('Taux de victoire par champ et par rank')
    plt.legend(title='Skill Tier')
    plt.show()

def Comp_selon_saison():
    data_list = []
    
    # Charger les données JSON dans la liste
    for i in range(1, 5):
        chemin_fichier = f'Best_Comp_Saison_{i}.json'  # Assurez-vous que le chemin est correct
        best_comp = pd.read_json(chemin_fichier)
        data_list.append(best_comp)
    
    # Afficher les graphiques après avoir lu toutes les données
    for i, best_comp in enumerate(data_list, start=1):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Hero', y='Pick Rate, %', hue='Role', data=best_comp)
        plt.title(f'Meilleure Composition Saison {i} (Grandmaster)')
        plt.xlabel('Héros')
        plt.ylabel('Taux de Sélection (%)')
        plt.xticks(rotation=45)
        plt.legend(title='Rôle')
        plt.tight_layout()
        plt.show()
        
def main():
    Comp_selon_saison()

if __name__ == "__main__":
    main()


