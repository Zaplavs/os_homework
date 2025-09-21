import os
import pytest
from tasks.task_2 import solve

def test_task_2():
    # Проверяем начальное состояние папки
    data_folder = os.path.join('tasks', 'data_for_task_2')
    
    # Проверяем, что в папке есть .tmp файлы до выполнения задания
    initial_files = os.listdir(data_folder)
    tmp_files_before = [f for f in initial_files if f.endswith('.tmp')]
    assert len(tmp_files_before) > 0, "В папке должны быть .tmp файлы для тестирования"
    
    # Проверяем, что есть другие файлы
    other_files_before = [f for f in initial_files if not f.endswith('.tmp')]
    assert len(other_files_before) > 0, "В папке должны быть файлы с другими расширениями для тестирования"
    
    # Вызываем функцию solve для удаления временных файлов
    solve()
    
    # Проверяем состояние папки после выполнения задания
    final_files = os.listdir(data_folder)
    
    # Проверяем, что .tmp файлы удалены
    tmp_files_after = [f for f in final_files if f.endswith('.tmp')]
    assert len(tmp_files_after) == 0, f"В папке остались .tmp файлы: {tmp_files_after}"
    
    # Проверяем, что другие файлы остались
    other_files_after = [f for f in final_files if not f.endswith('.tmp')]
    assert set(other_files_before) == set(other_files_after), "Файлы с другими расширениями были удалены или изменены"