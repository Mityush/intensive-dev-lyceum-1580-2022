def zip(*objects):
    answer = {}
    for obj in objects:
        for i, j in obj.items():
            if i not in answer:
                answer[i] = j
    return answer
