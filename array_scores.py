import sys

def calculate_sum(scores):
    """calculate sum of given scores."""
    return sum(scores)

def calculate_average(scores):
    """calculate average of given scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

if __name__ == "__main__":
    print("=== Array Scores Processor (main branch) ===")
    try:
        # Case 1: CLI arguments passed (for Jenkins)
        if len(sys.argv) > 1:
            scores = []
            for x in sys.argv[1:]:
                scores.append(int(x))  # converts to integer only

        # Case 2: Console input
        else:
            raw_input_value = input("Enter integer scores: ")
            parts = raw_input_value.split()
            scores = []
            for x in parts:
                scores.append(int(x))  # converts to integer only

        print("\n=== Program Parameters ===")
        print("Scores entered:", scores)

        total = calculate_sum(scores)
        avg = calculate_average(scores)

        print(f"Sum of scores: {total}")
        print(f"Average of scores: {avg:.2f}")

    except Exception as e:
        print("Error:", e)
