'''
Isaiah Andre Pabillon
BSCS-2
2018-5769

Algorithm(Do Better):

    Combining recursion and iteration algorithm to produce "Andre" algorithm

    1) Define a function that has 1 non-default(fib) and 3 default(kawnter,lead and tail) parameters

    2) The after every iteration, plug in the sum of the lead and tail in the place of a new lead
       And plug in the lead as the new tail for the next recursive iteration

    3) If the counter reaches the non default parameter, return the lead as the final term


'''
import time
import matplotlib.pyplot
def fib_1(fib):
    if fib<=1:
        return fib
    else:
        return fib_1(fib-1)+fib_1(fib-2)


def fib_2(fib):
    lead=1
    tail=0
    newlead=1
    for i in range(fib-1):
        newlead=lead+tail
        tail=lead
        lead=newlead
    return newlead

def fib_3(fib,kawnter=1,lead=1,tail=0):
    if kawnter>=fib:
        return lead
    return fib_3(fib,kawnter+1,lead+tail,lead)
    #print(fib,fib1)

fib_times=[[],[],[]]
xaxis=[]
#print(fib_3())
for x in range(30):
    x+=1
    start=time.time()
    fib_1(x)
    fib_times[0].append(time.time()-start)
    #print(fib_times)
    start=time.time()
    fib_2(x)
    fib_times[1].append(time.time()-start)
    #print(fib_times)
    start=time.time()
    fib_3(x)
    fib_times[2].append(time.time()-start)
    xaxis.append(x)
    #print(fib_times)

matplotlib.pyplot.plot(xaxis, fib_times[0])
matplotlib.pyplot.plot(xaxis, fib_times[1])
matplotlib.pyplot.plot(xaxis, fib_times[2])
matplotlib.pyplot.xlabel('Terms')
matplotlib.pyplot.ylabel('Time')
matplotlib.pyplot.title('Time to produce a term in a fibbonaci sequence')
matplotlib.pyplot.show()
#print(fib_times[0][-1])
'''
print(fib_1(5))
print(1+1+2+3+5)
print(1024+512+256+128+64+16)
print(64)
print(fib_2(5))
print(fib_3(5))
'''
