import hashlib
from ecdsa import Signer, Verifier
from ecutil import curve
p  = int("fffffffffffffffffffffffffffffffeffffac73",16)
n  = int("0100000000000000000001b8fa16dfab9aca16b6b3",16) 
gx = int("3b4c382ce37aa192a4019e763036f4f5dd4d7ebb",16)
gy = int("938cf935318fdced6bc28286531733c3f03c4fee",16)
c = curve(0,7,p,n)
g = c.point(gx,gy)
if(not(g)) :
 print('Massive screwup')
pr = 5123
def hasher(m) :
 x = hashlib.sha1()
 x.update(str(m))
 return x.digest()

S = Signer(c, g, pr, hasher)
V = S.authorize()
m = 'This is the message, please don\'t tamper'
Sn = S.sign(m)
print( "'" + str(m) + "' " + str(Sn))
print(V.verify(m, Sn))
