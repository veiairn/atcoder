s = input()
match s:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('vowel')
    case _:
        print('consonant')