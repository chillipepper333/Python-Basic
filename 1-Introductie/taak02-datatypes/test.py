import time

def keerdelistom(x):
    for i in reversed(x):
        print(i, end= ' ')
    print()
    return
# functies hierboven
# main program hieronder
a = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
keerdelistom(a)
print('End program')