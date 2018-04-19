import random, math
import matplotlib.pyplot as plt

a = [1 for i in range(1000)]
survival = []
chance = 8 # expressed as a percentage

def death_chance(chance=10, type='lin', gen='1'):
    return chance

for i in range(100):
    for j in range(len(a)):
        if a[j] == 1:
            if random.randint(1,100) < death_chance(chance):
                a[j] = 0
    survival.append(a.count(1)/10)

# for i in range(len(survival)):
#     if survival[i] < 0.1:
#         survival[i] = None

# b = []
# for i in range(2,100):
#     base_chance = (0.99 ** i) ** i
#     b.append(base_chance)
    # if i == 0:
    #     modifier = 1
    #     b.append(100.0)
    # else:
    #     # modifier = 1-(1/(i**1.01))
    #     modifier = 1-(1/(math.log(i, 20)))
    #     b.append((base_chance - modifier) * 100)
    #     # b.append((modifier))
    #     if b[-1] < 0:
    #         b[-1] = 0

from pprint import pprint as pp
pp(survival)
# pp(b)
plt.xlabel('Percent maximum lifespan')
plt.ylabel('Percent surviving')
plt.plot(range(100), survival)
# plt.plot(range(len(b)), b)

plt.grid(True)
# plt.semilogy()

# plt.axis([0, 100, 0, 116])
# print(plt.axis())
# plt.yscale('symlog', linthreshy=.1)
plt.yscale('log')
# plt.hlines([0.01,0.1, 1, 10], 0, 100, linestyles='dashed')
# plt.ylim(ymin=-0.01)
plt.yticks([0.1,1,10,100], ('0.1%', '1%', '10%', '100%'))
plt.show()


