mystring="abcd"
print(mystring[:2])
for x in mystring:
    print(x)

str_1="Rabbi Hasan"
print(str_1[::3])

x="Item One: {y} Item Two:{x}".format(x='dog',y='cat')
print(x)

mylsit=[1,2,3,4]
print(mylsit[-3])

matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
print(first_col)
