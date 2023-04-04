import os
try:
    import sys
except:
    os.system('pip install sys')
try:
    import time
except:
    os.system('pip install time')
try:
    import requests
except:
    os.system('pip install requests')
try:
    import json
except:
    os.system('pip install json')
try:
    import user_agent
except: 
    os.system('pip install user_agent')
try:
    import re
except:
    os.system('pip install re') 
from time import sleep
from user_agent import generate_user_agent
# = = = = = = = = = = = = 

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

g = "\033[1;32m"
r = "\033[1;31m"
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
def si():
    os.system('clear') 
    import random
    import requests
    nam = '1234567890'
    saeim = '*'
    print(F+saeim*25)
    token = input(f'{Z}[{X}✥ {Z}] {B}ENTER TOKEN{B}     : '+Z)
    fahd = '*'
    print(F+fahd*25)
    ID = int(input(f'{Z}[{X}✥ {Z}] {B}ENTER ID {B}: '+Z))
    sss = '*'
    print(F+sss*25)
    nok = 'AAHSNotBfVMTBeQszUviauzgLaoyW-lMiP77650831743Aqq8Gi2bUnHQ82f3A19%3AAYfaeRYZWhfTXIAdybkLoeOCCQm2xZCW5bKgUvrTQQg3A243Aj1Rs7iMcDwIJaV3AAYfri6EA6PWObtklutkmSGEe9PI3Aj1Rs7iMcDwIJaVHqxJxJZCMDonkRg'
    nad = 'AAHSNotBfVMTBeQszUviauzgLaoyW-lMiP77650831743Aqq8Gi2bUnHQ82f3A19%3AAYfaeRYZWhfTXIAdybkLoeOCCQm2xZCW5bKgUvrTQQg3A243Aj1Rs7iMcDwIJaV3AAYfri6EA6PWObtklutkmSGEe9PI3Aj1Rs7iMcDwIJaVHqxJxJZCMDonkRg'
#nod = '3A193A244'
    nod = '5058796288'
    hod = 'AAHSNotBfVMTBeQszUviauzgLaoyW-lMiP77650831743Aqq8Gi2bUnHQ82f3A193AAYfaeRYZWhfTXIAdybkLoeOCCQm2xZCW5bKgUvrTQQg3A243Aj1Rs7iMcDwIJaV3AAYfri6EA6PWObtklutkmSGEe9PI3Aj1Rs7iMcDwIJaVHqxJxJZCMDonkRg'
    nq=("".join(random.choice(nam)for i in        range(11)))
    n2=("".join(random.choice(nok)for i in range(14)))
    n3=("".join(random.choice(nod)for i in         range(1)))
    n4=("".join(random.choice(nad)for i in         range(42)))
    rt = nq+':'+n2+':'+n3+':'+n4

    tlg =(f"""
🔥🔥🔥🔥🔥🔥🔥🔥🔥


 {rt}
 
  
🔥🔥🔥🔥🔥🔥🔥🔥🔥 
BY - 🇩🇿🇵🇸 @abou20""")
    print(" ")
    
    print(f'{E}====================================')
    requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))

#♡♡♡♡♡♡♡♡♡♡♡♡♡
print("معندكش سيزون اييدي كيلكي انتر ")
sesionid=input(X+'Sessionid : '+F)
m=0
os.system('clear')


def uu():
    os.system('clear') 
    import requests
    import telebot
    import random
    from time import sleep
    token = input('[~] Enter Token :')
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def start(message):
        first = message.from_user.first_name
        bot.send_message(message.chat.id, text=f"*🤍.هلا عزيزي{first}\nارسل يوزر وطلعلك كل معلومات",parse_mode="markdown")
    @bot.message_handler(func=lambda m: True)
    def Get(message):
        try:
        #Abwdy
            msg = message.text
            bot.send_message(message.chat.id, text="WIT - انتضر")
            sleep(2)
            url = f'https://echoar.ml/Apimedia/infon.php?user={msg}'
            rel = requests.get(url)
            res = rel.json()
            f = res['Info']["name"]
            b = res['Info']['account_id']
            l = res['Info']["Following"]
            list = ['By @AIODX | @qqiif','By @AIODX | @qqiif']
    
            ra = random.choice(list)
            e = res['Info']["Followers"]
            y = res['Info']['Posts']
            r = res['Info']["bio"]
            w = res['Info']['image']
        
            bot.send_message(message.chat.id,text=f'Information ✅:\n اسم الحساب : {f}\n\n عدد المتابعين: {e}\n\n عدد الذي متابعهم : {l}\n\n بوستات الحساب : {y}\n\n بايو الحساب : {r}\n\n{ra}  :',parse_mode="markdown")
            bot.send_photo(message.chat.id,w)
            
        
        except:
            pass
    bot.polling(True)

