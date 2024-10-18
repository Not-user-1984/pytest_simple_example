import pytest
from unittest.mock import patch
from my_module import fetch_data


@patch('my_module.requests.get')
def test_fetch_data(mock_get):
    # Настройка мока
    mock_get.return_value.json.return_value = {'key': 'value'}

    url = 'http://fakeurl.com'
    result = fetch_data(url)

    # Проверка, что функция возвращает ожидаемое значение
    assert result == {'key': 'value'}
    # Проверка, что requests.get была вызвана с правильным URL
    mock_get.assert_called_once_with(url)
