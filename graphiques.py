import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Graph_WinRate_PickRate():
    win_rate_par_rank_par_champ = pd.read_json('WinRate_PickRate.json')

    plt.figure(figsize=(20, 10))
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
    
    chemin_fichier = f'KDA_Global.json'  
    kda_data = pd.read_json(chemin_fichier)
    data_list.append(kda_data)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='KDA', y='Hero', hue='Skill Tier', data=kda_data, ci=None)
    plt.title(f'KDA par Champion')
    plt.xlabel('KDA')
    plt.ylabel('Héros')
    plt.xticks(rotation=45)
    plt.legend(title='Skill Tier')
    plt.tight_layout()
    plt.show()
    
    
def Graph_Headshot_Accuracy():
    chemin_fichier = 'Headshot_Accuracy.json'
    headshot_data = pd.read_json(chemin_fichier)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Crit Accuracy, %', y='Hero', hue='Skill Tier', data=headshot_data, ci=None)
    plt.title('Accuracy des Headshots par Champion et par Rank')
    plt.xlabel('Accuracy des Headshots (%)')
    plt.ylabel('Héros')
    plt.xticks(rotation=45)
    plt.legend(title='Skill Tier')
    plt.tight_layout()
    plt.show()

def Graph_Headshot_Accuracy_By_Tier():
    chemin_fichier = 'Headshot_Accuracy.json'
    headshot_data = pd.read_json(chemin_fichier)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Skill Tier', y='Crit Accuracy, %', data=headshot_data, ci=None)
    plt.title('Accuracy des Headshots par Rank')
    plt.xlabel('Skill Tier')
    plt.ylabel('Accuracy des Headshots (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def Graph_Best_Healers():
    # Charger les données à partir du fichier JSON
    best_healers_data = pd.read_json('Champion_Stats_Per_Tier.json')

    # Créer le graphique
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Healing / 10min', y='Hero', data=best_healers_data, ci=None)
    plt.title('Meilleurs guérisseurs par guérison en 10min')
    plt.xlabel('Guérison en 10min')
    plt.ylabel('Héros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def Graph_Best_Eliminators():
    # Charger les données à partir du fichier JSON
    best_eliminations_data = pd.read_json('Champion_Stats_Per_Tier.json')

    # Créer le graphique
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Eliminations / 10min', y='Hero', data=best_eliminations_data, ci=None)
    plt.title('Meilleurs éliminateurs par éliminations en 10min')
    plt.xlabel('Éliminations en 10min')
    plt.ylabel('Héros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def main():
    Comp_selon_saison()
    Graph_WinRate_PickRate()
    Graph_KDA_par_champion()
    Graph_Headshot_Accuracy()
    Graph_Headshot_Accuracy_By_Tier()
    Graph_Best_Healers()
    Graph_Best_Eliminators()

if __name__ == "__main__":
    main()
