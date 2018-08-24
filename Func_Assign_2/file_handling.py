from string import ascii_lowercase

my_list = []

f = open("lines.txt",mode='r')
contents = f.readlines()

f.close()

for line in contents:
    my_list.append(len(line))

print(my_list)


#----------------------------------------------------------------------------------------------

d ={}

def char_dict(name):
    with open(name) as f:
        text = f.read().strip()
        for x in ascii_lowercase:
            d[x] = text.count(x)

char_dict('lines.txt')
for key,values in d.items():

    print('\''+key+'\''+':'+ str(values)+',')

