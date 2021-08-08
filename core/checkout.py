"""
CHECKOUT ACTION FOR E-COMMERCE APP.

This file contains functions used for performing checkout by calculating total
price of input objects.

Created on: 2021/08/08
Author(s): Manika Arora

!/usr/bin/env python
 coding: utf-8
"""

# Import libraries
import json


# Checkout function
def checkout(id_list):
    """Calculate the total price(including discount) of items(watches) in id_list

    Args:
        id_list (list): list of items(watches) selected by user

    Returns:
        dict: dictionary containing total price
    """
    # check if the list is empty
    if(len(id_list) == 0 or id_list is None):
        return {'error': 'No watches selected.'}

    # load watch catalogue
    try:
        with open('./data/catalogue.json', 'r+') as f:
            data = json.load(f, strict=False)
    except Exception:
        return {'error': 'Unable to read catalogue.'}

    price_list = list()
    id_count = dict()
    total_price = 0

    # add price of watches without discount to price_list
    # and count the units of watches with discount
    for id in id_list:
        if id not in data.keys():
            return {'error': 'Id ' + id + ' not found in catalogue.'}
        if len(data[id]['discount']) == 0:
            price_list.append(data[id]['price'])
        else:
            id_count[id] = 1 if id not in id_count.keys() else id_count[id] + 1

    # add the discounted and normal price to price_list
    # based on units of each watch with discount
    for id, count in id_count.items():
        if count < data[id]['discount']['units']:
            price_list.append(count * data[id]['price'])
        else:
            discount_factor = count // data[id]['discount']['units']
            normal_price_factor = count % data[id]['discount']['units']
            price_list.append(discount_factor * data[id]['discount']['price'])
            price_list.append(normal_price_factor * data[id]['price'])

    total_price = sum(price_list)
    return {'price': total_price}
