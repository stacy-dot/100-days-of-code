print("Welcome!")

correct_name=("Taylor")
correct_password=("123")

attempts=0
max_attempts=3

while attempts<max_attempts:
    name=input("Enter your name:").strip()
    password=input("Enter your password:").strip()

    if name==correct_name and password==correct_password:
        print(f"Welcome back {name}! ")
        break
    else:
        attempts +=1
        print(f"Name/password is incorrect! You have {max_attempts-attempts} remaining.")
        
if attempts==max_attempts:
        print("Too many attempts. You are locked out!")








