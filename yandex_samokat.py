import requests
import configurarion
import data


def create_new_order():
    return requests.post(configurarion.URL+configurarion.create_order, json=data.order)


def receive_order_by_number(track):
    return requests.get(configurarion.URL + configurarion.track + str(track))

