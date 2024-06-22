import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

win_rate_par_rank_par_champ = pd.read_json('test.json')

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


