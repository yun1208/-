import random
friends_list=["Carol","David","Ann","Bob", "Eve","Grace","Monica","Frank","Heidi","Judy"]
print("我的好朋友有{}个，第一个好朋友是{}，第二个好朋友是{}".format(len(friends_list),friends_list[0],friends_list[1]))
del friends_list[0:2]
print("剩下的好朋友们是{}\n".format(friends_list))
friends_list=["Carol","David","Ann","Bob", "Eve","Grace","Monica","Frank","Heidi","Judy"]
print("当然，如果按名字排序的话，那就是{}了".format(sorted(friends_list)))
bad_guy_number=random.randint(0,len(friends_list))
reason=["没时间","不想去"]
bad_guy_reason=reason[random.randint(0,1)]
bad_guy_name=friends_list.pop(bad_guy_number)
print("但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为{}。".format(bad_guy_name,bad_guy_reason))
print("那我只能把他从我的嘉宾名单中删除咯。现在，能来的就剩下这些{}了".format(friends_list))
others=["坏蛋芸","可爱雨"]
new_friends_list=friends_list+others
print("人数好像有点不够啊，那我再叫些人来吧。对了，把{}和{}叫过来好了，这些的话，就有这些人来了{}。".format(others[0],others[-1],new_friends_list))
