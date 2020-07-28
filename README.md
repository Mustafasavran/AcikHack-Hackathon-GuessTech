# GuessTech Sonraki kelime tahmini projesi


###### YÜKLEME

> git clone https://github.com/Mustafasavran/AcikHack-Hackathon-GuessTech.git

> pip3 install -r requirements.txt

#### MODELİ EĞİTME PARAMETRELERİ
>-h, --help            show this help message and exit

> --data DATA   eğitmek için veri seti yolu

 > -m MODEL_ADI, --model_adi MODEL_ADI   eğitilmiş modelin kaydedilecek yeri
 
###### ÖRNEK KULLANIM
>python3 train.py --data "data.txt" --model "model.dat"

#### MODELİ TEST ETME
> python3 test.py --model model.h5


##### VERİ SETİ OLUŞTURMA
Veri setini oluştururken gmail'den sadece türkçe mailleri çekebilmek için bazı harfleri içermesini istedik ve ayrıca düzgün bir veri seti oluşturmak için sadece gmail hesabınızda yıldızlanmış olanları almasını sağladık. Böyle yaparak daha düzgün veriler çekmeyi amaçladık.
###### Örnek veri çekme kullanımı
> python3 collect_data.py --mail username@gmail.com --sifre mail_sifresi
##### VERİ SETİ
Biz kendi gmail hesaplarımızdan çekilen maillerle eğitim gerçekleştirdik ve verileri diğer maili atan veya alan tarafın izni olmadan paylaşmayı uygun bulmadık. Bu yüzden şu anlık verimizi paylaşamıyoruz.
