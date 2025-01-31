import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"


class PetFriends:
    def __init__(self):
        self.base_url = BASE_URL

    def get_list_of_pets(self, auth_key):

        headers = {"Authorization": auth_key}
        response = requests.get(f"{self.base_url}/findByStatus?status=available", headers=headers)
        try:
            return response.status_code, response.json()
        except ValueError:
            return response.status_code, "Ошибка: Ответ не в формате JSON"


def create_test_data():
    """Функция возвращает тестовый ключ авторизации"""
    return {"auth_key": "valid_token"}  # Замените на реальный токен


def test_get_all_pets():
    auth_data = create_test_data()  # Получаем тестовые данные
    auth_key = auth_data["auth_key"]  # Достаём ключ авторизации
    pet_friends = PetFriends()  # Создаём экземпляр класса
    status_code, result = pet_friends.get_list_of_pets(auth_key=auth_key)  # Вызываем API

    assert status_code == 200, f"Expected status 200, but got {status_code}"
    assert result is not None, "Expected non-empty result"
    assert isinstance(result, list), "Expected a list of pets"

    print("Тест успешно пройден!")  # Сообщение при успешном тесте


# Запускаем тест
test_get_all_pets()

# Получение питомцев без указания статуса
def test_get_pets_without_status():
    response = requests.get(f"{BASE_URL}/findByStatus")
    print("GET /findByStatus without status")
    print(f"Статус-код: {response.status_code}")
    try:
        pets = response.json()
        print("Ответ от сервера:")
        print(pets)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Получение питомца с очень большим ID
def test_get_pet_with_large_id():
    large_pet_id = 99999999999999999999999  # Большой ID
    response = requests.get(f"{BASE_URL}/{large_pet_id}")
    print(f"GET /pet/{large_pet_id}")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Получение питомца с неверным ID
def test_get_pet_with_invalid_id():
    invalid_pet_id = 1234567890
    response = requests.get(f"{BASE_URL}/{invalid_pet_id}")
    print(f"GET /pet/{invalid_pet_id}")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Запрос с неверным токеном авторизации
def test_get_pet_with_invalid_auth():
    headers = {'Authorization': 'Bearer invalid_token'}
    response = requests.get(f"{BASE_URL}/findByStatus?status=available", headers=headers)
    print("GET /findByStatus with invalid auth")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Добавление питомца с пустыми данными
def test_add_pet_with_empty_data():
    empty_pet = {}
    response = requests.post(f"{BASE_URL}", json=empty_pet)
    print("POST /pet with empty data")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Добавление питомца без имени
def test_add_pet_without_name():
    pet_without_name = {
        "category": {"id": 0, "name": "Кошки"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}", json=pet_without_name)
    print("POST /pet without name")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Обновление питомца с неверным ID
def test_update_pet_with_invalid_id():
    invalid_pet_id = 9999999999
    updated_pet = {
        "id": invalid_pet_id,
        "name": "Барсик_новый",
        "category": {"id": 0, "name": "Кошки"},
        "photoUrls": ["https://example.com/photo2.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.put(f"{BASE_URL}", json=updated_pet)
    print(f"PUT /pet with invalid ID {invalid_pet_id}")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Удаление питомца с неверным ID
def test_delete_pet_with_invalid_id():
    invalid_pet_id = 6035044845e163611481
    response = requests.delete(f"{BASE_URL}/{invalid_pet_id}")
    print(f"DELETE /pet/{invalid_pet_id}")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Добавление питомца с некорректным типом ID
def test_add_pet_with_invalid_id_type():
    pet_with_invalid_id = {
        "id": "not_a_number",
        "name": "Барсик",
        "category": {"id": 0, "name": "Кошки"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}", json=pet_with_invalid_id)
    print("POST /pet with invalid id type")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')


# Запрос на несуществующий эндпоинт
def test_non_existent_endpoint():
    response = requests.get(f"{BASE_URL}/nonExistentEndpoint")
    print("GET /nonExistentEndpoint")
    print(f"Статус-код: {response.status_code}")
    try:
        result = response.json()
        print("Ответ от сервера:")
        print(result)
    except ValueError:
        print("Ответ не в формате JSON!")
        print('response.text')
