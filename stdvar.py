#Roughly predict the amount of likes on a given day when posting

import matplotlib.pyplot as plt
import json
from numpy.random import rand
from pprint import pprint

with open('test.json') as data_file:
    data = json.load(data_file)
pics = data["data"]
month = []
likes = []
days = []
time = []
for member in pics:
    month.append(member["month"])
    if member["day"] == 0:
        likes.append(member["likes"])
    days.append(member["day"])
    time.append(member["time"])
likes = np.array(likes)
plt.hist(likes)
plt.show()
pprint(likes)
likes.mean() + (likes.std() / 2)
