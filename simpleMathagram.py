##Simple mathagram puzzle from /r/dailyprogrammer

string = "xxx + 5x1 = 86x"
listed = list(string)

if listed[6] == "x":
    x = 100 + int(listed[7])*10 + int(listed[8])

if listed[7] == "x":
    x = int(listed[6])*100 + int(listed[8])

if listed[8] == "x":
    x = int(listed[6])*100 + int(listed[7])*10

if listed[12] == "x":
    z = 100 + int(listed[13])*10 + int(listed[14])

if listed[13] == "x":
    z = int(listed[12])*100 + int(listed[14])

if listed[14] == "x":
    z = int(listed[12])*100 + int(listed[13])*10


y = z - x
digits = 1234567890
seen = False
change = False

numbers = list(str(x)) + list(str(y))

while(1):
    for i in list(str(digits)):
        seen = False
        for n in numbers:
            if i == n:
                if seen == True:
                    change = True
                    seen = False
                else:
                    seen = True
            
    
    if change == False:
        print "%d + %d = %d" % (x, y, x+y)
        break

    if change == True:
        change = False
        x += 1
        y -= 1
        
    numbers = list(str(x)) + list(str(y))
