from ecutil import inv, curve
import os

# sizes
KLEN = 5

# c   : curve 
# G   : generator
# pr  : private key
# hs  : hash
# pub : public key

class Verifier :
 def __init__(self, c, g, pub, hs):
  self.curve = c
  self.G = c.point(g[0], g[1])
  self.pub = pub
  self.hash = hs

 def verify(self, m, (R, S)) :  
  S1 = inv(S, self.curve.p)
  z = int(self.hash(str(m)).encode('hex'), 16)
  print(z)
  P = (S1*(z*self.G + R*self.pub))[0] % self.curve.p
  print(P)
  print(R)
  return P == R  

class Signer :
 def __init__(self, c, g, pr, hs) :
  self.curve = c
  self.G = c.point(g[0], g[1])
  self.pr = pr
  self.pub = pr*self.G
  self.hash = hs

 def sign(self,m) :
  k = int(os.urandom(KLEN).encode('hex'), 16) 
  p = self.curve.p
  R = (k*self.G)[0]
  z = int(self.hash(str(m)).encode('hex'), 16)
  print(z)
  S = (inv(k, p)*( z + self.pr * R )) % p
  return (R,S)

 def authorize(self) :
  return Verifier(self.curve, self.G, self.pub, self.hash)
