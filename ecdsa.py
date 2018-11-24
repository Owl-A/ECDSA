from ecutil import inv, curve
import os

# sizes
KLEN = 20

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

 def verify(self, m, (R, S)):  
  n = self.curve.n
  S1 = inv(S, n)
  z = int(self.hash(str(m)).encode('hex'), 16)
  u1 = (S1*z) % n
  v1 = (S1*R) % n 
  P = (u1*self.G + v1*self.pub)[0] % n 
  return (P-R)%n == 0  

class Signer :
 def __init__(self, c, g, pr, hs) :
  self.curve = c
  self.G = c.point(g[0], g[1])
  self.pr = pr
  self.pub = pr*self.G 
  self.hash = hs

 def sign(self,m) :
  k = int(os.urandom(KLEN).encode('hex'), 16) 
  n = self.curve.n
  R = (k*self.G)[0] % n
  z = int(self.hash(str(m)).encode('hex'), 16)
  S = (inv(k, n)*( z + self.pr * R )) % n
  return (R,S)

 def authorize(self) :
  return Verifier(self.curve, self.G, self.pub, self.hash)
