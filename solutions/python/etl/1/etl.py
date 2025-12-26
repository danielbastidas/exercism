def transform(legacy_data):
    transformed_dict = {}
    for point in legacy_data:
        for letter in legacy_data[point]:
            transformed_dict[str.lower(letter)] = point
    dict(sorted(transformed_dict.items(), key=lambda letter: letter[1]))
    return transformed_dict
