"""
[実行方法] Anaconda Promptで streamlit環境を起動して
streamlit run simple_app.py
コマンドを実行する。

処理を止めるには、 Ctrl + c 
"""

import streamlit as st  

#　タイトル表示
st.title("簡単な Streamlit アプリ")

#　ユーザーにテキスト入力してもらう
name = st.text_input("あなたの名前を入力してください")

#　ユーザーにスタイダーで入力してもらう (最小値、最大値、デフォルト値)
age = st.slider("年齢を選んでください", 0, 100, 25)

#　結果表示
if name:   # nameという変数が空(null)でなかったら
    st.write(f"こんにちは、{name}さん！ あなたは{age}歳ですね。")
    st.write(f"{age}って人間には見えないですけど")
else:
    st.write("上の入力欄に名前を入力してください。")