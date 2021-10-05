import time

i = 1
while i <20:
  b=(19-i)*"--" 
  c=(0+i)*"A"
  d=c+b+c  
  print(d)
  time.sleep(0.05)
  i += 1