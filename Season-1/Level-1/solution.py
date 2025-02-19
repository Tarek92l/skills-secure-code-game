'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from decimal import Decimal
from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_AMOUNT = Decimal(1_000_000)  # 10 000 dollars/euros en cents

def validorder(order: Order):
    net = Decimal(0)
    total_amount = Decimal(0)

    for item in order.items:
        amount = Decimal(item.amount) * Decimal(100)  # convert in cents
        quantity = Decimal(item.quantity)

        item_total = amount * quantity
        total_amount += item_total

        if item.type == 'payment':
            net += item_total
        elif item.type == 'product':
            net -= item_total
        else:
            return "Invalid item type: %s" % item.type

    if total_amount > MAX_ORDER_AMOUNT:
        return "Total amount payable for an order exceeded"

    error_tolerance = Decimal("0.001")

    if abs(net) >= error_tolerance:
        return "Order ID: %s - Payment imbalance: $%.2f" % (order.id, net / 100)
    else:
        return "Order ID: %s - Full payment received!" % order.id
