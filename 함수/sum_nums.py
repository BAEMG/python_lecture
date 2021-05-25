def greet(*args):
    data = 0
    for i in args:
        data += i
    data_mean =data / len(args)
    reutrn data, data_mean

    sum_nums(10,20,30)
    sum_nums(10,20,30,40,50)
    print('합은 : {a}, 평균은 {b}')