import os, sys
# zmienne srodowiskowe
envs = os.environ.items()
# argumenty z linii komend
argv = sys.argv[1::]
# wynik
result = {}
# jesli brak argumentow wypisz wszystkie zmienne
if len(argv)==0: 
    for n, v in envs:
        result[n]= v
# jesli sa arg to wyswietlamy tylko zmienne zawierajace w nazwie ktorys argument 
else:
    for a in argv:
        for n, v in envs:
            if ((a in n) and (not a in result)): result[n]=v


for r in result:
    print(r, result.get(r), "\n")