| № | Сценарий | Условие (входные данные) | Код ответа (HTTP) | Пример ответа (Response body) | Примечания |
|---|---|---|---|---|---|
| 1 | gns/tp-business-activity-by-pin/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 2 | gns/tp-business-activity-by-pin/found | Query param 'pin' equalTo '11111111111111' | 200 | ```json
{
  "Farm": "Крестьянское хозяйство 'Агро'",
  "FullName": "Иванов Иван Иванович",
  "RayonCode": "003",
  "RayonName": "Свердловский р-н",
  "TaxActiveDate": "2022-08-09T00:00:00",
  "TaxTypeCode": "1020",
  "TIN": "{{request.query.pin}}"
}
``` | Happy-path сценарий, полный корректный ответ |
| 3 | gns/tp-business-activity-by-pin/not-found | Query param 'pin' equalTo '22222222222222' | 200 | ```json
{
  "Farm": null,
  "FullName": null,
  "RayonCode": null,
  "RayonName": null,
  "TaxActiveDate": null,
  "TaxTypeCode": null,
  "TIN": "{{request.query.pin}}"
}
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 4 | gns/tp-business-activity-by-pin/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 5 | kadastr/search-all-by-full-name/bad-request | Query param 'firstname' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'firstname' является обязательным"
}
``` | Проверка валидации входных параметров |
| 6 | kadastr/search-all-by-full-name/multiple-properties | Query param 'surname' equalTo 'Петров', Query param 'firstname' equalTo 'Петр' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 7 | kadastr/search-all-by-full-name/no-properties | Query param 'surname' equalTo 'Сидоров', Query param 'firstname' equalTo 'Сидор' | 200 | ```json
[]
``` | N/A |
| 8 | kadastr/search-all-by-full-name/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 9 | kadastr/search-all-by-full-name/single-property | Query param 'surname' equalTo 'Иванов', Query param 'firstname' equalTo 'Иван' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 10 | kadastr/search-all-by-prop-code/bad-request | Query param 'propCode' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'propCode' является обязательным"
}
``` | Проверка валидации входных параметров |
| 11 | kadastr/search-all-by-prop-code/property-found | Query param 'propCode' equalTo 'PROP123' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 12 | kadastr/search-all-by-prop-code/property-not-found | Query param 'propCode' equalTo 'PROP999' | 200 | ```json
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
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 13 | kadastr/search-all-by-prop-code/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 14 | kadastr/search-pin-all/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 15 | kadastr/search-pin-all/multiple-properties | Query param 'pin' equalTo '99999999999999' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 16 | kadastr/search-pin-all/no-properties | Query param 'pin' equalTo '00000000000000' | 200 | ```json
[]
``` | N/A |
| 17 | kadastr/search-pin-all/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 18 | kadastr/search-pin-all/single-property | Query param 'pin' equalTo '88888888888888' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 19 | passport/passport-data-by-psn/bad-request | Query param 'series' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'series' является обязательным"
}
``` | Проверка валидации входных параметров |
| 20 | passport/passport-data-by-psn/passport-found | Query param 'pin' equalTo '66666666666666', Query param 'series' equalTo 'AN', Query param 'number' equalTo '123456' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 21 | passport/passport-data-by-psn/passport-not-found | Query param 'pin' equalTo '77777777777777', Query param 'series' equalTo 'ID', Query param 'number' equalTo '654321' | 200 | ```json
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
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 22 | passport/passport-data-by-psn/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 23 | patent-polis/get-patents-by-pin/bad-request | Query param 'dateCurrent' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'dateCurrent' является обязательным"
}
``` | Проверка валидации входных параметров |
| 24 | patent-polis/get-patents-by-pin/multiple-documents | Query param 'pin' equalTo '22222222222222' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 25 | patent-polis/get-patents-by-pin/no-documents | Query param 'pin' equalTo '33333333333333' | 200 | ```json
[]
``` | N/A |
| 26 | patent-polis/get-patents-by-pin/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 27 | patent-polis/get-patents-by-pin/single-patent | Query param 'pin' equalTo '11111111111111' | 200 | ```json
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
``` | N/A |
| 28 | sanarip-aymak/get-address-fact/address-found | Query param 'pin' equalTo '44444444444444' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 29 | sanarip-aymak/get-address-fact/address-not-found | Query param 'pin' equalTo '55555555555555' | 200 | ```json
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
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 30 | sanarip-aymak/get-address-fact/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 31 | sanarip-aymak/get-address-fact/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 32 | sanarip-aymak/get-family-members/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 33 | sanarip-aymak/get-family-members/get-family-members-empty | Query param 'pin' equalTo '33333333333333' | 200 | ```json
{
  "code": "OK",
  "message": "Успешно",
  "members": []
}
``` | N/A |
| 34 | sanarip-aymak/get-family-members/get-family-members-multiple | Query param 'pin' equalTo '22222222222222' | 200 | ```json
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
``` | N/A |
| 35 | sanarip-aymak/get-family-members/get-family-members-single | Query param 'pin' equalTo '11111111111111' | 200 | ```json
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
``` | N/A |
| 36 | sanarip-aymak/get-family-members/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 37 | zags/get-data-by-pin/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "faultCode": 400,
  "faultString": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 38 | zags/get-data-by-pin/found | Query param 'pin' equalTo '11111111111111' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 39 | zags/get-data-by-pin/not-found-error | Query param 'pin' equalTo '22222222222222' | 200 | ```json
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
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 40 | zags/get-data-by-pin/service-unavailable | Любой запрос | 503 | ```json
{
  "faultCode": 503,
  "faultString": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |
| 41 | zags/get-death-act-data-by-pin/bad-request | Query param 'pin' absent 'True' | 400 | ```json
{
  "code": "BAD_REQUEST",
  "message": "Параметр 'pin' является обязательным"
}
``` | Проверка валидации входных параметров |
| 42 | zags/get-death-act-data-by-pin/found | Query param 'pin' equalTo '11111111111111' | 200 | ```json
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
``` | Happy-path сценарий, полный корректный ответ |
| 43 | zags/get-death-act-data-by-pin/not-found | Query param 'pin' equalTo '22222222222222' | 200 | ```json
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
``` | Ответ соответствует бизнес-ошибке (данных нет) |
| 44 | zags/get-death-act-data-by-pin/service-unavailable | Любой запрос | 503 | ```json
{
  "code": "SERVICE_UNAVAILABLE",
  "message": "Сервис временно недоступен"
}
``` | Проверка обработки недоступности внешнего сервиса |