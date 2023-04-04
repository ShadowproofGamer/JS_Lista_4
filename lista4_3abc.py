def zad3_b():
    # b
    f = open(file_path, "r")
    all_content = f.read()
    #print("N f")

    # liczba znaków
    sign_count = len(all_content.strip())

    # liczba słów
    all_content_tab = all_content.split()
    word_count = len(all_content_tab)


    # liczba wierszy
    lines_count = len(all_content.split("\n"))
 

    # najliczniejszy znak
    signs_dict = {}
    for sign in all_content:
        if signs_dict.get(sign): signs_dict[sign] += 1
        else: signs_dict[sign] = 1
    # zakładam, że spacja (znak biały) nie jest znakiem, więc usówam ze słownika
    signs_dict.pop(' ')

    # sprawdzanie najliczniejszego znaku
    sign_max:str = ""
    count=0
    for entry in signs_dict:
        temp_c = signs_dict[entry]
        if temp_c>count:
            sign_max=entry
            count=temp_c


    # najliczniejsze słowo
    words_dict={}
    for word in all_content_tab:
        if words_dict.get(word): words_dict[word]+=1
        else: words_dict[word] = 1

    # sprawdzanie najliczniejszego słowa
    word_max:str = ""
    count_w=0
    for entryw in words_dict:
        temp_w = words_dict[entryw]
        if temp_w>count_w:
            word_max=entryw
            count_w=temp_w
    
    # zamykanie pliku
    f.close()

    # c
    # wyświetlanie wyniku w formacie tsv
    print("{}\t{}\t{}\t{}\t{}".format(sign_count, word_count, lines_count, sign_max, word_max))


# a
# pobiera sciezke do pliku z wejscia standardowego:
try:
    file_path = str(input())
    zad3_b()
except Exception:
    #print("AWARIA ", str(Exception.with_traceback()))
    print("#")

