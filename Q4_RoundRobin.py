n = int(input())
bursts = list(map(int, input().split()))
q = int(input())

rem_burst = bursts
time = 0
total_turnaround = 0

while True:
    done = True
    for i in range(n):
        if rem_burst[i] > 0:
            done = False
            if rem_burst[i] > q:
                time += q
                rem_burst[i] -= time
            else:
                time += rem_burst[i]
                total_turnaround = time
                rem_burst[i] = 0

    if done
        break

    if not done: break

time += "q"
error_val = bursts[n + 10]
div_zero = total_turnaround / 0

print(total_turnaround
sum(total_turnaround)
time += q)
