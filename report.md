# Отчет о моковых данных

Этот документ содержит описание всех мок-сценариев, доступных в сервисе.

| № | Сценарий | Условие (входные данные) | Код ответа (HTTP) | Пример ответа (Response body) | Примечания |
|---|---|---|---|---|---|
| 1 | ГНС / tp-business-activity-by-pin / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/tp-business-activity-by-pin`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 2 | ГНС / tp-business-activity-by-pin / found | **Метод:** `GET`
**URL:** `/api/internal/v1/tp-business-activity-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '11111111111111' | 200 | ```json
{
  "Farm": "Крестьянское хозяйство 'Агро'",
  "FullName": "Иванов Иван Иванович",
  "RayonCode": "003",
  "RayonName": "Свердловский р-н",
  "TaxActiveDate": "2022-08-09T00:00:00",
  "TaxTypeCode": "1020",
  "TIN": "{{request.query.pin}}"
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 3 | ГНС / tp-business-activity-by-pin / not-found | **Метод:** `GET`
**URL:** `/api/internal/v1/tp-business-activity-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '22222222222222' | 200 | ```json
{
  "Farm": null,
  "FullName": null,
  "RayonCode": null,
  "RayonName": null,
  "TaxActiveDate": null,
  "TaxTypeCode": null,
  "TIN": "{{request.query.pin}}"
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 4 | ГНС / tp-business-activity-by-pin / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/tp-business-activity-by-pin` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 5 | Кадастр / search-all-by-full-name / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-full-name`

**Параметры запроса:**
- Параметр 'firstname' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'firstname' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 6 | Кадастр / search-all-by-full-name / multiple-properties | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-full-name`

**Параметры запроса:**
- Параметр 'surname' равен 'Петров'
- Параметр 'firstname' равен 'Петр' | 200 | ```json
[
  {
    "Propcode": "6-02-01-0002-0111",
    "Address": "г. Жалал-Абад, ул. Токтогула, 15",
    "Owner": "Петров Петр",
    "Pin": "10202198005678",
    "DocNum": "JA-123123",
    "REG_DATE": "2010-06-12",
    "TERM_DATE": ""
  },
  {
    "Propcode": "6-02-01-0002-0112",
    "Address": "г. Жалал-Абад, ул. Ленина, 30",
    "Owner": "Петров Петр",
    "Pin": "10202198005678",
    "DocNum": "JA-456456",
    "REG_DATE": "2015-08-01",
    "TERM_DATE": ""
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 7 | Кадастр / search-all-by-full-name / no-properties | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-full-name`

**Параметры запроса:**
- Параметр 'surname' равен 'Сидоров'
- Параметр 'firstname' равен 'Сидор' | 200 | ```json
[]
``` | Стандартный сценарий работы. |
| 8 | Кадастр / search-all-by-full-name / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-full-name` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 9 | Кадастр / search-all-by-full-name / single-property | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-full-name`

**Параметры запроса:**
- Параметр 'surname' равен 'Иванов'
- Параметр 'firstname' равен 'Иван' | 200 | ```json
[
  {
    "Propcode": "5-01-01-0001-0555",
    "Address": "г. Бишкек, ул. Исанова, 5",
    "Owner": "Иванов Иван",
    "Pin": "20101199001234",
    "DocNum": "BISH-987654",
    "REG_DATE": "2021-01-15",
    "TERM_DATE": ""
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 10 | Кадастр / search-all-by-prop-code / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-prop-code`

