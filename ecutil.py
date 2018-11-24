def inv(x, p) :
 u, v = __inv(x,p)
 if ( u == 0 and v == 0) :
  return 0
 else :
  return u%p

def __inv(x, p) :
 if x%p == 0 :
  if p == 1 :
   return (0,1)
  else :
   return (0,0)
 else :
  u1,v1 = __inv(p, x%p)
  return (v1, u1 - (x/p)*v1)

class curve:
 def __init__(self, a, b, p, n) :
  self.a = a
  self.b = b
  self.p = p
  self.n = n

 class p_point :
  def __init__(self, x, y, i, a, b, p) :
   self.x = x
   self.y = y
   self.a = a
   self.b = b
   self.p = p
   self.inf = i
 
  def __getitem__(self, value) :
   if(type(value) != int) :
    raise Exception('expected integer index, __getitem__()')
    return False
   if value == 0 :
    return self.x
   elif value == 1:
    return self.y
   else : 
    raise Exception('index out of bounds')
    return False
   
  def __str__(self) :
   if self.inf :
    return 'Inf'
   else :
    return 'point ( ' + str(self.x) + ', ' + str(self.y) +') mod ' + str(self.p)
 
  def __repr__(self) :
   if self.inf :
    return 'Inf'
   else :
    return 'point ( ' + str(self.x) + ', ' + str(self.y) +') mod ' + str(self.p)
 
  def __add__(self, p) :
   if(self.a != p.a or self.b != p.b or self.p != p.p) :
    raise Exception('add failed, points are on different elliptic curves')
    return False
   
   if self.inf :
    if p.inf :
     return curve.p_point(0,1,True,p.a,p.b,p.p)
    else :
     return curve.p_point(p.x,p.y,False,p.a,p.b,p.p)
   else :
    if p.inf :
     return curve.p_point(self.x,self.y,False,p.a,p.b,p.p)
    else : 
     if self.x != p.x:
      L = ((self.y - p.y) * (inv((self.x - p.x) % p.p, p.p)))% p.p
     else :
      if self.y == p.y :
       L = (3*self.x**2 + self.a) * inv(2*self.y, self.p)
      else :
       return curve.p_point(0,1,True,p.a,p.b,p.p)
   
   x = L**2 - self.x - p.x   
   y = L*(p.x - x) - p.y
   return curve.p_point(x % p.p,y % p.p,False,p.a,p.b,p.p)

  def __rmul__(self, k) :
   if type(k) != int :
    k = int(k)

   # might lead to side-channels ? 
   p = self
   acc = curve.p_point(0,1,True,p.a,p.b,p.p)
   while(k > 0) :
    if k%2 == 1 : 
     acc = acc + p
    p = p + p
    k = k>>1
     
   return acc
 
 def __mul__(self,p) :
  return __rmul__(self,p)

 def point(self, x, y) :
  if(0 == (x**3 + self.a*x + self.b - y**2) % self.p) :
   return self.p_point(x % self.p, y % self.p, False, self.a, self.b, self.p) 
  else :
   return False

 def __str__(self) :
  return '<elliptic curve with a = ' + str(self.a) + ', b = ' + str(self.b) + ', p = ' + str(self.p) + '>'

 def __repr__(self) :
  return '<elliptic curve with a = ' + str(self.a) + ', b = ' + str(self.b) + ', p = ' + str(self.p) + '>'

