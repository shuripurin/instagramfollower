import json

# Load followers
with open('followers_1.json', 'r', encoding='utf-8') as f:
    followers_data = json.load(f)

# Load following
with open('following.json', 'r', encoding='utf-8') as f:
    following_data = json.load(f)

# Extract follower usernames
followers = set()
for item in followers_data:
    if 'string_list_data' in item:
        followers.add(item['string_list_data'][0]['value'])

# Extract following usernames
following = set()
for item in following_data['relationships_following']:
    following.add(item['title'])

# Find who doesn't follow back
not_following_back = following - followers

# Find who you don't follow back
not_followed_back = followers - following

print(f"\n RESULTS:")
print(f"You follow: {len(following)} people")
print(f"Your followers: {len(followers)} people")
print(f"\n People you follow who DON'T follow you back ({len(not_following_back)}):")
for username in sorted(not_following_back):
    print(f"   @{username}")

print(f"\n✅ People who follow you that you DON'T follow back ({len(not_followed_back)}):")
for username in sorted(not_followed_back):
    print(f"   @{username}")

# Save to file
with open('not_following_back.txt', 'w') as f:
    f.write(f"People you follow who DON'T follow you back ({len(not_following_back)}):\n\n")
    for username in sorted(not_following_back):
        f.write(f"@{username}\n")

print(f"\n✅ Saved to 'not_following_back.txt'")