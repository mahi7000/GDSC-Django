patt = input('Please enter the pattern to be printed: ')


if (patt == 'a' or patt == 'o' or
    patt == 'e' or patt == 'u' or
    patt == 'i'):
        print("Vowels are not allowed in the input")
elif (len(patt) > 1):
    print("The length of the character should be 1")
else:
    i = 1
    while (i <= 10):
        j = 1
        while (j <= i):
            print(patt, end='')
            j += 1
        print()
        i += 2
            
    