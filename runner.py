from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser


henry = FreeUser('Henry', 24, "717-666-8888", "email@email.com", 'free')
henry.adding_posts('This is my first post')
print(henry.posts)

henry.adding_posts('This is my second post')
print(henry.posts)

henry.adding_posts('This is my third post')



