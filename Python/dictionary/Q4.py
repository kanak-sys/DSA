"create a dictionary mapping 5 countries to their capital cities"
"iterate through this dictionary using items()"
"and print each pair in the format country -> capital"

mapping = {"India": "New Delhi",
           "China": "Beijing",
           "Pakistan": "Islamabad",
           "SriLanka": "Sri Jayawardenepura Kotte",
           "America": "Washington, D.C",
           "Russia": "Moscow"}
print(mapping.items())

for country, capital in mapping.items():
    print(f"Country & capital: {country}->{capital}")