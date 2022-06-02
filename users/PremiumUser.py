from users.User import Users
class PremiumUser(Users):
    def __init__(self, name, age, phone, email):
        parent_instance = super()
        parent_instance.__init__(name, age, phone, email)