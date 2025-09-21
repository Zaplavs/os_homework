import os
import pytest
from tasks.task_1 import solve

def test_task_1():
    # Вызываем функцию solve для создания структуры директорий
    solve()
    
    # Проверяем, что структура директорий создана правильно
    expected_path = os.path.join('tasks', 'data_for_task_1', 'media', 'images', 'icons')
    assert os.path.exists(expected_path), f"Папка {expected_path} не была создана"