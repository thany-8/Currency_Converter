import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'



def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the Currency COnversion API
    """
    response = requests.get(url)
    return response

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # define the function: 
    FUNCTION format_currencies_url()
    BEGIN FUNCTION
        SET currencies_URL TO concatanate string into a URL with currency endpoint
        RETURN currencies_URL
    END FUNCTION

    -------
    str
        Formatted URL to the currency endpoint
    """
    currencies_URL = _HOST_+ _CURRENCIES_

    return currencies_URL


def get_currencies():
    """
    Retrieves a list of available currencies from an API.
    Returns:
    list: A list of currency codes.
    """

    data = call_api(format_currencies_url()).json()
    key_extract = list(data.keys())

    return key_extract


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint with the 2 currency codes provided
    Returns:
    str: A string of the URL to the latest endpoint with the 2 currency codes provided
    """
    latest_URL = _HOST_+ _LATEST_ + "?from="+from_currency+"&to="+to_currency
    
    return latest_URL

