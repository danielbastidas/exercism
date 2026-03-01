def sum_of_multiples(limit, multiples):

    energy_points = 0

    if limit != 0:
        magic_items_set = set()
        for magic_item in multiples:
            if magic_item != 0:
                i = 1
                while i * magic_item < limit:
                    magic_items_set.add(i * magic_item)
                    i = i + 1
                
        for magic_item_points in magic_items_set:
            energy_points = energy_points + magic_item_points

    return energy_points