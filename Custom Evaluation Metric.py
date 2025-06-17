def my_weighted_score(y_true, y_pred):
    correct = 0
    total = 0
    for i in range(len(y_true)):
        if y_true[i] == 1:
            total += 2
            if y_pred[i] == 1:
                correct += 2
        else:
            total += 1
            if y_pred[i] == 0:
                correct += 1
    return correct / total