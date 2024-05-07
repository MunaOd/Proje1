from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QLineEdit, QCalendarWidget, QMessageBox, QTableWidget, QTableWidgetItem, QDialog
from PyQt5.QtCore import QDate, Qt

class Arac:
    def __init__(self, id, model, yil, km, durum, fiyat):
        self.id = id
        self.model = model
        self.yil = yil
        self.km = km
        self.durum = durum
        self.fiyat = fiyat

    def __str__(self):
        return f"{self.model} ({self.yil}) - {self.durum}"

# Araç verileri
arac_listesi = [
    Arac(1, "Toyota Corolla", 2019, 25000, "Müsait", 20000),
    Arac(2, "Honda Civic", 2020, 30000, "Müsait", 25000),
    Arac(3, "Ford Focus", 2018, 20000, "Müsait", 18000),
    Arac(4, "Volkswagen Golf", 2017, 18000, "Müsait", 22000),
    Arac(5, "Renault Megane", 2019, 22000, "Müsait", 19000)
]

class VeriPenceresi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kiralama Verileri")
        self.initUI()

    def initUI(self):
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(9)  # 8'den 9'a
        self.table_widget.setHorizontalHeaderLabels(["Adı", "Soyadı", "Telefon", "Kredi Kartı", "Araç", "Kaç Gün", "Tarih", "Fiyat", "Toplam Fiyat"])  # Toplam Fiyat sütunu eklendi

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

class KiralamaSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Araç Kiralama Sistemi")
        self.initUI()

    def initUI(self):
        self.label_adi = QLabel("Adınız:")
        self.input_adi = QLineEdit()

        self.label_soyadi = QLabel("Soyadınız:")
        self.input_soyadi = QLineEdit()

        self.label_telefon = QLabel("Telefon Numaranız:")
        self.input_telefon = QLineEdit()

        self.label_kredi_kart = QLabel("Kredi Kartı Bilgileriniz:")
        self.input_kredi_kart = QLineEdit()

        self.label_arac_sec = QLabel("Araç Seçimi:")
        self.combo_arac_sec = QComboBox()
        # Araç listesini combobox'a ekleyin
        for arac in arac_listesi:
            if arac.durum == "Müsait":
                self.combo_arac_sec.addItem(str(arac), arac)

        self.label_fiyat = QLabel("Araç Fiyatı:")
        self.label_secili_arac_fiyat = QLabel("")  # Başlangıçta boş olacak

        self.label_gun_sec = QLabel("Kaç Gün Kiralamak İstiyorsunuz?")
        self.combo_gun_sec = QComboBox()
        # Örneğin, 1 ila 7 gün arasında seçenekler ekleyebiliriz.
        for i in range(1, 8):
            self.combo_gun_sec.addItem(str(i), i)

        self.label_tarih_sec = QLabel("Kiralamak İstediğiniz Tarih:")
        self.calendar_widget = QCalendarWidget()

        self.button_kiralama_yap = QPushButton("Kiralama Yap")
        self.button_kiralama_iptal_et = QPushButton("Kiralama İptal Et")
        self.button_veri_goster = QPushButton("Kiralama Verilerini Göster")

        layout = QVBoxLayout()
        layout.addWidget(self.label_adi)
        layout.addWidget(self.input_adi)
        layout.addWidget(self.label_soyadi)
        layout.addWidget(self.input_soyadi)
        layout.addWidget(self.label_telefon)
        layout.addWidget(self.input_telefon)
        layout.addWidget(self.label_kredi_kart)
        layout.addWidget(self.input_kredi_kart)
        layout.addWidget(self.label_arac_sec)
        layout.addWidget(self.combo_arac_sec)
        layout.addWidget(self.label_fiyat)
        layout.addWidget(self.label_secili_arac_fiyat)
        layout.addWidget(self.label_gun_sec)
        layout.addWidget(self.combo_gun_sec)
        layout.addWidget(self.label_tarih_sec)
        layout.addWidget(self.calendar_widget)
        layout.addWidget(self.button_kiralama_yap)
        layout.addWidget(self.button_kiralama_iptal_et)
        layout.addWidget(self.button_veri_goster)

        self.setLayout(layout)

        self.button_kiralama_yap.clicked.connect(self.kiralamaYap)
        self.button_kiralama_iptal_et.clicked.connect(self.kiralamaIptalEt)
        self.button_veri_goster.clicked.connect(self.veriGoster)
        self.combo_arac_sec.currentIndexChanged.connect(self.guncelleSeciliAracFiyat)

        # Başlangıçta fiyatı güncelleyin
        self.guncelleSeciliAracFiyat()

    def guncelleSeciliAracFiyat(self):
        secili_arac = self.combo_arac_sec.currentData()
        self.label_secili_arac_fiyat.setText(str(secili_arac.fiyat) + " TL")

    def kiralamaYap(self):
        secili_arac = self.combo_arac_sec.currentData()
        secili_gun = int(self.combo_gun_sec.currentText())
        secili_tarih = self.calendar_widget.selectedDate().toString("dd.MM.yyyy")
        
        # Aynı gün içinde başka bir araç kiralanmış mı kontrol et
        for arac in arac_listesi:
            if arac.durum == "Kiralandı" and arac.yil == secili_arac.yil:
                QMessageBox.warning(self, "Hata", "Seçilen tarih için başka bir araç kiralanmış.")
                return

        # Kiralama işlemleri burada gerçekleştirilebilir.
        # Örneğin, burada veritabanına veya başka bir depolama mekanizmasına kiralama bilgileri kaydedilebilir.

        # Başarılı kiralama mesajı göster
        QMessageBox.information(self, "Başarılı", "Araç kiralama işlemi başarıyla gerçekleştirildi.")

    def kiralamaIptalEt(self):
        # İptal durumunda giriş alanlarını temizle
        self.input_adi.clear()
        self.input_soyadi.clear()
        self.input_telefon.clear()
        self.input_kredi_kart.clear()
        self.combo_arac_sec.setCurrentIndex(0)
        self.combo_gun_sec.setCurrentIndex(0)
        self.calendar_widget.setSelectedDate(QDate.currentDate())

    def veriGoster(self):
        dialog = VeriPenceresi(self)
        dialog.table_widget.setRowCount(len(arac_listesi))  # Satır sayısını araç listesi uzunluğu kadar ayarla
        for idx, arac in enumerate(arac_listesi):
            # Aracın durumunu kontrol et
            durum = "Müsait" if arac.durum != "Kiralandı" else "Kiralandı"
            # Aracın kiralanma tarihini belirle (örneğin, bugünün tarihini al)
            kiralama_tarihi = QDate.currentDate().toString("dd.MM.yyyy")
            dialog.table_widget.setItem(idx, 0, QTableWidgetItem(self.input_adi.text()))  # Ad
            dialog.table_widget.setItem(idx, 1, QTableWidgetItem(self.input_soyadi.text()))  # Soyad
            dialog.table_widget.setItem(idx, 2, QTableWidgetItem(self.input_telefon.text()))  # Telefon
            dialog.table_widget.setItem(idx, 3, QTableWidgetItem(self.input_kredi_kart.text()))  # Kredi kartı
            dialog.table_widget.setItem(idx, 4, QTableWidgetItem(arac.model))  # Araç modeli
            dialog.table_widget.setItem(idx, 5, QTableWidgetItem(str(self.combo_gun_sec.currentText())))  # Kiralama süresi
            dialog.table_widget.setItem(idx, 6, QTableWidgetItem(kiralama_tarihi))  # Kiralama tarihi
            dialog.table_widget.setItem(idx, 7, QTableWidgetItem(str(arac.fiyat)))  # Fiyat
            dialog.table_widget.setItem(idx, 8, QTableWidgetItem(str(arac.fiyat * int(self.combo_gun_sec.currentText()))))  # Toplam fiyat
            
            # Hücreleri renklendir
            if arac.durum == "Müsait":
                dialog.table_widget.item(idx, 4).setBackground(Qt.green)  # Araç adı hücresini yeşil yap
            else:
                dialog.table_widget.item(idx, 4).setBackground(Qt.red)  # Araç adı hücresini kırmızı yap

        dialog.exec_()

if __name__ == "__main__":
    app = QApplication([])
    kiralama_sistemi = KiralamaSistemi()
    kiralama_sistemi.show()
    app.exec_()
