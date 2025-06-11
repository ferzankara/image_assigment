Dijital Görüntü İşleme ve Analizi

Bu proje, Multimedya dersi kapsamında, dijital görüntülerin yapısını analiz etmek için Python ve Pillow kütüphanesi kullanılarak geliştirilmiştir. Amaç, bir örnek görüntü üzerinde çeşitli işlemler yaparak görüntü işleme tekniklerini anlamaktır.

Özellikler
Görüntünün boyutlarını yazdırır ve RGB renk uzayında (24 bit) sıkıştırma oranını hesaplar.
Görüntüyü YCbCr renk modeline dönüştürür, Y bileşenini artırarak parlaklığı değiştirir ve RGB'ye geri döner.
Kırmızı tonlu alanları seçer, Cr değerlerini sıfırlayarak görüntüyü YCbCr'den RGB'ye dönüştürür ve sonucu gösterir.
JPEG sıkıştırma yöntemiyle Cb ve Cr bileşenlerini alt örnekler, sonra üst örnekleyerek görüntüyü yeniden oluşturur ve kalite değişikliğini değerlendirir.
Tüm üç bileşeni (Y, Cb, Cr) alt örnekleyerek kalite değişikliklerini analiz eder.

Kullanılan Teknolojiler
Python
Pillow kütüphanesi

Teslimat
Tüm adımların sonuçları bir raporda açıklanmış ve kodlar eklenmiştir.
Sonuçlar tartışılmıştır.
Bu proje, dijital görüntü işleme, renk uzayları ve JPEG sıkıştırma tekniklerini anlamak için geliştirilmiştir.
