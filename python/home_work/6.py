word = input("Введите слово из маленьких латинских букв: ")

glasniye = 0
soglasniye = 0

for letter in word:
    if letter in "aeioqu":
        glasniye += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        soglasniye += 1
else:
    print(False)

print("Количество гласных букв:", glasniye)
print("Количество согласных букв:", soglasniye)