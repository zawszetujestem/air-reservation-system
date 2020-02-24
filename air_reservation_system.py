from pprint import pprint as pp

from flight import Flight
from airplanes import *
from helpers import *

def make_flight():
    f = Flight("LO124", AirbusA370())
    # print(airplane.get_num_seats())
    # print(f.flight_number)
    # print(f.get_airline())
    # print(f.get_flight_number())
    # print(f.get_plane())
    # UML -
    f.allocate_passenger(passenger="Juliusz Cezar", seat="23D")
    f.allocate_passenger(passenger="Obelix", seat="23G")
    f.allocate_passenger(passenger="Asterix", seat="23E")
    f.allocate_passenger(passenger="Moja stara", seat="1A")
    f.allocate_passenger(passenger="Julek", seat="2D")
    f.allocate_passenger()
    f.relocate_passenger("1A", "23C")
    pp(f.seats)
    print(f.num_empty_seats())
    f.print_tickets(card_printer)


make_flight()
