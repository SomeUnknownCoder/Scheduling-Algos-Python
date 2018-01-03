processes = [None] + list(range(1, 21))
bt = [None] + list(range(1, 21))
wt = [None] + list(range(1, 21))
tat = [None] + list(range(1, 21))
avwt = 0
avtat = 0
total = 0
n = int(input("Enter number of processes(max. 20):"))

print "Enter Burst Time:"
for i in range(0, n):
    bt[i] = int(input("P" + str(i + 1) + ":"))
    processes[i] = i + 1

for i in range(0, n):
    min = i
    for j in range(i + 1, n):
        if bt[j] < bt[min]:
            min = j
    swap = bt[i]
    bt[i] = bt[min]
    bt[min] = swap

    swap = processes[i]
    processes[i] = processes[min]
    processes[min] = swap

wt[0] = 0
for i in range(n):
    wt[i] = 0
    for j in range(i):
        wt[i] += bt[j]
    total += wt[i]
avwt = float(total) / n
total = 0
for i in range(0, n):
    tat[i] = bt[i] + wt[i]
    total += tat[i]


avtat = float(total) / n

print '\n'
print "Process\t Burst Time\t Waiting Time\t Turnaround Time\t"
for i in range(0, n):
    print str(processes[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t\t" + str(tat[i])
    print '\n'

print "Average Waiting Time:", avwt
print "Average Turnaround Time:", avtat
