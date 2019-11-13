sq1 = [[0,0], [0,2]]
sq2 = [[0,1], [0,0]]
sq3 = [[0,0], [3,0]]
sq4 = [[4,0], [0,0]]
values = [1,2,3,4]
for i in range(2):
    print (sq1[i], " ", sq2[i])
print ("\n")
for i in range(2):
    print (sq3[i], " ", sq4[i])
a = sq1[1][1]; b = sq2[0][1]; c = sq3[1][0]; d = sq4[0][0]
# print (a,b,c,d)
k = 0
while (sq4[1][1] == b or sq4[1][1] == d or sq4[1][1] == c or sq4[1][1] == 0):
    sq4[1][1] = values[k]
    k +=1
k=0
while (sq4[0][1] == b or sq4[0][1] == d or sq4[1][1] == sq4[0][1] or sq4[0][1] == 0):
    sq4[0][1] = values[k]
    k +=1
sq4[1][0] = (10 - (sq4[1][1] + sq4[0][1] + d))
sq2[1][1] = (10 - (sq4[1][1] +sq4[0][1] + b))
sq3[1][1] = (10 - (sq4[1][0] +sq4[1][1] + c))
sq1[1][0] = (10 - (sq2[1][1] +sq1[1][1] + sq3[1][0]))
sq2[1][0] = (10 - (sq1[1][0] +sq1[1][1] + sq2[1][1]))
sq2[0][0] = (10 - (sq2[1][0] +sq4[0][0] + sq4[1][0]))
k=0
while (sq1[0][0] == b or sq1[0][0] == a or sq1[0][0] == sq1[1][0] or sq1[0][0] == sq3[1][0] or sq1[0][0] == 0):
    sq1[0][0] = values[k]
    k +=1
sq1[0][1] = (10 - (sq1[0][0] +sq2[0][0] + sq2[0][1]))
sq1[0][1] = (10 - (sq1[0][0] +sq2[0][0] + sq2[0][1]))
sq3[0][0] = (10 - (sq1[0][0] +sq1[1][0] + sq3[1][0]))
sq3[0][1] = (10 - (sq3[0][0] +sq4[0][0] + sq4[0][1]))
print("\n", "answer is :",  "\n")
for i in range(2):
    print (sq1[i], " ", sq2[i])
print ("\n")
for i in range(2):
    print (sq3[i], " ", sq4[i])
