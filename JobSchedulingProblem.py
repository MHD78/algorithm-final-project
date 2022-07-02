jobsCount = int(input("number of jobs : "))
jobs = [("job"+str(x),int(input("job"+str(x)+" : "))) for x in range(1,jobsCount+1)]

def sortJobs(jobTuple):
    lst = len(jobTuple)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (jobTuple[j][1] > jobTuple[j + 1][1]):
                temp = jobTuple[j]
                jobTuple[j]= jobTuple[j + 1]
                jobTuple[j + 1]= temp
    return jobTuple

def jobScheduling(jobs):
    sortedJobs = sortJobs(jobs)
    print("optimal jobs scheduling order : ",sortedJobs)
    times = [x[1] for x in sortedJobs]
    optimalTime = 0
        
    for i in range(len(times)+1):
        optimalTime += sum(times[:i])

    print("optimal time : " ,optimalTime)



# jobScheduling([("job1",1),("job2",4),("job3",2),("job4",6),("job5",2),("job6",13),("job7",7),("job8",8)])
jobScheduling(jobs)