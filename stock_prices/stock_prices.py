#!/usr/bin/python

import argparse


def find_max_profit(prices):
    big_diff = prices[1] - prices[0]
    for i in range(len(prices)):
        for j in range(i):
            if (prices[i] - prices[j]) > big_diff:
                big_diff = prices[i] - prices[j]
    return big_diff
# def find_max_profit(prices):
#     print("prices: ", prices)
#     big_diff = prices[1] - prices[0]
#     print("big_diff: ", big_diff)
#     current_min = prices[0]
#     for i in range(len(prices)):
#         print("price: ", prices[i])
#         if i > 0:
#             if current_min > prices[i]:
#                 current_min = prices[i]
#                 print("current_min: ", current_min)
#             if prices[i] - current_min > big_diff:
#                 big_diff = prices[i] - current_min
#                 print("big_diff: ", big_diff)
#         print("")
#     print("=======================================================")
#     return big_diff


# print(find_max_profit([45, 7, 62, 5]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
