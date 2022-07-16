from pathlib import Path

def get_input_path():
    return Path(__file__).absolute().parent.parent.joinpath("Input")

def get_input(day):
    input_path = get_input_path().joinpath(f"{day}.txt")
    with input_path.open("r") as f:
        return f.read()