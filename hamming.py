data=''
m=0
r=0
encodedList=[]
encodedData=""

def calculateRedundantBitSize():
    for i in range(1,m,1):
        if(2**i >= m+i+1):
            return i;

def createEncodedData():
    j=0
    k=0
    global encodedList
    global encodedData

    encodedList =['0']*(m+r)
    for i in range(1,m+r+1,1):
        if(i==(2**j)):
            j=j+1
        else:
            encodedList[i-1]=data[k]
            k=k+1

    #now calculate parity bits
    for j in range(0,r,1):
        parityBitLoc = 2**j
        for i in range(1,m+r+1,1):
           if((parityBitLoc & i) != 0):
               p=parityBitLoc-1
               encodedList[p]= str(int(encodedList[i-1]) ^ int(encodedList[p]))
               #print(n,p,encodedList[n],encodedList[p])

    for e in encodedList:
        encodedData = encodedData+e

def decodedData(rcvdList):
    chkList =['0']*(m+r)
    postion_err=0
    
    for j in range(0,r,1):
        parityBitLoc = 2**j
        for i in range(1,m+r+1,1):
            if((parityBitLoc & i) != 0):
               p=parityBitLoc-1
               chkList[p] = int(rcvdList[i-1]) ^ int(rcvdList[p]) ^ int(chkList[p])
               #print(i,parityBitLoc,chkList[p])

    for j in range(0,r,1):
        parityBitLoc = 2**j
        postion_err = postion_err+ int(chkList[parityBitLoc-1]) * parityBitLoc

    print(postion_err)
    
if __name__ == "__main__":
    data=input('Enter data string in binary: ')
    m=len(data)
    r=calculateRedundantBitSize()
    createEncodedData()
    print(encodedData)

    #create manual corruption in 1 bit
    loc_err=input('Enter bit to corrupt: ')
    rcvdList=encodedList.copy()
    loc_err_ind=int(loc_err)-1
    if int(rcvdList[loc_err_ind]) == 1:
        rcvdList[loc_err_ind]=0
    else:
        rcvdList[loc_err_ind]=1
    print(rcvdList)
    decodedData(rcvdList)      
