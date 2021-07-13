#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:38:24 2021

@author: ageiges
"""

import pandas as pd
import matplotlib.pyplot as plt

#%%
pw = pd.read_excel('data/global_pathways_short.xlsx',index_col=0)

plt.figure('global')
plt.clf()

plt.fill_between(pw.columns, pw.loc['CPP_low',:], y2= pw.loc['CPP_high',:], label = 'Current policies', alpha=.8)
plt.plot(pw.loc['pledge_high',:], '-', color='lightblue', label='Pledges & Targets')
plt.plot(pw.loc['optimistic',:], '-', color='orange', label='Optimistic net-zero targets')

for temp, color in zip(['2.0C', '1.5C'], ['yellow', 'green']):
    plt.fill_between(pw.columns, pw.loc[f'{temp}_low',:], y2= pw.loc[f'{temp}_high',:], 
                     label = None, color=color, alpha=.5)
    plt.plot(pw.loc[f'{temp}_median',:], '-', color=color, label=f'{temp} compatible')
plt.plot(pw.loc['Historical',:], '-k', label='Historic emissions')
plt.grid('on')
plt.legend()
plt.ylabel('Globale GHG emissions [Gt CO2eq]')
plt.xlabel('Year')
plt.tight_layout()


