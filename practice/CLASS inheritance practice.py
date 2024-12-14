
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilegfje}")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# 創建一個 Admin 實例，並提供名字和姓氏
admin_user = Admin('John', 'Doe')

admin_user.privileges.privileges = ['can add post', 'can delete post', 'can ban user']

admin_user.privileges.show_privileges()
