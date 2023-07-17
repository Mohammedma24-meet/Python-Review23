def create_youtube_video(title, description):
	return {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}


def like(new_video):
	if "likes" in new_video:
		new_video["likes"] += 1
	
def dislik(new_video):
	if "dislikes"in new_video:
		new_video ["dislikes"] += 1


def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo
				
Dict_1=create_youtube_video("gg","naus ween")


for x in range(495):
   like(Dict_1)

print(Dict_1)