#to check if python program is valid ipv4 address or not.


def check_ipaddress(ip):
	numbers = ip.split(".")

	for x in numbers:
		if len(x)>3 or len(x)==0:
			return False
		if x[0] == 0 and len(x)!=1 or not x.isdigit() or int(x)>255:
			return False
	return True
print("check if its a valie ip addrees or not", check_ipaddress("192.72.62.1"))
print("check if its a valie ip addrees or not", check_ipaddress("ab.72.62.1"))
print("check if its a valie ip addrees or not", check_ipaddress("1.72.62.1"))
print("check if its a valie ip addrees or not", check_ipaddress("0.0.0.0"))
print("check if its a valie ip addrees or not", check_ipaddress("256.72.62.1"))
