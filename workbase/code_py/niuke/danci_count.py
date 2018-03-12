# coding:utf-8


# s = 'nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2scyn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn39'
# s1 = input()
# print(dict([(x, s.count(x))for x in set(s.split(' ')[0]) if x.isalpha()]))
# # print(dict([(x, s.count(x))for x in set(s.split(' ')[0]) if x.isalpha()]).values())
# # print(min(dict([(x, s.count(x))for x in set(s.split(' ')[0]) if x.isalpha()]).values()))
# print(s[:-1])
# print(s[-1])
# print(s.lower().count(s1))
# lis = []
# n = input()
# for x in range(int(n)):
#     lis.append(int(input()))
# lis = list(set(lis))
# lis.sort()
# for i in lis:
#     print(i)

s = input()
n = 8
count = len(s) / n

def adder(s):
    if len(s) >8:
        pass
