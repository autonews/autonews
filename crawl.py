import pagevisitor;
import re;
import urllib;
from bs4 import BeautifulSoup;

seed="http://www.xinhuanet.com/";
html=urllib.urlopen(seed).read().decode("utf-8");
soup=BeautifulSoup(html);
links=soup.find_all("a");
def extract(pageurl):
	urlr=r"http://news.xinhuanet.com/";
	if not re.match(urlr,pageurl):
		return;
	try:
		pagevisitor.page(pageurl);
	except:
		pass
for link in links:
	extract(link["href"]);

'''
urlr=r"http://news.xinhuanet.com/";
url="http://www.xinhuanet.com/health/2014-01/09/c_125977606.htm";
if(re.match(urlr,url)):
	print("yes");
else:
	print("no");
'''
