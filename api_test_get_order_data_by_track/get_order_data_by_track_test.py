import data
import sender_requests as req

# Татьяна Петракова, 28-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_data_by_track():
    create_order_response = req.create_order(data.order_data).json()
    track = create_order_response.get("track")
    get_order_response = req.get_order(track)
    assert get_order_response.status_code == 200
