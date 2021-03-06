import random
import numpy as np
import math

OPTIONS = (#"Welcome Page", 
           "Campagna Marketing",
           #"pag2: Title",
           #"pag3: Title",
           #"pag4: Title" # then add in the app.py if-else
           )


def ad_calc_profit(price_item, cost_item, ad_budget):

    profit_item = []
    break_even_cnt = 0

    # Calculate profit for each case
    for i in range(len(price_item)):

        # Get all key factors
        unit_price = price_item[i]
        unit_cost = cost_item[i]
        sales_expense = 37000
        unit_sold = ad_budget*1000*0.7

        # Calculate total profit
        profit = unit_sold * (unit_price - unit_cost) - sales_expense
        print("------")
        print(f"unit sold: {unit_sold}")
        print(unit_price, unit_cost, profit)

        profit_item.append(profit)

        if profit >= 0.0:
            break_even_cnt += 1

    # Calculate probability of break-even
    prob_profit = break_even_cnt / len(profit_item)

    return profit_item, prob_profit


def get_items_ad_triangular(unit_price, unit_cost, N):

    price_item = np.random.triangular(size=N, left=unit_price-25.0, right=unit_price+10.0, mode=unit_price)
    cost_item = np.random.triangular(size=N, left=unit_cost-5.0, right=unit_cost+10.0, mode=unit_cost)

    return price_item, cost_item


def get_items(value_range, N, shape):

    if shape == "Normal":
        return np.random.normal(size=N, loc= (value_range[0] + value_range[1])/2)

    elif shape == "Triangle":
        return np.random.triangular(size=N, left=value_range[0], right=value_range[1],
                                    mode=(value_range[0] + value_range[1])/2)

    elif shape == "Uniform":
        return np.random.uniform(size=N, low=value_range[0], high=value_range[1])


def apply_function(input_items, distribution):

    if distribution == 'Secret Formula 1':
        return np.sqrt(input_items + 1) * 2 + np.random.uniform(size=len(input_items), low=1, high=5)

    elif distribution == 'Secret Formula 2':
        return np.sqrt(input_items+1)*2 + np.random.poisson(size=len(input_items))

    elif distribution == 'Secret Formula 3':
        return np.sqrt(input_items + 1) * 2 + np.random.triangular(size=len(input_items), left=1, right=5, mode=2.5)