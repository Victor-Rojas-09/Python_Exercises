def greedy(activities):
    """
    Greedy Activity Selection Algorithm

    Selects the maximum number of
    non-overlapping activities.
    """

    # Sort by ending time
    activities.sort(key=lambda x: x[1])

    selected = []

    # Pick first activity
    last_end = -1

    # Process activities
    for start, end in activities:

        # Select non-overlapping activity
        if start >= last_end:

            selected.append(
                (start, end)
            )

            last_end = end

    return selected


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------

activities = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (8, 9),
    (5, 9)
]

result = greedy(
    activities
)

print("Selected Activities:")
for activity in result:
    print(activity)