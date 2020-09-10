# %%
# Traversing the dictionary

grades = {'Ram': 'A', 'Sham': "B", 'Tom': 'C', "Dom": "D"}
for keys in grades:
    print(keys, ":", grades[keys])

# %%

players = {"VIRAT": {"ODI": 7212, "TEST": 10123},
           "SACHIN": {"ODI": 10345, "TEST": 20456}}
for name, details in players.items():
    print("Player :", name)
    print("Run scored in ODI  :", details["ODI"])
    print("Run scored in TEST  :", details["TEST"])

# %%

players = {"VIRAT": {"ODI": 7212, "TEST": 10123},
           "SACHIN": {"ODI": 10345, "TEST": 20456}}
players["VIRAT"]["ODI"]
#players ["VIRAT"]["TEST"]
#players ["SACHIN"]["ODI"]
#players ["SACHIN"]["TEST"]
