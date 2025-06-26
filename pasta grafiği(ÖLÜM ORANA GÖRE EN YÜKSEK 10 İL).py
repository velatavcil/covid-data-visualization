import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi oku
df = pd.read_csv("covid_turkiye_81_il.csv")

# 2. Ölüm oranını hesapla
df["Ölüm Oranı (%)"] = (df["Toplam Vefat"] / df["Toplam Vaka"]) * 100

# 3. Ölüm oranına göre en yüksek 10 ili seç
ilk10 = df.sort_values("Ölüm Oranı (%)", ascending=False).head(10)

# 4. Pasta dilimlerini biraz ayırmak için explode listesi oluştur
explode = [0.05] * 10  # her dilim %5 dışa taşsın

# 5. Pasta grafiği oluştur
plt.figure(figsize=(8, 8))
plt.pie(
    ilk10["Ölüm Oranı (%)"],
    labels=ilk10["İl"],
    autopct="%1.1f%%",
    startangle=140,
    explode=explode,            # dışa taşma
    shadow=True,                # gölge efekti
    colors=plt.cm.Reds_r(range(0, 250, 25))  # kırmızı tonlar
)

# 6. Başlık ve düzenleme
plt.title("Ölüm Oranı En Yüksek 10 İl", fontsize=14)
plt.tight_layout()
plt.show()
(.venv) C:\Users\wavci\PycharmProjects\PythonProject\covid_proje
git remote add origin https://github.com/velatavcil/covid-data-visualization.git