
"""Add Names and Ages to a List of Users that can be returned on demand."""

class User:
    """Initialise new User with a Name and Age, can return details of the user."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        """Return the user's details."""
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __repr__(self):
        return "User(name=%s, age=%s)" % (self.name, self.age)

# Inherit from User


class Admin(User):
    """Initialise new Admin using an existing User object, can return details of the admin."""
    def details(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) + "\n"

    # __str__ will return this line when calling the class. eg: print(user1)
    def __str__(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) + "\n"

    def __repr__(self):
        return "Admin(name=%s, age=%s)" % (self.name, self.age)


class Users:
    """An object to hold the list of users, can add new user,
    print current list and return as array.
    """
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Check for the type of the object to determine admin status and then add accordingly."""
        if user is type(Admin):
            user = Admin(user.name, user.age)
        elif user is type(User):
            user = User(user.name, user.age)
        self.users.append(user)

    # Returns the array contents
    def get_users(self):
        """Return the array of the current users."""
        return self.users

    # Prints the contents of the users array
    def print_users(self):
        """Prints the current array of users to the screen in a user-readable format."""
        print("There are {0} users\n".format(str(len(self.users))))
        for user in self.users:
            print('User Details: ')
            print(user.details())

    def __str__(self):
        return "There are {0} users, use print_users to show them" \
            .format(str(len(self.users)))

    def __repr__(self):
        return "Users()"


users = Users()
numberOfUsers = int(input("How many users do you want to add?: "))
# Disabled the pylint naming convention for constant, due to false positive
# userCount object is not a constant, rather a counter that increases
userCount = 1 #pylint: disable=c0103

while userCount <= numberOfUsers:
    userName = input("What is the name of user " + str(userCount) + "?: ")
    userAge = input("What is the age of user " + str(userCount) + "?: ")
    # Create a new user with the accepted information
    currentUser = User(userName, userAge)
    print('Adding User: ')
    print(currentUser)
    # Add new user to the list
    users.add_user(currentUser)
    userCount += 1

# Create an admin user and add to the list
admin = Admin("Chris", 30)
users.add_user(admin)

# List the current users
users.print_users()

print(f'Result of calling users.get_users(): {users.get_users()}')
