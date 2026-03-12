import itertools
import string

# Define the target password YOU chose
TARGET_PASSWORD = input("Enter your password: ")

# Define the character set and length range
CHARS = string.ascii_letters + string.digits + string.punctuation + " " # a-zA-Z0-9
MIN_LEN = 1
MAX_LEN = 10

def brute_force():
    if len(TARGET_PASSWORD) <= MAX_LEN:
        attempts = 0
        for length in range(MIN_LEN, MAX_LEN + 1):
            for combo in itertools.product(CHARS, repeat=length):
                attempts += 1
                candidate = "".join(combo)
                if candidate == TARGET_PASSWORD:
                    print(f"Found: {candidate} in {attempts} attempts")
                    return candidate
        print("Password not found in search space")
        return None
    else:
        print("Password is longer than maximum allowed length!")
        return None

if __name__ == "__main__":
    brute_force()
