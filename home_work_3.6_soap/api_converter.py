import osa

def temp_converter_from_fahr_to_cels(temp):
    FromUnit = 'degreeFahrenheit'
    ToUnit = 'degreeCelsius'

    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    result = client.service.ConvertTemp(temp, FromUnit, ToUnit)
    return round(result, 2)


def currency_converter_to_ru(summ, curr):
    licenseKey = ''
    fromCurrency = curr
    toCurrency = 'RUB'
    amount = summ
    rounding = False
    date = ''
    type = ''

    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    result = client.service.ConvertToNum(licenseKey, fromCurrency, toCurrency, amount, rounding, date, type)
    return round(result, 0)


def length_converter_from_miles_to_km(length):
    LengthValue = length,
    fromLengthUnit = 'Miles',
    toLengthUnit = 'Kilometers'

    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    result = client.service.ChangeLengthUnit(LengthValue, fromLengthUnit, toLengthUnit)
    return round(result, 2)



def read_file(file_name):
    result = []
    with open(file_name, 'r') as file:
        for line in file:
            a = line.replace(',', '').split()
            result.append(a)
    return result


print('')
print('Задание 1:')
print('')

file_name_1_task = 'temps.txt'

print('..читаю файл {} и перевожу Фаренгейты в Цельсии.. подождите..'.format(file_name_1_task))
print('')

x = 0

for item in (read_file(file_name_1_task)):
    z = int(temp_converter_from_fahr_to_cels(item[0]))
    print('Температура {} по Фаренгейту составляет {} Цельсия'.format(item[0], z))
    x += z

temp_rez = round((x / len(read_file(file_name_1_task))), 2)

print('')
print('Среднее значение температур из файла {} составляет: {} C'.format(file_name_1_task, temp_rez))
print('')

print('')
print('Задание 2:')

file_name_2_task = 'currencies.txt'

print('..читаю файл {} и конвертирую валюту.. подождите..'.format(file_name_2_task))
print('')

summ = 0

for direction in read_file(file_name_2_task):
    z = int(currency_converter_to_ru(direction[1], direction[2]))
    print('Перелет {} - {} {} обойдется {} рублей'.format(direction[0], direction[1], direction[2], z))
    summ += z

print('')
print('Итого на путешествие: {} рублей'.format(summ))
print('')

print('')
print('Задание 3:')
print('')

file_name_3_task = 'travel.txt'

print('..читаю файл {} и конвертирую расстояния.. подождите..'.format(file_name_3_task))
print('')

summ = 0

for distance in read_file(file_name_3_task):
    z = length_converter_from_miles_to_km(distance[1])
    print('Расстояние {} - {} миль или {} километров'.format(distance[0], distance[1], z))
    summ += z

print('')
print('Суммарное расстояние путешествия по маршруту из файла {} составит: {} км'.format(file_name_3_task, summ))
print('')