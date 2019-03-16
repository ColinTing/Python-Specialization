largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done": 
        break
    try:
        fval = int(sval)
    except:
        print("Invalid input")
        continue
    
    if largest is None:
        largest = fval
    elif largest<fval:
        largest = fval
    
    if smallest is None:
        smallest = fval
    elif smallest>fval:
        smallest = fval
        

print("Maximum is", largest)
print("Minimum is", smallest)