import flipflops

# inputs: C,W,D C=Clock,W=Write,D=Data
# outputs: Q
def register1bitAND(C,W,D):
    Q,Qneg = flipflopD((C & W),D)
    return Q
 
# inputs: C,W,D C=Clock,W=Write,D=Data
# outputs: Q
def register1bitOR(C,W,D):
    Q,Qneg = flipflopD((C | (W ^1)),D)
    return Q
    
# inputs: C,W,D C=Clock,WLow=WriteLow,D=Data
# outputs: Q
def register1bitActiveLow(C,Wlow,D):
    Q,Qneg = flipflopD((C | W),D)
    return Q
    
# inputs: C,W,D C=Clock,WLow=Write,D=Data[0:4]
# outputs: Q[0:4]
def register4bit(C,Wlow,D[0:4]):
    Q = [0,0,0,0]
    W = C | Wlow
    Q[0] = flipflopD(W,D[0])
    Q[1] = flipflopD(W,D[1])
    Q[2] = flipflopD(W,D[2])
    Q[3] = flipflopD(W,D[3])
    return Q
