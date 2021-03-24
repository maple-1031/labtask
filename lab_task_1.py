# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:21:43 2021

@author: maple
"""

import numpy as np
import random

n = 20                      #ここの数字を入れ替えるとデータの数になる
r_list = [(random.random() * 2 - 1) for s in range(n)]

mu = np.mean(r_list)                #平均値
sigma_1 = np.std(r_list)            #標準偏差
sigma_2 = np.std(r_list, ddof=1)    #不偏標準偏差

max_data = max(np.abs(r_list))
n = (max_data - mu) / sigma_1

nl = "\n"
print(f"データ数：{n}{nl}平均値：{mu}{nl}標準偏差：{sigma_1}{nl}不偏標準偏差：{sigma_2}{nl}n={n}")