# Røddi

Å gjøre opp dødsbo og er kjipt. Det er vanskelig å bli enige mellom familiemedlemmer hvem som  skal ha hvilke eiendeler og hva som skal skje med andre eiendeler. Etterlatte familiemedlemmer har  et behov for en tjeneste som hjelper dem med å løse slike floker.  
Admin-teamet i Røddi går igjennom leiligheten til den som er gått bort og loggfører eiendelene som  er der. Så skal familiemedlemmene kunne bestemme om de vil fordele eiendeler mellom seg,  donere det bort eller kaste det. Skal de fordele eiendeler mellom seg, trenger vi en smart måte å la  dem komme med ønsker og faktisk få fordelt eiendelene. Alle familiemedlemmer over 18 år må  skulle kunne opprette en profil og bli koblet til et oppgjør/dødsbo. Det er viktig at all informasjon om  eiendeler, ønsker, og slikt blir lagret persistent, så ikke alle trenger å være pålogget samtidig.  
Det hadde også vært kult og man kunne legge inn kommentarer på eiendelene, men da må det i så  fall være mulig å moderere kommentarene for administratorer og eiere av Røddi.  
Vi har ikke helt bestemt om det skal være en mobil-app eller nettside, men det er viktig med et godt  design.

Opprette databsen og connection til django:
følg nedlastingsunstruksjoner som ligget i Databasefaget. Opprett en database med navn roddi, gjennom workbench eller i terminal. (workbench: CREATE DATABASE roddi;)
Bruk disse kommandoene i terminalen:
py -m pip install mysqlclient
py manage.py makemigrations
py manage.py migrate 

Til mySQL databasen første gang:
Må skrive følgende i terminalen;
py -m pip install django-crispy-forms    (python3 for mac ikke py)
Får å opprette første admin;
py manage.py createsuperuser
