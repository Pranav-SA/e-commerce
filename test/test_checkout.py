"""
UNIT TESTS FOR CHECKOUT ACTION FOR E-COMMERCE APP.

This file contains unit tests for checkout function used in
E-commerce app.

Created on: 2021/08/08
Author(s): Manika Arora

!/usr/bin/env python
coding: utf-8

"""

import pytest
from core.checkout import checkout


""" FIXTURES """


@pytest.fixture
def single_discount_sample():
    id_list = ['001', '002', '002', '002', '003', '004']
    return id_list


@pytest.fixture
def multiple_discount_sample():
    id_list = ['001', '001', '001', '001', '001', '001', '002',
               '002', '002', '002', '003', '003', '004']
    return id_list


""" TESTS """


def test_checkout_empty_list():
    results = checkout([])
    assert type(results) == dict
    assert results['error'] == 'No watches selected.'


def test_checkout_invalid_item():
    results = checkout(['005'])
    assert type(results) == dict
    assert results['error'] == 'Id 005 not found in catalogue.'


def test_checkout_single_item():
    results = checkout(['001'])
    assert type(results) == dict
    assert results['price'] == 100


def test_checkout_single_discount(single_discount_sample):
    results = checkout(single_discount_sample)
    assert type(results) == dict
    assert results['price'] == 380


def test_checkout_multiple_discounts(multiple_discount_sample):
    results = checkout(multiple_discount_sample)
    assert type(results) == dict
    assert results['price'] == 770
