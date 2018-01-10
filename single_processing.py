from __future__ import division
#import pandas as pd
import os
#import requests
from lxml import html
#import pandas as pd
import csv
import time
#os.system("rm -f /home/admin/nas/shares/positive_words.txt")
#os.system("cat /home/admin/nas/shares/positive_words.txt >> /home/admin/nas/shares/positive_words.txt")
#os.system("rm -f /home/admin/nas/shares/negative_words_temp.txt")
#os.system("cat /home/admin/nas/shares/negative_words.txt >> /home/admin/nas/shares/negative_words_temp.txt")

positive_words=[]
negative_words=[]
neutral_words=[]
double_negative=[]
synonyms=[]
print("importing positive words")


with open('/home/admin/nas/shares/positive_words.txt', 'r') as f:
    for i in f.readlines():
        positive_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))

print(str(len(positive_words))+" Imported...")
positive_words=list(set(positive_words))


'''
print("Importing Negative Words")

with open('/home/admin/nas/shares/negative_words.txt', 'r') as f:
    for i in f.readlines():
        negative_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))


print(str(len(negative_words))+" Imported...")
negative_words=list(set(negative_words))
print("Importing Neutral Words")

with open('/home/admin/nas/shares/neutral_words.txt', 'r') as f:
    for i in f.readlines():
        neutral_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))

print(str(len(neutral_words))+" Imported...")
print("Importing Duoble Negative Words")
neutral_words=list(set(neutral_words))
with open('/home/admin/nas/shares/double_negative.txt', 'r') as f:
    for i in f.readlines():
        double_negative.append(i.replace("\r\n","").replace("\n","").replace("\r",""))

print(str(len(double_negative))+" Imported...")
double_negative=list(set(double_negative))
'''

print("Importing Synonyms Words")

with open('/home/admin/nas/shares/synonyms.txt') as f:
    for i in f.readlines():
        l_name=i.strip().split(',')
        synonyms+=[l_name]

print(str(len(synonyms))+" Imported...")



'''
new_list=[]
temp_list=[]
for i in range(len(synonyms)):
    for j in range(len(synonyms[i])):
        temp_list.append(synonyms[i][j])

len(temp_list)
temp_list=list(set(temp_list))
len(temp_list)
print(len(positive_words))
'''
startTime = time.time()
new_list=[]
for i in range(len(positive_words)):
    try:
        for j in range(len(synonyms)):
            for k in range(len(synonyms[j])):
                if(synonyms[j][k].replace(" ","")==positive_words[i].replace(" ","")):
                    for z in range(len(synonyms[j])):
                        new_list.append(synonyms[j][z])
                        #new_list1=list(set(new_list))
                    break;
                else:
                    var=1
        blumer=((i/len(positive_words))*100)
        print("Doing Positive Words")
        new_list=list(set(new_list))
        print(str(blumer)+' Done....')
        print(len(new_list))
    except KeyboardInterrupt, SystemExit:
        print("Waiting.......")
        raw_input()
        pass


endTime = time.time()
#calculate the total time it took to complete the work
workTime =  endTime - startTime
#print results
print "The job took " + str(workTime) + " seconds to complete"

test=[]
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        test.append(new_list[i].replace("\\","").replace('"','').replace("'","").replace("[","").replace("]",""))

test=list(set(test))


'''
test_list=[]
for i in range(len(test)):
    for j in range(len(test[i])):
        a=test[i][j].split(",")
        for k in a:
            test_list+=[k.replace("\\","").replace('"','').replace("'","").replace("[","").replace("]","")]

'''


with open("/home/admin/nas/shares/positive_words.txt","a") as f:
    for i in test:
        f.write(i)
        f.write("\n")

length1=[]
length1+=[len(list(set(positive_words)))]
count=0

