import jieba
path1=r"C:\Users\26051\Desktop\score.txt"
f1=open(path1,'r',encoding='utf-8')
content=f1.read()
words=content.split()
counts={}
for word in words:
  if len(word)==1:#单个字符的分词结果
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(2):
   word,count=items[i]
   print("{}==={}".format(word,count))
