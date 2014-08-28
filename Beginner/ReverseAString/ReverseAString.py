string = input("Word that you want reversed ? :")

print(string[0])
i = 0
j = len(string)-1
reverse = ""
while i <= j:
    reverse = str(reverse) + string[j]
    j = j -1
print (reverse)
