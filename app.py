import random
import streamlit as st

st.set_page_config(page_title="しごとのあいぼう β", page_icon="🤝", layout="centered")

st.title("🤝 しごとのあいぼう β")
st.caption("働く人の、今日を支える小さな相棒。")

st.divider()

# -------------------------
# ② 今日のタスク（最小）
# -------------------------
st.subheader("② 今日のタスク")
if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("add_task", clear_on_submit=True):
    task_text = st.text_input("タスクを追加", placeholder="例：見積作成、メール返信、資料修正…")
    submitted = st.form_submit_button("追加")
    if submitted and task_text.strip():
        st.session_state.tasks.append({"text": task_text.strip(), "done": False})

if st.session_state.tasks:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.12, 0.88])
        with col1:
            done = st.checkbox("", value=t["done"], key=f"done_{i}")
        with col2:
            st.write(t["text"])
        st.session_state.tasks[i]["done"] = done

    done_count = sum(1 for t in st.session_state.tasks if t["done"])
    st.caption(f"完了：{done_count} / {len(st.session_state.tasks)}")
else:
    st.info("タスクを追加すると、ここに一覧が出ます。まずは1つだけでもOK。")

st.divider()

# -------------------------
# ⑤ 給料逆算（最小）
# -------------------------
st.subheader("⑤ 給料逆算（今日のがんばりを見える化）")

pay_type = st.radio("給与のタイプ", ["時給", "月給"], horizontal=True)

if pay_type == "時給":
    hourly = st.number_input("時給（円）", min_value=0, step=50, value=1200)
    hours = st.number_input("今日働いた時間（時間）", min_value=0.0, step=0.25, value=2.0)
    value = int(hourly * hours)
else:
    monthly = st.number_input("月給（円）", min_value=0, step=5000, value=220000)
    workdays = st.number_input("月の稼働日数（目安）", min_value=1, step=1, value=20)
    hours = st.number_input("今日働いた時間（時間）", min_value=0.0, step=0.25, value=2.0)
    daily = monthly / workdays
    hourly = daily / 8
    value = int(hourly * hours)

st.metric("今日積み上がった価値（目安）", f"{value:,} 円")

st.caption("※目安です。あなたの価値は、お金だけじゃ測れないけど…“今日も積み上がってる”のは事実。")

st.divider()

# -------------------------
# ⑧ ワンポイント法令（超ミニ）
# -------------------------
st.subheader("⑧ 働く人へのワンポイント法令（β）")

LAW_TIPS = [
    ("休憩って必ず取れる？", "労働時間が6時間超→45分以上、8時間超→60分以上の休憩が原則。"),
    ("有給って断られるの？", "年次有給休暇は原則取得できます。時季変更権は“事業の正常な運営を妨げる場合”など限定的。"),
    ("サービス残業はOK？", "原則NG。『業務命令』や『黙示の指示』で働いた分は賃金の対象になり得ます。"),
    ("残業代っていくら？", "法定時間外（1日8h/週40h超）は割増賃金が必要。深夜や休日はさらに加算。"),
    ("副業って禁止できる？", "会社の規程次第。ただし一律禁止が常に妥当とは限らず、競業・健康・情報漏洩などが論点。"),
]

mode = st.radio("表示モード", ["今日の1つ", "逆引き（Q→A）"], horizontal=True)

if mode == "今日の1つ":
    q, a = random.choice(LAW_TIPS)
    st.write(f"**Q：{q}**")
    st.write(f"**A：** {a}")
else:
    q_list = [q for q, _ in LAW_TIPS]
    selected_q = st.selectbox("気になる質問を選ぶ", q_list)
    a = dict(LAW_TIPS)[selected_q]
    st.write(f"**A：** {a}")

st.caption("※これは一般的な情報です。個別の案件は地域の労働局・社労士・弁護士等に相談を推奨。")

st.divider()
st.caption("β版：機能はこれから増やしていきます。フィードバック歓迎。")
