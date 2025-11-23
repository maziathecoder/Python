import random
import time
def getRandomDate(startDate,endDate):
    print("printing random date between ",startDate,"and ",endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%y"
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strftime(startDate,dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print("randomDate = ",getRandomDate("1/1/2016","12/12/2018"))