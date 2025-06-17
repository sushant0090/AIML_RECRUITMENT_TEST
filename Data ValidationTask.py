def validate_data(data):
    result = []
    for item in data:
        if type(item["age"]) != int:
            result.append(item)
    return result


