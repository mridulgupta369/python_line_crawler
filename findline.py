from subprocess import getstatusoutput as out
import os
os_path=os.path
from queue import Queue

count=0

def search(address, search_string, depth=1, max_depth=None):
    global count
    if max_depth != None:
        if max_depth<depth:
            return
    Q=Queue()
    string=out('ls '+ address)[1].split('\n')
    for i in string:
        if i=='':
            break
        if search_string in i:
            print('found in name: ', address+ '/' +i)
        if os_path.isdir(address+'/'+i):
            Q.put(address+'/'+i)
        else:
            try:
                file=open(address+'/'+i)
                content=file.read()
            except:
                continue
            if search_string in content:
                print ('found in ' + address +'/'+i)
                count+=1
                file.close()
    while not Q.empty():
        search(Q.get(), search_string, depth+1, max_depth)

print('Enter the search string')
search_string=input()
print('enter the directory address')
address=input()
search(address, search_string)
print ('found in', count)
        
