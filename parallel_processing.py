from __future__ import division
#import pandas as pd
import os
#import requests
from lxml import html
#import pandas as pd
import csv
import time
from multiprocessing import Pool,Process, Queue
import multiprocessing
#os.system("rm -f /home/admin/nas/shares/negative_words_temp.txt")
#os.system("cat /home/admin/nas/shares/negative_words_temp.txt >> /home/admin/nas/shares/negative_words.txt")
#os.system("rm -f /home/admin/nas/shares/negative_words_temp.txt")
#os.system("cat /home/admin/nas/shares/negative_words.txt >> /home/admin/nas/shares/negative_words_temp.txt")

positive_words=[]
negative_words=[]
neutral_words=[]
double_negative=[]
synonyms=[]
print("importing negative words")


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

	
positive_words1=[]
positive_words1=[positive_words[i] for i in range(0,int(len(positive_words)/4))]

positive_words2=[]
positive_words2=[positive_words[i] for i in range(int(len(positive_words)/4),int(len(positive_words)/2))]

positive_words3=[]
positive_words3=[positive_words[i] for i in range(int(len(positive_words)/2),int((3*len(positive_words))/4))]

positive_words4=[]
positive_words4=[positive_words[i] for i in range(int((3*(len(positive_words)))/4),len(positive_words))]





def initial(pos,q):
    new_list=[]
    for i in range(len(pos)):
        try:
            for j in range(len(synonyms)):
                for k in range(len(synonyms[j])):
                    if(synonyms[j][k].replace(" ","")==pos[i].replace(" ","")):
                        for z in range(len(synonyms[j])):
                            new_list.append(synonyms[j][z])
                            #new_list1=list(set(new_list))
                        break;
                    else:
                        var=1
            blumer=((i/len(pos))*100)
            print("Doing Positive Words")
            new_list=list(set(new_list))
            print(str(blumer)+' Done....')
            print(len(new_list))
        except KeyboardInterrupt as e:
            print("Waiting.......")
            raw_input()
            pass
    test=[]
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            test.append(new_list[i].replace("\\","").replace('"','').replace("'","").replace("[","").replace("]",""))
            
    test=list(set(test))
    q.put(test)
    #q.put(test)
    #q.put(test)

'''
test_list=[]
for i in range(len(test)):
    for j in range(len(test[i])):
        a=test[i][j].split(",")
        for k in a:
            test_list+=[k.replace("\\","").replace('"','').replace("'","").replace("[","").replace("]","")]

'''
# ########################## uncomment back ################
'''
with open("/home/admin/nas/shares/negative_words.txt","a") as f:
    for i in test:
        f.write(i)
        f.write("\n")
'''
def word_sorter():
    length1=[]
    length1+=[len(list(set(positive_words)))]
    count=0
    while(count<2):
        positive_words=[]
        print("Again importing negative words")
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
            except KeyboardInterrupt as e:
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




startTime = time.time()
#create a Queue to share results
q = Queue()
#create 4 sub-processes to do the work
p1 = Process(target=initial, args=(positive_words1,q))
p1.start()
p2 = Process(target=initial, args=(positive_words2,q))
p2.start()
p3 = Process(target=initial, args=(positive_words3,q))
p3.start()
p4 = Process(target=initial, args=(positive_words4,q))
p4.start()


results = []
print("All Done.... Joining....")
for i in range(4):
	#set block=True to block until we get a result
	results.append(q.get(True))


#mark the end time
endTime = time.time()
#calculate the total time it took to complete the work
workTime =  endTime - startTime


#print results
print "The job took " + str(workTime) + " seconds to complete"
print(len(results))
#print(results)
result=[]
for i in range(len(results)):
	for j in range(len(results[i])):
		result.append(results[i][j])
print(len(result))
result=list(set(result))
#print(result)
print(len(result))


