#1. รับค่า text จากผู้ใช้ 
#2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
#3. แสดงผลจ่านวณของอักขระในข้อความ 
# ตัวอย่างหน้าจอ 
# Insert your text: Issara Thong-in
# Character to find: o 
# 5 letters 'o' found in 'Issara Thong-in'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text : ")
char = input("Character to find : ")

for letter in text:
    if letter == char: 
        count += 1
print(f"{count} letter {char} found in '{text}'")


# เขียนโปรแกรมตรวจสอบความแข็งแรง PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว,มีตัวเลข, มีตัวอักษร
#
#ตัวอย่างหน้าจอ
#Insert your password: Boonchoo
# Your password is strong!
#
# Insert your passwor : Test@123
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')


if len(words) > 1: 
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;


if lenght >= 8 and len(word) == 2 and left and right:
    print("Your password is strong!")
else:
    print("Your password is not strong!")