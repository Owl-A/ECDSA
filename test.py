import hashlib
from ecdsa import Signer, Verifier
from ecutil import curve

c = curve(5,3,9997)
g = c.point(1,3)
pr = 5123
def hasher(m) :
 x = hashlib.sha1()
 x.update(str(m))
 return x.digest()

S = Signer(c, g, pr, hasher)
V = S.authorize()
m = 'hello world'
print(V.verify(m, S.sign(m)))
