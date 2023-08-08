# Requests ve BeautifulSoup kütüphanelerini Python'a dahil eder. HTTP isteklerini yollamak ve HTML'i ayrıştırmak için kullanılır.
# Beautiful Soup, web scraping, web analiz etme ve web geliştirme gibi çeşitli amaçlar için kullanılabilir.
# frombs4 modülü, Python'da HTML ve XML belgelerini işlemek için kullanılır.
# frombs4 Beautiful Soup modülünü içe aktarır ve BeautifulSoup sınıfını kullanılabilir hale getirir.
import requests
from bs4 import BeautifulSoup
import pymysql

host = "localhost"
user = "root"
password = "gizem555"
database = "stajdb"

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

# Kullanıcıdan veri girişi almak içindir.
word = input("Aranacak kelimeyi girin: ")

# Kullanıcının girdiği kelimeyle alakalı bir URL oluşturur ve bu URL'ye bir HTTP isteği yollar. HTTP isteği sonucunda elde edilen yanıt response değişkenine atanır.
# word arama sorgusu için Google'ın arama sonuçları sayfasını alır.
url = "https://www.google.com/search?q=" + word
response = requests.get(url)

# response değişkeninde saklanan HTML içeriğini BeautifulSoup kütüphanesi ile ayrıştırır.
soup = BeautifulSoup(response.content, "html.parser")

# HTMLdeki tüm img etiketlerini bulur. find_all() metodu, bulunan tüm img etiketlerinin bir listesini bize döndürür.
# soup nesnesindeki tüm img etiketlerini bir list nesnesi olarak images değişkenine atar.
# find_all() işlevi, bir soup nesnesi içinde belirli bir etiketi arar ve tüm eşleşen öğeleri bir list nesnesi olarak döndürür.
images = soup.find_all("img")

# Bu for döngüsü, images değişkeninde saklanan img etiketlerinin listesini tarar. Src, style, width ve height özelliklerini alır.
# src özelliği, görüntünün kaynağını gösterir. style özelliği, görüntünün stilini gösterir. width ve height özellikleri, görüntünün genişliğini ve yüksekliğini gösterir.
for image in images:
    src = image["src"]
    style = image["style"]
    width = None
    height = None

# NOT: Python'da image nesnesinin genişliği ve yüksekliğinin sıfır veya negatif olması durumunda width ve height hata oluşur. 
# Görüntünün genişliği ve yüksekliği sıfır veya negatifse, görüntünün boyutu belirlenemez ve görüntü görüntülenemez.

# style değişkeninde bulunan stil özelliklerini bir list nesnesi olarak style_properties değişkenine atar.
# Stil özellikleri, görüntünün görünümünü kontrol eden CSS kurallarıdır.
# split() işlevi, bir metin dizisini belirli bir karaktere göre ayrıştırır. Burada split() işlevi, style değişkenini ; karakterine göre ayrıştırır. 
    style_properties = style.split(";")


# Bu for döngüsü, style_properties değişkeninde saklanan CSS stil kurallarının listesini tarar. 
# Her CSS stil kuralı için, kuralın "max-width:" veya "max-height:" ile başlayıp başlamadığını kontrol eder. 
# Eğer öyleyse, kuralın değeri width veya height değişkenine atanır. Bu nedenle başta width ve height i 0'a eşitlemiştik.
# replace() yöntemi, özellikten "max-width:" önekini kaldırmak için kullanılır. 
# strip() yöntemi, özelliğin sonundaki boşluk karakterlerini kaldırmak için kullanılır.
    for prop in style_properties:
        prop = prop.strip()
        if prop.startswith("max-width:"):
            width = prop.replace("max-width:", "").replace("px", "").strip()
        elif prop.startswith("max-height:"):
            height = prop.replace("max-height:", "").replace("px", "").strip()


# Bu satırlarda görüntünün URL'sini, genişliğini ve yüksekliğini yazdırmış oluruz.
    print("Image URL:", src)
    print("Width:", width)
    print("Height:",height)
    if width and height is not None:

     sql_query = "INSERT INTO image_info (key_value,image_link, width, height) VALUES (%s,%s,%s,%s)"
     data = (word,str(src),width,height)
     cursor.execute(sql_query, data)
     connection.commit()