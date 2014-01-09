import urllib;
import uuid;
import os;
from bs4 import BeautifulSoup;
if not os.path.exists("data"):
	os.makedirs("data");
def page(pageurl):
	html=urllib.urlopen(pageurl).read().decode("utf-8");
	soup=BeautifulSoup(html);
	r=soup.find_all(id="content");
	result="";
	for p in r:
		result+=p.get_text()+"\n";
		print(p.get_text());

	f=open("data/"+str(uuid.uuid1())+".txt","w");
	f.write(result.encode("utf-8"));
	f.close();
