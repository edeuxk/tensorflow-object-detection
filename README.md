# For first time use please run this :
`git clone https://github.com/tensorflow/models`

``cd models/research ; export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim ; protoc object_detection/protos/*.proto --python_out=. ; cd ../..``

``cd data ; wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz ; tar -xzf ssd_mobilenet_v1_coco_11_06_2017.tar.gz``

## 1 - Convert video to images
`sh 1_movie_to_images.sh`

## 2 - After labeling please resize convert to csv randomly
- `python 2_resize_images.py`
- `python 3_xml_to_csv.py`
- `python 4_random_split_csv.py`

## 3 - Generate TF Files for Tensorflow
### Modify ssd_mobilenet_v1_pets.config to your files.
- Create train data:
`python 5_generate_tf_records.py --csv_input=data/train_labels.csv  --output_path=data/train.record`
- Create test data:
`python 5_generate_tf_records.py --csv_input=data/test_labels.csv  --output_path=data/test.record`

## 4 - Train your models
### Start training
- You need to follow the instructions
`echo 6_training_job.txt`

### Start evaluation
- You need to follow the instructions
`echo 6_evaluation_job.txt`

### Start Tensorbard
``tensorboard --logdir=`pwd`/train``

## 5 - Run OpenCV
`python 7_object_detection_app.py`
or do it by multithreading
`python 7_object_detection_multithreading.py`
