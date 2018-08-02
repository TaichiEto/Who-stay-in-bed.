import sys
import time
name = input("誰が眠っていますか？: ")

first = 1
for i in range(1,5):
    if first == 1:
        sys.stdout.write("{} > ".format(name))
        first = 0
    sys.stdout.write("z")
    sys.stdout.flush()
    time.sleep(0.3)
print ("\n")
time.sleep(2)
print ("{}は眠っているようだ。".format(name))
time.sleep(1)
for char in "良い夢見ろよ":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.5)
    if char == "よ":
        print ("")
time.sleep(5)
