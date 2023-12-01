palin = input("Please enter a word to check: ").lower()
reverse_palin = palin[::-1]

if (reverse_palin == palin):
    print("The word {} is a palindrome".format(palin))
else:
    print("The word {} is not a palindrome,\nbecause {} is not equal to {}".format(palin, reverse_palin, palin))