# = = = = = = = = = = = =
def folg():
    os.system(f"rm -rf id.txt")
    os.system('clear')
    os.system('clear')
    target=input(X+'Entar User Get Following : '+F)
    os.system('clear')
    hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
  }
    try:
        rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target}",headers=hd).json()['data']['user']
        idd=rer['id']
    except KeyError:
        print(Z+'❌ Entar GooD Username ')
    cookies = {"sessionid": sessionid,}
    print  (F + " USERNAME : " + C +target)
    headers = {
	'Host': 'www.instagram.com',
	'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'X-IG-App-ID': '936619743392459',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Referer': 'https://www.instagram.com/'+str(target)+'/following/',
	'TE': 'Trailers'
    }
    patrek1=0
    patrek2=0
    response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":false,"first":50}',headers=headers,cookies=cookies)
    while True:
        if str('"has_next_page":false,') in response.text:
            try:
                reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
                for iu in reg:
                    patrek1+=1
                    print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                    open("id.txt","a").write(iu['node']['id']+'\n')
                print(F+"GooD GeT List - Done Save In id.txt")
                break
            except KeyboardInterrupt:
                print(F+"GooD GeT List - Done Save In id.txt")
                break
        else:
            if patrek2 !=0:
                try:
                    end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
                    response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":false,"first":50,"after":"'+end[0]+'"}',headers=headers,cookies=cookies)
                    reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
                    for iu in reg:
                        patrek1+=1
                        print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                        open("id.txt","a").write(iu['node']['id']+'\n')
                except KeyboardInterrupt:
                    print(F+"GooD GeT List - Done Save In id.txt")
                    break
            else:
                try:
                    reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
                    for iu in reg:
                        patrek1+=1
                        print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                        open("id.txt","a").write(iu['node']['id']+'\n')
                except KeyboardInterrupt:
                    print(F+"GooD GeT List - Done Save In id.txt")
                    break
                patrek2+=1
def fols():
    os.system(f"rm -rf id.txt")
    os.system('clear')
    
    os.system('clear')
    target=input(X+'Entar User Get Followers : '+F)
    os.system('clear')
    hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
  }
    try:
        rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target}",headers=hd).json()['data']['user']
        idd=rer['id']
    except:
        print(Z+'❌ Entar GooD Username ')
    cookies = {"sessionid": sesionid,}
    print  (F + " USERNAME : " + C +target)
    headers = {
	'Host': 'www.instagram.com',
	'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'X-IG-App-ID': '936619743392459',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Referer': 'https://www.instagram.com/'+str(target)+'/followers/',
	'TE': 'Trailers'}
    patrek1=0
    patrek2=0
    response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":true,"first":50}',headers=headers,cookies=cookies)
    while True:
        if str('"has_next_page":false,') in response.text:
            try:
                reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
                for iu in reg:
                    patrek1+=1
                    print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                    open("id.txt","a").write(iu['node']['id']+'\n')
                print(F+"GooD GeT Id List - Done Save In id.txt")
                break
            except KeyboardInterrupt:
                print(F+"GooD GeT List - Done Save In id.txt")
                break
        else:
            if patrek2 != 0:
                try:
                    end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
                    response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":true,"first":50,"after":"'+end[0]+'"}',headers=headers,cookies=cookies)
                    reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
                    for iu in reg:
                        patrek1 += 1
                        print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                        open("id.txt","a").write(iu['node']['id']+'\n')
                except KeyboardInterrupt:
                    print(F+"GooD GeT List - Done Save In id.txt")
                    break
            else:
                try:
                    reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
                    for iu in reg:
                        patrek1+=1
                        print(f"""{X}[{C}{patrek1}{X}]{F}"""+str(iu['node']['id']))
                        open("id.txt","a").write(iu['node']['id']+'\n')
                except KeyboardInterrupt:
                    print(F+"GooD GeT List - Done Save In id.txt")
                    break
                patrek2+=1
def pp():
    link = input(g+"[~] ENTER LINK POST : ")
    m=0
try:
	ree = requests.get(link).text
	if "media_id" in ree:
		ds = sessionid.split("%")[0]
		id = ree.split('media_id":"')[1].split('"')[0]
		print(f"{g}[ {id} ] DONE GET ID POST")
		time.sleep(2)
		url = "https://www.instagram.com/api/v1/media/"+id+"/likers/"
		headers = {
    "Host": "www.instagram.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48 Build/NRD90N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "viewport-width": "360",
    "accept": "*/*",
    "x-asbd-id": "198387",
    "x-csrftoken": "Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J",
    "x-ig-app-id": "1217981644879628",
    "referer": link,
    "accept-encoding": "gzip, deflate, sdch, br",
    "accept-language": "ar-EG,ar;q\u003d0.8,en-US;q\u003d0.6,en;q\u003d0.4",
    "cookie": 'mid=Y83WYwABAAG1muBigpOEBOy0R5tI;ig_did=260D38C2-3E35-4FDD-8C11-EDEBB7346E9A;ig_nrcb=1;datr=5z_YY76uvkVOr138hT9g0rQ7;shbid="16500\05457055641229\0541706798795:01f7e936f330355399eb2de81575aabf9e323d8b4f530fe5d93bbd31fe45a07bc3e4add9";shbts="1675262795\05457055641229\0541706798795:01f7f8064121b83986b00931d067bac19271f20e265a56bd3639684e274e472caa833c9d";ig_direct_region_hint="ODN\05457055641229\0541706798805:01f7a1df3ab2af99b37d446bf9322acebddadfcd81c2b5fde83ddb9e2169e1f6403a0797";sessionid='+sessionid+';csrftoken=Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J;rur="LDC\05457055641229\0541706798858:01f7ef09ec77691b2f477880e9ef68bb8e456c392546e0bfb5142248bec0d2e56de7d201";ds_user_id='+ds
		}
		re = requests.get(url,headers=headers)
		for i in re.json()["users"]:
			pk = (i["pk"])
			m+=1
			print(f"{g}[ {m} ] {r}{pk}")
			with open("id.txt","a") as save:
				save.write(f"{pk}")
		print("done save in id.txt")
	else:
		print(r+"ERROR LINK")
