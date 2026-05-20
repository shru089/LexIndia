from services.bootstrap import initialize_persistence


if __name__ == "__main__":
    initialize_persistence(seed_demo_data=True)
    print("LexIndia persistence initialized.")
