def fap(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fap(num-1)+fap(num-2)
def lucas(num):
    if num==0:
        return 2
    elif num==1:
        return 1
    else:
        return lucas(num-1)+lucas(num-2)

def sum_series (r,x=0,y=1):
    if r==0:
        return x
    elif r==1:
        return y
    else:
        return sum_series(r-1,x,y)+sum_series(r-2,x,y)
    