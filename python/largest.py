#Write a program that outputs the top n elements from a list.
#Example:
#largest(2, [7,6,5,4,3,2,1])=> [6,7]
def largest(n,xs):
  """Find the n highest elements in a list"""
  
  l = []
  
  for i in range(n):
      m = max(xs)
      l.append(m)
      xs.remove(m)
      
  l = sorted(l)
  return l
