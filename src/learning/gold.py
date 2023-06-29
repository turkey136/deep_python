from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# https://kkmax-develop.com/machinelearning-scikit-learn-1/

gold_data = pd.read_csv('../output/gold.csv')

count_s = len(gold_data)

# 株価の上昇率を算出、おおよそ-1.0～1.0の範囲に収まるように調整
modified_data = []
for i in range(1,count_s):
    modified_data.append(float(gold_data.loc[i,['gold_price']] - gold_data.loc[i-1,['gold_price']])/float(gold_data.loc[i-1,['gold_price']])*20)
# 要素数の設定
count_m = len(modified_data)

# 過去４日分の上昇率のデータを格納するリスト
successive_data = []

# 正解値を格納するリスト　価格上昇: 1 価格低下:0
answers = []

#  連続の上昇率のデータを格納していく
for i in range(4, count_m):
    successive_data.append([modified_data[i-4],modified_data[i-3],modified_data[i-2],modified_data[i-1]])
    # 上昇率が0以上なら1、そうでないなら0を格納
    if modified_data[i] > 0:
        answers.append(1)
    else:
        answers.append(0)

# データの分割（データの90%を訓練用に、10％をテスト用に分割する）
X_train, X_test, y_train, y_test =train_test_split(successive_data, answers, train_size=0.9,test_size=0.1,random_state=1)

# サポートベクターマシーン
clf = svm.LinearSVC()
# サポートベクターマシーンによる訓練
clf.fit(X_train , y_train)

# 学習後のモデルによるテスト
# トレーニングデータを用いた予測
y_train_pred = clf.predict(X_train)
# テストデータを用いた予測
y_val_pred = clf.predict(X_test)

# 正解率の計算
train_score = accuracy_score(y_train, y_train_pred)
test_score = accuracy_score(y_test, y_val_pred)

# 正解率を表示
print("トレーニングデータに対する正解率：" + str(train_score * 100) + "%")
print("テストデータに対する正解率：" + str(test_score * 100) + "%")
