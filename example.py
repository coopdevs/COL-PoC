#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from libs.col import col, constants

import sys


def format_cell(c):
    if not c:
        return ""
    if isinstance(c, (int, float)):
        c = str(int(100 * c)/100.0)
    return str.center(c, 12)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: {} <hostname> <port> <path>")
        exit

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    client = col.Col(hostname, port, filename)

    print("- Adding Bledes 3000m2 3€ 500kg")
    client.add_crops(constants.CU_BLEDES, 3000, 3, 500)

    print("- Adding Calçots 1000m2 2€ 500kg")
    client.add_crops(constants.CU_CALCOT, 1000, 2, 500)

    print("- Setting working costs: 5€/h qualified, 4€/h unqualified")
    client.set_working_costs(5, 4)

    print("- Getting Calçots operations costs table")
    for row in client.get_results_table(constants.CU_CALCOT, constants.CT_OPERATIONS_COSTS):
        print( " | ".join(map(format_cell, row)))

    print("- Getting Bledes operations costs table")
    for row in client.get_results_table(constants.CU_BLEDES, constants.CT_OPERATIONS_COSTS):
        print( " | ".join(map(format_cell, row)))

    print("- Getting Global operations costs table")
    for row in client.get_results_table("global", constants.CT_OPERATIONS_COSTS):
        print( " | ".join(map(format_cell, row)))

    print("- Getting global tractor schedule")
    for row in client.get_results_chart("global", constants.CT_TRACTOR_SCHEDULE):
        print( " | ".join(map(format_cell, row)))
