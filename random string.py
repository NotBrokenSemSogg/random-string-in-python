from os import system
from posixpath import split
import datetime
import string
import random

randString = ''.join(random.choices(string.printable.replace(string.whitespace, "_"), k=random.randint(1, 128)))
xTime = datetime.datetime.now()



try: 
    with open("output.txt", "x") as output_file:
        print(xTime, "\n--------START--------\n" + randString, "\n--------END--------\n", file=output_file)
        output_file.close()
        print(xTime, "\n--------START--------\n" + randString, "\n--------END--------\n")
except FileExistsError:
    with open("output.txt", "a") as output_file:
        print(xTime, "\n--------START--------\n" + randString, "\n--------END--------\n", file=output_file)
        output_file.close()
        print(xTime, "\n--------START--------\n" + randString, "\n--------END--------\n")