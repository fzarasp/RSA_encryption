import random
def Prime(start , end):
    ps = []
    for i in range(start, end+1):
      if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            ps.append(i)
    return ps

def E(phi , n):
    es = []
    for i in range(2 , phi):
        if i%phi and i%n:
            #return i
            es.append(i)
    return es
def D(e , phi):
    d = 2
    #print(d)
    while True:
        if ((d *e)%phi) == 1 and d != e:
            return d
        if d > 100000:
            return False
        d = d + 1
        #print(d)


def Code():
    p = random.choice(Prime(1, random.randint(5,50)))
    while True:
        q = random.choice(Prime(2, random.randint(5,50)))
        if p != q:
            break

    n = p*q
    phi = (p - 1) * (q - 1)
    #e = random.choice(E(phi , n))
    echoice = Prime(1 , phi - 1)
    if len(echoice) == 0:
        return False
    e = random.choice(echoice)
#    e = E(phi , n)
#    e = 5
    #print(p , q , n , phi , e)
    k = random.randint(1,10)
    d = D(e , phi)
    if not d:
        return False
    #print(p , q , n , phi , e , k)
    key = {'public':(e ,n), 'private':(d, n)}
    #print("n is "+str(n)+ ", Public key is "+ str(e) + ", and the Private key is "+ str(d))
    return key


def Encoding(publickey , min):
    message = list(min)
    n = publickey[1]
    e = publickey[0]
    #print(message)
    outm = ''
    for c in message:
    #    print(c,chr((pow(ord(c),e))%n))
        outm = outm + chr((pow(ord(c),e))%n)
    return outm

def Decoding(privatekey , min):
    message = list(min)
    #print(message)
    n = privatekey[1]
    d = privatekey[0]
    outm = ''
    for c in message:
    #    print(c,chr((pow(ord(c),d))%n))
        outm = outm + chr((pow(ord(c),d))%n)
    return outm



def Keys():
    m = 'This is a test'
    me = ''
    while me != m:
        while True:
            key0 = Code()
            if key0:
                break
        keypu = key0['public']
        keypr = key0['private']
        #print(keypu , keypr)
        md = Encoding(keypu , m)
        me = Decoding(keypr , md)
        if md == me:
            me = ''
    return key0

#print('message: ' , m)
#print('decoded: ', md)
#print('encoded: ' ,me)
