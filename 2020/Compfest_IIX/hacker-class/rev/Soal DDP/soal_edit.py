
def pw(xx, yx=0, xy=0, xjl=None, llx=None):
    
    print(xy)
    # print(llx)
    if xjl is None:
        llx=xx.pop
        xjl=len(xx)
    if yx < xjl:
        # print(llx() << (yx << 3))
        # print (llx())
        return pw(xx, yx+1, xy + (llx() << (yx << 3)), xjl, llx)

    return xy

def master(f, xx, yy=0):
    if yy == len(xx):
        return xx
    f(xx, yy)
    return master(f, xx, yy + 1)

def wg(xy):
    fgx = []
    i = 3
    fxg = getattr(fgx, "append")
    for _ in map(fxg, map(jxl, xy)):
        i <<= i ^ i
    print (fgx)
    return fgx

def mm():
    pass

def hh(xx):
    def ff(aa, bb):
        # print ("bef :",aa[bb])
        aa[bb] += (bb + 0b1) if (bb & 0o1) else (bb | 0x1)
        # print (aa[bb])

    return master(ff, xx)

def jj(xx):
    def ff(aa, bb):
        aa[bb] = ((0xF & aa[bb]) << 4) + ((aa[bb] >> 4))
        # print (aa[bb])

    return master(ff, xx)

def kl(xx):
    exec("{}(gw)".format(xx))


def eh(xx):
    def ff(aa, bb):
        aa[bb] -= (bb + 0b1) if (bb & 0o1) else (bb | 0x1)

    return master(ff, xx)

def wiwi(x):
    if x == 0:
        return 1
    else:
        return x * wiwi(x-1)




# x = input("Enter an input:")
x= "COMPFEST12{"
# jlx = len
jxl = ord
# sw = "{}(gw)".format
# ww = exec
gw = wg(x)
kl("hh")
print ("after kl(hh)")
print(gw)
kl("jj")
print ("after kl(jj)")
print(gw)

print(pw(gw))
if pw(gw) == 120290679218832191630163797978118096998325980286646140214484761791004452553:
    print("The flag is", x)
else:
    print("That doesn't look right")