except:
    print(r+"ERROR LINK")

#~~~~~~~~~~~~~~~~
def oo():
    os.system('clear')
    import requests
    
    G = "\033[1;32m"
    R = "\033[1;31m"
    id = input(G+"[~] ENTER ID : ")
    token = input(R+"[~] ENTER TOKEN : ")
    file = input("[~] ENTER FILE ID : ")
    for i in open(file,"r").read().splitlines():
        ID = i.split("\n")[0]
        r = requests.get(f"https://check-coin.mahmoidayman.repl.co/?target="+ID+"&submit=submit").text
        if "COIN" in r:
            coin = r.split("><h2>")[1].split(": COIN </h2>")[0]
            if int(coin)>=400:
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=NEW ID => {ID}\nCOIN => {coin}\nBY @N_F_W")
                print(f"{G}( {ID} ) | {coin}")
            else:
                print(f"{R}( {ID} ) | {coin}")
        else:
    	    print(f"{G}( {ID} ) | ERROR ID")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def hh():
    os.system('clear')
    import requests
    import telebot
    import re
    token =input ("ادخل توكن بوت ")
    bot = telebot.TeleBot('token')
    proxies = {
    "http": "http://fnygbuyr:r1ofzqbjw488@188.74.210.21:6100",
    "https": "http://fnygbuyr:r1ofzqbjw488@188.74.210.21:6100"
}
    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, 'مرحبا، قم بإرسال الآن ايدي منشور وايدي الضحية بهذا الشكل:\n\n11111:22222\n\nحيث 11111 هو ايديك و 22222 هو ايدي الضحية.\n@N_F_W')
    @bot.message_handler(func=lambda m: True)
    def send_request(message):
        bot.send_message(message.chat.id, "جاري المعالجة ......")
        ll = message.text
        if not re.match(r'^\d+:\d+$', ll):
            bot.send_message(message.chat.id, "يرجى إدخال رسالة صالحة.")
        return   
        baqer = ll.split(':')[0]
        tak = ll.split(':')[1]
        url = f"https://php-web-server.aaunbidiwidjh.repl.co/?target={tok}&userid={baqer}&submit=%D8%B1%D8%B4%D9%82+"
    
        try:
            response = requests.get(url, proxies=proxies)
            response_text = response.text
        
            if 'DONE : ' in response_text:
                RR = response_text.split('''class='success'><center><font color='red'><hr>''')[1].split('{"status":"')[0]
                good = f'تم الرشق  عدد ==>{RR}'
                bot.send_message(message.chat.id, good)       
            else:
                DD = response_text.split('message":"')[1].split('<hr>')[0]
                bad2 = f'{DD}'
                bot.send_message(message.chat.id, bad2)
    
        except Exception as e:
            error_msg = f"حدث خطأ أثناء تنفيذ الأمر: {str(e)}"
            bot.send_message(message.chat.id, error_msg)

    bot.polling(True)


def ee():
    import os
    os.system('clear')
    import instaloader,os,requests,time
    import webbrowser
    os.system("clear")
    R = '\033[1;31m'
    B = '\033[2;36m'
    G = '\033[1;32m'
    P = '\u001b[35m'
    Y = '\033[1;33m'
    W = "\033[0m"
    logo=(R+f"""━━━━━━━━━━━━━
                     _            
  ___ ___  _ __   __| | ___  _ __ 
 / __/ _ \| '_ \ / _` |/ _ \| '__|
| (_| (_) | | | | (_| | (_) | |   
 \___\___/|_| |_|\__,_|\___/|_|   
                                  

━━━━━━━━━━━━━ >> 
@abou20""")
    print(logo)

    webbrowser.open('https://t.me/keeptech')

    USER = input(G+"Enter UserName Fake  : ")
    PASSWORD = input(R+"Enter PassWord Fake : ")
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    username1 = input(B+"Enter Targted UserName  : ")
    sendtoo = input(R+"Enter ID For Send Followers : ")
    profile = instaloader.Profile.from_username(L.context, username1)
    for follow in profile.get_followers():
                profile = str(instaloader.Profile.from_username(L.context,follow.username))
                idd=str(profile.split(')>')[0])
                userid=idd.split(' (')[1]
                
                print(R+"ID Victim Is "+userid)
                url=f"https://unfaltering-session.000webhostapp.com/order-placer.php?oid={userid}&uid={sendtoo}&submit=submit"
                url1=f'https://unfaltering-session.000webhostapp.com/coin-checker.php?oid={userid}&submit=submit'
                
                condor=str(requests.get(url).text)
                
                smahi=str(requests.get(url1).text)
                if '"message":"Something went wrong, Please try again."' in condor:
                	print(R+"[❌] User Not On InstaUp")
                if '"status":"Error"' in condor:
                	print(R+"[❌] User Blocked Or Less Coins")
                if 'coins":"' in smahi:
                	coin=str(smahi.split('coins":"')[1])
                	coins=str(coin.split('"')[0])
                	print(R+f'Coins is ==> {coins}')
                if '"status":"Successful"' in condor:
                	print(G+f'[✅]Successful Send 100 Followers To ==> {sendtoo} ')
                if 'coins":"' in condor:
                	coin=str(condor.split('coins":"')[1])
                	coins=str(coin.split('"')[0])
                	print(G+f'Coins Is ==> {Coins}')
                	
