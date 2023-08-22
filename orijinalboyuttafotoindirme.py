import urllib.request

url = "https://img.a.transfermarkt.technology/portrait/big/439022-1681476532.jpg?lm=1"

# url yi bu şekilde verdim ama istersen kullanıcıdan alıyormuş gibi de yapabilirsin.

file_path = "C:\\Users\\Ali\\Desktop\\indirr\\resim3.jpg"

# Dosya yolunu doğru şekilde belirtmen gerekiyor. Klasörler arası muhakkak \ değil \\ olarak belirtilmelidir.
# Klasörden sonra da dosya ismi.jpg şeklinde yazıp tırnağı kapat.

urllib.request.urlretrieve(url,file_path)

# urllib.request.urlretrieve( (linki içeren değişken) , (dosya yolu) ) satırı indirmeyi gerçekleştirir.
# urllib ve request modüllerini kullanarak dosya indirme işlemini gerçekleştirdim.