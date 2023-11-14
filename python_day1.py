#integer
print(10)
print(type(10))
print(type(10) == int)

#float
print(4.2)
print(type(4.2))
print(type(4.2) == float)
print(type(4.2) == int)

#input data type selalu string
year = input('tahun berapa?')
print(year)
print(type(year))
#ganti data type jadi int
year = int(year)
print(type(year))

#string
print('Hacktiv8')
print(type('Hactiv8'))
#len() menghitung panjang karakter
print(len('Hacktiv8'))
#index : 0, mengambil karakter 
name = 'fajar ibrah'
indexTerakhir = len(name) - 1 #ambil index terakhir
print(name[0])
print(name[2])
print(name[indexTerakhir])

#boolean => True/False
statusOnline = True
print(statusOnline)
print(type(statusOnline))
print(statusOnline != False)

#Luwy umurnya adalah 4 beratnya 4.5kg status single
name = "Luwy"
age = 4
weight = 4.5
isSingle = True

#variable naming
nama_panggil = 'Fajar'
namaPanggil = 'Fajar'

#array
#list[]
myFruit = ['apple','orange','durian']
print(myFruit[0])
print(myFruit[0][0])
infoCat = ['Luwy', 4, 4.5, True]
#append, menambah isi list
myFruit.append('rambutan')
#remove
myFruit.remove('apple')
#slice, remove with index
myFruit.pop(2)
print(myFruit)
#set, cari unique index, dan hilangkan yang sama


#dictionary{}
infoCat = {
    'name': 'Luwy',
    'age': 4,
    'weight': 4.5,
    'isSingle': True,
    'socialMedia': {
        'IG': 'Lulwy',
        'twitter': 'Lulwy'
    },
    'favFood': ['fish','catnip','tuna']

}
print(infoCat)
print(len(infoCat))
print(infoCat['name'])
print(infoCat['name'][0])
print(infoCat['favFood'])
print(infoCat['favFood'][0])
print(len(infoCat['favFood']))
#add another lable
infoCat['name'] = 'luffy'
infoCat['height'] = 50
print(len(infoCat))
print(infoCat['name'])

#tuple sama seperti list tapi digunakana untuk menyimpan value2 konstan(tidak bisa diubah)

#operator
a = 9
b = 4

total = a + b
print(total)

print(a % b) #modulo/modulus, hasil sisa pembagian a dibagi b
print(a ** b) #pangkat

#comparison -> biasa digunakan untuk conditional, boolean output
a = 40
b = 20

print(a == b) #sama
print(a != b) #tidak sama dengan

#string manipulation
s='foo'
t='bar'
u='baz'

print(s+t)
print(s+t+u)
print(f'{s} {t} {5}')
print(s*4)

# in Operators, mencari string di dalam kalimat

s = 'foo'

print(s in 'That food for us')

print(s in 'That good for us')

#pass reference, variable yang sama dipakai bareng
listNum = [1991, 1998, 1990]
numbers = listNum
numbers[0] = 1967
#paksa copy 
numbers = listNum.copy()
print(numbers)
print(listNum)

#min() dan max()
print(min(listNum))
print(max(listNum))