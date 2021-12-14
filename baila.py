'''
 See on seltskonnamäng Baila, mäng käib kogu kaardipaki peale
ning kaardid pannakse enamasti ilusasti ringi ja kordamööda võetakse
ringist kaarte ilma ringi lõhkumata.
#randomiga ka tekst oih, ring läks katki, võta lonks
'''
from random import randint

def randomize(algne):
    uus = []
    for a in range(algne):
        print(uus[a])
    
    #return uus

def milline(number):
    try:
        kaardid = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        käsud = ['1 lonks', '2 lonksu', 'võta 1, anna 1', 'tee džunglimahla!!', 'vali teema!', 'alusta riimi!', 'BAILA!!', 'mõtle uus reegel!', 'küsimusekaart!!', 'kuni kaart on, ei tohi telefonis olla!', 'poisid võtavad!', 'naised võtavad!', 'WATERFALL!!']
        koht = kaardid.index(number)
        #print(number)
        print(käsud[koht])
    except:
        return False

mastid = ['♣', '♦', '♥', '♠']
kaardid = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
kõik_kaardid = ['2♣', '2♦', '2♥', '2♠', '3♣', '3♦', '3♥', '3♠', '4♣', '4♦', '4♥', '4♠', '5♣', '5♦', '5♥', '5♠', '6♣', '6♦', '6♥', '6♠', '7♣', '7♦', '7♥', '7♠', '8♣', '8♦', '8♥', '8♠', '9♣', '9♦', '9♥', '9♠', '10♣', '10♦', '10♥', '10♠', 'J♣', 'J♦', 'J♥', 'J♠', 'Q♣', 'Q♦', 'Q♥', 'Q♠', 'K♣', 'K♦', 'K♥', 'K♠', 'A♣', 'A♦', 'A♥', 'A♠']
n = ['2♦', '3♥', '3♠', '4♣', '5♣', '6♠', '7♣', '8♠', '9♣', '10♠', 'J♣', 'Q♠', 'K♣', 'A♥']
vahepealne = kõik_kaardid

for a in vahepealne:
    try: 
        if len(a) > 2:
            #print(a[0:2])
            milline(a[0:2])
            
        else:
            #print(a[0])
            milline(a[0])
    except:
        break
randomize(milline)
