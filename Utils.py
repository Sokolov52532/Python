from requests import get, utils
import datetime as dt

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

value_usd = content[content.find('Доллар США'):content.find('Доллар США') + 35]
value_eur = content[content.find('Евро'):content.find('Евро') + 35]

dict1 = {
    'USD': value_usd,
    'EUR': value_eur,
}

def currency_rates(value):
    """
    returns the value of the requested currency in rubles

    :param: value: str
    :return: Tuple(float, date)
    """
    val = ''
    value = value.upper()

    if value not in dict1:
        return
    else:
        for i in range(len(dict1[value])):
            if dict1[value][i].isdigit():
                val += dict1[value][i]
            else:
                pass

    date = content[content.find('Date'):content.find('Date') + 17]
    unform_date = ''

    for i in range(len(date)):
        if date[i].isdigit():
            unform_date += date[i]
        else:
            pass

    date = dt.datetime.strptime(unform_date, '%d%m%Y').date()

    return round(float(val) / 10000, 2), date
