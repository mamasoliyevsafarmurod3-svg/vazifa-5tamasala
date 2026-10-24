def yetkazish_haqi(narx,haq=5000):
    return narx+haq

data = input().split()
if len(data)==2:
    print(yetkazish_haqi(int(data[0]), int(data[1])))
else:
    print(yetkazish_haqi(int(data[0])))