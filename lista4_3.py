def zad3_b():
    # b
    f = open(file_path, "r")
    all_content = f.read()

    # liczba znaków
    sign_count = len(all_content)

    #liczba słów
    all_content_tab = all_content.split()
    word_count = len(all_content_tab)

    #liczba wierszy
    lines_count = len(all_content.split("\n"))

    # najliczniejszy znak
    signs_dict = {}
    for sign in all_content:
        if signs_dict.get(sign): signs_dict[sign] += 1
        else: signs_dict[sign] = 1

    sign:str = ""
    count=0
    for entry in signs_dict:
        temp_c = signs_dict[entry]
        if temp_c>count:
            sign=entry
            count=temp_c

    print("' "+sign+" '", count)


# a
# pobiera sciezke do pliku z wejscia standardowego:
try:
    file_path = str(input())
    zad3_b()
except Exception:
    pass
