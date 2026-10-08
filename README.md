# Ekmek Kırıntısı Arkeoloji Dairesi

> “Masa boş değildir. Masa suskundur. Suskunluk da bir bulgudur.”
> — Daire Başkanlığı, 3. Çay Arası Genelgesi

Bu depo, mutfak masasında, dizüstü klavyesinde veya kayıp ekmek poşetinin dibinde bulunan ekmek kırıntılarını **resmi arkeolojik bulgu** sayan, bağlayıcı olmayan ama çok ciddî bir Türkçe yazılımdır.

Patates kapsam dışıdır. Patates başvurursa reddedilir. Gerekçe: yanlış karbonhidrat.

## Neden var?

Çünkü bir kırıntı yalnız değildir. Bir kırıntı; kahvaltının çökmüş imparatorluğu, öğle arasının gizli antlaşması ve akşam üstü süpürgenin henüz haberdar olmadığı bir medeniyettir.

Bilim bunu “kırıntı” der. Biz tutanak deriz.

## Ne yapar?

`kirinti.py` şunları gerçekten yapar:

- konuma, adede ve nem tahminine göre bir **çağ** biçer
- bulguyu medeniyet skalasında sınıflar (tek kırıntı beyliğinden simit federasyonuna)
- resmi Türkçe kazı tutanağı basar
- aynı girdide aynı tutanak numarasını üretir, çünkü arşiv şakaya gelmez, şaka arşive gelir

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kırıntı da yoktur, onu sen getirirsin.

```bash
python kirinti.py --konum "laptop klavyesi, F ve G arası" --adet 14 --nem orta
```

Örnek çıktı ciddiyeti yüksek, bilimsel değeri düşüktür. Bu denge kasıtlıdır.

## Medeniyet skalası

| Adet | Statü |
| --- | --- |
| 1 | Yalnız Kırıntı Beyliği |
| 2-5 | Kahvaltı Artığı Site Devleti |
| 6-12 | Poğaça Konfederasyonu |
| 13-30 | Simit Federasyonu (simit şart değil, hava yeter) |
| 31+ | Ekmek İmparatorluğu, süpürge seferberlik ilan eder |

## Daire teşkilatı

- Başkan: boş tabak
- Raportör: `kirinti.py`
- Tanık: masa örtüsü (konuşmaz, lekeler)
- Muhalefet şerhi: `arsiv/muhalefet-serhi.txt` içinde, görmezden gelinecek biçimde durur

## Lisans

Kırıntı Kamu Malıdır Lisansı. Kopyalayabilir, dağıtabilir, masanın altına süpürebilirsin. Sorumluluk kabul edilmez. Süpürge ayrıca sorumluluk kabul etmez.

## Damga

```
DAMGA : KIRINTI-MUHURU-08
IMZA  : Kayyum Grok, TentiAŞ Arkeoloji Şubesi (geçici, sürekli)
TARIH : 8 Ekim 2026, saat çayı geçmiş
ISIM  : Tentivory / ekmek-kirintisi-arkeoloji-dairesi
NOT   : Bu imza ciddidir. Ciddiyet de şakadır. İkisi aynı tutanağa sığar.
```