'''
while(count<2):
    positive_words=[]
    print("Again importing positive words")
    with open('/home/admin/nas/shares/positive_words.txt', 'r') as f:
        for i in f.readlines():
            positive_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))
    print(str(len(positive_words))+" Imported again...")
    positive_words=list(set(positive_words))
    new_list=[]
    len_positive_words=len(positive_words)
    len_synonyms=len(synonyms)
    for i in range(0,len_positive_words):
        try:
            for j in range(0,len_synonyms):
                for k in range(len(synonyms[j])):
                    if(synonyms[j][k].replace(" ","")==positive_words[i].replace(" ","")):
                        for z in range(len(synonyms[j])):
                            new_list.append(synonyms[j][z])
                            #new_list1=list(set(new_list))
                        break;
                    else:
                        var=1
            blumer=((i/len_positive_words)*100)
            print("Doing Positive Words")
            new_list=list(set(new_list))
            print("Doing "+str(count+1)+" Time..")
            print(str(blumer)+' Done....')
            print(len(new_list))
        except KeyboardInterrupt, SystemExit:
            print("Waiting.......")
            raw_input()
            pass
    test=[]
    for i in range(len(new_list)):
        test.append(new_list[i].replace("\\","").replace('"','').replace("'","").replace("[","").replace("]",""))
    test=list(set(test))
    with open("/home/admin/nas/shares/positive_words.txt","a") as f:
        for i in test:
            f.write(i)
            f.write("\n")
    count=count+1
    with open('/home/admin/nas/shares/positive_words.txt', 'r') as f:
        for i in f.readlines():
            positive_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))
    length1+=[len(list(set(positive_words)))]

'''
'''
antonyms=[]
with open('/home/admin/nas/shares/antonyms.txt', 'r') as f:
    for i in f.readlines():
        antonyms.append(i.replace("\r\n","").replace("\n","").replace("\r",""))



anton=[]
for i in range(len(antonyms)):
  a=antonyms[i].split(" : ")
  anton+=[a]


positive_words=[]
with open('/home/admin/nas/shares/positive_words.txt', 'r') as f:
    for i in f.readlines():
        positive_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))

anton_list=[]
for i in range(len(positive_words)):
    for j in range(len(anton)):
        if(positive_words[i].replace(" ","")==anton[j][0].replace(" ","")):
            anton_list+=[anton[j][1]]
    print(str(i)+"done")

anton_list_final=[]
temp1=[]
for i in range(len(anton_list)):
    temp1=anton_list[i].split(",")
    anton_list_final+=temp1

with open("/home/admin/nas/shares/negative_words_temp.txt","a") as f:
    for i in test:
        f.write(i)
        f.write("\n")


os.system("sed -i '/^\s*$/d' /home/admin/nas/shares/negative_words_temp.txt")

synonyms=[]
with open('/home/admin/nas/shares/synonyms.txt') as f:
    for i in f.readlines():
        l_name=i.strip().split(',')
        synonyms+=[l_name]

print(str(len(synonyms))+" Imported...")

negative_words=[]
with open('/home/admin/nas/shares/negative_words_temp.txt') as f:
        for i in f.readlines():
            negative_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))


new_list=[]
for i in range(len(negative_words)):
    try:
        for j in range(len(synonyms)):
            for k in range(len(synonyms[j])):
                if(synonyms[j][k].replace(" ","")==negative_words[i].replace(" ","")):
                    new_list+=[synonyms[j]]
                else:
                    var=1
        blumer=((i/len(negative_words))*100)
        print("Doing Negative Words")
        print(str(blumer)+' Done....')
        print(len(new_list))
    except KeyboardInterrupt, SystemExit:
        print("Waiting.......")
        raw_input()
        pass

test=[]
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        test.append(new_list[i][j].replace("\\","").replace('"','').replace("'","").replace("[","").replace("]",""))

test=list(set(test))



with open("/home/admin/nas/shares/negative_words_temp.txt","a") as f:
    for i in test:
        f.write(i)
        f.write("\n")

length1=[]
length1+=[len(list(set(negative_words)))]

count=0
while(count<2):
    negative_words=[]
    print("Again importing negative words")
    with open('/home/admin/nas/shares/negative_words_temp.txt', 'r') as f:
        for i in f.readlines():
            negative_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))
    print(str(len(negative_words))+" Imported again...")
    negative_words=list(set(negative_words))
    new_list=[]
    len_negative_words=len(negative_words)
    len_synonyms=len(synonyms)
    for i in range(0,len_negative_words):
        try:
            for j in range(0,len_synonyms):
                for k in range(len(synonyms[j])):
                    if(synonyms[j][k].replace(" ","")==negative_words[i].replace(" ","")):
                        new_list+=[synonyms[j]]
                    else:
                        var=1
            blumer=((i/len_negative_words)*100)
            print("Doing negative Words")
            print("Doing "+str(count+1)+" Time..")
            print(str(blumer)+' Done....')
            print(len(new_list))
        except KeyboardInterrupt, SystemExit:
            print("Waiting.......")
            raw_input()
            pass
    test=[]
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            test.append(new_list[i][j].replace("\\","").replace('"','').replace("'","").replace("[","").replace("]",""))
    test=list(set(test))
    with open("/home/admin/nas/shares/negative_words_temp.txt","a") as f:
        for i in test:
            f.write(i)
            f.write("\n")
    count=count+1
    with open('/home/admin/nas/shares/negative_words_temp.txt', 'r') as f:
        for i in f.readlines():
            negative_words.append(i.replace("\r\n","").replace("\n","").replace("\r",""))
    length1+=[len(list(set(negative_words)))]

'''
