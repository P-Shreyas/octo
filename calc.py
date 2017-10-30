class Cal:
	def __init__(self):
		pass

	def add(self,x,y):
		return x+y

	def sub(self,x,y):
		return x-y

	def mul(self,x,y):
		return x*y

	def div(self,x,y):
		return x/y

cal=Cal()
print("Enter the value of 'A' and 'B'");
a=int(raw_input());
b=int(raw_input());
print(str(a)+"+"+str(b)+"="+str(cal.add(a,b)));
print(str(a)+"-"+str(b)+"="+str(cal.sub(a,b)));

print(str(a)+"*"+str(b)+"="+str(cal.mul(a,b)));
print(str(a)+"/"+str(b)+"="+str(cal.div(a,b)));
