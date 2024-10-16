import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def load_data(file_path):
    return pd.read_csv(file_path)


data_a = load_data(r"data_a.csv")
data_b = load_data(r"data_b.csv")

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].scatter(data_a.index, data_a['data_a'], color="r")
ax[1].scatter(data_b.index, data_b['data_b'], color="b")

for i in range(2):
    ax[i].set_title(f"Data {'A' if i == 0 else 'B'}")
    ax[i].set_xlabel("Index")
    ax[i].set_ylabel("Value")

ax[0].axhline(data_a['data_a'].mean(), color='r', linestyle='dashed', linewidth=2)
ax[1].axhline(data_b['data_b'].mean(), color='b', linestyle='dashed', linewidth=2)
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].hist(data_a['data_a'], bins=13, color="r")
ax[1].hist(data_b['data_b'], bins=13, color="b")

for i in range(2):
    ax[i].set_title(f"Data {'A' if i == 0 else 'B'}")
    ax[i].set_xlabel("Value")
    ax[i].set_ylabel("Frequency")

plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 5), num='Boxplot')

# Plot for data_a on ax[0]
ax[0].boxplot(data_a['data_a'], widths=0.6, patch_artist=True,
              boxprops=dict(facecolor='r'), whiskerprops=dict(color='black'),
              capprops=dict(color='black'), medianprops=dict(color='black'),
              flierprops=dict(marker='o', markerfacecolor='white', markeredgecolor='black'),
              positions=[1])

# Plot for data_b on ax[1]
ax[1].boxplot(data_b['data_b'], widths=0.6, patch_artist=True,
              boxprops=dict(facecolor='b'), whiskerprops=dict(color='black'),
              capprops=dict(color='black'), medianprops=dict(color='black'),
              flierprops=dict(marker='o', markerfacecolor='white', markeredgecolor='black'),
              positions=[1])

plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 5), num='QQ-Plot')

stats.probplot(data_a['data_a'], dist="norm", plot=ax[0])
stats.probplot(data_b['data_b'], dist="norm", plot=ax[1])

plt.show()

data = pd.concat([data_a, data_b], axis=1)
data.columns = ['data_a', 'data_b']
print(data.describe())

# generate n random numbers centered around 71 with a standard deviation of 10


# generate another n random numbers centered around 70 following students t-distribution


# Der gezeigte Code lädt Daten aus zwei CSV-Dateien und visualisiert diese in zwei verschiedenen Diagrammen. Zunächst werden die notwendigen Bibliotheken `pandas` und `matplotlib.pyplot` importiert, um Daten zu laden und zu visualisieren.
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# Die Funktion `load_data` nimmt einen Dateipfad als Argument und gibt die gelesenen Daten als DataFrame zurück.
#
# def load_data(file_path):
#     return pd.read_csv(file_path)
#
# Anschließend werden die Daten aus den Dateien `data_a.csv` und `data_b.csv` geladen und in den Variablen `data_a` und `data_b` gespeichert.
#
# data_a = load_data(r"data_a.csv")
# data_b = load_data(r"data_b.csv")
#
# Der erste Plot wird erstellt, indem ein Scatter-Plot für beide Datensätze in einem 1x2-Subplot-Layout erzeugt wird. Die Datenpunkte von `data_a` werden in rot und die von `data_b` in blau dargestellt.
#
# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# ax[0].scatter(data_a.index, data_a['data_a'], color="r")
# ax[1].scatter(data_b.index, data_b['data_b'], color="b")
#
# Um die Diagramme zu beschriften, wird eine Schleife verwendet, die den Titeln, den x-Achsen und den y-Achsen der Subplots entsprechende Beschriftungen hinzufügt.
#
# for i in range(2):
#     ax[i].set_title(f"Data {'A' if i == 0 else 'B'}")
#     ax[i].set_xlabel("Index")
#     ax[i].set_ylabel("Value")
#
# Der Plot wird dann angezeigt.
#
# plt.show()
#
# Ein zweiter Plot wird erstellt, diesmal als Histogramm für beide Datensätze, ebenfalls in einem 1x2-Subplot-Layout. Die Histogramme von `data_a` und `data_b` werden in rot bzw. blau dargestellt.
#
# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# ax[0].hist(data_a['data_a'], bins=10, color="r")
# ax[1].hist(data_b['data_b'], bins=10, color="b")

# Auch hier wird eine Schleife verwendet, um die Diagramme zu beschriften.
#
# for i in range(2):
#     ax[i].set_title(f"Data {'A' if i == 0 else 'B'}")
#     ax[i].set_xlabel("Value")
#     ax[i].set_ylabel("Frequency")
#
#
# Schließlich wird auch dieser Plot angezeigt.
#
# plt.show()
