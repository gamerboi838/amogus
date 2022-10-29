class CSP_crypt:	
	def __init__(self,str):
		p = str.split()
		self.p1=p[0]
		self.p2=p[2]
		self.p3=p[4]
		self.opr = p[1]
		self.state = []		
		self.solved = False		
		for q in self.p1:
			if(not(q in self.state)):
				self.state.append(q)				
		for q in self.p2:
			if(not(q in self.state)):
				self.state.append(q)				
		for q in self.p3:
			if(not(q in self.state)):
				self.state.append(q)
		for i in range(10-len(self.state)):
			self.state.append('x')	
	def display(self):
		print("Line 1 : ", self.p1)
		print("Line 2 : ", self.p2)
		print("Line 3 : ", self.p3)
		print("Operation : ", self.opr)
		print("State : ", self.state)
		print("Solved : ", self.solved)	
	def display_ans(self):
		for i in self.state:
			if(not(i == 'x')):
				print(i," - ",self.state.index(i))	
	def apply_constraints(self,depth):
		if((len(self.p3) > len(self.p1)) and (len(self.p3) > len(self.p2))):
			if(self.state[0] == self.p3[0]):
				return True
			if(self.state[1] == self.p3[0]):
				return True
			elif(depth < 2):
				return True
		else:
			return True		
		return False		
	def get_number(self,p):
		num = 0
		for q in p:
			num = num*10
			num = num + self.state.index(q)		
		return num	
	def solve(self):
		num1 = self.get_number(self.p1)
		num2 = self.get_number(self.p2)
		num3 = self.get_number(self.p3)		
		if(self.opr == '+'):
			ans = num1 + num2
		elif(self.opr == '-'):
			ans = num1 - num2
		elif(self.opr == '*'):
			ans = num1 * num2
		elif(self.opr == '/'):
			ans = num1 / num2		
		#print("ans = ",ans)
		if(ans == num3):
			print("ans = ",ans)
			print("num1 = ",num1)
			print("num2 = ",num2)
			print("num3 = ",num3)
			self.solved = True
	
	def expand(self,l,r,depth):		
		self.solve()		
		if(self.solved == True):
			return
		elif(l == r):
			return
		else:
			for i in range(l,r+1):
				self.state[l],self.state[i]  = self.state[i],self.state[l]
				if(self.apply_constraints(depth)):
					depth = depth + 1
					self.expand(l+1,r,depth)
					depth = depth - 1 
				if(self.solved == True):
					return
				self.state[i],self.state[l]  = self.state[l],self.state[i]

if(__name__=="__main__"):	
	str = input("Enter the problem : ")
	c_csp = CSP_crypt(str)	
	c_csp.display()	
	c_csp.expand(0,9,0)	
	c_csp.display()	
	if(c_csp.solved == True):
		c_csp.display_ans()