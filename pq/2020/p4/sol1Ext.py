import sol1
# thank you stack overflow for cls option based on : os.system('cls' if os.name == 'nt' else 'clear')
# sha i just printed empty lines instead, manual clear salaam
print("\n"*2)
for country,president in sol1.presesSort:
    print(president, "\t", country)
# so, things cut short, the above is an actual table. Can be copied to excel
