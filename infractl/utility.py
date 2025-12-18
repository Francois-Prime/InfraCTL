import os

def is_ci():
    if os.getenv("CI") == "true":
        print(f"CI detected - skipping terraform execution")
        return