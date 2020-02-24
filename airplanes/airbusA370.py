from plane import Plane

class AirbusA370(Plane):
    def get_name(self):
        return "Airbus A370"

    def get_seating_plan(self):
        return range(1, 24), "ABCDEG"
