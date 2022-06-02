from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser


# free_user = FreeUser("Bob",23,"7615555","sumthin@gmail.com")
# print(free_user.adding_posts("post 1"))
# print(free_user.adding_posts("post 2"))
# print(free_user.adding_posts("post 3"))
# print(free_user.adding_posts("post 4"))
# print(free_user.posts)

free_user = PremiumUser("Bob",23,"7615555","sumthin@gmail.com")
print(free_user.adding_posts("post 1"))
print(free_user.adding_posts("post 2"))
print(free_user.adding_posts("post 3"))
print(free_user.adding_posts("post 4"))
print(free_user.posts)



