from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check if the currency provided is a valid currency code.
    Returns:
    bool: True if the currency is valid, False otherwise.
    """

    if currency in CURRENCIES:
        return True
    else:
        return False

@dataclass
class Currency:
    """
    A class to represent the currency conversion result. 
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Calculates the inverse rate of the current rate.
        
        Returns:
            float: The inverse rate rounded to 5 decimal places.
        """

        self.inverse_rate = round(1/self.rate, 5)

    def format_result(self):
        """
        Formats the result of the currency conversion.
        Returns:
            str: A formatted string containing the date, currencies, conversion rate, and inverse rate.
        
        """
        return "Today's " + "(" + self.date + ")" + " conversion rate from " + self.from_currency + " to "+self.to_currency + " is " + str(self.rate) + ". The inverse rate is " + str(self.inverse_rate)


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate.
    
    """
    from_currency = result.get("base")
    to_currency = list(result.get("rates").keys())[0]
    amount = result.get("amount")
    rate = result.get("rates").get(to_currency)
    date = result.get("date")

    currency = Currency(from_currency, to_currency, amount, rate, None, date)
    currency.reverse_rate()

    return currency
