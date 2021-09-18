#project 1: Basic School Admistration Tool

condition = True
i=1

with open("sdetails.csv", "a") as f:
    f.write("Name, age, contact, email\n")

while condition:
    

    print("\n\nEnter Details for Student "+str(i))
    name = input("Enter Name: ")
    c1 = True
    while c1:
        try:
            age = int(input("Enter Age: "))
            c1 = False
        except:
            print("Enter a valid age! Try again")

    contact = input("Enter Contact Number: ")
    email = input("Enter Mail ID: ")
    
    with open("sdetails.csv", "a") as f:
        f.write(f"{name}, {age}, {contact}, {email}\n")
    
    cc = input("Want to add more student details (Y/N): ")

    c2 = True
    while c2:
        if cc == 'y' or cc == 'Y':
            i+=1
            c2 = False
        elif cc == 'n' or cc == 'N':
            c2 = False
            condition = False
        else:
            print("Please enter a valid choice! Try Again!")

print("""All details saved in the file sdetails.csv
Thanks for Using
Made by:- Naman Sharma""")
