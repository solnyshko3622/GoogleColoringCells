import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Определяем область действия
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

# Чтение учетных данных из файла ключа ServiceAccount
credentials = ServiceAccountCredentials.from_json_keyfile_name('enroll_token.json', scope)

# Инициализация объекта авторизации
gc = gspread.authorize(credentials)

# Открываем таблицу
sheet = gc.open('testGoogeApi').get_worksheet(0)  # Получаем первый лист

# Определяем диапазон ячеек и форматирование
cell_range = 'A1:B2'  # Укажите диапазон ячеек
formatting = {
    "backgroundColor": {
        "red": 1,
        "green": 0,
        "blue": 0
    }
}

# Формируем запрос для изменения формата ячеек
requests = [{
    "repeatCell": {
        "range": {
            "sheetId": sheet.id,
            "startRowIndex": 0,
            "endRowIndex": 2,
            "startColumnIndex": 0,
            "endColumnIndex": 2
        },
        "cell": {
            "userEnteredFormat": formatting
        },
        "fields": "userEnteredFormat(backgroundColor)"
    }
}]

# Отправка запроса на изменение формата
body = {
    'requests': requests
}

# Выполняем обновление формата
sheet.spreadsheet.batch_update(body)