def ff():
    os.system('clear')
    import requests
    import time

    g = "\033[1;32m"
    r = "\033[1;31m"

    link = input(g+"[~] ENTER LINK POST : ")
    
    m=0
    try:
	    ree = requests.get(link).text
	    if "media_id" in ree:
		    ds = sessionid.split("%")[0]
		    id = ree.split('media_id":"')[1].split('"')[0]
		    print(f"{g}[ {id} ] DONE GET ID POST")
		    time.sleep(2)
		    url = "https://www.instagram.com/api/v1/media/"+id+"/likers/"
		    headers = {
    "Host": "www.instagram.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48 Build/NRD90N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "viewport-width": "360",
    "accept": "*/*",
    "x-asbd-id": "198387",
    "x-csrftoken": "Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J",
    "x-ig-app-id": "1217981644879628",
    "referer": link,
    "accept-encoding": "gzip, deflate, sdch, br",
    "accept-language": "ar-EG,ar;q\u003d0.8,en-US;q\u003d0.6,en;q\u003d0.4",
    "cookie": 'mid=Y83WYwABAAG1muBigpOEBOy0R5tI;ig_did=260D38C2-3E35-4FDD-8C11-EDEBB7346E9A;ig_nrcb=1;datr=5z_YY76uvkVOr138hT9g0rQ7;shbid="16500\05457055641229\0541706798795:01f7e936f330355399eb2de81575aabf9e323d8b4f530fe5d93bbd31fe45a07bc3e4add9";shbts="1675262795\05457055641229\0541706798795:01f7f8064121b83986b00931d067bac19271f20e265a56bd3639684e274e472caa833c9d";ig_direct_region_hint="ODN\05457055641229\0541706798805:01f7a1df3ab2af99b37d446bf9322acebddadfcd81c2b5fde83ddb9e2169e1f6403a0797";sessionid='+sessionid+';csrftoken=Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J;rur="LDC\05457055641229\0541706798858:01f7ef09ec77691b2f477880e9ef68bb8e456c392546e0bfb5142248bec0d2e56de7d201";ds_user_id='+ds
		}
		    re = requests.get(url,headers=headers)
		    for i in re.json()["users"]:
		    	pk = (i["pk"])
    			m+=1
		    	print(f"{g}[ {m} ] {r}{pk}")
    			with open("id.txt","a") as save:
    			    save.write(f"{pk}")
    			    print("done save in id.txt")
		    else:
		        print(r+"ERROR LINK")
    except:print(r+"ERROR LINK")
def oop():
    os.system('clear') 
    import requests
    import telebot
    import random
    from telebot import types
#programming = u_zzf
    print("اذهب الى البوت بعد ادخال التوكن")
    token = input("Enter token bot : ")
    bot = telebot.TeleBot(token)
    co = types.InlineKeyboardButton(text ="- Start Checker ✅",callback_data = 'st')
    ch = types.InlineKeyboardButton(text ="- Dev",url="https://t.me/Abdullah_Abd_alsalam")
    iraq = types.InlineKeyboardButton(text ="- @yahoo.com 📧✅ ",callback_data = 'n1')
    @bot.message_handler(commands=["start"])
    def start(message):
        fr = message.from_user.first_name
        maac = types.InlineKeyboardMarkup()
        maac.row_width = 1
        maac.add(co,ch)
        bot.send_message(message.chat.id,f"""
    <strong>
welcome {fr},  🌝💗
=== === ===
Wellcome To Hunter yahoo Bot! 
To Start Checker Click :
=== === ===
By : @PV_59
</strong>
    """,parse_mode="html",reply_markup=maac)
    @bot.callback_query_handler(func=lambda call: True)
    def qwere(call):
        if call.data == "st":
        	li(call.message)
        if call.data == "n1":
            n1(call.message)
    def li(message):
    	fr = message.from_user.first_name
    	l = types.InlineKeyboardMarkup()
    	l.row_width = 2
    	l.add(iraq)
    	bot.send_message(message.chat.id,f"""
    <strong>
Hello {fr}, 
=== === ===
Choice
=== === ===
By : @PV_59
</strong>
    """,parse_mode="html",reply_markup=l)
    def n1(message):
	      	a='qwertyuiopasdfghjklzxcvbnm'
	      	b='1234567890'
    	  	length = 1
	      	while True:
	  		    u= ''.join(random.sample(b,length))
	  		    r= ''.join(random.sample(a,length))
	  		    b= ''.join(random.sample(a,length))
	  		    o= ''.join(random.sample(a,length)) 
	  		    i=''.join(random.sample(a,length))
	  		    AA=(i+o+b+u+r)
	  		    A=(i+r+b+o+u)
	  		    AAA=(i+u+o+b+r)
	  		    AAAA=(i+o+r+b+u)
	  		    AAAAA=(r+i+o+u+b)
	  		    AAAAAA=(i+u+r+o+b)
	  		    AAAAAAA=(i+o+b+u+r)
	  		    AAAAAAAAA=(b+o+i+u+r)
	  		    u_zzf = AA , A , AAA , AAAA , AAAAA , AAAAAA , AAAAAAA , AAAAAAAAA
	  		    email = str("".join(random.choice(u_zzf)))
	  		    yahoo = requests.get('https://yahooe.herokuapp.com/check/yahoo/JJJJzJJJ/?Email='+email).json()['check']
	  		    bot.send_message(message.chat.id,f"""
Hi frind , Hits yahoo Eamail
=== === ===
yahoo : {email}@yahoo.com 📧✅
=== === ===
The situation : {yahoo} ✅🌝
=== === ===
By : @PV_59 
    """)
    mees = types.InlineKeyboardMarkup(row_width=1)
    buut5 = types.InlineKeyboardButton(f"- Email 📧 : {email}@yahoo.com",callback_data='jhi5')
    buut1 = types.InlineKeyboardButton(f"- The situation  ✅ : {yahoo}",callback_data='jhi1')
    buut3 = types.InlineKeyboardButton(f"- 💁 ✅ : Dev",url="https://t.me/u_zzf ",callback_data='jhi2')
    buut4 = types.InlineKeyboardButton(f"- 🧑‍💻💁  programming : ",url="https://t.me/Abdullah_Abd_alsalam ",callback_data='jhi9')
    mees.add(buut1,buut5,buut3,buut4)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Bot Started ✅</strong>",parse_mode='html',reply_markup=mees)
