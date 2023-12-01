num = 2
count_three = 0
count_five = 0
count_fifteen = 0

while (num <= 50):
    if (num % 15 == 0):
        print("ThreeFive")
        count_fifteen += 1
        count_three += 1
        count_five += 1
    elif (num % 3 == 0):
        print("Three")
        count_three += 1
    elif (num % 5 == 0):
        print("Five")
        count_five += 1
    else:
        print(num)
    num += 2

print("There are {} numbers replaced by three".format(count_three))
print("There are {} numbers replaced by five".format(count_five))
print("There are {} numbers replaced by both three and five".format(count_fifteen))
print("There are {} numbers replaced by words".format(count_three + count_five - count_fifteen))