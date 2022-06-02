class Users:
    posts = {}
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.count = 0
    
    def adding_posts(self, post):
        if self.count == 0:
            Users.posts[self.name] = {self.count : post}
            self.count += 1
        else: 
            Users.posts[self.name][self.count] = post
            self.count += 1
    
    def deleting_post(self, name, number):
        del Users.posts[name][number]



# john = Users("John", 22, "777-000-2222", "john@email.com")


# john.adding_posts('my log number one')
# print(john.count)
# print(Users.posts)
# john.adding_posts('my log number two')
# print(john.count)
# print(Users.posts)
# print(john.deleting_post('John', 0))
# print(Users.posts)



