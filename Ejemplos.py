import os
f = open("demofile3.txt","w")
f.write(" Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
f.close()

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

os.rmdir("Taller #6")