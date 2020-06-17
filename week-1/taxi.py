out_file = open("output.txt", "w")

with open("input.txt", "r") as file:
    taxis = file.read().split(" ")
    taxis[-1] = taxis[-1][:-1]
for i in range(len(taxis)):
    taxis[i] = int(taxis[i])


def mid_num(arr):
    return sum(arr) / len(arr)


mid_number = mid_num(taxis)
if mid_number % 1 != 0:
    out_file.write("IMPOSSIBLE")
    out_file.close()
    exit()



ans = 0
for taxi in taxis:
    if taxi > mid_number:
        ans += taxi - mid_number
out_file.write(str(int(ans)))
out_file.close()
