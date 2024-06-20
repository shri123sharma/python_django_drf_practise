def gen_func():
    sum=0
    for i in range(1,10):
        sum+=i
        yield sum

if __name__=="__main__":
    result=gen_func()
    print(result)
