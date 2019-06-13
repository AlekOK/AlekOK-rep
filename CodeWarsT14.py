def count_positives_sum_negatives(arr):
    neg_num= 0
    poz_num = 0
    for i in arr: 
        if i >= 1:
            poz_num += 1
        else:
            neg_num += i
    if len(arr) == 0:
        return []
    result_list = [poz_num, neg_num]
    return result_list