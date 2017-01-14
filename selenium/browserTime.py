import time
import sys,getopt
import subprocess
import csv
import emailmodule
from selenium import webdriver

CONFIG_FILE = "url_list.txt"
NUM_ITERATION = 1
RESULT_FILE='result.csv'

class BrowserTest(object):

    testUrl = ''
    curlTime = 0.0
    endtoendTime = 0.0
    diffTime = 0.0

    def __init__(self, url):
        self.url = url

    def getCurlTime(self):
        return self.curlTime

    def getEndToTime(self):
        return self.endtoendTime

    def getdiffTime(self):
        self.diffTime = self.endtoendTime - self.curlTime
        return self.diffTime

    def ui_check(self, n):
        driver = webdriver.Chrome()
        tot = 0
        for i in range(n):
            start = time.time()
            driver.get(self.url)
            end = time.time()
            tot = tot + (end - start)
        driver.quit()
        avgAccessTime = tot / n
        self.endtoendTime = avgAccessTime
        return avgAccessTime

    def transport_check(self, n):
        tot = 0
        for i in range(n):
            t = float(subprocess.Popen("curl -w \"%{time_total}\" -o /dev/null -s " + '\"' + self.url + '\"', shell=True,
                                       stdout=subprocess.PIPE).stdout.read())
            tot = tot + t
        avgAccessTime = tot / n
        self.curlTime = avgAccessTime
        return avgAccessTime

def main(argv):
    userName = ''
    passWord = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["username=", "pwd="])
    except getopt.GetoptError:
        print 'browserTest.py -i <username> -o <pwd>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'browserTest.py -i <username@gmail.com> -o <pwd>'
            sys.exit()
        elif opt in ("-i", "--username"):
            userName = arg
        elif opt in ("-o", "--pwd"):
            passWord = arg
    print 'UserName is:', userName
    print 'PassWord is:', passWord

    if userName:
        if passWord:
            # Read Data from Config File
            f = open(CONFIG_FILE, 'r')
            if not f:
                printf("Cannot open file: " + CONFIG_FILE)
                sys.exit()
            resultFile=open(RESULT_FILE,'wb')
            # Create CSV File to store Data for Operations
            csvResult=csv.writer(resultFile)
            csvResult.writerow(["URL","Transport Access Time","UI Access Time","Difference","UI Overhead %"])

            # Iterate over each instance of url in Config file
            for line in f:
                line=line.strip()

                # Create BrowserTest Object
                browserTest = BrowserTest(line)
                # Run Test with curl operations time for curl operations
                browserTest.transport_check(10)
                # Run Test by launching Browser and Load Url
                browserTest.ui_check(10)

                # Get time for Curl Operations
                transportTime = browserTest.getCurlTime()
                # Get time for Browser Launch operation
                uiTime = browserTest.getEndToTime()
                # Get diff time for Curl and Browser Test
                uiOverhead = browserTest.getdiffTime()

                # Write Data to csv file
                csvResult.writerow([line,str(transportTime),str(uiTime),str(uiOverhead),str(int(uiOverhead/uiTime*100))])

            emailmodule.sendEmail(userName,passWord)
        else:
            print "Input password please!!"
    else:
        print "Input username please!!"
if __name__ == '__main__':
  main(sys.argv[1:])
