# Write your solution here
#command= int(input("command (1 search, 2 add, 3 quit): "))
def search(phonebook):
    name=input("name: ")
    if name in phonebook:
         print(phonebook[name])
    else:
         print("no number")
    return
def add(phonebook):
        name= input("name: ")
        names=[]
        names.append(name)
        number= input("number: ")
        numbers=[]
        numbers.append(number)
        phonebook[name]= number
        print("ok!")
        return names, numbers

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(phonebook)
        if command == 2:
            add(phonebook)
        if command == 3:
            break
    print("quitting...")

main()