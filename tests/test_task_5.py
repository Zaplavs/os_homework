import os
import pytest
from tasks.task_5 import solve

def test_task_5():
    # Папка с данными для задания
    data_folder = os.path.join('tasks', 'data_for_task_5')
    
    # Вызываем функцию solve для рекурсивного поиска .log файлов
    result = solve()
    
    # Проверяем, что результат является списком
    assert isinstance(result, list), "Функция solve должна возвращать список"
    
    # Проверяем, что все элементы списка являются строками (путями к файлам)
    for item in result:
        assert isinstance(item, str), "Все элементы списка должны быть строками (путями к файлам)"
    
    # Проверяем, что все найденные файлы имеют расширение .log
    for path in result:
        assert path.endswith('.log'), f"Файл {path} не имеет расширения .log"
    
    # Проверяем, что найдены правильные файлы (на основе структуры, которую мы создали)
    # Ожидаемые файлы:
    expected_files = [
        os.path.join(data_folder, 'folder1', 'file2.log'),
        os.path.join(data_folder, 'folder1', 'subfolder1', 'file4.log')
    ]
    
    # Проверяем, что все ожидаемые файлы найдены
    for expected_file in expected_files:
        assert expected_file in result, f"Ожидаемый файл {expected_file} не найден в результате"
    
    # Проверяем, что количество найденных файлов соответствует ожидаемому
    assert len(result) == len(expected_files), f"Найдено {len(result)} файлов, ожидается {len(expected_files)}"