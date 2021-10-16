import matplotlib.pyplot as plt

answer = 0
inp = range(-10, 11)

predicted = map(lambda x: (x-answer)**2, inp)
plt.plot(inp, list(predicted))
plt.show()
