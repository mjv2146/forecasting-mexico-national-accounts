# Mexico National Accounts
### Task
This project studies three crisis episodes in Mexico:
1. The Mexican Peso Crisis of 1994
2. The Global Financial Crisis of 2008
3. The Covid-19 Crisis

The question for each crisis is whether it produces a permanent decline in the Mexican economy belows its trend. I estimate the trend using two methods:
1. Linear regression
2. ARIMA forecasting

### Data
1. Quarterly National Accounts - [OECD Main Economic Indicators](https://www.oecd.org/sdd/oecdmaineconomicindicatorsmei.htm)
2. Interest Rates - [IMF International Financial Statistics](https://data.imf.org/?sk=4c514d48-b6ba-49ed-8ab9-52b0c1a0179b)

### Data Wrangling
1. Separate trend and cyclical components using Hodrick-Prescott Filter and linear regression
2. Forecast trends using linear regression
3. Compute real interest rates using CPI
4. Linearly interpolate annual population to quarterly levels

### Tools
1. Pandas - data wrangling
2. Matplotlib/seaborn - visualization
3. Sklearn - linear regression forecasting
4. autoarima - arima forecasting