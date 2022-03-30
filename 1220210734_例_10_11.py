path1 = r"C:\Users\26051\Desktop\lemon.txt"
f1 = open(path1,"r")
content = f1.read()#读取文件内容,返回-个字符串
content = content.lower()#将字符串中所有的字母小写
for ch in[',',':', '.']:
     content = content.replace(ch," ")#将文本中特殊字 符替换为空格

words = content.split() #不加参数，默认参数为按照空格和换行符进行分割
counts = {}

#计数
for word in words:
   counts[word] = counts.get(word,0) + 1

#排序
items=list(counts.items())#将字典元素转换为列表
items.sort(key=lambda x:x[1],reverse= True) #按照元素的第1列进行永久降序排列
for i in range(10):
   word,count = items[i]
   print ("{}==={}".format(word,count))
