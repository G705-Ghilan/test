from random import randint as N
from N4Tools.Design import Square
from time import sleep
import os

class test:
	def __init__(self):
		self.size=12
		self.NM=[' ','#','\033[1;34m#\033[0m']
		self.equal=0
		self.LU=[]
		self.NL=3
		self.cols=3
		self.li=[]
	def getList(self):
		return [[[N(0,1)for _ in range(self.size+1)]for __ in range(self.size//2)]for x in range(self.NL)]
	def index(self,li):
		for _ in range(len(li)):
			for __ in range(len(li[_])):
				for ___ in range(len(li[_][__])):
					yield(_,__,___)
	def setindex(self):
		l=[self.li[0]]
		li=self.li[1:]
		for _,__,___ in self.index(l):
			s2=l[_][__][___]
			p=1
			for i in range(len(li)):
				p=1
				s1=li[i][__][___]
				if s1==1:self.LU.append(2)
				if s2==1:self.LU.append(2)
				if s1!=s2:
					p=0
					a=N(0,1)
					aa=N(0,1)
					li[i][__][___]=a
					l[_][__][___]=aa
					if a==aa and a==1:self.LU.append(-4)
			if p==1:
				for i in range(len(li)):
					li[i][__][___]=2
					l[_][__][___]=2
				self.equal+=len(self.li)
		self.li=l+li
	def BOX(self):
		self.li=self.getList()
		self.setindex()
		sq=Square()
		sq.cols=self.cols
		sq.padding=[1,0,1,0]
		print(sq.style([(('\n'.join([''.join([self.NM[_]for _ in __])for __ in self.li[f]])))for f in range(len(self.li))]))
		print(f'[ equal : {self.equal} ] , [ {str(self.equal/sum(self.LU)*100).split(".")[0]} % 100 ]   ')


n=int(input('Enter Num Box:'))
c=int(input('Enter Num Cols:'))
os.system('clear')
while True:
	s=test()
	s.cols=c 
	s.NL=n if n>=2 else 2
	try:s.BOX()
	except:pass
	print('\x1b[H',end='')
	sleep(.3)
#	break
