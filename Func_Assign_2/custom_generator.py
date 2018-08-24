print('FORMAT: END,START,STEP')
end = int(raw_input())
start = int(raw_input())
step = int(raw_input())
global my_list
my_list= []

def cust_gen(end,start=0,step=1):
    num=start
    while num<end:
        yield num
        num += step

for ele in cust_gen(end,start,step):
    my_list.append(ele)
print (my_list)

"""def cust_gen1(start,end):
    num=start
    while num<end:
        yield num
        num +=1
for ele in cust_gen1(3,9):
    print(ele)

def cust_gen2(start,end,step):
    num=start
    while num<end:
        yield num
        num +=step
for ele in cust_gen2(3,9,2):
    print(ele)"""