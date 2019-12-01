# tweetik-karakter-analizi

Twitter etkileşimleri ile kişilerin karakter analizi.

Günümüzde twitter kullanıcıları etkileşimelleri ile düşünce yapısı, karakteristik özellikleri ve ruh hali gibi birçok konuda kişisel veriler sunarak karakter analizi konusunda birçok veri barındırır. 

<img src="https://github.com/gulsume/tweetik-karakter-analizi/blob/master/tweet.jpeg">

Bu projede tweet,retweet ve mention verileri dikkate alınarak kariyer yöneticileri tarafından oldukça tercih edilen Myers- Briggs Kişilik Tipleri Envanteri ile kategorize edilmesi ve karakteristik analizlerin yapılması amaçlanmıştır.

Alternatif Türkçe doğal dil işleme kütüphanelerine bir göz atalım:

Kütüphane | Avantajları | Dezavantajları
------------ | ------------ | -------------
Zemberek-NLP | Morfolojik kök-bağlam ilşkisi güçlü. | Gürültülü text verisini arındırabilecek 'stop-words' desteği yetersiz.
NLTK | Türkçe text ayıklama işlevi mevcut. | 'Stop-words' veri seti kısıtlı.
spaCY | Gürüntü arındırma konusunda yetkin. | Türkçe kelime ayıklama desteği geliştirilmeli.

Bu kütüphanelerin her birini çalışmalarımız sırasında test ettik ve verimlilik açısından spaCY kütüphanesini tercih ettik. Türkçe gürültü arındırma desteği henüz çok yeni dahil olduğundan geliştirmelerimizi mevcut yapıyı pekiştirerek geliştirdik.

Ortam değişkenlerini sağlamak için gerekli kütüphaneleri yüklemek için:
```
pip install imageio
pip install plotly
pip install emoji
```
Ardından projeyi twitter kullanıcı adı ile aşağıdaki gibi çalıştırabilirsiniz.
```
python .\test.py <username>
```
