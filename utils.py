import json


def load_candidates_from_json():
    """
    Получает json файл и возвращает список со словарями.
    """
    with open('candidates.json', encoding="UTF-8") as f:
        candidates = json.load(f)

    return candidates


def get_candidate(candidate_id):
    """
     Ищет кандидата по id, и возвращает словарь с информацией о кандидате.
    """
    candidates = load_candidates_from_json()
    candidate = {}
    for item in candidates:
        if candidate_id == item['id']:
            candidate = item
    return candidate


def get_candidates_by_name(candidate_name: str):
    """
    Ищет кандидатов по имени, и возвращает список со словарями найденных кандидатов
    """
    candidates = load_candidates_from_json()
    candidates_by_name = []
    for item in candidates:
        if candidate_name.lower() in item['name'].lower().split(' '):
            candidates_by_name.append(item)
    return candidates_by_name


def get_candidates_by_skill(skill_name: str):
    """
    Ищет кандидатов по скиллу, и возвращает список со словарями найденных кандидатов
    """
    candidates = load_candidates_from_json()
    candidates_by_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_by_skill.append(candidate)
    return candidates_by_skill


