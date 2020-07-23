from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.datasets import load_breast_cancer, load_digits, make_classification, make_hastie_10_2

# get data set from standard library
# dataset = load_breast_cancer()
# dataset = load_digits()
# data = dataset.data
# labels = dataset.target

# dataset = make_classification(n_samples=1000, n_features=40)
dataset = make_hastie_10_2()
data = dataset[0]
labels = dataset[1]



possible_labels = list(dict.fromkeys(labels))

def get_label(val):
    curr = possible_labels[0]
    dist = abs(val - curr)
    for elem in possible_labels:
        d = abs(elem - val)
        if d <= dist:
            curr = elem
            dist = d
    return curr

def zero_one_error(actual_labels, predicted_labels):
    return sum(map(lambda p: 1 if p[0] != p[1] else 0, zip(actual_labels, predicted_labels))) / len(actual_labels)

# set aside a portion of the data for testing
training_data, testing_data, training_labels, testing_labels = train_test_split(data, labels, test_size=0.4, random_state=0)

# create, train, and classify with a linear separator
linear_separator = linear_model.LinearRegression()
linear_separator.fit(training_data, training_labels)
predicted_labels = list(map(get_label, linear_separator.predict(testing_data)))
print("Error using Linear Separator: " + str(zero_one_error(testing_labels, predicted_labels)))

# create, train, and classify with a decision tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(training_data, training_labels)
predicted_labels = decision_tree.predict(testing_data)
print("Error using a Decision Tree: " + str(zero_one_error(testing_labels, predicted_labels)))

# create, train, and classify with a neural network
neural_network = MLPClassifier()
neural_network.fit(training_data, training_labels)
predicted_labels = neural_network.predict(testing_data)
print("Error using a Neural Network: " + str(zero_one_error(testing_labels, predicted_labels)))
