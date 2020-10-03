import csv
import numpy as np


def get_train_data():   # gets the training data set from the file
    file = open('train.csv', 'r')
    reader = csv.reader(file)
    train = []
    next(reader)  # to remove labels in the returned data
    for row in reader:
        train.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]])
    return train


def get_test_data():    # gets the test data set from the file
    file = open('test.csv', 'r')
    reader = csv.reader(file)
    test = []
    next(reader)  # to remove labels in the returned data
    for row in reader:
        test.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]])
    return test


def get_class_labels(train_data):   # gets the class labels and their frequency
    out_labels = {}
    for x in train_data:
        if x[-1] not in out_labels:
            out_labels[x[-1]] = 1
        else:
            out_labels[x[-1]] += 1
    return out_labels


def get_class_probability(train_data, class_labels):    # computes class probability for all the classes
    class_probability = {}
    train_data_len = len(train_data)
    for x in class_labels:
        temp = sum(p.count(x) for p in train_data)
        class_probability[x] = temp / train_data_len
    return class_probability


def get_mean_sigma(train_data, class_label):    # computes the mean and the covariance matrix for a given class
    feature_count = len(train_data[0]) - 1
    temp = []
    temp.append([p[:feature_count] for p in train_data if p[-1] == class_label])
    x = np.array(temp[0])
    x = np.transpose(x)
    sigma = np.cov(x)
    mean = np.mean(x, axis=1).reshape(4, 1)
    return mean, sigma


def get_mean_covariance(train_data, class_labels):  # calls get_mean_sigma function for all classes
    temp = {}
    for x in class_labels:
        temp[x] = ()
        mean_covariance = get_mean_sigma(train_data, x)
        temp[x] += mean_covariance
    return temp


def calculate_class_conditional(x, d, mean, covariance):     # calculates p(x) for the given features

    x_m = x - mean
    temp = (1. / (np.sqrt(((2 * np.pi) ** d) * np.linalg.det(covariance)))) * np.exp((-1 / 2) * (np.matmul(np.matmul(np.transpose(x_m), np.linalg.inv(covariance)),  x_m)))
    return temp[0][0]


def get_class_conditional(features, mean_covariance):   # calls calculate_class_conditional for all classes
    d = len(features)
    class_cond = {}
    for x in mean_covariance:
        temp = calculate_class_conditional(features, d, mean_covariance[x][0], mean_covariance[x][1])
        class_cond[x] = temp
    return class_cond


def predict(posterior, class_probability):  # returns the probability for each class
    denominator = 0
    for x in posterior:
        denominator += posterior[x] * class_probability[x]
    final_probab = {}
    for x in posterior:
        final_probab[x] = (posterior[x] * class_probability[x]) / denominator
    return final_probab


def data_prediction(class_probability, mean_covariance, data):   # calls the above functions appropriately for all the
    # test set examples and computes the accuracy
    accuracy = 0
    feature_count = len(data[0]) - 1
    for i in range(len(data)):
        temp = np.array(data[i][:feature_count]).reshape(feature_count, 1)
        class_conditional_probability = get_class_conditional(temp, mean_covariance)
        final_probability = predict(class_conditional_probability, class_probability)
        out_class = max(final_probability, key=lambda x: final_probability[x])
        print(data[i][0], data[i][1], data[i][2], data[i][3], 'predicted: ', out_class, ' actual: ',data[i][4])
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
    mean_covariance = get_mean_covariance(train_data, class_labels)
    test_data = get_test_data()
    test_accuracy = data_prediction(class_probability, mean_covariance, test_data)
    train_accuracy = data_prediction(class_probability, mean_covariance, train_data)

    print('accuracy on test set: ', test_accuracy)
    print('accuracy on train set: ', train_accuracy)
