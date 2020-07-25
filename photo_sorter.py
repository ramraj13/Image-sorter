import os
import sys
import random

actress_list=[b'E:\New folder\Kareena Kapoor',b'E:\New folder\Shraddha Kapoor',b'E:\New folder\Sonakshi Sinha']
length=len(actress_list)

#print((actress_list[2]).decode('utf-8'))

def list_func(directory):
    l=[]
    final=[]
    list=os.listdir(directory)
    l=select(list)
    for i in  l:
        final.append(str(directory)+ '/'+ str(i))

    open_folder(final)


def open_folder(list):
    os.mkdir(sys.argv[1])
    count=0
    for i in list:
        with open(i,'rb+')as f:
           data=f.read()
           with open(sys.argv[1]+'/'+str(count)+'.jpg','wb+')as g:
                g.write(data)
                count+=1

        g.close()
        f.close()

def select(list):
    sorted_list=[]
    list_length=len(list)
    for i in range(1,25):
        sorted_list.append(list[random.randrange(0,list_length)])

    return sorted_list

if __name__=='__main__':
    list_func(actress_list[random.randrange(0,len(actress_list))].decode('utf-8'))

