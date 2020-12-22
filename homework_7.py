from bs4 import BeautifulSoup as BS
import requests

CITIES = [
    ['Tallinn', 'tallinn-4072'],
    ['Kohtla-Järve', 'kohtla-jarve-11049'],
    ['Narva', 'narva-4077'],
    ['Tartu', 'tartu-4105'],
    ['Pärnu', 'parnu-4095'],
]


def get_today_temp(city_alias):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.75 Safari/537.36'}

    current_temp_tallinn_url = f'https://www.gismeteo.ru/weather-{city_alias}/now/'
    full_page = requests.get(current_temp_tallinn_url, headers=headers)
    soup = BS(full_page.content, 'html.parser')
    # найти необходимый блок с общей информацией о погоде на сегодня, завтра и текущий момент:
    city_block = soup.find('div', class_='tabs _left')
    # из полученного блока найти блок с информацией о погоде на текущий момент:
    today_temp_block = city_block.find('div', class_='tab tooltip')
    # в полученном блоке найти иноформацию о текущей реальной температуре и температуре по ощущениям:
    weather_tab = today_temp_block.find('div', class_='tab-weather__value')
    weather_tab_feel = today_temp_block.find('div', class_='tab-weather__feel')
    # найти данные о текущей реальной температуре и температуре по ощущениям в Цельисиях:
    curr_temp_c = weather_tab.find('span', class_='unit_temperature_c')
    curr_temp_c_feel = weather_tab_feel.find('span', class_='unit_temperature_c')

    # вернуть текущую реальную температру и температуру по ощущениям в Цельсиях:
    return curr_temp_c.text.strip(), curr_temp_c_feel.text.strip()


def menu():
    while True:
        # len(CITIES) на случай, если в список городов добавится еще несколько (на данный момент неизвестно
        # конечное число городов для выбора)
        for i in range(0, len(CITIES)):
            print(str(i+1) + '.', CITIES[i][0])

        city_choice = int(input('Please choose the city: '))
        if city_choice < 1 or city_choice > len(CITIES):
            print('\nInvalid choice. Try again.\n')
            continue

        break

    return CITIES[city_choice-1]  # вернуть элемент с данными выбранного города


def main():
    city = menu()
    today_temp, today_temp_feel = get_today_temp(city_alias=city[1])
    print('\nCurrent temperature in', city[0], 'is', today_temp, '°C.', 'Feels like', today_temp_feel, '°C.',
          'Have a nice day! :)')


main()
