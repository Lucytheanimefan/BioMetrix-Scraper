import requests
import xml.etree.ElementTree
from xml.dom import minidom
#RSS feed urls:

biometrix="https://www.google.com/alerts/feeds/08814015741937339749/14722115462138798663"

athlete_injury="https://www.google.com/alerts/feeds/08814015741937339749/8879591437926387764"

college_sports="https://www.google.com/alerts/feeds/08814015741937339749/11633575491695984145"

def getInfo():
	bio = requests.get(biometrix)
	ath = requests.get(athlete_injury)
	coll = requests.get(college_sports)
	return {"biometrix":bio.content, "athlete_injury":ath.content,"college_sports":coll.content}

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def writeToFile(content, file = None):
	if file is None:
		file = open('data.xml', 'w')	
	file.write(content)

def parseXML(xmlContent=None):
	data = []

	dom = xml.dom.minidom.parseString(xmlContent)
	for entry in dom.getElementsByTagName("entry"):
		title = entry.getElementsByTagName("title")[0]
		content = entry.getElementsByTagName("content")[0]
		#print "---------"
		#print "Title: "+getText(title.childNodes)
		#print "Content: "+getText(content.childNodes)
		data.append({"title":getText(title.childNodes), "content":getText(content.childNodes)})
	return data

def getAllData():
	info = getInfo()
	data = {}
	data["biometrix"]=parseXML(info["biometrix"])
	data["athlete_injury"]=parseXML(info["athlete_injury"])
	data["college_sports"]=parseXML(info["college_sports"])
	return data

if __name__ == '__main__':
	print getAllData()

