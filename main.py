"""One Star, Written in Sap — a houseplant's one-star review.

Reads the review line from entry.txt and prints it.
"""

import os


def load_review():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    review = load_review()
    if not review:
        raise SystemExit("entry.txt is empty — nothing to review.")
    print(review)


if __name__ == "__main__":
    main()
