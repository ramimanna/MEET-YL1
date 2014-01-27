class Integer(object):
	def __init__(self, number,PosBool):
		self.positive = PosBool
		self.variable = number
	def display(self):
		if self.positive:
			print self.variable
		else:
			print "-"+self.variable
	def negative(self):
		if not self.positive:
			self.variable = "-"+self.variable

class NegativeInteger(Integer):
	def __init__(self, number):
		super(NegativeInteger,self).__init__(number, False)

if __name__=="__main__":
	new_number = raw_input("Enter an Integer: ")
	new_positive = raw_input("Enter 'p' for positive & 'n' for negative: ")
	if new_positive == "n":
		new_positive = False
	elif new_positive == "p":
		new_positive = True
	
	# self.positive = True
	# if self.variable <0:
	# 	self.positive = False
	test = Integer(new_number, new_positive)
	test.display()
	negtest = NegativeInteger(new_number)
	negtest.display()



	#print test.positive
# class MySubClass(MySuperClass):
#     def __init__(self):
#         MySuperClass.__init__(self)