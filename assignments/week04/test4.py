#รับชื่อจริง (หรือข้อความ) จากผู้ใช้
#นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a,e,i,o,u)

#ตัวอย่างหน้าจอ
#What is you name?:Techin
#Your text have 4 vowels.

name = input("What is your name?: ")
letters = list("Techin")
print(letters)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

# Addy


count = 0
for letter in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    elif letter == 'e' or letter == 'E':
        count = count + 1
    elif letter == 'i' or letter == 'I':
        count = count + 1
    elif letter == 'O' or letter == 'O':
        count = count + 1
    elif letter == 'U' or letter == 'U':
        count = count + 1

count = 0
for letter in name:
    if letter in ['a' + 'e' + 'i' + 'o' + 'u' + 'A' + 'E' + 'I' + 'O' + 'U'] :
     count = count + 1 

    #print(f"ตัวอักษร: {letter}")

#print("You text have", count,"vowels")
