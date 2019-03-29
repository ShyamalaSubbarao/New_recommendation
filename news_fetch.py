import requests
import datetime

def NewsFromBBC(search_criterion,prev):
	date = str(datetime.datetime.now().date())
	if search_criterion == "daily news" :
		main_url = "https://newsapi.org/v2/top-headlines?sources=google-news&from="+date+"&apiKey=87823d631cc14e4d9c4b7a79d2850dd3"
	else :
		main_url = "https://newsapi.org/v2/everything?q="+search_criterion+"&from="+date+"&sortBy=publishedAt&apiKey=87823d631cc14e4d9c4b7a79d2850dd3"
		print(main_url)
	# fetching data in json format
	open_bbc_page = requests.get(main_url).json()
	print(search_criterion,open_bbc_page["status"])
	# getting all articles in a string article
	article = open_bbc_page["articles"]

	return_arr = []

	for ar in article :
		date_time_str = ar["publishedAt"]
		try :
			date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S+00:00')
		except :
			date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%SZ')
		date_time_obj+=datetime.timedelta(minutes=330)
		if search_criterion != "daily news" :
			if ar.has_key("title") and ar.has_key("description") and ar.has_key("content") and ar.has_key("publishedAt") :
				return_arr.append({"title":ar['title'],"description":ar['description'],"content":ar['content'],"publishedAt":ar['publishedAt'],"click_count":0,"category":search_criterion})
		else :
			if ar.has_key("title") and ar.has_key("description") and ar.has_key("content") and ar.has_key("publishedAt") :
				if date_time_obj > prev :
					return_arr.append({"title":ar['title'],"description":ar['description'],"content":ar['content'],"publishedAt":ar['publishedAt'],"click_count":0})
					#print(ar["publishedAt"],ar["content"],True)
	return return_arr

if __name__ == '__main__':
	# function call
	prev = datetime.datetime.now() - datetime.timedelta(minutes=1000000000)
	NewsFromBBC("daily news",prev)