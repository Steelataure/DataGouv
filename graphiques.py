import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Graph_WinRate_PickRate():
    win_rate_par_rank_par_champ = pd.read_json('WinRate_PickRate.json')

    plt.figure(figsize=(14, 10))
    sns.barplot(x='Pick Rate, %', y='Hero', hue='Skill Tier', data=win_rate_par_rank_par_champ)
    plt.title('Taux de sélection par Héros et par Rank')
    plt.legend(title='Skill Tier')
    plt.show()

    plt.figure(figsize=(14, 10))
    sns.barplot(x='Win Rate, %', y='Hero', hue='Skill Tier', data=win_rate_par_rank_par_champ)
    plt.title('Taux de victoire par Héros et par Rank')
    plt.legend(title='Skill Tier')
    plt.show()

def Comp_selon_saison():
    data_list = []
    
    for i in range(1, 5):
        chemin_fichier = f'Best_Comp_Saison_{i}.json' 
        best_comp = pd.read_json(chemin_fichier)
        data_list.append(best_comp)
    
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

def Graph_KDA_par_champion():
    data_list = []
    
    for i in range(1, 5):
        chemin_fichier = f'KDA_Saison_0{i}.json'  
        kda_data = pd.read_json(chemin_fichier)
        data_list.append(kda_data)
    
    for i, kda_data in enumerate(data_list, start=1):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='KDA', y='Hero', hue='Skill Tier', data=kda_data)
        plt.title(f'KDA par Champion Saison {i}')
        plt.xlabel('KDA')
        plt.ylabel('Héros')
        plt.xticks(rotation=45)
        plt.legend(title='Skill Tier')
        plt.tight_layout()
        plt.show()

def main():
    Comp_selon_saison()
    Graph_WinRate_PickRate()
    Graph_KDA_par_champion()

if __name__ == "__main__":
    main()
