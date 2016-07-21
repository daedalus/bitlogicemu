# Control circuit
# inputs: OP[0:5]
# outputs: RegDST,ALUSrc,MemtoReg,RegWrite,MemRead,MemWrite,Branch,AluOp1,AluOp2

def control(OP):
	and1 = (OP[5] ^ 1) & (OP[4] ^ 1) & (OP[3] ^ 1)  & (OP[2] ^ 1)  & (OP[1] ^ 1)  & (OP[0] ^ 1) 
	and2 = OP[5] & (OP[4] ^ 1) & (OP[3] ^ 1) & (OP[2] ^ 1) & OP[1] & OP[0]
	and3 = OP[5] & (OP[4] ^ 1) & OP[3] & (OP[2] ^ 1) & OP[1] & OP[0]
	and4 = (OP[5] ^ 1) & (OP[4] ^ 1) & (OP[3] ^ 1) & OP[2] & (OP[1] ^ 1) & (OP[0] ^ 1)
 
	RegDST = and1
	ALUSrc = (and2 | and3)
	MemtoReg = and2
	RegWrite = (and1 | and2)
	MemRead = and2
	MemWrite = and3
	ALUOp1 = and1 
	ALUOp0 = and4	

	return RegDST,ALUSrc,MemtoReg,RegWrite,MemRead,MemWrite,Branch,AluOp1,AluOp2
