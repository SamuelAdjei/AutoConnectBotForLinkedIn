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
    data = []
    with open (fileName) as info:
        dataFile = csv.reader(info)
        for r in dataFile:
            data.append(r)
    return data

def loadDataAsDict(fileName, keyColumn):
    data = {};
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
        #diagnosisFileName=sys.argv[2]
        #physFileName=sys.argv[3]
        #diagnosisOutputFileName=sys.argv[4]
        patientFileName="/home/admin/market_focus/Patient_data.csv"
        diagnosisFileName= "/home/admin/market_focus/CMS32_DESC_LONG_SHORT_DX.csv"
        physFileName= "/home/admin/market_focus/Physician_Data.csv.csv"
        diagnosisOutputFileName="/home/admin/market_focus/daignosis_claims.csv"
        #print "aaaaaaaa"
        diag_data=loadDataAsList(diagnosisFileName)
        pyhs_data=loadDataAsDict(physFileName,5)
        diagCount = len(diag_data)
        claimID=1
        patient_array = []
        
        with open(patientFileName) as patientFile:
            patientRows = csv.reader(patientFile)
            for patientRow in patientRows:
                print str(patientRows.line_num) +"/15000"
                rowsPerPatient = random.randint(10, 1000)
                for k in range(0, rowsPerPatient):
                    random_num = random.randint(1, diagCount-1)
                    diagnosisRecord = diag_data[random_num]
                    physList=pyhs_data[patientRow[1]]
                    physRecNum = random.randint(0, len(physList)-1)
                    
                    patient_array.append({'patient_id': int(patientRow[0]),'claim_id': claimID, 'service_date' : randomDate("2015-01-01", "2016-06-30", random.random()), 'diagnosis_code' : diagnosisRecord[1], 'physician_id':physList[physRecNum][0]})
                    claimID=claimID+1
        
        with open(diagnosisOutputFileName, 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=["patient_id","claim_id","service_date", "diagnosis_code","physician_id"])
            #dict_writer.writeheader()
            dict_writer.writerows(patient_array)
            output_file.close()
       
    #else:
    #    SystemExit