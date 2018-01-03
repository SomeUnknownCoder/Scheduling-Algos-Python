at = [None] + list(range(1, 11))
bt = [None] + list(range(1, 11))
rt = [None] + list(range(1, 11))
wait_time, turnaround_time =  0, 0
counter = 0
n = int(input("Enter Total Process:\t"))
limit = n
for i in range(0, n):
    print "\nEnter Details of Process\n" + str(i + 1)
    at[i] = int(input("Arrival Time:\t"))
    bt[i] = int(input("Burst Time:\t"))
    rt[i] = bt[i]

time_quantum = int(input("\nEnter Time Quantum :\t"))
print "\nProcess ID\t\tBurst Time\t Turnaround Time\t Waiting Time\n"
i = 0
total = 0
while limit is not 0:
    if time_quantum >= rt[i] > 0:
        total += rt[i]
        rt[i] = 0
        counter = 1
    elif rt[i] > 0:
        rt[i] -= time_quantum
        total += time_quantum
    if rt[i] == 0 and counter == 1:
        limit -= 1
        print "\nP:\t\t" + str(i + 1) + "|\t\t" + str(total - at[i]) + "\t\t\t" + str(total - at[i] - bt[i])
        wait_time += total - at[i] - bt[i]
        turnaround_time += total - at[i]
        counter = 0
    if i == n - 1:
        i = 0
    elif at[i + 1] <= total:
        i += 1
    else:
        i = 0

print "Average Waiting Time:" + str(float(wait_time) / n)
print "Average TurnAround Time:" + str(float(turnaround_time) / n)
