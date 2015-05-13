from money import Money
from nose.tools import raises


def test_money_can_be_added_with_std_operator():
    five_dollars = Money(5, "USD")
    two_dollars = Money(2, "USD")
    assert five_dollars + two_dollars == Money(7, "USD")


@raises(ValueError)
def test_money_with_differing_codes_cannot_be_added():
    one_usd = Money(1, "USD")
    one_can = Money(1, "CAN")
    one_usd + one_can


@raises(TypeError)
def test_money_can_only_add_with_money():
    Money(1, "USD") + 1


def test_money_equality():
    assert Money(1, "USD") == Money(1, "USD")
    assert Money(1, "USD") == Money(1.0, "USD")


def test_money_inequality():
    assert Money(1, "USD") != Money(2, "USD")
    assert Money(1, "USD") != Money(1, "CAN")


def test_money_dollars_method():
    assert Money.usd(1) == Money(1, "USD")
