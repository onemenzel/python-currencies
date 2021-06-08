#!/usr/bin/env python
from typing import Union, List, Optional
from currencies.config import MONEY_FORMATS
from currencies.exceptions import CurrencyDoesNotExist
from decimal import Decimal

__VERSION__ = (2021, 6, 8)


def get_version() -> str:
    """Returns the package version."""
    return ".".join(str(v) for v in __VERSION__)

default_quantization = Decimal('1.00')

class Currency:
    money_currency: Optional[str] = None
    money_formats = MONEY_FORMATS

    def __init__(self, money_currency: str):
        self.set_money_currency(money_currency)

    def set_money_currency(self, money_currency: str) -> None:
        if money_currency not in self.money_formats:
            raise CurrencyDoesNotExist

        self.money_currency = money_currency

    def get_money_currency(self) -> str:
        return self.money_currency

    @classmethod
    def get_currency_formats(cls) -> list:
        return list(cls.money_formats.keys())
    
    def get_quantization(self) -> Decimal:
        return self.money_formats[
            self.get_money_currency()
        ].get('quantization', default_quantization)
    
    def quantize_amount(self, amount: Decimal, *args, **kwargs) -> Decimal:
        return amount.quantize(self.get_quantization(), *args, **kwargs)

    def get_money_format(self, amount: Union[int, float, str]) -> str:
        """
        Usage:
        >>> currency = Currency('USD')
        >>> currency.get_money_format(13)
        >>> '$13'
        >>> currency.get_money_format(13.99)
        >>> '$13.99'
        >>> currency.get_money_format('13,2313,33')
        >>> '$13,2313,33'
        """
        return self.money_formats[
            self.get_money_currency()
        ]['money_format'].format(amount=amount)

    def get_money_with_currency_format(self, amount: Union[int, float, str]) -> str:
        """
        Usage:
        >>> currency = Currency('USD')
        >>> currency.get_money_with_currency_format(13)
        >>> '$13 USD'
        >>> currency.get_money_with_currency_format(13.99)
        >>> '$13.99 USD'
        >>> currency.get_money_with_currency_format('13,2313,33')
        >>> '$13,2313,33 USD'
        """
        return self.money_formats[
            self.get_money_currency()
        ]['money_with_currency_format'].format(amount=amount)

