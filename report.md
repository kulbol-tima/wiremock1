# Отчет о моковых данных

Этот отчет содержит анализ моковых данных, используемых для эмуляции различных сервисов.
## Endpoint: `/asb/asb-address`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| No addresses | `POST` | `200` |  |
| One address | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Two addresses | `POST` | `200` |  |

## Endpoint: `/gns/tp-business-activity-by-pin`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Found | `POST` | `200` |  |
| Not found | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/kadastr/search-all-by-full-name`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Multiple properties | `POST` | `200` |  |
| No properties | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Single property | `POST` | `200` |  |

## Endpoint: `/kadastr/search-all-by-prop-code`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Property found | `POST` | `200` |  |
| Property not found | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/kadastr/search-pin-all`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Multiple properties | `POST` | `200` |  |
| No properties | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Single property | `POST` | `200` |  |

## Endpoint: `/passport/passport-data-by-psn`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Passport found | `POST` | `200` |  |
| Passport not found | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/patent-polis/get-patents-by-pin`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Multiple documents | `POST` | `200` |  |
| No documents | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Single patent | `POST` | `200` |  |

## Endpoint: `/sanarip-aymak/get-address-fact`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Address found | `POST` | `200` |  |
| Address not found | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/sanarip-aymak/get-family-members`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Get family members empty | `POST` | `200` |  |
| Get family members multiple | `POST` | `200` |  |
| Get family members single | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/sf-kr/get-pension-info`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| No objects | `POST` | `200` |  |
| One object | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Two objects | `POST` | `200` |  |

## Endpoint: `/sf-kr/get-pension-info-with-sum`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| No objects | `POST` | `200` |  |
| One object | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Two objects | `POST` | `200` |  |

## Endpoint: `/sf-kr/get-work-period-info`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| No objects | `POST` | `200` |  |
| One object | `POST` | `200` |  |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
| Two objects | `POST` | `200` |  |

## Endpoint: `/zags/get-data-by-pin`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Found | `POST` | `200` |  |
| Not found error | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |

## Endpoint: `/zags/get-death-act-data-by-pin`

| Сценарий | HTTP Метод | Код ответа | Примечания |
|---|---|---|---|
| Bad request | `POST` | `400` | Сценарий связан с ошибкой 400. |
| Found | `POST` | `200` |  |
| Not found | `POST` | `404` | Сценарий связан с ошибкой 404. |
| Service unavailable | `POST` | `503` | Сценарий связан с ошибкой 503. |
