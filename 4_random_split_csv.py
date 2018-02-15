# Author Eddy Almeida
# github : https://github.com/edeuxk/tensorflow-object-detection
import numpy as np
import pandas as pd

np.random.seed(1)
full_labels = pd.read_csv('data/generated_labels.csv')
full_labels.head()

grouped = full_labels.groupby(['filename','xmin'])
grouped.apply(lambda x: len(x)).value_counts()
# split each file into a group in a list
gb = full_labels.groupby(['filename','xmin'])
grouped_list = [gb.get_group(x) for x in gb.groups]

# I give 80 images to train with parameter size
size_for_test = int(len(grouped_list)*0.15) # will be used 
train_index = np.random.choice(len(grouped_list), size=(len(grouped_list) - size_for_test), replace=False)
# I also give the total range of my list
test_index = np.setdiff1d(list(range(len(grouped_list))), train_index)

print('Total records :', len(grouped_list))
print('[Random] Train records :', len(train_index), 'and test records :', len(test_index))

train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])

train.to_csv('data/train_labels.csv', index=None)
test.to_csv('data/test_labels.csv', index=None)
print('Successfully splitted files :)')
