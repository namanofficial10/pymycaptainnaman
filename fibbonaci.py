a = int(input("Enter the number of terms: "))

fterm = 0
term = 1

for i in range(a):
    print(fterm)
    temp = term
    term = fterm + term 
    fterm = temp
    
    
