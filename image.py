maizeStage = [{"waterUsage" : "1mm", "stageName" : "Dormancy", "w"}]
wheatStage = [{"waterUsage" : ""}]

import sys
image_path = sys.argv[1]

imageType = ''
import tensorflow as tf, sys, os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()
# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
    in tf.gfile.GFile("/home/rahultarak12345/stonehill/ML/Inception/ML/retrained_labels.txt")]
# Unpersists graph from file
with tf.gfile.FastGFile("/home/rahultarak12345/stonehill/ML/Inception/ML/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
# Feed the image_data as input to the graph and get first prediction
print("Possible Results of the Image: (Ordered by Confidence)")
with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor,
    {'DecodeJpeg/contents:0': image_data})
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score * 100))
        if (score*100 >50):
            imageType = human_string

def split(var):
    var = str(var)
    var = var.split('-')
    var =  (var[1])
    var = var.split('.')
    return (var[1])
    
    
stageOfGrowth = split(image_path)
print("Best Predicted Crop Type :" + imageType)
print("Current Stage of Growth :" + stageOfGrowth)

#if (imageType == "maize"):
    #a
    
#elif (imageType =="common wheat"):
    #a
#import urllib.request
#contents = urllib.request.urlopen("https://etwas_tarak:lLE42epPtJ0rZ@api.meteomatics.com/now/t_2m:C,relative_humidity_2m:p,effective_cloud_cover:p/12.971599,77.594566/json").read()
#print(contents)
import requests 
URL = "https://etwas_tarak:lLE42epPtJ0rZ@api.meteomatics.com/now/t_2m:C,relative_humidity_2m:p,effective_cloud_cover:p/12.971599,77.594566/json"
r = requests.get(url = URL) 
data = r.json()
print(data)

