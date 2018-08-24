seq = [n for n in range(0,50,2)]

def f1(seq):
   global my_list
   my_list= [i*2 for i in seq]
   return my_list

def f2(seq):
   global my_list
   my_list= [i*5 for i in seq]
   return my_list

def Cus_map(f1,seq):
    result=f1(seq)
    return result

out = Cus_map(f1,seq)
print(out)


#using inbuilt function

#new_list=list(map(f1,seq))
#print(new_list)