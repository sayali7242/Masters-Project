from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys

A = [163975, 163984, 163987, 163992]

'''
df = pd.read_csv(sys.argv[1], sep='\t', header=None)
A = df[1].tolist()
B = df[0].tolist()
'''
for i in range(len(A)):
	genes = []
	ss_id = A[i]
	#url="https://www.ncbi.nlm.nih.gov/snp/rs3132555"
	url = "https://www.ncbi.nlm.nih.gov/snp/?term=" + str(ss_id)
	page=urlopen(url)
	html_bytes = page.read()
	html = html_bytes.decode("utf-8")
	soup = BeautifulSoup(html, features="lxml")
	try:
		rs_id = soup.find("div", attrs={"class":"rslt"}).span.text
		rs_number = rs_id.split("  ")[0]

		url1 = "https://www.ncbi.nlm.nih.gov/snp/" + rs_number
		page1=urlopen(url1)
		html_bytes1 = page1.read()
		html1 = html_bytes1.decode("utf-8")
		soup1 = BeautifulSoup(html1, features="lxml")

		gene = soup1.find("dt",text="Gene : Consequence").findNext("dd").text
		print(B[i], ss_id, gene.lstrip().rstrip())
	except:
		pass
