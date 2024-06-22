class User:
    def __init__(self, name, id, address, contactno, password, email):
        self.name = name
        self.id= id
        self.address = address
        self.contactno = contactno
        self.password = password
        self.email = email

class FoodDeliverySystem:
    def __init__(self):
        self.users = {}

    def login_user(self):
        print("Enter the user details entered during registration to proceed with login")
        s=input("For login via contact number enter 1 \n for login via email enter 2:\n")
        if s=="1":
            contactno= input("Enter contact number: ")
            password = input("Enter password: ")
            user = self.users.get(contactno)
        else:
            email= input("Enter email id: ")
            password = input("Enter password: ")
            user = self.users.get(email)


        if user and user.password == password:
            print("Login successful!")
        else:
            print("Invalid id or password!")
            self.login_user()

    def register_user(self):
        print("Enter the user details to register")
        name = input("Enter name: ")
        id = input("Enter id: ")
        address = input("Enter address: ")
        contactno = input("Enter contactno: ")
        password = input("Enter password: ")
        email = input("Enter email: ")

        user = User(name, id, address, contactno, password, email)
        self.users[contactno] = user
        self.users[email] = user

        print("Registration successful proceed to login")
        self.login_user()
        
def main():
    system = FoodDeliverySystem()
    print("Welcome to the home page of the online food delivery app")
    c=input("Select 1) for new user and \n 2)for existing user: ")
    if c =="1":
        system.register_user()
    elif c == "2":
        system.login_user()
    else:
        print("Enter valid input")
        main()
        

    while True:
        print("1. Browse Restaurants and items")
        print("2. Edit details")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.register_user()
        elif choice == "2":
            system.login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
    


