def gen():
    num = 0
    while True:
        x = yield num
        print('kkkk:' + str(x))
        num += 1

m = gen()
print(next(m))
print(next(m))
print(m.send(14))