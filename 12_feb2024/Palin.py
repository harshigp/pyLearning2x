#check if a string is palindrome
st = str(input("enter the string\n"))
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO, its not a Palindrome")
else:
    print("Yes, its a Palindrome")


