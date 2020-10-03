import csv
import math


def get_train_data():  # gets the training data set from the file
    file = open('train.csv', 'r')
    reader = csv.reader(file)
    train = []
    next(reader)  # to remove labels in the returned data
    for row in reader:
        train.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]])
    return train


def get_test_data():  # gets the test data set from the file
    file = open('test.csv', 'r')
    reader = csv.reader(file)
    test = []
    next(reader)  # to remove labels in the returned data
    for row in reader:
        test.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]])
    return test


def get_class_labels(train_data):  # gets the class labels and their frequency
    out_labels = {}
    for x in train_data:
        if x[-1] not in out_labels:
            out_labels[x[-1]] = 1
        else:
            out_labels[x[-1]] += 1
    return out_labels


def get_class_probability(train_data, class_labels):  # computes class probability for all the classes
    class_probability = {}
    train_data_len = len(train_data)
    for x in class_labels:
        temp = sum(p.count(x) for p in train_data)
        class_probability[x] = temp / train_data_len
    return class_probability


def calculate_mean(col_number, train_data, out_label, label_count):  # calculates the mean for a given feature, for a given class
    summation = 0
    for x in train_data:
        if x[-1] == out_label:
            summation += x[col_number]
    return summation / label_count


def calculate_variance(mean, col_number, train_data, out_label, label_count):  # calculates the variance for a given feature, for a given class
    summation = 0
    for x in train_data:
        if x[-1] == out_label:
            summation += (x[col_number] - mean) ** 2
    return summation / label_count


def get_mean_and_variance(train_data, class_labels):  # calls the calculate_mean and calculate_variance functions for all features and classes
    mean_variance = {}
    for x in class_labels:
        mean_variance[x] = []
        for i in range(len(train_data[0]) - 1):
            temp_mean = calculate_mean(i, train_data, x, class_labels[x])
            temp_var = calculate_variance(temp_mean, i, train_data, x, class_labels[x])
            mean_variance[x].append([temp_mean, temp_var])
    return mean_variance


def calculate_class_conditional(x, mean, variance):  # calculates p(x) for the given features
    return (1 / (math.sqrt(2 * math.pi * variance))) * math.exp((-1 / 2) * (((x - mean) ** 2) / variance))


def get_class_conditional(features, mean_variance):
    class_cond = {}
    for x in mean_variance:
        class_cond[x] = []
        for i in range(4):
            temp = calculate_class_conditional(features[i], mean_variance[x][i][0], mean_variance[x][i][1])
            class_cond[x].append(temp)
    return class_cond


def get_posterier(class_cond):
    postirer = {}
    for x in class_cond:
        temp = 1
        for p in class_cond[x]:
            temp *= p
        postirer[x] = temp
    return postirer


def predict(posterier, class_probability):
    denominator = 0
    for x in posterier:
        denominator += posterier[x] * class_probability[x]
    final_probab = {}
    for x in posterier:
        final_probab[x] = (posterier[x] * class_probability[x]) / denominator
    return final_probab


def data_prediction(class_probability, mean_variance, data):
    accuracy = 0
    feature_count = len(data[0]) - 1
    for i in range(len(data)):
        class_conditional_probability = get_class_conditional(data[i][:feature_count], mean_variance)
        posterior = get_posterier(class_conditional_probability)
        final_probability = predict(posterior, class_probability)
        out_class = max(final_probability, key=lambda x: final_probability[x])
        print(data[i][0], data[i][1], data[i][2], data[i][3], 'predicted: ', out_class, ' actual: ', data[i][4])
        if out_class == data[i][4]:
            accuracy += 1
    accuracy = (accuracy / len(data)) * 100
    return accuracy


if __name__ == '__main__':
    train_data = get_train_data()
    class_labels = get_class_labels(train_data)
    # class_probability = get_class_probability(train_data, class_labels)
    class_probability = {}
    for x in class_labels:
        class_probability[x] = 1 / len(class_labels)  # as the priors are equal

    mean_variance = get_mean_and_variance(train_data, class_labels)
    test_data = get_test_data()
    test_accuracy = data_prediction(class_probability, mean_variance, test_data)
    train_accuracy = data_prediction(class_probability, mean_variance, train_data)

    print('accuracy on test set: ', test_accuracy)
    print('accuracy on training set: ', train_accuracy)
