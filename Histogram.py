import matplotlib.pyplot as plt
plt.hist(df['MSFT'], bins=10)
plt.xlabel('Weekly Closing Price')
plt.ylabel('Frequency')
plt.title('Histogram of MSFT Weekly Closing Prices')
plt.show()
