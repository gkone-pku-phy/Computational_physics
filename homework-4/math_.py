
def Sturm(main,sub):
    # 对齐指标
    main = [0]+main
    sub = [0]+sub+[0]
    def f(x,i):
        if i==0:
            return 1
        elif i==1:
            return main[1]-x 
        else:
            return (main[i]-x)*f(x,i-1)-sub[i-1]**2 * f(x,i-2)
    def signal_change(series):
        s=0
        prev = None
        for idx,ele in enumerate(series):

            if idx != 0:
                if ele ==0 or ele*prev<0:
                    s+=1
            prev=ele 
        return s     
    
    n = len(main)-1
    lowerBound = min([main[i]-(abs(sub[i-1])+abs(sub[i])) for i in range(1,n+1)])
    upperBound = max([main[i]+(abs(sub[i-1])+abs(sub[i])) for i in range(1,n+1)])
    print(f"本征值范围：\nlowerbound: {lowerBound},upperbound: {upperBound}")
    for target in range(1,n+1):
        def func(x):
            series = [f(x,i) for i in range(n+1)]
            # print(f"x: {x}\nseries: {series}")
            return signal_change(series) #等于小于本征值中小于x的数目
        res = bin_search(func,lowerBound,upperBound,target,20)
        print(f"taget {target}: res={res}")
def bin_search(f,start,stop,target,iter):
    mid = 0
    cnt=0
    while(cnt<iter):
        cnt+=1
        mid = (stop+start)/2
        # print(f"lower: {start}, upper: {stop}")
        y=f(mid)
        if y>=target:
            stop = mid
        elif y<target:
            start = mid 
        if cnt % 5 == 0:
            print(f"{cnt} iters approximate:{mid}")
    return mid 
            

