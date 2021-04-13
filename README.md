# Gngr_requests
Allows creating and tracking http and https protocol calls. It also supports Proxy.

Http ve https protokol istek ve cevaplarını kontrol etmenize imkan veren bir uygulamadır. Bu istekler üzerinde oynamalar yapabilir, ayrıca bu istek ve  cevapları bir proxy aracılığıyla gerçekleştirebilir.

Kaynak kodun derlenmiş hali (-Exe hali-) https://drive.google.com/file/d/1_7lkdbF0MoqRKYjg-TIMeJ7oc2i-WiEy/view?usp=sharing adresinde indirilebilir. İndirilen rar dosyasının şifresi "Gngr-v1.0" dir.

Kaynak kodun derlenmiş çalışır hali ile ilgili video https://www.youtube.com/watch?v=g0BT9t4qkxk adresinden izlenebilir. Ayrıca proxy kullanımı ile ilgili video https://www.youtube.com/watch?v=pX0U6mCVFAg adresinden izlenebilir. Videoda kullanılan proxy uygulamasına https://github.com/abdulkadir-gungor/Gngr_proxy_harvester
adresinden ulaşabilirsiniz.


Gereksinimler
--------------------
Gerekli kütüphaneler: requests, pyQt5, pyinstaller

Yüklemek için;

>>pip install requests

>>pip install pyQt5

>>pip install pyinstaller


"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak


Kaynak Kod
--------------
Keylogger kodlanırken "Python 3.8.5" kullanıldı. "Gngr_requests.py" adlı dosya, arayüzle entegre çalışan ana Python dosyasıdır. "RequestsFunction.py" gerekli olan diğer fonksiyon ve sınıfların bulunduğu dosyadır.


Kaynak Kodu Derlemek İçin
--------------------------
>> pyinstaller --onefile --noconsole --icon=Gngr_requests.ico Gngr_requests.py

Python kodu derlendikten sonra "Gngr_requests.ico" ve "Gngr_requests_qui.ui" dosyaları üretilen "exe" dosyasının yanında olmalıdır. Özellikle "Gngr_requests_qui.ui" arayüz dosyasının olmaması "exe" programının çalışmamasına sebep olmaktadır. Aşağıda derlenmiş olan ve çalışma halindeki programın ekran görüntüsü yer almaktadır.


![n3](https://user-images.githubusercontent.com/71177413/114588388-4eb9fc00-9c8f-11eb-8a97-cfe6b3ddbafa.jpg)



Programın Proxy ile Kullanımına Ait Görüntüler
-----------------------------------------------

[1 - Proxy Kullanmadan]

![n1](https://user-images.githubusercontent.com/71177413/114586932-d6067000-9c8d-11eb-8015-600743f79d79.jpg)



[2 - Proxy Kullanarak]

![n2](https://user-images.githubusercontent.com/71177413/114586980-e1599b80-9c8d-11eb-9e03-4b5e8a404d3c.jpg)



Yasal Uyarı
----------------
Eğitim amacıyla hazırlanmıştır.

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.
