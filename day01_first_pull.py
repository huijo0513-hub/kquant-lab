"""2026-08-26 Day 1 — 삼성전자 일봉 첫 수집"""
from pathlib import Path
import matplotlib.pyplot as plt
import FinanceDataReader as fdr

Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("reports/figs").mkdir(parents=True, exist_ok=True)

# 005930 = 삼성전자 종목코드.
# FinanceDataReader의 네이버 소스는 KRX 로그인 없이 동작하고,
# 액면분할이 보정된 '수정주가'를 준다.
df = fdr.DataReader("005930", "2015-01-01", "2025-12-31")

print("받은 행 수:", len(df))
print("기간:", df.index.min().date(), "~", df.index.max().date())
print(df.head(3))

# CSV로 저장 (엑셀에서 한글 안 깨지게 utf-8-sig)
df.to_csv("data/raw/005930.csv", encoding="utf-8-sig")

# 종가 그래프 1장
ax = df["Close"].plot(figsize=(11, 4), linewidth=1.5, color="#2a78d6")
ax.set_title("Samsung Electronics (005930)  2015-2025")
ax.set_xlabel(""); ax.set_ylabel("KRW")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("reports/figs/day01_005930.png", dpi=120)
print("그래프 저장 → reports/figs/day01_005930.png")

# 수정주가인지 눈으로 확인하는 구간
# 삼성전자는 2018년 5월 50대 1 액면분할을 했다.
print("\n--- 2018 액면분할 구간 ---")
print(df.loc["2018-04-25":"2018-05-08", "Close"])
