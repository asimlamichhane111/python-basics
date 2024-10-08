letter=input('Enter a letter')
match letter:
    case 'a'|'e'|'i'|'o'|'u':
        print('Vowel')
    case other:
        print('Consonant')
    
