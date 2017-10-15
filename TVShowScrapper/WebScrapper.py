#######################################

# Author: Yash Kumar Singh
# Title : TV Show Scrapper

#######################################


import urllib.request as urllib2
import pandas as pd
from bs4 import BeautifulSoup

channel_list = ["HBO", "MOVIES NOW", "MNX", "STAR MOVIES", "WB", "ZEE STUDIO", "COMEDY CENTRAL", "COLORS INFINITY", "ZEE CAFE", "ZEE CINEMA", "SONY MAX", "STAR GOLD"]
links_list = ["http://tv.burrp.com/channel/hbo/8/", "http://tv.burrp.com/channel/movies-now/207/", "http://tv.burrp.com/channel/mnx/746/", "http://tv.burrp.com/channel/star-movies/59/", 
"http://tv.burrp.com/channel/wb/99/", "http://tv.burrp.com/channel/zee-studio/63/", "http://tv.burrp.com/channel/comedy-central/267/", "http://tv.burrp.com/channel/colors-infinity/655/", 
"http://tv.burrp.com/channel/zee-cafe/65/", "http://tv.burrp.com/channel/zee-cinema/4/", "http://tv.burrp.com/channel/sony-max/51/", "http://tv.burrp.com/channel/star-gold/64/"]

file = open('C:/Users/Yash_Kumar_Singh/Documents/Projects/Python/TVShowScrapper/ShowListings.txt', 'w')

for link in links_list:
	T = []
	S = []
	df = pd.DataFrame()
	wiki = link
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page, "html.parser")
	listing = soup.find('table', class_='result')

	for row in listing.findAll("tr"):
		data_list = [text for text in row.stripped_strings]
		if(len(data_list) == 3):
			time = data_list[0] + data_list[1]
			show = data_list[2]
			T.append(time)
			S.append(show)
	df['Time'] = T
	df['Show'] = S
	
	i = links_list.index(link)
	file.write("\n\n" + channel_list[i] + "\n\n")
	file.write(str(df))
	
file.close()


