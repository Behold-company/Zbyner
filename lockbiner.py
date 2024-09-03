enfirst = 'ৌৈাীূড়োে্িুچشسপরকতচыགནཔཚཛটংваьбюض7صཁསཧཨйфпоظ5طزཞཟའཕབসཙবرذлдমثقیযཀцукজཡར01енгшўзхམনفغعهবলལহཆཇཉཝاগদཤжэخحجячстبلངིེོུཅتཏཐདنمکدئوژ'
first = 'a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZالفبپتثجچحخدذرزژسشصطظضعغفقکگلمنوهی1234567890!@#$%^&*()_+=-/\ .:;\"\'\t،,][}<>'
q = ''
#enlist = []
def fin(b):
    global q
    global enlist
    h = enfirst.find(b)
    t = first[h]
    q = q + t
    #enlist.append(t)



a = input("Entered: ")
lenn = len(a)
print(type(lenn))

lem = 0
while lem < lenn:
    b = a[lem]
    fin(b)
    lem = lem + 1

#print(enlist)
print(q)
input()
