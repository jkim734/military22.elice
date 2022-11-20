#%%
import matplotlib.pyplot as plt

pos = range(4)
years = [2015, 2016, 2017, 2018]
temperatures = [17,16,19,22]

plt.bar(pos, temperatures)
plt.xticks(pos, years)

# %%
