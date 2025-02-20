"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # DONE: Load NEO data from the given CSV file.
    near_earth = []
    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for r in reader:
            object_ = NearEarthObject(**{'designation': r['pdes'],
                                         'hazardous': r['pha'],
                                         'name': r['name'],
                                         'diameter': r['diameter']})
            near_earth.append(object_)
    return near_earth


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # DONE: Load close approach data from the given JSON file.
    approaches = []
    with open(cad_json_path) as file:
        load = json.load(file)
        data = load['data']
        for i in load['data']:
            des, cd, dist, v_rel = i[0], i[3], i[4], i[7]
            object_ = CloseApproach(**{'designation': des,
                                       'time': cd,
                                       'distance': dist,
                                       'velocity': v_rel})
            approaches.append(object_)
    return approaches
