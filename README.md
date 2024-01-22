# Mexico National Accounts
### Task
This project studies three crisis episodes in Mexico:
- The Mexican Peso Crisis of 1994
- The Global Financial Crisis of 2008
- The Covid-19 Crisis

The question for each crisis is whether it produces a permanent decline in the Mexican economy belows its trend. I estimate the trend using two methods:
- Linear regression
- ARIMA forecasting

### Findings
- The Mexican Peso Crisis produced a *temporary* decline in the economy
- The Global Financial Crisis and Covid-19 crisis produced a *permanent* decline in the economy

### Data
- Quarterly National Accounts - [OECD Main Economic Indicators](https://www.oecd.org/sdd/oecdmaineconomicindicatorsmei.htm)
- Interest Rates - [IMF International Financial Statistics](https://data.imf.org/?sk=4c514d48-b6ba-49ed-8ab9-52b0c1a0179b)

### Data Wrangling
- Separate trend and cyclical components using Hodrick-Prescott Filter and linear regression
- Forecast trends using linear regression
- Compute real interest rates using CPI
- Linearly interpolate annual population to quarterly levels

### Tools
- Pandas - data wrangling
- Matplotlib/seaborn - visualization
- Sklearn - linear regression forecasting
- autoarima - arima forecasting