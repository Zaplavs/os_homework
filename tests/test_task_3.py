import os
import pytest
from tasks.task_3 import solve

def test_task_3():
    # Папка с данными для задания
    data_folder = os.path.join('tasks', 'data_for_task_3')
    
    # Получаем список файлов до выполнения задания
    initial_files = os.listdir(data_folder)
    assert len(initial_files) > 0, "В папке должны быть файлы для тестирования"
    
    # Вызываем функцию solve для группировки файлов
    solve()
    
    # Получаем список файлов и папок после выполнения задания
    final_items = os.listdir(data_folder)
    
    # Проверяем, что созданы папки по первой букве файлов
    # Ожидаемые папки для наших тестовых файлов: A, B, C, D, E
    expected_folders = {'A', 'B', 'C', 'D', 'E'}
    actual_folders = {item for item in final_items if os.path.isdir(os.path.join(data_folder, item))}
    assert expected_folders.issubset(actual_folders), f"Не все ожидаемые папки созданы. Ожидаемые: {expected_folders}, Созданные: {actual_folders}"
    
    # Проверяем, что файлы перемещены в правильные папки
    # apple.txt должен быть в папке A
    assert os.path.exists(os.path.join(data_folder, 'A', 'apple.txt')), "Файл apple.txt не найден в папке A"
    
    # Bear.jpg должен быть в папке B
    assert os.path.exists(os.path.join(data_folder, 'B', 'Bear.jpg')), "Файл Bear.jpg не найден в папке B"
    
    # cat.png должен быть в папке C
    assert os.path.exists(os.path.join(data_folder, 'C', 'cat.png')), "Файл cat.png не найден в папке C"
    
    # Dog.gif должен быть в папке D
    assert os.path.exists(os.path.join(data_folder, 'D', 'Dog.gif')), "Файл Dog.gif не найден в папке D"
    
    # elephant.bmp должен быть в папке E
    assert os.path.exists(os.path.join(data_folder, 'E', 'elephant.bmp')), "Файл elephant.bmp не найден в папке E"