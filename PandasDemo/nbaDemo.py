import pandas as pd

df = pd.read_csv("dataset/nba.csv")

# 1- İlk 10 kaydı getiriniz.
df.head(10)
# 2- Toplam kaç kayıt vardır ?
len(df.index)
# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
df["Salary"].mean()
# 4- En yüksek maaşı ne kadardır ?
df["Salary"].max()
# 5- En yüksek maaşı alan oyuncu kimdir ?
df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
df[(df["Age"]>= 20) & (df["Age"]<=25)][["Name","Team","Age"]].sort_values("Age", ascending = False)
# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
df[df["Name"]=="John Holland"]["Team"].iloc[0]
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

# 9- Kaç farklı takım mevcut ?
df["Team"].nunique()
# 10- Her takımda kaç oyuncu oynamaktadır ?
df["Team"].value_counts()
