import urllib.request
import schedule
import time

externalIp = urllib.request.urlopen(
    'https://api.ipify.org').read().decode('utf8')

print("this is your current IP", externalIp)

def job():
    print(urllib.request.urlopen('https://api.ipify.org').read().decode('utf8'))

refreshedIP = job()

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    if refreshedIP == externalIp:
        exec(open("dynupdater.py").read())
    else:  
        schedule.run_pending()