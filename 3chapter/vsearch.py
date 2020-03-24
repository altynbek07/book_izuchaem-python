def search4vowels(word: str) -> set:
    """Выводит гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
