scores = []

for i in range(1, 6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)
 
print()

for i in range(len(scores)):
    if scores[i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    print(f"Student {i + 1}: {scores[i]} -> {result}")