# python code to retrieve value of code


object1 = { 'a': {'b': {'c':'d'} }}
object2 = { 'x': {'y': {'z':'a'} }}


def getvalue(dict,key1,key2,key3):
    print ((((dict.get(key1)).get(key2)).get(key3)))

getvalue(object1,'a','b','c')

getvalue(object2,'x','y','z')


OUTPUT

d
a
