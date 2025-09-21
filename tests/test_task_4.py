import os
import pytest
from tasks.task_4 import solve

def test_task_4():
    # Папка с данными для задания
    data_folder = os.path.join('tasks', 'data_for_task_4')
    
    # Вызываем функцию solve для сбора информации о файлах
    result = solve()
    
    # Проверяем, что результат является словарем
    assert isinstance(result, dict), "Функция solve должна возвращать словарь"
    
    # Проверяем, что словарь содержит правильные ключи
    expected_keys = {'small', 'medium', 'large'}
    assert set(result.keys()) == expected_keys, f"Словарь должен содержать ключи {expected_keys}"
    
    # Проверяем, что значения являются целыми числами
    for key, value in result.items():
        assert isinstance(value, int), f"Значение для ключа '{key}' должно быть целым числом"
    
    # Проверяем конкретные значения (на основе файлов, которые мы создали)
    # small_file.txt должен быть <= 100 байт
    # medium_file.txt должен быть > 100 и <= 1000 байт
    # large_file.txt должен быть > 1000 байт
    
    # Ожидаем: 1 small, 1 medium, 1 large
    assert result['small'] >= 1, f"Ожидается как минимум 1 small файл, получено {result['small']}"
    assert result['medium'] >= 1, f"Ожидается как минимум 1 medium файл, получено {result['medium']}"
    assert result['large'] >= 1, f"Ожидается как минимум 1 large файл, получено {result['large']}"