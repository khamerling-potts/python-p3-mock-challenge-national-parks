#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")
    breakpoint()
    vis_1 = Visitor("Tammothy")
    vis_2 = Visitor("Bryce")
    vis_3 = Visitor("Wolfe")
    p_1 = NationalPark("Alaska Wilds")

    Trip(vis_1, p_1, "February 2nd", "February 3rd")
    Trip(vis_2, p_1, "February 5th", "February 9th")

    assert vis_1 in p_1.visitors()
    assert vis_2 in p_1.visitors()
    assert vis_3 not in p_1.visitors()
    ipdb.set_trace()
