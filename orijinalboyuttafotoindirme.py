import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg"

# url yi bu şekilde verdik ama istersek kullanıcıdan veri alıyormuş gibi de yapabiliriz.

file_path = "C:\\Users\\Ali\\Desktop\\indirr\\resim.jpg"

# Dosya yolunu doğru şekilde belirtmeniz gerekiyor. Klasörler arası muhakkak \ değil \\ olarak belirtilmelidir.
# Klasörden sonra da dosya ismi.jpg şeklinde yazıp tırnağı kapatın.

urllib.request.urlretrieve(url,file_path)

# urllib.request.urlretrieve( (linki içeren değişken) , (dosya yolu) ) satırı indirmeyi gerçekleştirir.
# urllib ve request modüllerini kullanarak dosya indirme işlemini gerçekleştirdik.
