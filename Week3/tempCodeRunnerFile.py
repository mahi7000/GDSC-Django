while (i <= len(palin)):
    reverse_palin[j] = palin[i]
    j -= 1
    i += 1
print(palin)
print(reverse_palin)