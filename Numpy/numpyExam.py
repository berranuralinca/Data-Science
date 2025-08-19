import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
array = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
array = np.arange(5,15)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
array = np.arange(50,100,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
zeros = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
ones = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
array = np.linspace(0, 100,5)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
random = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
random = np.random.rand(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
array = np.random.randint(10,50,15).reshape(3,5)
# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
sum = array.sum()


# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
max = array.max()
min = array.min()
mean = array.mean()

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
index = array.argmax()




