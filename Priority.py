bt = [None] + list(range(1, 21))
priority = [None] + list(range(1, 21))
wt = [None] + list(range(1, 21))
tat = [None] + list(range(1, 21))

n = int(input("Enter the number of processes(max.20):"))
processes = []
for i in range(n):
    processes.insert(i, i + 1)
print "Enter burst time and Priority:"
for i in range(n):
    print "\nP[" + str(i + 1) + "]\n"
    bt[i] = int(input("Burst Time:"))
    priority[i] = int(input("Priority:"))

for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if priority[j] > priority[j + 1]:
            swap = priority[j]
            priority[j] = priority[j + 1]
            priority[j + 1] = swap

            swap = bt[j]
            bt[j] = bt[j + 1]
            bt[j + 1] = swap

            swap = processes[j]
            processes[j] = processes[j + 1]
            processes[j + 1] = swap

for i in range(n):
    wt[i] = 0
    for j in range(i):
        wt[i] = wt[i - 1] + bt[i - 1]

avwt = 0
avtat = 0
for i in range(n):
    tat[i] = wt[i] + bt[i]
    avwt = avwt + wt[i]
    avtat = avtat + tat[i]

avwt = float(avwt) / n
avtat = float(avtat) / n

print '\n'
print "Process\t Burst Time\t Waiting Time\t Turnaround Time\t"
for i in range(0, n):
    print "No:" + str(processes[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t\t" + str(tat[i])
    print '\n'

print "Average Waiting Time:", avwt
print "Average Turnaround Time:", avtat
