total = 0
for pw in range(136818, 685979):
    pw = str(pw)
    adj = False
    incr = True
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            adj = True
        if int(pw[i]) > int(pw[i+1]):
            incr = False
    if adj and incr:
        total += 1
print(total)
