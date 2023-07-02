n = int(input())
l = []
for i in range(0,n):
    vorudi = input().split('.')
    word = vorudi[1]
    harf_aval = word[0]
    harf_aval = harf_aval.upper()
    baghie = word[1:]
    baghie = baghie.lower()
    vorudi[1] = harf_aval + baghie
    a = vorudi[0] + ' ' + vorudi[1] + ' ' + vorudi[2]
    l.append(a)
    l.sort()

for j in range(0,len(l)):
    print (l[j])