#تخمط  بدون متذكر مصدر= ماعدك شرف 
    bot.polling(True)
def abdo():
       
       
     os.system('clear') 
     print(" يتم تثبيت جميع المكاتب")
     os.system('pip install aiofiles ')
     os.system('pip install android')
     os.system('pip install ansicolors')
     os.system('pip install ansiwrap')
     os.system('pip install APScheduler')
     os.system('pip install astroid')
     os.system('pip install async-generator')
     os.system('pip install async-timeout')
     os.system('pip install asyncio')
     os.system('pip install attrs')
     os.system('pip install audi    ostream')
     os.system('pip install b')
     os.system('pip install barcode')
     os.system('pip install beautifulsoup4')
     os.system('pip install Brotli')
     os.system('pip install bs4')
     os.system('pip install cachetools')
     os.system('pip install cairocffi')
     os.system('pip install Cair    osVG')
     os.system('pip install calcu')
     os.system('pip install certif')
     os.system('pip install cffi')
     os.system('pip install chainmap')
     os.system('pip install chardet')
     os.system('pip install charset-normalizer')
     os.system('pip install cinemagoer')
     os.system('pip install click')
     os.system('pip install cloudscraper')
     os.system('pip install cmake')
     os.system('pip install colorama')
     os.system('pip install colored')
     os.system('pip install colour')
     os.system('pip install combometho')
     os.system('pip install covid')
     os.system('pip install cowpy')
     os.system('pip install cryptography')
     os.system('pip install cssselect2')
     os.system('pip install darklib')
     os.system('pip install dataclasses')
     os.system('pip install DateTime')
     os.system('pip install decorator')
     os.system('pip install defusedxml')
     os.system('pip install Deprecated')
     os.system('pip install distro')
     os.system('pip install docutils')
     os.system('pip install emoji')
     os.system('pip install et-xmlfile')
     os.system('pip install fake-useragent')
     os.system('pip install Faker')
     os.system('pip install filelock')
     os.system('pip install Flask')
     os.system('pip install fonttools')
     os.system('pip install fore')
     os.system('pip install future')
     os.system('pip install gdolib')
     os.system('pip install geocoder')
     os.system('pip install geographiclib')
     os.system('pip install geopy')
     os.system('pip install gitdb')
     os.system('pip install GitPython')
     os.system('pip install glitch-this')
     os.system('pip install google-api-core')
     os.system('pip install google-api-python-client')
     os.system('pip install google-auth')
     os.system('pip install google-auth-httplib2')
     os.system('pip install google-auth-oauthlib')
     os.system('pip install inboxkitten')
     os.system('inboxkitten')
     os.system('pip install googleapis-common-prot    os')
     os.system('pip install googletrans')
     os.system('pip install gTTS')
     os.system('pip install gunicorn')
     os.system('pip install h11')
     os.system('pip install h2')
     os.system('pip install hachoir')
     os.system('pip install HamodyTools')
     os.system('pip install helpers')
     os.system('pip install heroku3')
     os.system('pip install hijri-converter')
     os.system('pip install hpack')
     os.system('pip install hstspreload')
     os.system('pip install html-telegraph-p    oster')
     os.system('pip install html5lib')
     os.system('pip install httpcore')
     os.system('pip install httplib2')
     os.system('pip install httpx')
     os.system('pip install huepy')
     os.system('pip install humanize')
     os.system('pip install hyperframe')
     os.system('pip install idna')
     os.system('pip install imageio')
     os.system('pip install imageio-ffmpeg')
     os.system('pip install IMDbPY')
     os.system('pip install importlib-metadata')
     os.system('pip install iniconfig')
     os.system('pip install instabot')
     os.system('pip install InstagramAPI')
     os.system('pip install InstagramIG')
     os.system('pip install install')
     os.system('pip install instaloader')
     os.system('pip install isort')
     os.system('pip install itsdangerous')
     os.system('pip install jedi')
     os.system('pip install jellyfish')
     os.system('pip install Jinja2pip install jsscraper')
     os.system('pip install JustWatch')
     os.system('pip install Kivy')
     os.system('pip install kivymd')
     os.system('pip install kivymd-extensions')
     os.system('pip install kivymd-extensions.akivymd')
     os.system('pip install lazy-object-proxy')
     os.system('pip install libretranslatepy')
     os.system('pip install logger')
     os.system('pip install lottie')
     os.system('pip install lxml')
     os.system('pip install lyricsgenius')
     os.system('pip install Markdown')
     os.system('pip install markdown-it-py')
     os.system('pip install MarkupSafe')
     os.system('pip install mccabe')
     os.system('pip install mdurl')
     os.system('pip install mechanize')
     os.system('pip install mem-top')
     os.system('pip install mement    os')
     os.system('pip install mock')
     os.system('pip install motor')
     os.system('pip install moviepy')
     os.system('pip install multitasking')
     os.system('pip install mutagen')
     os.system('pip install names')
     os.system('pip install nek    os.py')
     os.system('pip install Nova-Tools')
     os.system('pip install nulltype')
     os.system('pip install numpy')
     os.system('pip install oauthlib')
     os.system('pip install OneClick')
     os.system('pip install openai')
     os.system('pip install openpyxl')
     os.system('pip install options')
     os.system('pip install outcome')
     os.system('pip install packaging')
     os.system('pip install pafy')
     os.system('pip install pandas')
     os.system('pip install pandas-stubs')
     os.system('pip install parsedatetime')
     os.system('pip install parso')
     os.system('pip install payment')
     os.system('pip install Pillow')
     os.system('pip install pkgconfig')
     os.system('pip install platformdirs')
     os.system('pip install pluggy')
     os.system('pip install prettytable')
     os.system('pip install proglog')
     os.system('pip install protobuf')
     os.system('pip install psutil')
     os.system('pip install py')
     os.system('pip install pyaes')
     os.system('pip install pyasn1')
     os.system('pip install pyasn1-modules')
     os.system('pip install pybind11')
     os.system('pip install pycparser')
     os.system('pip install pycryptodomex')
     os.system('pip install pydantic')
     os.system('pip install pydub')
     os.system('pip install pyfiglet')
     os.system('pip install pygame')
     os.system('pip install Pygments')
     os.system('pip install pyjnius')
     os.system('pip install pylast')
     os.system('pip install pylint')
     os.system('pip install pymediainfo')
     os.system('pip install pyminizip')
     os.system('pip install pymongo')
     os.system('pip install pyOpenSSL')
     os.system('pip install pyparsing')
     os.system('pip install PyQt5')
     os.system('pip install Pyrogram')
     os.system('pip install PySDL2')
     os.system('pip install pySmartDL')
     os.system('pip install PySocks')
     os.system('pip install pyTelegramBotAPI')
     os.system('pip install pytest')
     os.system('pip install python-barcode')
     os.system('pip install python-cfonts')
     os.system('pip install python-dateutil')
     os.system('pip install python-dotenv')
     os.system('pip install python-Levenshtein')
     os.system('pip install pytube')
     os.system('pip install pytz')
     os.system('pip install pytz-deprecation-shim')
     os.system('pip install pywebio=')
     os.system('pip install qrcode')
     os.system('pip install ratelim')
     os.system('pip install rebot')
     os.system('pip install redis')
     os.system('pip install regex')
     os.system('pip install requests')
     os.system('pip install requests-oauthlib')
     os.system('pip install requests-toolbelt')
     os.system('pip install responses')
     os.system('pip install result')
     os.system('pip install rfc3986')
     os.system('pip install rich')
     os.system('pip install rivals-top8-results')
     os.system('pip install rsa')
     os.system('pip install sacpy')
     os.system('pip install say')
     os.system('pip install scapy')
     os.system('pip install schedule')
     os.system('pip install scikit-build')
     os.system('pip install scipy')
     os.system('pip install selenium')
     os.system('pip install ShazamAPI')
     os.system('pip install simplere')
     os.system('pip install six')
     os.system('pip install smmap')
     os.system('pip install sniffio')
     os.system('pip install sortedcontainers')
     os.system('pip install soupsieve')
     os.system('pip install spamwatch')
     os.system('pip install speedtest-cli')
     os.system('pip install SQLAlchemy')
     os.system('pip install sqlalchemy-json')
     os.system('pip install stdiomask')
     os.system('pip install telebot')
     os.system('pip install telegram')
     os.system('pip install telegraph')
     os.system('pip install Telethon')
     os.system('pip install texttable')
     os.system('pip install textwrap3')
     os.system('pip install TgCrypto')
     os.system('pip install TikTok-dl')
     os.system('pip install tinycss2')
     os.system('pip install toml')
     os.system('pip install tomli')
     os.system('pip install tornado')
     os.system('pip install tqdm')
     os.system('pip install TrackCobra')
     os.system('pip install trak    os')
     os.system('pip install translate')
     os.system('pip install trio')
     os.system('pip install trio-websocket')
     os.system('pip install TSMRS')
     os.system('pip install typed-ast')
     os.system('pip install typer')
     os.system('pip install types-pytz')
     os.system('pip install typing_extensions')
     os.system('pip install tzdata')
     os.system('pip install tzlocal')
     os.system('pip install ua-parser')
     os.system('pip install uritemplate')
     os.system('pip install uritools')
     os.system('pip install urlextract')
     os.system('pip install urllib3')
     os.system('pip install us')
     os.system('pip install user-agent')
     os.system('pip install user-agents')
     os.system('pip install utils')
     os.system('pip install uuid')
     os.system('pip install validators')
     os.system('pip install vcsi')
     os.system('pip install Wand')
     os.system('pip install wcwidth')
     os.system('pip install webdriver-manager')
     os.system('pip install webencodings')
     os.system('pip install websockets')
     os.system('pip install Werkzeug')
     os.system('pip install wget')
     os.system('pip install wrapt')
     os.system('pip install wsproto')
     os.system('pip install xarray')
     os.system('pip install yfinance')
     os.system('pip install youtube-dl')
     os.system('pip install youtube-search')
     os.system('pip install youtube-search-python')
     os.system('pip install yt-dlp')
     os.system('pip install zerlib')
     os.system('pip install zipp')
     os.system('pip install zope.interfac')
     os.system('tkinter')
     os.system('*')
     os.system('ttk')
     os.system('wifi')
     os.system('Cell')
     os.system('googlesearch')
     os.system('random')
     os.system('webbrowser')
     os.system('requests')
     os.system('    os')
     os.system('time')
     os.system('sleep')
     os.system('InstagramIG')
     os.system('SidraELEzz')
     os.system('JO')
     os.system('exec')
     os.system('JO;exec')
     os.system('pyfiglet')
     os.system('user_agent')
     os.system('generate_user_agent')
     os.system('user')
     os.system('agent')
     os.system('datetime')
     os.system('webbrowser')
     os.system('socket')
     os.system('uuid')
     os.system('uuid4')
     os.system('json')
     os.system('date')
     os.system('system')
     os.system('threading')
     os.system('re')
     os.system('colorama')
     os.system('init')
     os.system('Fore')
     os.system('BeautifulSoup')
     os.system('secrets')
     os.system('token_hex')
     os.system('hex')
     os.system('token')
     os.system('instaloader')
     os.system('mechanize')
     os.system('gdolib')
     os.system('Nova_Tools')
     os.system('Nova')
     os.system('Tools')
     os.system('TrackCobra')
     os.system('Valid')
     os.system('names')
     os.system('jsscraper')
     os.system('darklib')
     os.system('OneClick')
     os.system('python-cfonts')
     os.system('python')
     os.system('cfonts')
     os.system('TrackCobra')
     os.system('telebot')
     os.system('Pytelegrambotapi==4')
     os.system('Pytelegrambotapi==5')
     os.system('Pytelegrambotapi==6')
     os.system('Pytelegrambotapi')
     os.system('pyshorteners')
     os.system('faker')
     os.system('gtts')
     os.system('gTTS')
     os.system('pip3 install colorama')
     os.system('install')
     os.system('rich')
     os.system('pip3 install rich')
     os.system('stdiomask')
     os.system('pyrogram')
     os.system('pywebio')
     os.system('pystyle')
     os.system('psnawp_api')
     os.system('psnawp')
     os.system('api')
     os.system('PSNAWP')
     os.system('pyrogram')
     os.system('types')
     os.system('pyrogram.types')
     os.system('InlineKeyboardButton')
     os.system('InlineKeyboardMarkup')
     os.system('Client')
     os.system('filters')
     os.system('speedtest')
     os.system('playsound')
     os.system('telethon')
     os.system('functions')
     os.system('TelegramClient')
     os.system('telethon.tl.types')
     os.system('tl.types')
     os.system('types')
     os.system('tl')
     os.system('InputPhoneContact')
     os.system("pip install instaloader")	
     os.system("pip install requsets")
     os.system("pip install names")
     os.system("pip install datetime")
     os.system("pip install user_agent")
     os.system("pip install json")
     os.system("pip install     os")
     os.system("pip install random")
     os.system("pip install sys")
     os.system("pip install mechanize")
     os.system("pip install uid")
     os.system("pip install datetime")
     os.system("pip install uuid")
     os.system("pip install uuid4")
     os.system("pip install sleep")
     os.system('pip install gdolib==0.3.1')
     os.system('pip install gdolib==0.4.1')
     os.system('pip install gdolib==0.5.1')
     os.system('meassage_handler')
     os.system('handler')
     os.system('meassage')
     os.system('kivymd.app')
     os.system('MDApp')
     os.system('kivymd')
     os.system('app')
     os.system('kivymd.uix.screen')
     os.system('uix.screen')
     os.system('uix')
     os.system('screen')
     os.system('textfield')
     os.system('button')
     os.system('dialog')
     os.system('lang')
     os.system('menu')
     os.system('MDDropdownMenu')
     os.system('webbrowser')
     os.system('mechanize')
     os.system('BeautifulSoup')
     os.system('flask')
     os.system('kivymd.uix.textfield')
     os.system('kivymd.uix.button')
     os.system('kivymd.uix.dialog')
     os.system('kivy.lang')
     os.system('kivymd.uix.menu')
     os.system('instaloader')
     os.system('tokenize')
     os.system('cookie_re')
     os.system('cookie')
     os.system('threading')
     os.system('playsound')
     os.system('Fore')
     os.system('Back')
     os.system('Style')
     os.system('init')
     os.system('Hunter')
     os.system('Hunter')
     os.system('InstagramAPI')
     print("تم تثبيت المكاتب بنجاح")
