import sender_requests as req

order_data = {
    "firstName": "Тест",
    "lastName": "Тестов",
    "address": "Тестовая улица, д.10",
    "metroStation": 156,
    "phone": "+78005553535",
    "delivery_date": "2025-05-05"
}

def create_order():
    return req.create_order(order_data).json().get("track")

track = create_order()

def test_get_order_data_by_track():
    response = req.get_order(track)
    assert response.status_code == 200
