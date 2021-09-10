import json

from flask import request
from sqlalchemy import desc, asc

from models.pokemon import Pokemon


def pokemons(page, per_page, query):
    data = Pokemon.query

    # Build the base url to return in response
    base_url = request.base_url + "?"

    # Get the order and filter
    if query:
        base_url = base_url + "query=" + json.dumps(query, separators=(',', ':')) + "&"
        order = query.get('order', None)
        search = query.get('filter', None)

        if order:
            for attribute, value in order.items():
                if value == 'desc':
                    data = data.order_by(desc(getattr(Pokemon, attribute)))
                elif value == "asc":
                    data = data.order_by(asc(getattr(Pokemon, attribute)))
                else:
                    raise AttributeError("The order {} is not valid".format(value))

        if search:
            for attribute, value in search.items():
                data = data.filter(
                    getattr(Pokemon, attribute).like("%{}%".format(value)) if type(value) == str else (
                            getattr(Pokemon, attribute) == value)
                )

    data = data.paginate(page=page, per_page=per_page, max_per_page=50)
    next_page = None if not data.has_next else base_url + "page=" + str(data.next_num) + "&per_page=" + str(per_page)
    prev_page = None if not data.has_prev else base_url + "page=" + str(data.prev_num) + "&per_page=" + str(per_page)
    response_data = []
    for item in data.items:
        response_data.append({
            'number': item.number,
            'name': item.name,
            'type1': item.type1,
            'type2': item.type2,
            'total': item.total,
            'hp': item.hp,
            'attack': item.attack,
            'defense': item.defense,
            'speed_atk': item.speed_atk,
            'speed_def': item.speed_def,
            'speed': item.speed,
            'generation': item.generation,
            'legendary': item.legendary,
        })
    response = {
        'total': data.total,
        'next': next_page,
        'prev': prev_page,
        'data': response_data
    }
    return response
