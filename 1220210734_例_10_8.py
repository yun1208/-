path1=r"C:\Users\26051\Desktop\students.txt"
student_dict={}

#读取学生名单，并保存在字典student _dict中
#其中key为学生学号，value为学生姓名
f1=open(path1,'r')
for line1 in f1.readlines():
  newline1=line1.rstrip()
  newwords1=newline1.split(",")
  sid,sname=newwords1
  student_dict[sid]=sname
f1.close()

#实现输入学生学号，返回学生姓名
while True:
  newsid=input("请输入学生学号:")
  if newsid in student_dict:
   print("学生姓名为：{}".format(student_dict[newsid]))
  else:
   print("该学号不存在")
