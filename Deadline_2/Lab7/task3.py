def calc_avg(numbers: list[float]) -> float:
    """
    Вычисляет среднее фриф списка чисел.

    Args: 
       numbers (list[float]): Список чисел. 

    Returns:
        float: Среднее значение или 0.0, если список пуст. 
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def fmt_fio(parts: list[str], capitalize: bool = True):
    """
        Формирует ФИО из списка строк. 
    
        Args: 
           parts(list[str]): Список строк 
            capitalize(bool): Делать ли первую букву заглавной  
    
        Returns:
            str: Отформатированное ФИО. 
        """
    fio = " ".join(parts)
    if capitalize:
        return fio.title()    
    return fio

def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    """
    Фильтрует словарь с оценками, оставляя только значения >= min_value.

    Args:
        data_dict (dict[str,int]): Cловарь с оценками.
        min_value (int): Минимальный порог для фильтрации.
    Returns:
        dict[str, int]: Новый словарь с подходящими оценками.
    """
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
    return result

print(calc_avg([10, 20, 30, 40]))
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
scores = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(scores, 90))