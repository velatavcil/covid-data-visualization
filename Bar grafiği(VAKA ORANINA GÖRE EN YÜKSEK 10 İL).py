import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid_turkiye_81_il.csv")
df["Vaka Oranı (%)"] = (df["Toplam Vaka"] / df["Nüfus"]) * 100
sirali = df.sort_values("Vaka Oranı (%)", ascending=False).head(10)
plt.figure(figsize=(12, 6))  # Grafik boyutu
plt.bar(sirali["İl"], sirali["Vaka Oranı (%)"], color='tomato')  # Bar grafiği

plt.title("Vaka Oranı En Yüksek 10 İl", fontsize=16)
plt.xlabel("İl", fontsize=12)
plt.ylabel("Vaka Oranı (%)", fontsize=12)
plt.xticks(rotation=45)  # İl isimlerini çapraz göster
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
