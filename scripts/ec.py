import os
import yaml

ANSWERS_FILE_PATH='answers.yaml'

def load_input(input_path):
    with open(input_path) as f:
        data = f.read().split("\n")
    if len(data) == 0 or len(data[0]) == 0:
        return None
    return data


def run(part1=None, part2=None, part3=None, **kwargs):
    solvers = [part1, part2, part3]
    inputs = [[] for _ in range(3)]

    files = sorted(
        [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".txt")]
    )
    total_tests = 0
    for f in files:
        if f.startswith("input") and "1" <= f[5] <= "3":
            inputs[int(f[5]) - 1].append((f, True))
            total_tests += 1
        elif f.startswith("example") and "1" <= f[7] <= "3":
            inputs[int(f[7]) - 1].append((f, False))
            total_tests += 1
    assert total_tests < 256

    answers = {}
    if os.path.isfile(ANSWERS_FILE_PATH):
        with open(ANSWERS_FILE_PATH) as f:
            answers = yaml.safe_load(f)

    correct_answers = 0
    for i in range(3):
        if not callable(solvers[i]):
            continue

        for target, is_input in inputs[i]:
            input = load_input(target)
            if not input:
                print(
                    f"Failed to process {target}, expected at least one line of input."
                )
                continue
            try:
                if is_input and "input" in kwargs and str(i + 1) in kwargs["input"]:
                    ans = solvers[i](input, **kwargs["input"][str(i + 1)])
                elif (
                    not is_input
                    and "example" in kwargs
                    and str(i + 1) in kwargs["example"]
                ):
                    ans = solvers[i](input, **kwargs["example"][str(i + 1)])
                else:
                    ans = solvers[i](input)
                print(f"Part {i + 1} for {target}: {ans}", end = '')

                basename = os.path.splitext(target)[0]
                if basename in answers:
                    expected_ans = answers[basename]
                    if expected_ans == ans:
                        correct_answers += 1
                        print("   Correct!", end = '')
                    else:
                        print(f", expected {expected_ans}", end = '')
                print()
            except Exception as e:
                print(f"Failed to process {target}, exception: {str(e)}")
    return total_tests - correct_answers