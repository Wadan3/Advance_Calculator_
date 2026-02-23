import math
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Tuple

Number = float


# ----------------------------
# Input helpers
# ----------------------------
def read_float(prompt: str, *, allow_empty: bool = False) -> Optional[Number]:
    """
    Read a float from input.
    If allow_empty=True, empty input returns None.
    Keeps asking until valid.
    """
    while True:
        raw = input(prompt).strip()
        if allow_empty and raw == "":
            return None
        try:
            return float(raw)
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def read_choice(prompt: str, valid: set[str]) -> str:
    """Read a menu choice that must be in `valid`."""
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print("❌ Invalid choice. Please try again.")


# ----------------------------
# Operations
# ----------------------------
def add(a: Number, b: Number) -> Number:
    return a + b


def sub(a: Number, b: Number) -> Number:
    return a - b


def mul(a: Number, b: Number) -> Number:
    return a * b


def div(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def power(a: Number, b: Number) -> Number:
    return a ** b


def sqrt_op(x: Number) -> Number:
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)


def log_op(x: Number, base: Optional[Number]) -> Number:
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    if base is None:
        return math.log(x)  # natural log
    if base <= 0 or base == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    return math.log(x, base)


def sin_deg(angle_deg: Number) -> Number:
    return math.sin(math.radians(angle_deg))


def cos_deg(angle_deg: Number) -> Number:
    return math.cos(math.radians(angle_deg))


def tan_deg(angle_deg: Number) -> Number:
    # Guard: tan blows up near 90 + k*180
    r = math.radians(angle_deg)
    c = math.cos(r)
    if abs(c) < 1e-12:
        raise ValueError("Tangent is undefined for angles where cosine is 0 (e.g., 90°, 270°, ...).")
    return math.tan(r)


# ----------------------------
# Menu system
# ----------------------------
@dataclass(frozen=True)
class MenuItem:
    key: str
    label: str
    handler: Callable[[], None]


def print_header() -> None:
    print("\n" + "=" * 38)
    print("      Advanced Calculator (Pro)")
    print("=" * 38)


def show_menu(items: Dict[str, MenuItem]) -> None:
    print_header()
    print("Select an operation:")
    for k in sorted(items.keys(), key=lambda x: int(x) if x.isdigit() else 999):
        print(f"{k}. {items[k].label}")


def run_binary_op(name: str, op: Callable[[Number, Number], Number]) -> None:
    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")
    try:
        result = op(a, b)  # type: ignore[arg-type]
        print(f"✅ {name} result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")


def run_unary_op(name: str, op: Callable[[Number], Number], prompt: str) -> None:
    x = read_float(prompt)
    try:
        result = op(x)  # type: ignore[arg-type]
        print(f"✅ {name} result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")


def run_log() -> None:
    x = read_float("Enter the number: ")
    base = read_float("Enter the base (press Enter for e): ", allow_empty=True)
    try:
        result = log_op(x, base)  # type: ignore[arg-type]
        base_label = "e" if base is None else str(base)
        print(f"✅ log base {base_label} result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main() -> None:
    items: Dict[str, MenuItem] = {}

    items["1"] = MenuItem("1", "Addition (+)", lambda: run_binary_op("Addition", add))
    items["2"] = MenuItem("2", "Subtraction (-)", lambda: run_binary_op("Subtraction", sub))
    items["3"] = MenuItem("3", "Multiplication (*)", lambda: run_binary_op("Multiplication", mul))
    items["4"] = MenuItem("4", "Division (/)", lambda: run_binary_op("Division", div))
    items["5"] = MenuItem("5", "Power (^)", lambda: run_binary_op("Power", power))

    items["6"] = MenuItem("6", "Square Root (√)", lambda: run_unary_op("Square Root", sqrt_op, "Enter the number: "))
    items["7"] = MenuItem("7", "Logarithm (log)", run_log)

    items["8"] = MenuItem("8", "Sine (sin)", lambda: run_unary_op("Sine", sin_deg, "Enter the angle (degrees): "))
    items["9"] = MenuItem("9", "Cosine (cos)", lambda: run_unary_op("Cosine", cos_deg, "Enter the angle (degrees): "))
    items["10"] = MenuItem("10", "Tangent (tan)", lambda: run_unary_op("Tangent", tan_deg, "Enter the angle (degrees): "))

    items["11"] = MenuItem("11", "Exit", lambda: None)

    valid_choices = set(items.keys())

    while True:
        show_menu(items)
        choice = read_choice("Enter your choice (1-11): ", valid_choices)

        if choice == "11":
            print("👋 Exiting the calculator. Goodbye!")
            break

        items[choice].handler()
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
