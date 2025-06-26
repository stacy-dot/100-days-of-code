gradebook={}

def add_student():
    name=input("Enter name of student: ")
    subjects={}

    while True:
        subject= input("Enter subject(or type done to exit): ")
        if subject.lower() in ["done"]:
            break
        try:
            grade=float(input(f"Enter grade for {subject}: "))
            subjects[subject]=grade
        except ValueError:
            print("Invalid grade. Try again!")

    gradebook[name]=subjects
    print(f"{name} added successfully!\n")

def view_report():
    for student, data in gradebook.items():
        print(f"\nReport for {student}")
        total=sum(data.values())
        count=len(data)
        average= total/count if count>0 else 0
        print("Subjects & grades: ", data)
        print(f"Average: {average:.2f}")

while True:
    print("\n---Student Gradebook---")
    choice=input("1.Add student" "2.View Report" "3.Exit\nChoose: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_report()
    elif choice=="3" or choice.lower() in ["done"]:
        break
    else:
        print("invalid choice!")
