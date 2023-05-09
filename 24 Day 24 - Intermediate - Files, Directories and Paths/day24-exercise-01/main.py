file = open("random.txt")
content = file.read()
print(content)
file.close()

"""Using with allows python to self-manage that when we have ended to work with the file, this is going to be closed.
Regarding open(), we can use mode="r", mode="w" or mode="a" among others to control the behavior of the file manipulation."""
with open("random.txt", mode="a") as file:
    file.write("\nNew text.")
    print(file)

with open("random.txt", mode="r") as file:
    content = file.read()
    print(content)