from pymongo import MongoClient
import datetime
import news_fetch

client = MongoClient()
db = client['news_recommendation']

user_log = db['user_auth_log']
news_db = db['news_db']
news_log = db['news_log']

#user authentication creation
'''username = []
for i in range(2,41):
	name = "15PD"
	if i < 10 :
		name += "0"+str(i)
	else :
		name += str(i)
	username.append(name)

	user_log.insert_one({"username" : name, "password" : "15pd", "last_login_time" : datetime.datetime.now(), "count" : 0})
print(username)'''

# initial news log feed
'''categories = ["Sports","Politics","Business","Education","Entertainment","Military","Real estate","Technology","Crime","Weather"]

for category in categories :
	news_arr = news_fetch.NewsFromBBC(category,datetime.datetime.now().date())
	news_db.insert_many(news_arr)

news_log.insert_one({"last_news_insertion_time":str(datetime.datetime.now())})'''