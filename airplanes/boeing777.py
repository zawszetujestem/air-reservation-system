from plane import Plane


class Boeing777(Plane):
    @staticmethod
    def get_name():
        return "Boeing 777"

    @staticmethod
    def get_seating_plan():
        return range(1, 39), "ABCDEGHIK"
