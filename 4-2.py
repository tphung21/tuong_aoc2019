total = 0
for pw in range(136818, 685979):
    pw = str(pw)
    adj = False
    incr = True
    for i in range(1,len(pw)-2):
        if pw[i]==pw[i+1] and pw[i+1]!=pw[i+2] and pw[i-1]!=pw[i]:
            adj = True
    if pw[len(pw)-2]==pw[len(pw)-1] and pw[len(pw)-3]!=pw[len(pw)-2]:
        adj = True
    if pw[0]==pw[1] and pw[1]!=pw[2]:
        adj = True
    for i in range(len(pw)-1):
        if int(pw[i]) > int(pw[i+1]):
            incr = False
    if adj and incr:
        total += 1
print(total)
