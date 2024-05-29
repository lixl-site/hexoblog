# utf-8
# Python 2.7.16
#
import os
import datetime
import sys

print("1:create \n2:run \n3:deploy \n4:clean")

isPY3 = (sys.version > "3")

commond = ""
num = "0"
if (isPY3):
    num = input("num:")
else:
    num = raw_input("num:" )
    
if "1" == num:
    if (isPY3):
        title = input("title:")
    else:
        title = raw_input("title:" )
    nowstr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    commond = 'hexo new "'+title+'" --id="'+nowstr+'"'
elif "2" == num:
    commond = "hexo clean&& hexo generate&& hexo server"
elif "3" == num:
    commond = "hexo clean&& hexo deploy"
elif "4" == num:
    commond = "hexo clean"
else:
    pass

os.system(commond)
