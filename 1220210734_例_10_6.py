path1=r"C:\Users\26051\Desktop\lemon.txt"
f1=open(path1,'r')
for line1 in f1.readlines():
  newline1=line1.rstrip()
  print(newline1)
f1.close()
