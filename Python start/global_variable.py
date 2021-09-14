isValid = True
count = 0

def validChanger():
    global isValid
    isValid = False
    print(isValid)

validChanger()
print(isValid)

def function():
    global count
    count += 1

for i in range(0,10):
    function()