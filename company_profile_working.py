from lxml import html
import requests
import  csv

csv_list=[]
columns=[]
open = open ("/home/nashit93/bhav.csv","r")
f = csv.reader(open)

for column in f:
    if column:
        columns.append(column[0])


#columns=["20MICRONS"]
for coll in range(len(columns)):
	url="https://in.finance.yahoo.com/q/pr?s="+str(columns[coll])+".NS"
	print(url)
	r=requests.get(url)
	text=r.text
	tree = html.fromstring(r.content)
	temp_list = tree.xpath('//table[@class="yfnc_datamodoutline1"]//tr//td//text()')
	temp_list=[temp_list[i] for i in range(len(temp_list)) if temp_list[i] != '\n                                ']
	temp_list=[temp_list[i].replace("\xa0","").replace("N/A","0").replace("\n","").replace("                                             ","").replace(",","") for i in range(len(temp_list))]
	temp_list=[temp_list[i] for i in range(len(temp_list)) if temp_list[i] != '']
	temp_list
	temp_list2=[]
	flag=0
	for i in range(len(temp_list)):
		if(temp_list[i][0].isdigit() and ((temp_list[i][len(temp_list[i])-1]=='M') or (temp_list[i][len(temp_list[i])-1]=='K') or (temp_list[i][len(temp_list[i])-1]=='k'))):
			temp_list2.append(float(temp_list[i].replace("M","").replace("K","").replace("k","")) * 1000000)
		elif(str(temp_list[i])=="Pay"):
			flag=1
			temp_list2.append(temp_list[i])
		elif(temp_list[i]=='0' and flag==1):
			var=1
		else:
			temp_list2.append(temp_list[i])
	column=""
	flag1=0
	final_list=[]
	final_list.append("company , "+str(url.replace("https://in.finance.yahoo.com/q/pr?s=","").replace(".NS","")))
	for i in range(len(temp_list2)):
		if(flag1==0):
			if(i==9):
				column+=" , "+str(temp_list2[i])
				final_list.append(column)
				flag1=1
				column=""
			elif(i%2==0):
				column=""
				column+=str(temp_list2[i])
			else:
				column+=" , "+str(temp_list2[i])
				final_list.append(column)
		else:
			if((len(str(temp_list2[i])) < 50) and str(temp_list2[i])[0].isalpha()):
				column+=str(temp_list2[i])
				#print("in names "+str(temp_list2[i]))
				#final_list.append(column)
				#column=""
			elif(str(temp_list2[i])[0].isdigit() and len(str(temp_list2[i]))>2):
				column+=" , "+str(int(float(temp_list2[i])))
				#print("in salaries "+str(temp_list2[i]))
				final_list.append(column)
				column=""

	csv_list+=[str(f) for f in final_list]
	print(str(coll)+" done ...")
	print(str(float(((coll+1)/(len(columns)))*100)))





lister=[]
tmp_list=[]
for i in range(len(csv_list)):
	if("company " not in csv_list[i]):
		tmp_list.append(csv_list[i])
	else:
		lister.append(tmp_list)
		tmp_list=[]
		tmp_list.append(csv_list[i])

tmp_list=[]
for i in range((len(csv_list)-7),len(csv_list)):
	tmp_list.append(csv_list[i])

lister.append(tmp_list)



thefile = open('/home/nashit93/test.csv', 'w')

for i in lister:
	thefile.write("%s\n" % i)


