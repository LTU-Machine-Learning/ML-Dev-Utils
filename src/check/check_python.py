
def hello():
    print("Hello Python!")


def show_python_path():
    import os
    import sys

    print(sys.path)
    print(os.environ['PYTHONPATH'].split(os.pathsep))


if __name__ == "__main__":
    hello()
    show_python_path()
