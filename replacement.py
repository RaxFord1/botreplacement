import http.client
from bs4 import BeautifulSoup as beso
import datetime
def get_replacement(group="КН-207"):
    repl = replacements(group)
    if(not repl[0]):
        return f"Нет замен"
    else:
        ans = ""
        for j in repl:
            if(j==True):
                pass
            else:
                ans+= f"\n{j[0]}: {j[1]}->*{j[2]}*"
        return ans

def replacements(group="КН-207"):
    conn = http.client.HTTPConnection("mbk.mk.ua")
    conn.request("GET","/?page_id=5933")
    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read().decode('utf-8').replace('\n', '').replace("\r","").replace("\t","")
    soup = beso(data)
    last_replacement_table = soup.table
    tables = soup.findChildren('table')
    rep = [False]
    i=1;
    for j in last_replacement_table.findChildren('tr'):
        if j.td.text == group:
            rep[0] = True
            tds = j.findChildren('td')
            rep.append([tds[1].text, tds[2].text, tds[3].text])
            i=i+1
            #+=f"\n{num}: {was}->*{will_be}*"
    return rep

def get_schedule(group="КН-207"):
    ans = ""
    n=1
    for i in shedule():
        ans+=(f"{n} {i}\n")
        n+=1
    return ans

def get_schedule_with_rep(group="КН-207"):
    ans = ""
    shed = shedule()
    repl = replacements()
    
    if(not repl[0]):
        return f"Нет замен"
    else:
        ans = ""
        reps = list()
        for j in repl:
            if(j==True):
                pass
            else:
                n=0
                if(j[0].lower()=="і"):
                    n = 0
                elif(j[0].lower()=="іі"):
                    n = 1
                elif(j[0].lower()=="ііі"):
                    n = 2
                elif(j[0].lower()=="іv"):
                    n = 3
                reps.append([n,j[2]])
        for j in reps:
            shed[j[0]] = j[1]
    ans = ""
    n=1
    for i in shed:
        ans+=(f"{n} {i}\n")
        n+=1
    return ans

def shedule(group="КН-207"):
    monday = ["Английский", "ОПЗ", "ОПАМ"]
    tuesday = ["ОПЗ", "Дискретная математика", "Економика"]
    wednesday = ["История Украины", "Основы Электротехники", "Укр мова", "Математика"]
    thursday = ["Физра","Линейная алгебра","Дискретная математика"]
    friday = ["Физра","ОПАМ","Линейная алгебра"]
    shed = [monday, tuesday, wednesday, thursday, friday]
    day = datetime.datetime.today().weekday()
    shedule = ""
    if(day>=5):
        day = -1
    return shed[day+1]