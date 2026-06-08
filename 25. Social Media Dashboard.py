class SocialMediaDashboard:
    def __init__(self):
        self.posts = []

    def add_post(self, content):
        self.posts.append({
            "content": content,
            "likes": 0
        })
        print("Post added successfully!")

    def view_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        print("\n--- Posts ---")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post['content']} | Likes: {post['likes']}")

    def like_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts[index]["likes"] += 1
            print("Post liked!")
        else:
            print("Invalid post number.")

    def dashboard_stats(self):
        total_posts = len(self.posts)
        total_likes = sum(post["likes"] for post in self.posts)
        print("\n--- Dashboard Statistics ---")
        print("Total Posts:", total_posts)
        print("Total Likes:", total_likes)


dashboard = SocialMediaDashboard()

while True:
    print("\n===== Social Media Dashboard =====")
    print("1. Add Post")
    print("2. View Posts")
    print("3. Like a Post")
    print("4. View Dashboard Stats")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        content = input("Enter post content: ")
        dashboard.add_post(content)
    elif choice == "2":
        dashboard.view_posts()
    elif choice == "3":
        dashboard.view_posts()
        post_no = int(input("Enter post number to like: "))
        dashboard.like_post(post_no - 1)
    elif choice == "4":
        dashboard.dashboard_stats()
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
