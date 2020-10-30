# 1.1 Changelog
# Added new method to Users to print the array of users
# Repurposed GetUsers method on the Users class to return the users array
# Refactored some repr and str methods to work better with the above changes


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __repr__(self):
        return "User(name=%s, age=%s)" % (self.name, self.age)

# Inherit from User


class Admin(User):
    def details(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) + "\n"

    # __str__ will return this line when calling the class. eg: print(user1)
    def __str__(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) + "\n"

    def __repr__(self):
        return "Admin(name=%s, age=%s)" % (self.name, self.age)


class Users:
    def __init__(self):
        self.users = []

    def AddUser(self, user):
        # Check for the type of the object to determine admin status
        if user is type(Admin):
            user = Admin(user.name, user.age)
        elif user is type(User):
            user = User(user.name, user.age)
        self.users.append(user)

    # Returns the array contents
    def GetUsers(self):
        return self.users

    # Prints the contents of the users array
    def PrintUsers(self):
        print("There are {0} users\n".format(str(len(self.users))))
        for user in self.users:
            print('User Details: ')
            print(user.details())

    def __str__(self):
        return "There are {0} users, use PrintUsers to show them" \
            .format(str(len(self.users)))

    def __repr__(self):
        return "Users()"


users = Users()
numberOfUsers = int(input("How many users do you want to add?: "))
userCount = 1

while userCount <= numberOfUsers:
    name = input("What is the name of user " + str(userCount) + "?: ")
    age = input("What is the age of user " + str(userCount) + "?: ")
    # Create a new user with the accepted information
    currentUser = User(name, age)
    print('Adding User: ')
    print(currentUser)
    # Add new user to the list
    users.AddUser(currentUser)
    userCount += 1

# Create an admin user and add to the list
admin = Admin("Chris", 30)
users.AddUser(admin)

# List the current users
users.PrintUsers()

print(f'Result of calling users.GetUsers(): {users.GetUsers()}')
