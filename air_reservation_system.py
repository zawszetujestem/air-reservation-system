from pprint import pprint as pp

from flight import Flight
from airplanes import *
from helpers import *


def make_flight():
    f = Flight("LO124", AirbusA370())
    f.allocate_passenger(passenger="Juliusz Cezar", seat="2D")
    f.allocate_passenger(passenger="Obelix", seat="1G")
    f.allocate_passenger(passenger="Asterix", seat="3E")
    f.allocate_passenger(passenger="Julek", seat="4D")
    f.allocate_passenger()
    f.relocate_passenger("4D", "23C")
    f.relocate_passenger("1G", "7C")
    pp(f.seats)
    f.print_tickets(card_printer)
    print(f"Number of empty seats: {f.num_empty_seats()}")


make_flight()
