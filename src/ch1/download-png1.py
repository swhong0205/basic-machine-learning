#read library
import urllib.request

#assign path for save and url
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#download
urllib.request.urlretrieve(url, savename)
print("저장되었습니다..!")
