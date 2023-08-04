from Core import *

print("Welcome To The Library Online Portal! 📖")
while True:
    print("1. [Login] (Access your account)")
    print("2. [Quit] (Exit the Online Library)")
    space()
    choice = int(input())
    if choice == 1:
        space()
        print("[Login]            ")
        username = input("Enter your account's username: \t")
        password = input("Enter the password:\t")
        a = Admin(username, password)
        if a.login1() != 1:
            space()
            print("The Username/Password you entered is incorrect or does not exist. ")
            space()
            break

        else:
            space()
            a.login1()
            print("You have logged in successfully. Welcome admin🖥️!")
            space()
        while True:
            print("1. [Issued/Issue Books] (Track and manage Issued books)")
            print("2. [Book List] (Manage available books)")
            print("3. [Users] (Manage all user and administrator accounts)")
            print("4. [Logout] (Log out of your account)")
            space()
            choice = int(input())
            if choice == 1:
                while True:
                    space()
                    print("1. [View Issued Books] (View all books currently Issued)")
                    print("2. [View Overdue Books] (View all overdue books)")
                    print("3. [Return Book] (Return an Issued Book)")
                    print("4. [Issue Book] (Issue a Book)")
                    print("5. [Back] (Go back to the menu)")
                    space()

                    choice = int(input())
                    if choice == 1:
                        space()
                        a.issuedbooks1()
                        space()
                    elif choice == 2:
                        space()
                        a.overduebooks()
                        space()
                    elif choice == 3:
                        while True:
                            username = input("Enter the username of the Issue: ")
                            name = input("Enter the name of the book to be returned: ")
                            if a.returnb(username, name) == 1:
                                a.returnb(username, name)
                                space()
                                print("Book Returned")
                                space()
                                break
                            else:
                                space()
                                print("Invalid Credentials")
                                space()
                                break

                    elif choice == 4:
                        while True:
                            username = input("Enter the username of the Issue: ")
                            name = input("Enter the name of the book to be Issued: ")
                            f = 0
                            for i in user:
                                if username in i:
                                    a.issue(username, name)
                                    space()
                                    f = 1
                                    print("Book Issued")
                                    space()
                                    break

                            if f == 1:
                                break
                            else:
                                print("The user with the given username doesn't exist")
                    elif choice == 5:
                        space()
                        break
                    else:
                        print("Invalid Option! Choose one from the list below")
                        space()
            elif choice == 2:
                while True:
                    space()
                    print("1. [View Books] (View all Books in the Library)")
                    print("2. [Add Book] (Add a book to the Library)")
                    print("3. [Remove Book] (Remove a book from the Library)")
                    print("4. [Back] (Go back to the menu)")
                    space()
                    choice = int(input())
                    space()
                    if choice == 1:
                        space()
                        a.avlb()
                        space()
                    elif choice == 2:
                        ISBN = input("Enter the ISBN of the Book: ")
                        Name = input("Enter the Name of the Book: ")
                        Pages = int(input("Enter the Number of Pages in the Book: "))
                        a.add(Name, ISBN, Pages)
                        space()
                        print("Book added succesfully.")
                        space()
                    elif choice == 3:
                        bid = input("Enter the Book Id")
                        if a.removeb(bid) != 1:
                            space()
                            print("Book with given BookID not found")
                            space()
                        else:
                            space()
                            a.removeb(bid)
                            print("Book removed succesfully")
                            space()
                    elif choice == 4:
                        space()
                        break
                    else:
                        print("Invalid Option! Choose one from the list below")
                        space()
            elif choice == 3:
                while True:
                    space()
                    print("1. [View Users] (View User accounts)")
                    print("2. [View Administrators] (View Administrator accounts)")
                    print("3. [Add Administrators] (Add an Administrator account)")
                    print("4. [Remove Administrators] (Remove an Administrator account)")
                    print("5. [Remove Users] (Remove a User account)")
                    print("6. [Back] (Go back to the menu)")
                    space()
                    choice = int(input())
                    space()
                    if choice == 1:
                        space()
                        a.viewuser()
                        space()
                    elif choice == 2:
                        space()
                        a.viewadmin()
                        space()
                    elif choice == 3:
                        Username = input("Set the desired Username of the account: ")
                        Password = input("Set the desired Password of the account: ")
                        a.addadmin(Username, Password)
                        space()
                        print("admin added successfully")
                        space()
                    elif choice == 4:
                        Username = input("Enter the Username of the account to be deleted: ")
                        if a.removeadmin(Username) != 1:
                            space()
                            print("Admin with entered username does not exist")
                            space()
                        else:
                            space()
                            a.removeadmin(Username)
                            print("Admin removed successfully")
                            space()
                    elif choice == 5:
                        Username = input("Enter the Username of the account to be deleted: ")
                        if a.removeuser(Username) != 1:
                            space()
                            print("User with entered username does not exist")
                            space()
                        else:
                            space()
                            a.removeuser(Username)
                            print("User removed successfully")
                            space()
                    elif choice == 6:
                        space()
                        break
                        space()
                    else:
                        space()
                        print("Invalid Option! Choose one from the list below")
                        space()
            elif choice == 4:
                space()
                print("Logging out.")
                space()
                break


            else:
                space()
                print("Invalid Option! Choose one from the list below")
                space()
    elif choice == 2:
        space()
        print("Exiting the software.")
        space()
        break

    else:
        space()
        print("Invalid Option! Choose one from the list below")
        space()
