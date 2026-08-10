def find_winner(votes):

    frequency = {}

    for candidate in votes:
        frequency[candidate] = frequency.get(candidate, 0) + 1

    winner = None
    max_votes = 0

    for candidate, count in frequency.items():

        if count > max_votes:
            max_votes = count
            winner = candidate

        elif count == max_votes and candidate < winner:
            winner = candidate

    return winner


def main():

    votes = [2, 3, 1, 2, 3, 2, 2, 1]

    print("Winner Candidate ID =", find_winner(votes))


if __name__ == "__main__":
    main()