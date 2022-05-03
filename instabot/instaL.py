# Get instance
import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "your_username"
password = "*******"
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followees
follow_list = []
count = 0
for follower in profile.get_followers():
    follow_list.append(follower.username)
    file = open("prada_followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    #print(follow_list[count])
    count += 1
followee_list = []
countf = 0
for followee in profile.get_followees():
    followee_list.append(followee.username)
    file = open("prada_following.txt", "a+")
    file.write(followee_list[countf])
    file.write("\n")
    file.close()
    #print(follow_list[countf])
    countf += 1
# (likewise with profile.get_followers())
print("People I don't follow back")
People_i_don_follow=list(set(follow_list)-set(followee_list))

print (People_i_don_follow)
print ("No. People I don't follow back", len(People_i_don_follow))

print("People that_don't follow me back")
People_that_don_follow_me= list(set(followee_list)-set(follow_list))


print (People_that_don_follow_me)
print ("N0. People that_don't follow me back" , len(People_that_don_follow_me))