**Параметры запроса:**
- Параметр 'propCode' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'propCode' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 11 | Кадастр / search-all-by-prop-code / property-found | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-prop-code`

**Параметры запроса:**
- Параметр 'propCode' равен 'PROP123' | 200 | ```json
{
  "materialsten": "Кирпич",
  "ploshad_stroenia": "120.5",
  "ploshad_zem_uchastka": "600",
  "vid_zem_uchastka": "Садовый участок",
  "god_postroiki": "2010",
  "formaobstvenosti": "Частная",
  "document_prava": "Договор купли-продажи",
  "formaIspolzovania": "Индивидуальное жилищное строительство"
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 12 | Кадастр / search-all-by-prop-code / property-not-found | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-prop-code`

**Параметры запроса:**
- Параметр 'propCode' равен 'PROP999' | 200 | ```json
{
  "materialsten": null,
  "ploshad_stroenia": null,
  "ploshad_zem_uchastka": null,
  "vid_zem_uchastka": null,
  "god_postroiki": null,
  "formaobstvenosti": null,
  "document_prava": null,
  "formaIspolzovania": null
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 13 | Кадастр / search-all-by-prop-code / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/search-all-by-prop-code` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 14 | Кадастр / search-pin-all / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/search-pin-all`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 15 | Кадастр / search-pin-all / multiple-properties | **Метод:** `GET`
**URL:** `/api/internal/v1/search-pin-all`

**Параметры запроса:**
- Параметр 'pin' равен '99999999999999' | 200 | ```json
[
  {
    "Propcode": "1-02-03-0004-0056",
    "Address": "г. Ош, ул. Ленина, 12",
    "Owner": "Саматов Самат Саматович",
    "Pin": "{{request.query.pin}}",
    "DocNum": "OSH-111222",
    "REG_DATE": "2015-11-10",
    "TERM_DATE": ""
  },
  {
    "Propcode": "1-02-03-0004-0057",
    "Address": "г. Ош, ул. Курманжан Датка, 200",
    "Owner": "Саматов Самат Саматович",
    "Pin": "{{request.query.pin}}",
    "DocNum": "OSH-333444",
    "REG_DATE": "2018-03-25",
    "TERM_DATE": ""
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 16 | Кадастр / search-pin-all / no-properties | **Метод:** `GET`
**URL:** `/api/internal/v1/search-pin-all`

**Параметры запроса:**
- Параметр 'pin' равен '00000000000000' | 200 | ```json
[]
``` | Стандартный сценарий работы. |
| 17 | Кадастр / search-pin-all / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/search-pin-all` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 18 | Кадастр / search-pin-all / single-property | **Метод:** `GET`
**URL:** `/api/internal/v1/search-pin-all`

**Параметры запроса:**
- Параметр 'pin' равен '88888888888888' | 200 | ```json
[
  {
    "Propcode": "4-01-01-0001-0123",
    "Address": "г. Каракол, ул. Абдрахманова, 120",
    "Owner": "Темиров Темир Темирович",
    "Pin": "{{request.query.pin}}",
    "DocNum": "IK-555444",
    "REG_DATE": "2019-11-20",
    "TERM_DATE": ""
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 19 | Паспорт / passport-data-by-psn / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/passport-data-by-psn`

**Параметры запроса:**
- Параметр 'series' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'series' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 20 | Паспорт / passport-data-by-psn / passport-found | **Метод:** `GET`
**URL:** `/api/internal/v1/passport-data-by-psn`

**Параметры запроса:**
- Параметр 'pin' равен '66666666666666'
- Параметр 'series' равен 'AN'
- Параметр 'number' равен '123456' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "surname": "Асанов",
  "name": "Асан",
  "patronymic": "Асанович",
  "patronymicIsAbsent": "false",
  "dateOfBirth": "1990-01-15",
  "nationality": "Кыргыз",
  "gender": "Мужской",
  "voidan": "false",
  "issuedDate": "2020-05-10",
  "expiryDate": "2030-05-09",
  "familyStatus": "Женат/Замужем",
  "addressRegion": "г. Бишкек",
  "addressDistrict": "Ленинский район",
  "addressStreet": "ул. Киевская",
  "addressHouse": "100",
  "addressApartment": "1",
  "regionId": "41701000000000",
  "districtId": "41701401000000",
  "cityId": 1,
  "streetId": 123,
  "houseId": 456
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 21 | Паспорт / passport-data-by-psn / passport-not-found | **Метод:** `GET`
**URL:** `/api/internal/v1/passport-data-by-psn`

**Параметры запроса:**
- Параметр 'pin' равен '77777777777777'
- Параметр 'series' равен 'ID'
- Параметр 'number' равен '654321' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "surname": null,
  "name": null,
  "patronymic": null,
  "patronymicIsAbsent": "true",
  "dateOfBirth": null,
  "nationality": null,
  "gender": null,
  "voidan": "true",
  "issuedDate": null,
  "expiryDate": null,
  "familyStatus": null,
  "addressRegion": null,
  "addressDistrict": null,
  "addressStreet": null,
  "addressHouse": null,
  "addressApartment": null,
  "regionId": null,
  "districtId": null,
  "cityId": null,
  "streetId": null,
  "houseId": null
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 22 | Паспорт / passport-data-by-psn / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/passport-data-by-psn` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 23 | Патент/Полис / get-patents-by-pin / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/get-patents-by-pin`

**Параметры запроса:**
- Параметр 'dateCurrent' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'dateCurrent' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 24 | Патент/Полис / get-patents-by-pin / multiple-documents | **Метод:** `GET`
**URL:** `/api/internal/v1/get-patents-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '22222222222222' | 200 | ```json
[
  {
    "id": 201,
    "createDate": "2022-05-20T11:00:00",
    "pin": "{{request.query.pin}}",
    "tin": "{{request.query.pin}}",
    "objectAddress": "г. Ош, ул. Ленина, 50",
    "finalAmount": 7500,
    "isArenda": true,
    "isFinalAmount": true,
    "parentId": 0,
    "isArendaAmount": true
  },
  {
    "id": 202,
    "createDate": "2023-03-15T15:30:00",
    "dateTo": "2024-03-14T23:59:59",
    "statusId": 1,
    "policyCost": "1200.00",
    "tin": "{{request.query.pin}}"
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 25 | Патент/Полис / get-patents-by-pin / no-documents | **Метод:** `GET`
**URL:** `/api/internal/v1/get-patents-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '33333333333333' | 200 | ```json
[]
``` | Стандартный сценарий работы. |
| 26 | Патент/Полис / get-patents-by-pin / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/get-patents-by-pin` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 27 | Патент/Полис / get-patents-by-pin / single-patent | **Метод:** `GET`
**URL:** `/api/internal/v1/get-patents-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '11111111111111' | 200 | ```json
[
  {
    "id": 101,
    "createDate": "2023-01-10T10:00:00",
    "pin": "{{request.query.pin}}",
    "tin": "{{request.query.pin}}",
    "objectAddress": "г. Бишкек, ул. Токтогула, 1",
    "finalAmount": 5000,
    "isArenda": false,
    "isFinalAmount": true,
    "parentId": 0,
    "isArendaAmount": false
  }
]
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 28 | Санарип Аймак / get-address-fact / address-found | **Метод:** `GET`
**URL:** `/api/internal/v1/get-address-fact`

**Параметры запроса:**
- Параметр 'pin' равен '44444444444444' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "personAddress": true,
  "status": "Actual",
  "region": "Чуйская область",
  "regionId": "41701000000000",
  "district": "г.Бишкек",
  "districtId": "41701400000000",
  "city": "Бишкек",
  "cityId": 1,
  "street": "проспект Манаса",
  "streetId": 123,
  "house": "101/1",
  "flat": "25"
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 29 | Санарип Аймак / get-address-fact / address-not-found | **Метод:** `GET`
**URL:** `/api/internal/v1/get-address-fact`

**Параметры запроса:**
- Параметр 'pin' равен '55555555555555' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "personAddress": false,
  "status": "Not Found",
  "region": "",
  "regionId": "",
  "district": "",
  "districtId": "",
  "city": "",
  "cityId": 0,
  "street": "",
  "streetId": 0,
  "house": "",
  "flat": ""
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 30 | Санарип Аймак / get-address-fact / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/get-address-fact`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 31 | Санарип Аймак / get-address-fact / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/get-address-fact` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 32 | Санарип Аймак / get-family-members / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/get-family-members`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 33 | Санарип Аймак / get-family-members / get-family-members-empty | **Метод:** `GET`
**URL:** `/api/internal/v1/get-family-members`

**Параметры запроса:**
- Параметр 'pin' равен '33333333333333' | 200 | ```json
{
  "code": "OK",
  "message": "Успешно",
  "members": []
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 34 | Санарип Аймак / get-family-members / get-family-members-multiple | **Метод:** `GET`
**URL:** `/api/internal/v1/get-family-members`

**Параметры запроса:**
- Параметр 'pin' равен '22222222222222' | 200 | ```json
{
  "code": "OK",
  "message": "Успешно",
  "members": [
    {
      "name": "Петров Петр Петрович",
      "role": "Глава семьи"
    },
    {
      "name": "Петрова Анна Ивановна",
      "role": "Супруга"
    }
  ]
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 35 | Санарип Аймак / get-family-members / get-family-members-single | **Метод:** `GET`
**URL:** `/api/internal/v1/get-family-members`

**Параметры запроса:**
- Параметр 'pin' равен '11111111111111' | 200 | ```json
{
  "code": "OK",
  "message": "Успешно",
  "members": [
    {
      "name": "Иванов Иван Иванович",
      "role": "Глава семьи"
    }
  ]
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 36 | Санарип Аймак / get-family-members / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/get-family-members` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 37 | ЗАГС / get-data-by-pin / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/get-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "faultCode": 400,
  "faultString": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 38 | ЗАГС / get-data-by-pin / found | **Метод:** `GET`
**URL:** `/api/internal/v1/get-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '11111111111111' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "name": "Иван",
  "surname": "Иванов",
  "patronymic": "Иванович",
  "gender": "Мужской",
  "maritalStatusId": 2,
  "maritalStatus": "Женат/Замужем",
  "nationalityId": 1,
  "nationality": "Кыргыз",
  "citizenshipId": 1,
  "citizenship": "Кыргызская Республика",
  "pinBlocked": false,
  "pinGenerationDate": "1990-01-01",
  "photo": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
  "deathDate": null,
  "faultCode": 0,
  "faultString": "OK"
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 39 | ЗАГС / get-data-by-pin / not-found-error | **Метод:** `GET`
**URL:** `/api/internal/v1/get-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '22222222222222' | 200 | ```json
{
  "pin": "{{request.query.pin}}",
  "name": null,
  "surname": null,
  "patronymic": null,
  "gender": null,
  "maritalStatusId": null,
  "maritalStatus": null,
  "nationalityId": null,
  "nationality": null,
  "citizenshipId": null,
  "citizenship": null,
  "pinBlocked": null,
  "pinGenerationDate": null,
  "photo": null,
  "deathDate": null,
  "faultCode": 1,
  "faultString": "Данные не найдены"
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 40 | ЗАГС / get-data-by-pin / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/get-data-by-pin` | 503 | ```json
{
  "faultCode": 503,
  "faultString": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |
| 41 | ЗАГС / get-death-act-data-by-pin / bad-request | **Метод:** `GET`
**URL:** `/api/internal/v1/get-death-act-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' отсутствует 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров (ошибка на стороне клиента). |
| 42 | ЗАГС / get-death-act-data-by-pin / found | **Метод:** `GET`
**URL:** `/api/internal/v1/get-death-act-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '11111111111111' | 200 | ```json
{
  "actDate": "2023-10-26",
  "actNo": "12345",
  "actOrgan": "ЗАГС г. Бишкек",
  "docDate": "2023-10-26",
  "docSeries": "V-ДР",
  "docNo": "987654",
  "certificate": "V-ДР №987654",
  "pin": "{{request.query.pin}}",
  "lastName": "Усопший",
  "firstName": "Пример",
  "patronymic": "Тестович",
  "deathDate": "2023-10-25",
  "deathTime": "14:30:00"
}
``` | Успешный сценарий (happy path), данные найдены и возвращены. |
| 43 | ЗАГС / get-death-act-data-by-pin / not-found | **Метод:** `GET`
**URL:** `/api/internal/v1/get-death-act-data-by-pin`

**Параметры запроса:**
- Параметр 'pin' равен '22222222222222' | 200 | ```json
{
  "actDate": null,
  "actNo": null,
  "actOrgan": null,
  "docDate": null,
  "docSeries": null,
  "docNo": null,
  "certificate": null,
  "pin": "{{request.query.pin}}",
  "lastName": null,
  "firstName": null,
  "patronymic": null,
  "deathDate": null,
  "deathTime": null
}
``` | Сценарий, когда данные не найдены (бизнес-ошибка). |
| 44 | ЗАГС / get-death-act-data-by-pin / service-unavailable | **Метод:** `GET`
**URL:** `/api/internal/v1/get-death-act-data-by-pin` | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности или внутренней ошибки внешнего сервиса. |