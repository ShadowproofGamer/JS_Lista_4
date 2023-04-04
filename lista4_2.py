import os, sys

# argumenty z linii komend
argv = sys.argv[1::]
#print(argv)
# zebranie katalogów do tablicy
paths = os.environ.get("PATH").split(":")

#jeżeli podany zostanie odpowiedni argument to wyświetla wszystkie katalogi i pliki w danej zmiennej środowiskowej, w innym wypadku podaje tylko zmienne
if (argv.__contains__('all' ) or argv.__contains__('--all' )  or argv.__contains__('files' ) or argv.__contains__('--files' )):
    # wyswietlanie wszystkich plików dla danej scieżki
    for name in paths:
        print(name, os.listdir(name))
else:
    # wyswietlanie katalogów
    for name in paths:
        print(name)
