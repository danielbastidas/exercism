"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list, = wagons
    return list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    first_wagon_id, second_wagon_id, *remaining_wagon_ids = each_wagons_id
    *fixed_wagon_ids, = *remaining_wagon_ids, first_wagon_id, second_wagon_id

    first_fixed_wagon_id, *remaining_fixed_wagon_ids = fixed_wagon_ids
    *fixed_wagon_ids, = first_fixed_wagon_id, *missing_wagons, *remaining_fixed_wagon_ids

    return fixed_wagon_ids


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    stops_dict = {}
    *stops_dict["stops"], = stops.values()

    route = {**route, **stops_dict}
    
    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    [[*column1], [*column2], [*column3]] = zip(wagons_rows[0], wagons_rows[1], wagons_rows[2])
    return [column1, column2, column3]

    
    
