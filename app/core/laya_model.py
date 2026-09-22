import laya


def load_laya():
    """Load and return the Laya decision model."""
    return laya.load("convaiinnovations/laya")

if __name__ == "__main__":
    model = load_laya()

    print(model)


    