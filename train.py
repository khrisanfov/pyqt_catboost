#!/usr/bin/env python3
import os
import catboost
import lightgbm as lgb
from catboost import datasets
from catboost.utils import create_cd

(train_df, test_df) = catboost.datasets.amazon()
y = train_df.ACTION
X = train_df.drop('ACTION', axis=1)
# cat_features = list(range(0, X.shape[1]))

dataset_dir = './amazon'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

train_df.to_csv(
    os.path.join(dataset_dir, 'train.csv'),
    index=False, sep=',', header=True
)
test_df.to_csv(
    os.path.join(dataset_dir, 'test.csv'),
    index=False, sep=',', header=True
)

feature_names = dict()
for column, name in enumerate(train_df):
    if column == 0:
        continue
    feature_names[column - 1] = name

create_cd(
    label=0,
    cat_features=list(range(1, train_df.columns.shape[0])),
    feature_names=feature_names,
    output_path=os.path.join(dataset_dir, 'train.cd')
)

pool = catboost.Pool(
    data=os.path.join(dataset_dir, 'train.csv'),
    delimiter=',',
    column_description=os.path.join(dataset_dir, 'train.cd'),
    has_header=True
)

model = catboost.CatBoostClassifier(
    iterations=100,
    learning_rate=0.03,
)
model.fit(
    pool,
    verbose=True
)
model.save_model('./catboost_model.bin')

train = lgb.Dataset(X, y)
booster = lgb.train({
    'learning_rate': 0.03
}, train, 100)
booster.save_model('./lightgbm_model.bin')
