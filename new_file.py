import pandas as pd

#насройка для вывода всех столбцов
pd.set_option('display.max_columns', None)


#вывод кодировок на заданную дату
url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'
pd.read(url)

#вывод кодировок на данный момент
url1 = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=20/01/2022'
pd.read_xml(url1, encoding='cp1251')


#динамика доллара на заданный период
url_dinamic_dollar = 'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ=R01235'
pd.read_xml(url_dinamic_dollar)
