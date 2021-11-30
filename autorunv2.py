import urllib.request
import schedule
import time

def getIp():
    urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')


externalIp = getIp()


def job():
    refreshedIp = getIp()
    if refreshedIp != externalIp:
        print("IP does not match")
        exec(open('./dynupdater.py').read())

schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
