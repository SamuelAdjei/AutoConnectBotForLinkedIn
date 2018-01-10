'''
Created on Jul 5, 2016

@author: nashit
'''
import random
import time
import csv
import sys

def strTimeProp(start, end, format1, prop):
    stime = time.mktime(time.strptime(start, format1))
    etime = time.mktime(time.strptime(end, format1))    
    
    ptime = stime + prop * (etime - stime)
    
    return time.strftime(format1, time.localtime(ptime))
    
def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)    

def loadDataAsList(fileName):
    data = [];
    with open (fileName) as info:
        dataFile = csv.reader(info)
        for r in dataFile:
            data.append(r)
    return data

def loadDataAsDict(fileName, keyColumn):
    data = {}
    with open (fileName) as info:
        dataFile = csv.reader(info)
        next(dataFile)
        for r in dataFile:
            if r[keyColumn] in data:
                data[r[keyColumn]].append(r)
            else:
                data[r[keyColumn]]=[]
                data[r[keyColumn]].append(r)
            
    return data

if __name__ == '__main__':
    #if (len(sys.argv)>=4):
        #patientFileName=sys.argv[1]
        #drugFileName=sys.argv[2]
        #physFileName=sys.argv[3]
        #planFileName=sys.argv[4]
        #rejectCodeFileName=sys.argv[5]
        #drugOutputFileName=sys.argv[6]
        patientFileName="E:/Astellas/Data/Patient_data.csv"
        drugFileName= "E:/Astellas/Data/ctcodes-drugs.csv"
        physFileName= "E:/Astellas/Data/physician_data.csv"
        planFileName="E:/Astellas/Data/full_plan_data.csv"
        rejectCodeFileName="E:/Astellas/Data/reject_code_data.csv"
        drugOutputFileName="E:/Astellas/Data/drug_claims.csv"
        #print "aaaaaaaa"
        drug_data=loadDataAsList(drugFileName)
        reject_code_data=loadDataAsList(rejectCodeFileName)
        pyhs_data=loadDataAsDict(physFileName,5)
        plan_data=loadDataAsDict(planFileName,6)
        drugCount = len(drug_data)
        rejectCodeCount=len(reject_code_data)
        refillCode=[0,1,2,3,4,5,6,7,8,9,10,11,12,51]
        claimStatus=[0,1,1,1,1,2,2]
        quantity=[15,30,45,60,75,90,120]
        new_to_product=[0,0,0,0,0,0,0,0,0,1]
        
        patient_array = []
        claimID=1
        with open(patientFileName) as patientFile:
            patientRows = csv.reader(patientFile)
            for patientRow in patientRows:
                
                
                rowsPerPatient = random.randint(50, 5000)
                print str(patientRows.line_num) +"/15000 --- " + str(rowsPerPatient) + " records"
                for k in range(0, rowsPerPatient):
                    drugClaim={}
                    drugClaim['patient_id']=int(patientRow[0])
                    drugClaim['claim_id']=claimID
                    
                    drugClaim['drug_code'] =drug_data[random.randint(1, drugCount-1)][0]
                    drugClaim['refill_code']=refillCode[random.randint(0, 13)]
                    drugClaim['claim_status']=claimStatus[random.randint(0, 6)]
                    
                    drugClaim['rx_fill_date'] = randomDate("2015-01-01", "2016-06-30", random.random())
                    if random.randint(0, 8)>5:
                        drugClaim['rx_written_date'] = randomDate("2015-01-01", drugClaim['rx_fill_date'], random.random())
                    else:
                        drugClaim['rx_written_date']=''
                        
                    drugClaim['patient_pay']=random.randint(0, 200)
                    drugClaim['patient_out_of_pocket']=drugClaim['patient_pay']
                    drugClaim['plan_pay']=random.randint(0, 500)
                    drugClaim['quantity']=quantity[random.randint(0, 6)]
                    drugClaim['days_supply']=drugClaim['quantity']
                    drugClaim['days_next_fill']=0
                    drugClaim['new_to_product']=new_to_product[random.randint(0, 9)]
                    
                    physList=pyhs_data[patientRow[1]]
                    physRecNum = random.randint(0, len(physList)-1)
                    drugClaim['physician_id']=physList[physRecNum][0]
                    
                    planList=plan_data[patientRow[1]]
                    planRecNum = random.randint(0, len(planList)-1)
                    drugClaim['plan_id']=planList[planRecNum][0]
                    drugClaim['pharmacy_id']= ("000000"+str(random.randint(0, 100000)))[-6:]
                    
                    if drugClaim['claim_status']==0:
                        drugClaim['reject_code'] =reject_code_data[random.randint(1, rejectCodeCount-1)][0]
                    else:
                        drugClaim['reject_code']=''
                    
                    claimID=claimID+1
                    patient_array.append(drugClaim )
            
        with open(drugOutputFileName, 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=["patient_id","claim_id","drug_code", "refill_code","claim_status","rx_fill_date","rx_written_date","patient_pay","patient_out_of_pocket","plan_pay","quantity","days_supply","days_next_fill","new_to_product","physician_id","plan_id","pharmacy_id","reject_code"])
            dict_writer.writeheader()
            dict_writer.writerows(patient_array)
            output_file.close()
       
    #else:
    #    SystemExit