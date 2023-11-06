import yandex_samokat


def test_create_order():
    new_order = yandex_samokat.create_new_order()
    assert new_order.status_code == 201

# Анастасия Лазарева, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def test_receive_order():
    new_order = yandex_samokat.create_new_order()
    numbers_order = yandex_samokat.receive_order_by_number(new_order.json()['track'])
    assert numbers_order.status_code == 200
