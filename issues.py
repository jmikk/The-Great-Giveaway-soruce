import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re
import random



UserAgent=input("Please enter your nation name: ")
UserAgent=UserAgent.replace(" ","_")
stockIndex=49
filename="cards_list.txt"
filename2="Gift Report.txt"
Version= 1

print("Version: "+ str(Version))

headers = {
    'User-Agent': UserAgent
}

OwnedCards =[]

if os.path.exists(filename):
	os.remove(filename)

if os.path.exists(filename2):
 	os.remove(filename2)


def build_list():
	final_list = []
	for x, y in zip(soup.find_all('CARDID'), soup.find_all('SEASON')):
		final_list.append("https://www.nationstates.net/page=deck/card="+x.text+"/season="+y.text+"/nation="+UserAgent+"\n")
		OwnedCards.append("https://www.nationstates.net/page=deck/card="+x.text+"/season="+y.text)
	return final_list
		
def save_list(list):
	print('writeing ' + name + ' now')
	with open(filename, 'a+') as f:
		f.writelines(list)

names = []
with open("names_list.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		names.append(row[0])


		
for index, name in enumerate(names):
	url = "https://www.nationstates.net/cgi-bin/api.cgi?q=cards+deck;nationname="+name
	result = requests.get(url, headers=headers)
	soup = BeautifulSoup(result.content, "xml")
	
	save_list(build_list())
	
	
	if index >= stockIndex: #CHECK FOR API LIMITS
		print('Sleeping for 30 SECONDS')
		stockIndex=stockIndex+49
		sleep(30)   #SLEEP 30 SECONDS

print("\n")
r = requests.get('https://docs.google.com/spreadsheets/u/2/d/e/2PACX-1vSaIaz_Gfn7xkk7AmKkGtSqa8EtJ2wjPgjZysCZwTL_vsFQ-CFNCm8rWYAulYqlweFpQOdx7W_Pl9cQ/pubhtml?gid=1970855203&single=true')
sleep(.7)
#print(r.text)

soup = BeautifulSoup(r.content, "html.parser")
outbutt = soup.get_text()
#outbutt=outbutt.replace("$","\n")
outbutt=outbutt.replace("Published by Google Sheets–Report Abuse–Updated automatically every 5 minutesactiveSheetId = '1970855203'; switchToSheet('1970855203');","")

x=outbutt.split("$")

count=0
listicleN=["Nation"]
listicleC=["CardID"]
listicleS=["Session"]
printcount=0 #why on earth do I really need this but it works with it ...
for i in x:
	count=count+1
	if(count==2):
		#print("Request Nation: " + i)
		listicleN.append(i)
	if(count==4):
		#print("Request Card: " + i)
		count=0
		for cardzzz in OwnedCards:
			if(cardzzz == i):
				if(printcount==1):
					print(""+listicleN[-1]+" Wants: " + i)
					with open(filename2, 'a+') as f2:
						ran=random.seed(UserAgent+i)
						f2.writelines(listicleN[-1]+" Wants: " + i +"\n\n" + "**********************Copy and paste block for reporting your donations (Thank you)**********************\nNation Donating: "+UserAgent+ "\nCard Donated TO: "+listicleN[-1]+"\nCard donated: "+i+"/trades_history=1\nProof Code: " + str(random.random())+"\n**************************************End of copy and paste block***************************************\n")
					printcount=0
				else:
					printcount=1
		#https://www.nationstates.net/page=deck/card=85949/season=1
		listicleC.append(i)	

print("\nIf a match was found please copy and paste the Copy and paste block in Gift Report.txt into a fourm post here:\nhttps://forum.thenorthpacific.org/topic/9190256/\nMake sure to send the card to the person!  You will only get credit when you make a post and gift the cards.\nThanks again for helping this program running.\n\n")
input("Make sure to open Gift Report.txt if I found any matches Press enter to exit.")
#for each in soup:
#	print(each)
	
print("Done thanks for running this with CMD")

