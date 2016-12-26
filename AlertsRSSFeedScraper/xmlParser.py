import requests

#RSS feed urls:

biometrix="https://www.google.com/alerts/feeds/08814015741937339749/14722115462138798663"

athlete_injury="https://www.google.com/alerts/feeds/08814015741937339749/8879591437926387764"

college_sports="https://www.google.com/alerts/feeds/08814015741937339749/11633575491695984145"

def getInfo():
	r= requests.get(biometrix)
	print r
	print r.content

if __name__ == '__main__':
    getInfo()