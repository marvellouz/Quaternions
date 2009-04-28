from math import sqrt
class Quaternion:
	def __init__(self, *args):
		if len(args)==0:
			self.e=self.i=self.j=self.k=0
		if len(args)==1:
			if type(args[0])==type(self):
				self.e=args[0].e
				self.i=args[0].i
				self.j=args[0].j
				self.k=args[0].k
			else:
				if (isinstance(args[0],(int, float))):
					self.e=args[0]
					self.i=self.j=self.k=0
				else:
					args=args[0]
		if len(args)==4:
			self.e=args[0]
			self.i=args[1]
			self.j=args[2]
			self.k=args[3]
		if len(args)==2:
			self.e=args[0].real
			self.i=args[0].imag
			self.j=args[1].real
			self.k=args[1].imag
		self.scalar=self.e
		self.all=[self.e, self.i, self.j, self.k]
	def vector(self):
                return Quaternion(0, self.i, self.j, self.k)
	vector=property(vector)
	def __getitem__(self,i):
		if not (i in range(0,4)):
			raise IndexError
		return self.all[i]
	def __setitem__(self, key, item): raise TypeError
	def __setattr__(self,name,value):
		if  name in self.__dict__.keys():
			raise TypeError
		self.__dict__[name]=value
	def __delattr__(self,name):
		raise TypeError
	def __eq__(self, other):
		if type(other)!=type(self):
			other=Quaternion(other)
		return (self.e==other.e and self.i==other.i and self.j==other.j and self.k==other.k)
	def __nq__(self, other):
		return not self==other
	def __add__(self, other):
		if (isinstance(other,(int, float))):
			other=(Quaternion(other))
		return Quaternion(self.e+other.e, self.i+other.i, self.j+other.j, self.k+other.k)
	def __radd__(self, other):
		return Quaternion(Quaternion(other)+self)
	def __neg__(self):
		return Quaternion(-1*self.e, -1*self.i, -1*self.j, -1*self.k)
	def __sub__(self, other):
		return self+-other
	def __mul__(self, other):
		if (isinstance(other,(int, float))):
			return Quaternion(self.e*other, self.i*other, self.j*other, self.k*other)
		else:
			qe=self.e*other.e-self.i*other.i-self.j*other.j-self.k*other.k
			qi=self.e*other.i+self.i*other.e+self.j*other.k-self.k*other.j
			qj=self.e*other.j-self.i*other.k+self.j*other.e+self.k*other.i
			qk=self.i*other.k+self.i*other.j-self.j*other.i+self.k*other.e
			return Quaternion(qe, qi, qj, qk)
	def __truermul__(self, other):
		return Quaternion(self.e*other, self.i*other, self.j*other, self.k*other)
	def __truediv__(self, other):
		if other!=0:
			return Quaternion(self.e/other, self.i/other, self.j/other, self.k/other)
	__div__=__truediv__
	def __invert__(self):
		return Quaternion(self.e, -self.i, -self.j, -self.k)
	def __pow__(self, other):
		if other==1:
			return self
		return self*self**(other-1)
	def __nonzero__(self):
		return self.e==self.i==self.j==self.k==0
	def tuple(self):
		return tuple(self.all)
	def __str__(self):
		pos_signs=[self[i]>=0 for i in range(4)]
		x=[]
		for i in pos_signs:
			if i==False:
				x+=('-')
			else: 
				x+=('+')
		if x[0]=="-":
			return (x[0]+str(abs(self.e))+x[1]+str(abs(self.i))+'i'+x[2]+str(abs(self.j))+'j'+x[3]+str(abs(self.k))+'k')
		else:
			return (str(abs(self.e))+x[1]+str(abs(self.i))+'i'+x[2]+str(abs(self.j))+'j'+x[3]+str(abs(self.k))+'k')
	def __repr__(self):
		return 'Quaternion('+str(self.e)+', '+str(self.i)+', '+str(self.j)+', '+str(self.k)+')'
	def reciprocal(self):
		return ~self/((sqrt((self.e)**2+(self.i)**2+(self.j)**2+(self.k)**2))**2)
	def __abs__(self):
		return sqrt((self.e)**2+(self.i)**2+(self.j)**2+(self.k)**2)
	def unit(self):
		if self!=Quaternion(0):
			return self/abs(self)
		else:
			raise ZeroDivisionError
	def __hash__(self):
		return self.__repr__().__hash__()



Quaternion.e=Quaternion(1,0,0,0)
Quaternion.i=Quaternion(0,1,0,0)
Quaternion.j=Quaternion(0,0,1,0)
Quaternion.k=Quaternion(0,0,0,1)

