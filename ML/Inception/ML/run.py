import os
for i in range(1,10):
	os.system("python3 /home/rahultarak12345/stonehill/ML/Inception/ML/retrain.py --bottleneck_dir=/home/rahultarak12345/stonehill/ML/Inception/ML/bottlenecks --how_many_training_steps 1000  --model_dir=/home/rahultarak12345/stonehill/ML/Inception/ML/ --output_graph=/home/rahultarak12345/stonehill/ML/Inception/ML/retrained_graph.pb --output_labels=/home/rahultarak12345/stonehill/ML/Inception/ML/retrained_labels.txt --image_dir=/home/rahultarak12345/stonehill/ML/data")
