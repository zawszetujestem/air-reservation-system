from plane import Plane


class AirbusA370(Plane):
    @staticmethod
    def get_name():
        return "Airbus A370"

    @staticmethod
    def get_seating_plan():
        return range(1, 24), "ABCDEG"
