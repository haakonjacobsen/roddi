# Røddi

Denne nettsiden, Røddi, hjelper etterlatte familier med å fordele dødsbo. I hvert dødsbo vises alle gjenstandene som skal fordeles. De etterlatte kan velge om de ønsker at en gjenstand skal kastes, doneres eller beholdes. I tillegg har de muligheten til å markere de gjenstandene de har mest lyst på ved å trykke på «en knapp». For at familien enklere skal fordele gjenstandene mellom seg, kan de legge inn kommentarer på gjenstandene.

## Opprette databsen og connection til django:

Opprett en database med navn roddi, gjennom workbench eller i terminal. 
For workbench, skriv: CREATE DATABASE roddi;

Derretter bruker man disse kommandoene i terminalen:
- **py -m pip install mysqlclient**
- **py manage.py makemigrations**
- **py manage.py migrate**

 

## Til mySQL databasen første gang:

Man må først skrive følgende i terminalen:

- **py -m pip install django-crispy-forms    (python3 for mac ikke py)**

Derretter må man opprette første admin, ved å skrive:
- **py manage.py createsuperuser**

## For å starte nettsiden

For å starte hele nettsiden, skriv:
- **py manage.py makemigrations**
- **py manage.py runserver**

