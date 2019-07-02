# rosaidb: 労災データの抽出サンプル
Japanese only

## 目的
保育士の知人が職場で保育中に腰を痛めたので労災申請をしようとしたところ、そのような事例は聞いたことがないと言われたので、事実を確認するために作成しました。

## 労災データベース
労災の事例は厚生労働省の[職場のあんぜんサイト](http://anzeninfo.mhlw.go.jp/anzen_pgm/SHISYO_FND.aspx)で11年間分をダウンロード可能ですが、
月毎のExcelファイルに分かれているため、そのままでは横断検索ができません。
自分で根気よくダウンロードして結合しても、そのままでは行が多すぎて扱いづらいものになります。

そこで、フィルタリングして扱いやすいサイズにした上でExcelファイルにする簡単なスクリプトを作成しました。

## 使い方
### 準備
必要なライブラリを準備しておきます。

```
$ pip3 install pandas logzero xlrd xlwt openpyxl
```

### スクリプトの修正
今回は `災害状況` に `保育` を含むレコードを抽出してExcelファイルに保存しています。必要な条件に修正してください。なお、抽出条件を書かずにすべてを保存しようとしても非常に時間がかかります。

```
###### modify according to your purpose 
hoiku = df[df['災害状況'].str.contains('保育', na=False)]
hoiku.to_excel('rosai18-28.xlsx', sheet_name='hoiku')
```

### スクリプトの実行
```
$ python3 rosaidb.py
```
出力される Excelファイルにて必要な分析をしてください。

## 注意点
ダウンロード時、`db`というディレクトリが直下に作成され、そこに各ファイルがダウンロードされます。再実行時に利用されます。必要な分析が終わったら削除してください。

ダウンロードされるデータは厚生労働省に帰属するものですので、サイトの注意点に従い使用してください。
