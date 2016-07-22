import flipflops

# inputs: C,W,D C=Clock,W=Write,D=Data
# outputs: Q
def register1bitAND(C,W,D):
    Q,Qneg = flipflopDMasterSlave((C & W),D)
    return Q
 
# inputs: C,W,D C=Clock,W=Write,D=Data
# outputs: Q
def register1bitOR(C,W,D):
    Q,Qneg = flipflopDMasterSlave((C | (W ^1)),D)
    return Q
    
# inputs: C,W,D C=Clock,WLow=WriteLow,D=Data
# outputs: Q
def register1bitActiveLow(C,Wlow,D):
    Q,Qneg = flipflopDMasterSlave((C | W),D)
    return Q
    
# inputs: C,W,D C=Clock,WLow=Write,D=Data[0:4]
# outputs: Q[0:4]
def register4bit(C,Wlow,D):
    Q = [0,0,0,0]
    W = C | Wlow
    Q[0] = flipflopDMasterSlave(W,D[0])
    Q[1] = flipflopDMasterSlave(W,D[1])
    Q[2] = flipflopDMasterSlave(W,D[2])
    Q[3] = flipflopDMasterSlave(W,D[3])
    return Q

# inputs: C,W,D C=Clock,WLow=Write,D=Data[0:8]
# outputs: Q[0:4]
def register8bit(C,Wlow,D):
    Q = [0,0,0,0,0,0,0,0]
    W = C | Wlow
    Q[0] = flipflopDMasterSlave(W,D[0])
    Q[1] = flipflopDMasterSlave(W,D[1])
    Q[2] = flipflopDMasterSlave(W,D[2])
    Q[3] = flipflopDMasterSlave(W,D[3])
    Q[4] = flipflopDMasterSlave(W,D[4])
    Q[5] = flipflopDMasterSlave(W,D[5])
    Q[6] = flipflopDMasterSlave(W,D[6])
    Q[7] = flipflopDMasterSlave(W,D[7])
    return Q

# inputs: C,W,D C=Clock,WLow=Write,D=Data[0:16]
# outputs: Q[0:4]
def register16bit(C,Wlow,D):
    Q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    W = C | Wlow
    Q[0] = flipflopDMasterSlave(W,D[0])
    Q[1] = flipflopDMasterSlave(W,D[1])
    Q[2] = flipflopDMasterSlave(W,D[2])
    Q[3] = flipflopDMasterSlave(W,D[3])
    Q[4] = flipflopDMasterSlave(W,D[4])
    Q[5] = flipflopDMasterSlave(W,D[5])
    Q[6] = flipflopDMasterSlave(W,D[6])
    Q[7] = flipflopDMasterSlave(W,D[7])
    Q[8] = flipflopDMasterSlave(W,D[8])
    Q[9] = flipflopDMasterSlave(W,D[9])
    Q[10] = flipflopDMasterSlave(W,D[10])
    Q[11] = flipflopDMasterSlave(W,D[11])
    Q[12] = flipflopDMasterSlave(W,D[12])
    Q[13] = flipflopDMasterSlave(W,D[13])
    Q[14] = flipflopDMasterSlave(W,D[14])
    Q[15] = flipflopDMasterSlave(W,D[15])
    return Q

# inputs: C,W,D C=Clock,WLow=Write,D=Data[0:32]
# outputs: Q[0:4]
def register32bit(C,Wlow,D):
    Q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    W = C | Wlow
    Q[0] = flipflopDMasterSlave(W,D[0])
    Q[1] = flipflopDMasterSlave(W,D[1])
    Q[2] = flipflopDMasterSlave(W,D[2])
    Q[3] = flipflopDMasterSlave(W,D[3])
    Q[4] = flipflopDMasterSlave(W,D[4])
    Q[5] = flipflopDMasterSlave(W,D[5])
    Q[6] = flipflopDMasterSlave(W,D[6])
    Q[7] = flipflopDMasterSlave(W,D[7])
    Q[8] = flipflopDMasterSlave(W,D[8])
    Q[9] = flipflopDMasterSlave(W,D[9])
    Q[10] = flipflopDMasterSlave(W,D[10])
    Q[11] = flipflopDMasterSlave(W,D[11])
    Q[12] = flipflopDMasterSlave(W,D[12])
    Q[13] = flipflopDMasterSlave(W,D[13])
    Q[14] = flipflopDMasterSlave(W,D[14])
    Q[15] = flipflopDMasterSlave(W,D[15])
    Q[16] = flipflopDMasterSlave(W,D[16])
    Q[17] = flipflopDMasterSlave(W,D[17])
    Q[18] = flipflopDMasterSlave(W,D[18])
    Q[19] = flipflopDMasterSlave(W,D[19])
    Q[20] = flipflopDMasterSlave(W,D[20])
    Q[21] = flipflopDMasterSlave(W,D[21])
    Q[22] = flipflopDMasterSlave(W,D[22])
    Q[23] = flipflopDMasterSlave(W,D[23])
    Q[24] = flipflopDMasterSlave(W,D[24])
    Q[25] = flipflopDMasterSlave(W,D[25])
    Q[26] = flipflopDMasterSlave(W,D[26])
    Q[27] = flipflopDMasterSlave(W,D[27])
    Q[28] = flipflopDMasterSlave(W,D[28])
    Q[29] = flipflopDMasterSlave(W,D[29])
    Q[30] = flipflopDMasterSlave(W,D[30])
    Q[31] = flipflopDMasterSlave(W,D[31])
    return Q
