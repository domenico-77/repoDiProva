import os

if os.path.exists("timer.txt"):
    with open("timer.txt", "r") as file:
        conteggio = int(file.read())
else:
    conteggio = 1


if conteggio % 2 == 1:
    print("END")
else:
    import time
    time.sleep(4 * 60 * 60)
    print("END")


conteggio += 1


with open("timer.txt", "w") as file:
    file.write(str(conteggio))
