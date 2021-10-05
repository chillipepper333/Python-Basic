import time
#de variabelen voor de klok hier kan je ook de starttijd instellen
seconden=50
minuten=37
uur=2

# de klok loop
while seconden <60:
    seconden +=1
    # de '%02d'% zorgt ervoor dat de getallen altijd uit 2 bestaan 01, 02 bijv.
    # de sep zorgt dat tussen de uur minuten en seconden een : komt.
    # en de time.sleep zorgt ervoor dat er iedere seconden een seconden bij komt.
    print('%02d'%uur, '%02d'%minuten, '%02d'%seconden, sep=":")
    time.sleep(1)
    #deze if zorgen ervoor dat als de seconden op 60 komt er 1 minuut bijkomt en de seconden weer gerzet word.
    #dit geld ook voor de andere if's
    if seconden == 59:
        minuten +=1
        seconden =-1
        if minuten == 60:
            uur +=1
            minuten =0
            if uur ==24:
                uur = 0