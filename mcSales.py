"""
Name: Nathan Roberts
Date: 10/20/19
PID: A14384608
"""

import pandas as pd
import numpy as np

daily = pd.read_csv('daily_sales.csv')
monthly = pd.read_csv('monthly_sales.csv')

daily['Day_OTW'] = daily['Unnamed: 0']
days_grp = daily.groupby('Day_OTW')[daily.columns[1:-1]].apply(np.mean)
days_grp['Average'] = days_grp[days_grp.columns[1:]].apply(np.mean, axis=1)
days_grp.to_csv(r'daily_grouped.csv')

monthly_HM = monthly[['Month, Year', 'HM-NE', 'HM-SW', 'HM-NW', 'HM-SE', 'HM-C']]
monthly_HM['Average'] = monthly_HM[monthly_HM.columns[1:]].apply(np.mean, axis = 1)
monthly_HM.to_csv(r'monthly_HMsales.csv')

before_IB = monthly.iloc[:32]
after_IB = monthly.iloc[33:]
before_IB = before_IB.append(before_IB[before_IB.columns[1:]].apply(np.mean, axis=0), ignore_index=True)
after_IB = after_IB.append(after_IB[after_IB.columns[1:]].apply(np.mean, axis=0), ignore_index=True)
before_IB.to_csv(r'mnth_before_ib.csv')
after_IB.to_csv(r'mnth_after_ib.csv')