def go():
    os.system('clear')
    import requests
    import telebot
    import re
    token=input('ادخل توكن بوت')
    print('روح للبوت اكتب strat')
    bot = telebot.TeleBot(token)




    proxies = {
    "http": "http://fnygbuyr:r1ofzqbjw488@188.74.210.21:6100",
    "https": "http://fnygbuyr:r1ofzqbjw488@188.74.210.21:6100"
}
    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, 'مرحبا، قم بإرسال الآن ايديك وايدي الضحية بهذا الشكل:\n\n11111:22222\n\nحيث 11111 هو ايديك و 22222 هو ايدي الضحية.\n@N_F_W')
    @bot.message_handler(func=lambda m: True)
    def send_request(message):
        bot.send_message(message.chat.id, "جاري المعالجة ......")
        ll = message.text
        if not re.match(r'^\d+:\d+$', ll):
            bot.send_message(message.chat.id, "يرجى إدخال رسالة صالحة.")
            return   
        baqer = ll.split(':')[0]
        tak = ll.split(':')[1]
        url = f"https://dev-sd-ahmid-sd.pantheonsite.io/wp-admin/sad/Black%2B1000.php?oid={tak}&uid={baqer}&submit=%D8%B1%D8%B4%D9%82"
    
        try:
            response = requests.get(url, proxies=proxies)
            response_text = response.text
        
            if 'DONE : ' in response_text:
                RR = response_text.split('''class='success'><center><font color='red'><hr>''')[1].split('{"status":"')[0]
                good = f'تم الرشق  عدد ==>{RR}'
                bot.send_message(message.chat.id, good)       
            else:
                DD = response_text.split('message":"')[1].split('<hr>')[0]
                bad2 = f'{DD}'
                bot.send_message(message.chat.id, bad2)
    
        except Exception as e:
            error_msg = f"حدث خطأ أثناء تنفيذ الأمر: {str(e)}"
            bot.send_message(message.chat.id, error_msg)

    bot.polling(True)
