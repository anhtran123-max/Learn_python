tre, dep, ny, giau = [True if i == "1" else False for i in input().split() ]
 
if tre and not dep:
    print(0)
    exit()
if not any([tre, dep, ny ,giau]):
    print(1)
    exit()
 
if (tre and dep and ny):
    print(1)
elif not dep and ny and giau:
    print(1)
else:
    print(0)