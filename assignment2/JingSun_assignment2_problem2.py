# Problem 2.
# The semi-empirical mass formula.
# The formula is as below:
# B=a1*A-a2*(A**(2/3))-a3*(Z**2/(A**(1/3)))-a4*(((A-2*Z)**2)/A)-(a5/(A**(1/2)))
# where
# B is the nuclear binding energy, in the unit of MeV
# A is the mass number,
# Z is the atomic number,
# a1=15.67,
# a2=17.23,
# a3=0.75,
# a4=93.2,
# a5
#	=0, if A is odd.
#	=12.0, if A and Z are both even.
#	=-12.0, if A is even and Z is odd.
# The purpose is:
#	1. Binding energy, B
#	2. Binding energy per nucleon, B/A
# 
#
#
# The name of this function is binding_energy.
# The input is A and Z.
# The output is B and B/A.
#
#
#
def binding_energy(Z,A):
	a1=15.67
	a2=17.23
	a3=0.75
	a4=93.2
	if A%2==1:
		a5=0
	elif A%2==0 and Z%2==0:
		a5=12.0
	else:
		a5=-12.0
	B=a1*A-a2*(A**(2/3))-a3*(Z**2/(A**(1/3)))-a4*(((A-2*Z)**2)/A)-(a5/(A**(1/2)))
	return B,B/A
#
#
#
# A=58,Z=28
# B=490.78425241273493, B/A=8.46179745539198
#
# A=59,Z=28
# B=489.31918309296384, B/A=8.43653763953386
#
# A=58,Z=27
# B=485.30934897614435, B/A=8.367402568554214