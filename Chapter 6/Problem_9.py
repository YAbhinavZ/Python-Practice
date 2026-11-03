with open("Donkey.txt") as f:
    content1 = f.read()

with open("poems.txt") as f:
    content2 = f.read()

if(content1==content2):
    print("Content is identical")
else :
    print("Content is not identical")