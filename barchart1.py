import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', sep=',',header=None, index_col =0)

data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.title('Title')

plt.show()
