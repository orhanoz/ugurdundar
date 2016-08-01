from django import forms
import datetime



cinsiyet = (
    ('erkek', 'Erkek'),
    ('kadin', 'Kadin'),
)
askerlik = (
    ('evet', 'Evet'),
    ('hayir', 'Hayir'),
    ('tescilli', 'Tescilli'),
)

egitim = (
    ('Ilkokul', 'Ilkokul'),
    ('Orta okul', 'Orta Okul'),
    ('Lise/Teknik Lise', 'Lise/Teknik Lise'),
	('Lise/Teknik Lise', 'Lise/Teknik Lise'),
	('Meslek yüksek okulu', 'Meslek yüksek okulu'),
	('Üniversite', 'Üniversite'),
	('Üniversite', 'Üniversite'),
	('Doktora', 'Doktora'),

)




class ContactForm1(forms.Form):
    Konu = forms.CharField(max_length=100)
    e_mail = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea)




class PersonalInformation(forms.Form):
	section_name = "Kisisel Bilgiler"


	# ad soyad dogum cinsiyet
	Soyad = forms.CharField(max_length=15)
	Ad = forms.CharField(max_length=20)
	Dogum_tarihi  = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, (datetime.datetime.now().year)+1)))
	Cinsiyet = forms.ChoiceField(choices=cinsiyet)
	Uyruk = forms.CharField(max_length=30)
	#askerlik
	Askerlik = forms.ChoiceField(choices=askerlik, widget=forms.RadioSelect())
	Tescilli_iseniz_süresi = forms.DateField(widget=forms.SelectDateWidget)

	#adress
	Adress = forms.CharField(max_length=100)
	Sehir = forms.CharField(max_length=20)
	Posta_Kodu = forms.CharField(max_length=10)
	Telefon =  forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                error_message = ("telefon numarasi : '+90123456789'. formatinda olmali."))
	e_posta = forms.EmailField();




class EducationInformation(forms.Form):
    section_name ="Egitim Bilgileri"

    gitim_durumu = forms.ChoiceField(choices=egitim)
    Egitim_görülen_kurum = forms.CharField(max_length=50)
    Yabanci_diller = forms.CharField(max_length=100)
    Son_calisilan_kurum = forms.CharField(max_length=100)
    Görev_tanimi = forms.CharField(widget=forms.Textarea)
    Giris_tarihi = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, (datetime.datetime.now().year)+1)))
    Cikis_tarihi = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, (datetime.datetime.now().year)+1)))
    Ayrilis_nedeni = forms.CharField(max_length=100)
