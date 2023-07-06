import json2 as json

print("Welcome to the who doesn't follow you back on ig code")
print("please request and download your data on the instagram website in json format")
print("and move the files called followers.json and following.json to the same")
print("directory as this .py file")
print("(if the files arent called exactly that, change the name please)")

#reads and stores json files in a dictionary format
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)
    
following_list = []

#makes a list of the usernames in the following.json file
for following in range(len(following_json["relationships_following"])):
    following_list.append(following_json["relationships_following"][following]["string_list_data"][0]["value"])
                          
#removes the follwers idk
for follower in range(len(followers_json)):
    if followers_json[follower]["string_list_data"][0]["value"] in following_list:
        following_list.remove(followers_json[follower]["string_list_data"][0]["value"])
        
number = 0
unfollowed = 0

for user in following_list:
    number += 1
print("--------------------------------")
print(f"you are not followed back by {number} accounts")
print("click enter to indicate an unfollow and any other key to indicate you won't unfollow")
 
for user in following_list: #following but not following back
    print(f"{following_list.index(user)+1}. {user}")
    unfollow = input(str())
    
    if unfollow == "":
        unfollowed += 1
        
print(f"you have unfollowed {unfollowed} accounts, now {len(following_list)-unfollowed} accoutns dont follow you back")

    
    
    