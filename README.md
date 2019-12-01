# tweetik-karakter-analizi

Twitter etkileşimleri ile kişilerin karakter analizi.

Günümüzde twitter kullanıcıları etkileşimelleri ile düşünce yapısı, karakteristik özellikleri ve ruh hali gibi birçok konuda kişisel veriler sunarak karakter analizi konusunda birçok veri barındırır. 

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/Images/tweet.jpeg">

Bu projede tweet,retweet ve mention verileri dikkate alınarak kariyer yöneticileri tarafından oldukça tercih edilen Myers- Briggs Kişilik Tipleri Envanteri ile kategorize edilmesi ve karakteristik analizlerin yapılması amaçlanmıştır.

Alternatif Türkçe doğal dil işleme kütüphanelerine bir göz atalım:

Kütüphane | Avantajları | Dezavantajları
------------ | ------------ | -------------
Zemberek-NLP | Morfolojik kök-bağlam ilşkisi güçlü. | Gürültülü text verisini arındırabilecek 'stop-words' desteği yetersiz.
NLTK | Türkçe text ayıklama işlevi mevcut. | 'Stop-words' veri seti kısıtlı.
spaCY | Gürüntü arındırma konusunda yetkin. | Türkçe kelime ayıklama desteği geliştirilmeli.

Bu kütüphanelerin her birini çalışmalarımız sırasında test ettik ve verimlilik açısından Türkçe gürültü arındırma desteği kütüphanelere henüz çok yeni dahil olmaya başladığından tek bir kütüphaneye bağlı kalmaksızın  geliştirmelerimizi mevcut yapıyı pekiştirerek geliştirdik.
Bu esneklik en nihayetinde ortaya konan 'Stop Words' veri setinin ihtiyaç doğrultusunda genişletilmesini sağladı.

Ortam değişkenlerini sağlamak için gerekli kütüphaneleri yüklemek için:
```
pip install requirements.txt

```
Ardından projeyi twitter kullanıcı adı ile aşağıdaki gibi çalıştırabilirsiniz.
```
python .\test.py <username>
```
Plotly kütüphanesi yardımı ile oluşan bar chart, kullanıcı istatistikleri gürültü oluşturan konudan bağımsız kelimelerden arındırılarak kalan küme içerisinde en yoğun anlamlı kelimeleri ölçekler.

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/Images/bar_chart_.jpg">

Şimdi de sistemi gerçek kullanıcı üzerinden giderek anlamlandırmaya çalışalım.
Örnek bir kullanıcı üzerinden yola çıkalım, bu kişi twitter ı sıkça kullanan Vedat Milör olarak belirledik. Kullanıcının son 200 tweet içerisindeki tweet,retweet ve mention dağılımı aşağıdaki gibidir.

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/Images/total.JPG">

Elde edilen verileri bir dataframe içerisinde bir araya getirdik, detayları aşağıdaki gibidir.

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/Images/dataframe.JPG">

Karakteri analizi için oldukça revaçta olan Myers- Briggs Kişilik Tipi Test tekniğini dikkate aldık. Bu teknik aşağıdaki başlıklarda karakter özelliklerini kategorize ederek bu metriklerin kombinasyonu ile elde edilen ana karakteri öne çıkarıyor. 

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/Images/karakter.JPG">

Biz de proje de bu kategorizasyondan yararlanarak kullanıcımızın twitter datasını analiz ettik ve aşağıdaki çıktıya ulaştık.


