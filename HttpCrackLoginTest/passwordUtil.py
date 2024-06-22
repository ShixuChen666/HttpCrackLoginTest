import itertools
from itertools import combinations
import multiprocessing


from autorequest import login
def get_password():
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(3,10):
        combine(list1,i)




def combine(temp_list, n):
    for c in combinations(temp_list, n):
        pwd_str = ''.join(c)
        login(pwd_str)




get_password()
