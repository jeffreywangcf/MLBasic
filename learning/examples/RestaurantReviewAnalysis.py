from learning.machinelearning import classify
from learning.Helper import DataPreprocessing


demo = DataPreprocessing()
demo.readParagraph("sushiReview.txt", True, '\t')
demo.convertLevelToBinary()
demo.balanceDataSet()
dictionary, wordMat = demo.wordBagging(demo.LANG_ENGLISH, demo.SETTYPE_NDARRAY, lambda x: len(x) > 2)

model = classify.NaiveBayes()
model.DataSet = wordMat
model.Labels = demo.Label
test_data, test_label, indexes = model.SeparateDataSet(0.1, if_return=True)

testWords = list()
for index in indexes:
    testWords.append(demo.DataSet[index])

model.WordMat = model.DataSet
model.Dictionary = dictionary
model.BuildModel()

model.ResultLabels = ("negative", "positive")
error, predicted = model.SmartTest(test_data, testWords, test_label)
print("error rate: %.6f%%"%(error*100))