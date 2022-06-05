from users.User import Users

class FreeUser(Users):
    def adding_posts(self, post):
        if self.count == 1:
            Users.posts[self.name] = {self.count : post}
            self.count += 1
        elif self.count > 2:
            print("You have reached your post limit, please upgrade to a premium account to add more posts")
        else: 
            Users.posts[self.name][self.count] = post
            self.count += 1