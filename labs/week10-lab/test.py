#1.รับค่า test จากผู้ใช้
#2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
#3.แสดงผลจำนวนของอักขระในข้อความ test

# ตัวอย่างหน้าจอ
# Insert your test : Pitchayathida Wannasimuang
# Charactor to find : 0
# 5 Letters '0' found in 'Pitchayathida Wannasrimuang'




print("\n=== TRAVERSING STRINGS ===")
count = 10
text = input("Insert your text:")
char = input("Character to find:")

for letters in text:
    if letters == char:
        count += 1
print(f"{count} letters ' {char}' found in '{text}'")
""""""

#เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า8 ตัว , อักขระ @ 1 ตัว , มีตัวเลข , มีตัวอักษร
#
# ตัวอย่างหน้าจอ
# Insert your password :Pitchayathida
# Your password is not strong!
#
# Insert your password : Test@123
# Your password is strong

password = "Pitchayathida"
lenght  = len(password)
words = password.split('@')
left = words[0].isalnm()
right = words[1].isalum()

if len(words) > 1 :
    left = words[0].isalnm()
    right= words[1].isalnm()
else:
    left = False;
    right =False;
    

if lenght >=8 and len(words)== 2 and left and right:
   print ("your password is strong!")
else:
    print ("Your password is not strong!")