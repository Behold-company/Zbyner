first = 'ৌৈাীূড়োে্িুچشسপরকতচыགནཔཚཛটংваьбюض7صཁསཧཨйфпоظ5طزཞཟའཕབসཙবرذлдমثقیযཀцукজཡར01енгшўзхམনفغعهবলལহཆཇཉཝاগদཤжэخحجячстبلངིེོུཅتཏཐདنمکدئوژ'
enfirst = 'a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZالفبپتثجچحخدذرزژسشصطظضعغفقکگلمنوهی1234567890!@#$%^&*()_+=-/\ .:;\"\'\t،,][}<>'
q = ''
#enlist = []
def fin(b):
    global q
    global enlist
    h = first.find(b)
    t = enfirst[h]
    q = q + t
    #enlist.append(t)



def Unlock(a):
    lenn = len(a)


    lem = 0
    while lem < lenn:
        b = a[lem]
        fin(b)
        lem = lem + 1
    print(q)

#print(enlist)
