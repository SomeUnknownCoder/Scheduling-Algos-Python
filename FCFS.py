bt = [None] + list(range(1, 21))
wt = [None] + list(range(1, 21))
tat = [None] + list(range(1, 21))
avwt = 0
avtat = 0
n = 0

n = int(input("Enter total number of processes(max.20):"))
for i in range(n):
    bt[i] = int(input("Enter burst time for processes:"))

# Calculating waiting time
for i in range(n):
    wt[i] = 0
    for j in range(i):
        wt[i] += bt[j]

print '\nProcess\t\tBurst-Time\t\tWaiting Time\t\tTurnAround-Time'

# Calculating TurnAround Time
for i in range(n):
    tat[i] = bt[i] + wt[i]
    avtat = avtat + tat[i]
    avwt = avwt + wt[i]
    print str(i+1)+"\t\t\t\t"+str(bt[i])+"\t\t\t\t"+str(wt[i])+"\t\t\t\t"+str(tat[i])
    print '\n'
avtat = float(avtat)/n
avwt = float(avwt)/n
print "Average Waiting Time:", avwt
print "Average Turnaround Time:", avtat
