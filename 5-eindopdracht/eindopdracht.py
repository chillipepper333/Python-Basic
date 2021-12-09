import time
#de variabelen voor de klok hier kan je ook de starttijd instellen
uur= int(input('enter uur'))
minuten= int(input('enter minuten'))
seconden= int(input('enter seconden'))

def showklok():
    print('%02d'%i, '%02d'%j, '%02d'%k, sep=":")

# de klok loop
while True:
    for i in range(uur,24):
            
        for j in range(minuten, 60):
           
            for k in range(seconden, 60):  
                time.sleep(1)
                showklok()
            seconden=0 
        minuten = 0
    uur = 0
                
# de if's zorgen dat de int na het instellen van de tijdnaar 0 gezet word
# de '%02d'% zorgt ervoor dat de getallen die in de console getoont woorden altijd uit 2 bestaan 01, 02 bijv.
# de sep zorgt dat tussen de uur minuten en seconden een : komt.
# en de time.sleep zorgt ervoor dat de loop iedere seconden een pauze neemt van een seconden.



