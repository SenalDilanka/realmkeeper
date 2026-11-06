def fibonacci(n):
    """Generate the first n numbers of the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    print("✨ The Ancient Fibonacci Scroll ✨")
    print("=" * 35)
    fib = fibonacci(10)
    for i, num in enumerate(fib, 1):
        print(f"  Position {i:>2}: {num}")
    print("=" * 35)
    print(f"🔮 Sequence: {fib}")
