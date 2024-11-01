"""Arbeidskrav 1

Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil 
samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån 
og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km."""


#felles kostnader
årlig_kjørelengde=12000
trafikkforsikringsavgift=8.38*365

#kostnader elbil
forsikring_elbil=5000
drivstoff_forbruk_elbil=0.2
strømpris=2
bomavgift_elbil=0.1

#kostnader bensinbil
forsikring_bensinbil=7500
bomavgift_bensinbil=0.3
drivstoff_forbruk_bensinbil=1.0


#Utregninger

#Kostnader elbil
årligeutgifter_elbil=forsikring_elbil+(trafikkforsikringsavgift)+(årlig_kjørelengde*(drivstoff_forbruk_elbil*strømpris))+(bomavgift_elbil*årlig_kjørelengde)

#kostnader bensinbil
årligeutgifter_bensinbil=forsikring_bensinbil+(trafikkforsikringsavgift)+(drivstoff_forbruk_bensinbil*årlig_kjørelengde)+(bomavgift_bensinbil*årlig_kjørelengde)

# Kostnadsdifferanse bensinbil vs elbil
kostnadsdifferanse=årligeutgifter_bensinbil-årligeutgifter_elbil

print()
print(f"De årlige kostnadene for å eie elbil er {årligeutgifter_elbil}kr")
print(f"De årlige kostnadene for å eie bensinbil er {årligeutgifter_bensinbil}kr")
print(f"Det er en årlig kostnadsdifferanse på {årligeutgifter_bensinbil-årligeutgifter_elbil}kr for å eie en bensinbil istedenfor enn en elbil")
print()
