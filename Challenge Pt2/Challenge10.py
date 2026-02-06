# Find common subscribers

news_sub = {"martin@mail.com", "carmen@mail.com", "kristen@mail.com"}
blog_sub = {"barry@mail.com", "louise@mail.com", "martin@mail.com"}

common = news_sub.intersection(blog_sub)
only_news = news_sub - blog_sub
all_subs = news_sub.union(blog_sub)

print(f"Common subscribers: {common}")
print(f"News-only subscribers: {only_news}")
print(f"All subscribers: {all_subs}")