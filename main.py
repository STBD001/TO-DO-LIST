def menu():
    print("\nTo-Do List")
    print("1. Add task")
    print("2. Show task")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Writing to a file")
    print("6. Load into file")
    print("7. Exit")

def Add_task(zadania):
    task=input("write the content of the task")
    zadania.append(task)
    print("zadanie zostało dodane")

def Show_task(zadania):
    if not zadania:
        print("Error")
    else:
        print("\Your To-do List")
        for idx, zadanie in enumerate(zadania, start=1):
            print(f"{idx}. {zadanie}")

def Delete_task(zadania):
    Show_task(zadania)
    try:
        numer=int(input("Enter the job number to delete: "))
        if 1 <= numer <= len(zadania):
            usuniete_zadanie=zadania.pop(numer-1)
            print(f"Task {usuniete_zadanie} delete.")
        else:
            print("Error")
    except ValueError:
        print("Wrong number!")

def Edit_task(zadania):
    Show_task(zadania)
    try:
        numbers=int(input("Enter the job number to edit: "))
        if 1<=numbers <= len(zadania):
            nowa_tresc=input("Enter new task content")
            zadania[numbers-1]=nowa_tresc
            print(f"Task number {numbers} has been updated")
        else:
            print("Error")
    except ValueError:
        print("Wrong number!")

def Save_fill(zadania, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        for zadanie in zadania:
            plik.write(zadanie + "\n")
    print(f"The tasks have been saved to a file {nazwa_pliku} .")

def Load_fill(zadania, nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            zadania.clear()
            for linia in plik:
                zadania.appemd(linia.strip())
        print(f"The tasks were loaded from the file '{nazwa_pliku}'.")
    except FileExistsError:
        print(f"Fill {nazwa_pliku} not exist")


def main():
    zadania=[]
    nazwa_pliku="zadania.txt"

    while True:
        menu()
        wybor=input("Select options (1-7)")

        if wybor=='1':
            Add_task(zadania)
        elif wybor=='2':
            Show_task(zadania)
        elif wybor=='3':
            Delete_task(zadania)
        elif wybor=='4':
            Edit_task(zadania)
        elif wybor=='5':
            Save_fill(zadania, nazwa_pliku)
        elif wybor=="6":
            Load_fill(zadania, nazwa_pliku)
        elif wybor=='7':
            print("Exiting...")
            break
        else:
            print("Error")
if __name__=="__main__":
    main()