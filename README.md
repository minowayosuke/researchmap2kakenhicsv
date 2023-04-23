# researchmap2kakenhicsv
Researchmapの「講演・口頭発表等」の情報を、科研費の実績報告書（研究実績報告書）にインポート可能なcsvファイルとしてエクスポートします。

# 注意事項
- ChatGPT（GPT4）に作ってもらいました。
- このプログラムの利用により直接的または間接的に生じた、いかなる損害に関しても、その責任を負いません。

# とにかく楽したい人向けの手順
## Researchmapでjsonlファイルをエクスポート
Researchmapにログインして、エクスポート画面にすすみます。

<br>

|![researchmapでエクスポート](https://github.com/minowayosuke/researchmap2kakenhicsv/blob/images/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9B%E3%82%9A%E3%83%BC%E3%83%88.png)|
|---|

さらに、この画面でも「エクスポート」ボタンを押します。

<br>

|![researchmapでエクスポート](https://github.com/minowayosuke/researchmap2kakenhicsv/blob/images/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9B%E3%82%9A%E3%83%BC%E3%83%882.png)|
|---|

出力形式をjsonとして、「業績情報」の「講演・口頭発表等」だけをチェックし、エクスポートしたい期間を選び、最後にエクスポートを行います。

<br>

|![researchmapでエクスポート](https://github.com/minowayosuke/researchmap2kakenhicsv/blob/images/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9B%E3%82%9A%E3%83%BC%E3%83%883.png)|
|---|

「状態」が「処理待ち」になっていると思います。
しばらく待ってから「更新」して「状態」が「完了」になったら、該当のファイル名をクリックして、zipファイルをダウンロードします。zipを解凍する際に使うパスワードが表示されているので忘れずに。

解凍して得られたjsonlファイルを次で変換します。
## Google Colabでcsvに変換
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minowayosuke/researchmap2kakenhicsv/blob/main/researchmap_presentation2kakenhi.ipynb)
をクリックして、上部の「使い方」のとおりに作業を進めてcsvファイルをダウンロードしてください。

## 科研費のweb入力
科研費の実績報告書のweb入力の際にcsvをアップロードすることができます。

# 詳しく知りたい人向けの情報
科研費の実績報告書にアップロード可能なcsvファイルの形式は
>発表者名,発表標題,学会等名,発表年（開始）,発表年（終了）,招待講演の判定の有無（1が招待講演）,国際学会の判定の有無（1が国際学会）

です。
例えば

>"発表花子, 山田太郎",テスト発表について,テスト学会,2012,2012,1,0

>山田太郎,テスト発表について2,テスト学会2,2019,2019,0,0

>"Taro Yamada, Hanako Happyo",On a mock presentation, International conference of parody science,2018,2019,1,1

のような内容でしょう。
注意として
- 文字コードがShift_JISの必要があります
- 改行コードはCR + LF の必要があります
- コンマの前後にスペースを入れないこと。特に最後の2項目の前後にスペースがあるとうまくいきません。
