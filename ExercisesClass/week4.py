def string_rect(string, w, h):
    if not string:
        return ""

    def build_row():
        repeated = (string * ((w // len(string)) + 1))[:w]
        return repeated


