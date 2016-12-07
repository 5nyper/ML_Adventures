%matplotlib inline
import matplotlib.pyplot as plt
import json
from numpy.random import rand
from operator import itemgetter
from scipy import stats

with open('test.json') as data_file:
    data = json.load(data_file)
pics = data["data"]
month = []
likes = []
likti = []
days = []
time = []
for member in pics:
    month.append(member["month"])
    if member["day"] == 0:
        likes.append(member["likes"])
        likti.append([member["likes"],member["time"]])
        time.append(member["time"])
    days.append(member["day"])
    #time.append(member["time"])
likes = np.array(likes)
a = []
newnew = np.array(sorted(likti, key=itemgetter(0), reverse=True))
for item in newnew[:6]:
    a.append(item[1])
plt.hist(likes)
plt.show()
print(likes.mean() + (likes.std() / 2),"on", np.mean(a))
