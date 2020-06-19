import pytest

from library.httpclient import HttpClient


class TestWeather:
    """Weather api test cases"""

    def setup(self):
        """"""
        self.host = 'http://www.weather.com.cn'
        self.api = '/data/cityinfo'
        self.client = HttpClient()

    @pytest.mark.parametrize('city_code, exp_city',[("101280601","深圳1"),("101010100","北京"),("101020100","上海")])
    def test_weather(self, city_code, exp_city):
        url = f'{self.host}{self.api}/{city_code}.html'
        response = self.client.Get(url=url)
        act_city = response.json()['weatherinfo']['city']
        print(f'Expect city = {exp_city}, while actual city = {act_city}')
        assert exp_city == act_city
