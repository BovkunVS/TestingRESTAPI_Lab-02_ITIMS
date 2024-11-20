import requests

def main():
    # URL та заголовки запиту
    url = "https://shazam.p.rapidapi.com/artists/get-latest-release"
    headers = {
        "x-rapidapi-host": "shazam.p.rapidapi.com",
        "x-rapidapi-key": "59458a150bmsh50d83e48bc4b4c1p151bbbjsn893dabdd54f7",
        "accept": "*/*"
    }
    
    # Параметри запиту
    params = {
        "id": "73406786",
        "l": "en-US"
    }
    
    # Виконання запиту
    response = requests.get(url, headers=headers, params=params)
    
    # Обробка відповіді
    if response.status_code == 200:
        print("Успішний відповідь від сервера!")
        data = response.json()
        
        # Якщо є дані про альбом
        if 'data' in data and data['data']:
            album = data['data'][0]['attributes']
            print(f"Назва альбому: {album['name']}")
            print(f"Артист: {album['artistName']}")
            print(f"Дата релізу: {album['releaseDate']}")
            print(f"Жанри: {', '.join(album['genreNames'])}")
            print(f"Посилання на альбом: {album['url']}")
            print(f"Зображення обкладинки: {album['artwork']['url']}")
        else:
            print("Немає доступних даних про релізи.")
    else:
        print(f"Помилка: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
