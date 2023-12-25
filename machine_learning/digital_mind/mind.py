from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

predctions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'giraffe.jpg'), result_count=5)
# result_count is how many predictions we want it to make
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')

predctions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'godzilla.jpg'), result_count=5)
# result_count is how many predictions we want it to make
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')

predctions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'house.jpg'), result_count=5)
# result_count is how many predictions we want it to make
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')
