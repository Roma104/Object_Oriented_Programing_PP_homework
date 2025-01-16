class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"User name: {self.username}")
        for i, p in enumerate(self.posts):
            print(f"{i}: {p}")


def main():
    johndoe = SocialMediaProfile(username='johndoe')

    add_posts = ["Hello, world!",
                 "Had a great day at the park!",
                 "What's up, Natalie? How are you?"]
    for post in add_posts:
        johndoe.add_post(post)

    print()
    johndoe.display_timeline()


if __name__ == '__main__':
    main()