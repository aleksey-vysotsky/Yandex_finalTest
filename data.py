# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# тело запроса для оформления заказа
order_body = {
    "firstName": "Vlad",
    "lastName": "Tester_1",
    "address": "Moscow, 20 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 35",
    "rentTime": 1,
    "deliveryDate": "2025-11-30",
    "comment": "Test_1",
    "color": [
        "BLACK"
    ]
}