from atproto import Client

client = Client()
client.login(
    "Username.bsky.social",
    "PassWord"
)

#Subject intended to be searched

Search = input("What do you wish to search?")

Result = client.app.bsky.feed.search_posts(
    params={
        "q":Search,
        "limit" : 10
    }
) 

print(f"\n Posts that were found about: {Search} \n")

for post in Result.posts:
    print(post.record.text)
    print()




