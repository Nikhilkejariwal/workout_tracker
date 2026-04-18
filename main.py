def menu(): 
    print("Having trouble keeping track of gym progress?")
    print("Well lucky for you I have created a gym tracker!")
    print("You can keep track of workouts and progress ETC.")
    print("************************************************\n")
    print("Please select an option of what you want to do below:")
    choice = int(input("Press 1 to add workout\n2 to view workout\n3 to add an exercise to an already created workout\n4 to add a set to an exercise\n5 to delete an exercise "))

    if(choice == 1):
        add_workout()
    elif choice == 2:
        view_workout()
    elif choice == 3:
        add_exercise()    
    elif choice == 4:
        add_set()
    elif choice == 5:
        j = input("What exercise do you want to delete:")
        del_exercise(j)
    
def add_workout():
    date = input("Enter date: ")

    exercise = input("Enter exercise: ")
    set_num = int(input("Enter num of sets: "))
    file = open("workouts.txt", "a")
    file.write(f"Date:{date}\nExercise : {exercise} | {set_num} Sets\n")
    file.close()
    choice = int(input("Do you want to add a set? 1 = Yes,2 = No: "))
    if choice == 1:
        add_set()
    else:
        view_workout()
def view_workout():
    file = open("workouts.txt", "r")
    data = file.readlines()    
    for d in data:
        print(d)
def del_exercise(choice):
    file = open("workouts.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    skip = False

    for line in lines:
        if line.lower().startswith("exercise"):
            if line.lower().startswith(f"exercise : {choice.lower()}"):
                skip = True
                continue
            else:
                skip = False
        if skip:
            continue

        new_lines.append(line)

    file = open("workouts.txt", "w")
    file.writelines(new_lines)
    file.close()
    j = input("Is there any other exercise you want to delete?: 1 = Yes, 2 = No")
    if j == 1:
        exer = input("What exercise?:")
        del_exercise(exer)
    else:
        view_workout()
def del_set():
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if user_input.lower() not in line.lower():
                file.write(line)

def add_exercise():
    exercise = input("Enter exercise:")
    set_num = int(input("Enter num of sets: "))
    file = open("workouts.txt", "a")
    file.write(f"Exercise : {exercise} | {set_num} sets\n")
    file.close()
    choice = input("Do you want to add any sets to your exercise right now? 1=yes, 2=No: ")
    if choice == 1:
        add_set()
    else:
        view_workout()
def add_set():
    sets = input("Set number: ")
    reps = input("Enter reps: ")
    weight = input("Enter weight: ")
    file = open("workouts.txt", "a")
    file.write(f"set #{sets} | {reps} rep(s) | {weight}lbs\n")
    file.close()
    choice = int(input("Do you want to add another set?: 1=Yes, 2=No: "))
    if choice == 1:
        add_set()
    else:
        view_workout()
if __name__ == "__main__":
    menu()




