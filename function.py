katata = []

def repeat():
    word = input('kata dimulai dari p = ').upper()
    for kata in word:
        if kata[:1] == 'P':
            katata.append(kata)
            repeat()
        else:
            break
        print(f'point permanianmu adalah {len(katata)}')

repeat()