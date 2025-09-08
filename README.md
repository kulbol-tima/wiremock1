# WireMock standalone (Кадастр по ПИН)

## Запуск
```bash
docker compose up -d
```

## Проверка
```bash
curl "http://localhost:8029/api/internal/v1/search-pin-all?pin=12345678901234"
```

Ожидаемый ответ (пример):
```json
[
  {
    "Propcode": "0000000000001",
    "Address": "обл. Нарын, р-н Жумгальский, а/а Куйручук-Кызарт, с. Жаны-Арык, уч. Балтабай усту.",
    "Owner": "Иванов Иван",
    "Pin": "12345678901234",
    "DocNum": "id1234567",
    "REG_DATE": "2008-02-15",
    "TERM_DATE": ""
  }
]
```

## Состав
- docker-compose.yml
- wiremock/mappings/search-pin-all.json — успешный кейс (200)
- wiremock/mappings/search-pin-all-bad.json — некорректный запрос (400)

## Примечания
- Меняйте JSON прямо в `mappings` и перезапускайте контейнер (`docker compose restart wiremock`).
- Для работы в одной сети с вашим сервисом укажите baseUrl: `http://wiremock:8080`.
