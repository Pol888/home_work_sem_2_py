def task_1(num: int) -> str:
    string_resault: str = ""
    list_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    while num > 16:
        b = num % 16
        num = num // 16
        string_resault = list_values[b] + string_resault

    string_resault = list_values[num] + string_resault
    return string_resault



def task_2(*args:str, key=1) -> str:
    if key == 1:
        sum_of_fractions = list(map(int,args[0].split('/')))
        for i in args[1:]:
            a = list(map(int, i.split('/')))
            if a[1] == sum_of_fractions[1]:
                sum_of_fractions[0] = sum_of_fractions[0] + a[0]

            elif a[1] != sum_of_fractions[1]:
                if a[1] < sum_of_fractions[1]:
                    sum_of_fractions, a = a, sum_of_fractions

                count = 1
                flag = True
                while flag:
                    l = a[1] * count
                    if a[1] * count % sum_of_fractions[1] == 0:
                        flag = False
                        i = (sum_of_fractions[0] * (l / sum_of_fractions[1]))
                        sum_of_fractions[0] = (sum_of_fractions[0] * (l / sum_of_fractions[1])) + (a[0] * (l / a[1]))
                        sum_of_fractions[1] = l
                    count += 1
            return str(int(sum_of_fractions[0])) + '/' + str(int(sum_of_fractions[1]))

    elif key != 1:
        product_of_fractions = list(map(int, args[0].split('/')))
        for i in args[1:]:
            a = list(map(int, i.split('/')))
            product_of_fractions[0] = product_of_fractions[0] * a[0]
            product_of_fractions[1] = product_of_fractions[1] * a[1]
        return str(int(product_of_fractions[0])) + '/' + str(int(product_of_fractions[1]))




