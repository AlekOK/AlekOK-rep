def solution(number):
    new_list =[y for y in range(number) if y%3==0 or y%5==0]
    return sum(new_list)