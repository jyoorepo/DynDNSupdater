import dynupdater
import urllib.request
import dynupdater



externalIp = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')


exec(open("dynupdater.py").read())