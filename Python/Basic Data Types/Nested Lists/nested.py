if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the list based on scores
    students.sort(key=lambda x: x[1])

    # Find the second lowest score
    second_lowest_score = sorted(set([score for name, score in students]))[1]

    # Filter students with the second lowest score
    second_lowest_students = [name for name, score in students if score == second_lowest_score]

    # Print names in sorted order
    print("\n".join(sorted(second_lowest_students)))