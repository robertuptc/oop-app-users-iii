class Users:
    posts = {}
    def __init__(self, name, age, phone, email, user_type):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.user_type = user_type
        self.count = 1
    
    def adding_posts(self, post):
        if self.count == 1:
            Users.posts[self.name] = {self.count : post}
            self.count += 1
        else: 
            Users.posts[self.name][self.count] = post
            self.count += 1
    
    def deleting_post(self, name, number):
        del Users.posts[name][number]