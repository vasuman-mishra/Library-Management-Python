from datetime import *


def space():
    print("", end="\n")


admin = [["shikamarunara", '123']]
issuedbooks = [["Sumesh Kumar", "Harry Potter", date(2023, 7, 10)], ['Vasuman Mishra', 'Python', date(2023, 6, 5)]]
availablebooks = [["Harry Potter2", '7125910', '374'], ['Python', '125415', '1203']]
user = [["Sumesh Kumar", "123"], ["Vasuman Mishra", '2921']]


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login1(self):
        for i in admin:
            if i == [self.username, self.password]:
                return 1
            else:
                return 0

    @staticmethod
    def issuedbooks1():
        for i in issuedbooks:
            print(i)

    def overduebooks(self):
        for i in issuedbooks:
            if (i[2] + timedelta(days=7)) < date.today():
                print(i)
                a = date.today() - i[2] + timedelta(days=7)
                b = (a.total_seconds() / (24 * 60 * 60))
                print(f"Penalty:{b * 15} Rupees")

    def returnb(self, username, bookname, ):
        for i in issuedbooks:
            if i[0] == username and i[1] == bookname:
                issuedbooks.remove(i)
                return 1

    def issue(self, username, name):
        issuedbooks.append([username, name, date.today()])

    def avlb(self):
        for i in availablebooks:
            for j in issuedbooks:
                if i[1] == j[0]:
                    availablebooks.remove(i)
                    break
        for i in availablebooks:
            print(i)

    def add(self, name, bookid, pages):
        availablebooks.append([name, bookid, pages])

    def removeb(self, name):
        for i in availablebooks:
            if i[1] == name:
                availablebooks.remove(i)
                return 1

    def adduser(self, name, password):
        user.append([name, password])

    def viewuser(self):
        for i in user:
            print(i)

    def viewadmin(self):
        for i in admin:
            print(i)

    def addadmin(self, username, password):
        admin.append([username, password])

    def removeuser(self, name):
        for i in user:
            if i[0] == name:
                user.remove(i)
                return 1

    def removeadmin(self, name):
        for i in admin:
            if i[0] == name:
                admin.remove(i)
                return 1


class User(Admin):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.username = username
        self.password = password

    def login1(self):
        for i in user:
            if i == [self.username, self.password]:
                return 1

    def register(self):
        user.append([self.username, self.password])

    def issuedbooksi(self):
        for i in issuedbooks:
            if i[0] == self.username:
                print(i[1:])
                if (i[2] + timedelta(days=7)) < date.today():
                    print(f"The Book is overdue for:{date.today()-i[2] + timedelta(days=7)}")
                    a = date.today() - i[2] + timedelta(days=7)
                    b = (a.total_seconds() / (24 * 60 * 60))
                    print(f"Penalty:{b * 15} Rupees")
                else:
                    print(f"The Book is due in:{i[2] + timedelta(days=7)-date.today()}")

    def change_password(self, password):
        for i in user:
            if i[0] == self.username:
                i[1] = password

    def change_username(self, username):
        for i in user:
            if i[0] == self.username:
                i[0] = username

    def removeuser1(self):
        for i in user:
            if i[0] == self.username:
                user.remove(i)
                return 1
