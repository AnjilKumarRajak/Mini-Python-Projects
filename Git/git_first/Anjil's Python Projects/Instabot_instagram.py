from instabot import Bot
bot=Bot()
bot.login(username="",password="")
bot.follow("")
bot.unfollow("")
bot.upload_photo("path", caption="any_message")
bot.send_message("i love coding ", ["username","username"])

#get info of yours followers
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))


# get info you are following.
following =bot.get_user_following("username")
for Following in following:
    print(bot.get_user_following("following"))    
