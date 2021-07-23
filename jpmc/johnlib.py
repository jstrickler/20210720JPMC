
ANIMAL = "wombat"

def spam():
    print("Hello from spam()")

def _ham():   # "private"
    print("   and _ham()")

def toast():
    print("Hello from toast()")
    _ham()

def get_animal():
    return ANIMAL
