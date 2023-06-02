import requests


def get_query(url, *params, **kwargs):

    return requests.get(url, *params, **kwargs)


def post_query(url, *args, **kwargs):

    return requests.post(url, *args, **kwargs)


def put_query(url, *args, **kwargs):

    return requests.put(url, *args, **kwargs)


def delete_query(url, **kwargs):

    return requests.delete(url, **kwargs)