def gg():
    os.system('clear')
    import requests
    import random
    print('مرحبا بك في صيد بينا')
    MMMM = '1234567890'
    while True:
        bin = int("".join(random.choice(MMMM) for i in range(6)))
        url = f"https://api.dlyar-dev.tk/info-bin?bin={bin}"
        CLAF = requests.get(url).json()
        if CLAF["status"] == True:
            try:
                co = CLAF["country"]
                fl = CLAF["flag"]
                print(f'\033[2;32m  Good bin : \033[2;34m {bin}  \n \033[2;33m Bin Visa ✅ \n  Country : \033[2;37m{co} \n \033[2;33m Flag : \033[2;31m{fl} ')
        
        
        
        
            except:
                print(f'\033[2;31m  Bad bin : \033[2;35m {bin} ')
                pass
    
    
    
    
    
        else:
            print(f'\033[2;31m  Bad bin : \033[2;35m {bin} ')

def patrek():
    os.system('clear')
    print(g+"""1- GeT Id Following : سحب من المتابعهم
2- GeT Id Followers : سحب من المتابعين 
3- GeT id form post.: سحب من منشور 
4-فحص الايديات 
5-رشق تلقائي ومباشر 
6-سحب ايدي منشور 
7-بوت سحب ايدي حسابك
8-استخراج سيزون عشوائي 
9-بوت صيد انستا غرام بدون معلومات
10-موقع رشق متابعين 
11-موقع رشق لايكات 
12-تثبيت جميع مكاتب بايثون
13-بوت رشق 
14-صيد بينات
15-بوت رشق لايكات 
""")
   
    
    xx=input("Entar : ")
    if xx=='1':
        folg()
    if xx=='2':
        fols()
    if xx=='3':
        pp()
    if xx=='4':
        oo()
    if xx=='5':
        ee()
    if xx=='6':
        ff()     
    if xx=='7':
        uu()
    if xx=='8':
        si()
    if xx=='9':
        oop()
    if xx=='10':
        import webbrowser
        webbrowser.open('https://Hio.aaunbidiwidjh.repl.co')
    if xx=='11':
        import webbrowser
        webbrowser.open('https://PHP-Web-Server.aaunbidiwidjh.repl.co')
    if xx=='12':
         abdo()
    if xx=='13':
        go()
    if xx=='14':
        gg()
    if xx=='15':
        hh()
patrek()