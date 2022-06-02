from users.User import Users

class FreeUser(Users):

    def adding_posts(self, post):
        parent_instance = super()
        if self.count < 2:
            parent_instance.adding_posts(post)
        else: 
            return "You have reached your post limit"