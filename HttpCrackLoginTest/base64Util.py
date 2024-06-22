import base64


def base64decode(data):
    temp = data.encode("utf-8")
    content_b = base64.b64encode(temp)
    str_result = content_b.decode("utf-8")
    return str_result

