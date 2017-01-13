import time
import sys
import subprocess
import csv
from selenium import webdriver

CONFIG_FILE = "url_list.txt"
NUM_ITERATION = 1
RESULT_FILE='result.csv'

def ui_check(url,n):
    driver = webdriver.Chrome()
    tot=0
    for i in range(n):
        start = time.time()
        driver.get(url)
        end = time.time()
        tot=tot+(end-start)
    driver.quit()
    avgAccessTime=tot/n
    return avgAccessTime

def transport_check(url, n):
    tot=0
    for i in range(n):
        t = float(subprocess.Popen("curl -w \"%{time_total}\" -o /dev/null -s " + '\"' + url + '\"', shell=True,
                               stdout=subprocess.PIPE).stdout.read())
        tot = tot + t
    avgAccessTime=tot/n
    return avgAccessTime

def main():
    f = open(CONFIG_FILE, 'r')
    if not f:
        printf("Cannot open file: " + CONFIG_FILE)
        sys.exit()
    resultFile=open(RESULT_FILE,'wb')
    csvResult=csv.writer(resultFile)
    csvResult.writerow(["URL","Transport Access Time","UI Access Time","Difference","UI Overhead %"])
    for line in f:
        line=line.strip()
        transportTime = transport_check(line,10)
        uiTime=ui_check(line,10)
        uiOverhead=uiTime - transportTime
        csvResult.writerow([line,str(transportTime),str(uiTime),str(uiOverhead),str(int(uiOverhead/uiTime*100))])

if __name__ == '__main__':
  main()
