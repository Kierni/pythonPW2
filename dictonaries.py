phones = {"Adam Smith": "11-22-33", "Britney Spears": "44-55-66"}

phones["Bob Marley"] = "99-88-77"


#print(phones)

person = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com",
  "parents": [
    {
      "name": "Sam Doe",
      "age": 60,
      "city": "New York",
      "email": "sam.doe@gmail.com",
    },
    {
      "name": "Barbara Doe",
      "age": 55,
      "city": "New York",
      "email": "basia.doe@gmail.com",
    }
  ]
}

for parent in person["parents"]:
    print(parent["name"], parent["age"])


person = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com",

}
print(person.items())

dictionary_test = {}
while True:
    command = input("Peek an option: new_contact, show_contact")
    if command =="new_contact":
        name = input("Wprowadź imię i nazwisko: ")
        phone = input("Wprowadź numer teleofnu: ")
        dictionary_test[name] = phone
    elif command == "show_contatcts":
        print(dictionary_test)
    #else:
     #   print("unknown command")
    command = input("Do you want to continue Y/N? ")
    if command == "N":
        break
    else:
        continue





