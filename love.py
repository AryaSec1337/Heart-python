# Coded By AryaAlfahrezy
# Import dulu package turtle
import turtle

# deklarasi variale pen ke package turtle
pen = turtle.Turtle()

# Indetifikasi metode dulu untuk menggambar di fungsi kurva
def curve():
	for i in range(200):

		# indentifikasi gerakan step by step
		pen.right(1)
		pen.forward(1)

# kita mulai menggambar Love yang penuh
def heart():

	# kasih warna merah untuk hati nya
	pen.fillcolor('red')

	# kita isi warna di dalam hati
	pen.begin_fill()

	# gambar garis kiri
	pen.left(140)
	pen.forward(113)

	# gambar garis kanan
	curve()
	pen.left(120)

	# cetak fungs curva
	curve()

	# gambar garis kanan
	pen.forward(112)

	# tahap akhir mewarnai dan menggambar
	pen.end_fill()

# membuat kalimat ditengah lve
def txt():

	# pindahkan text di atas love
	pen.up()

	# pindahkan love dengan tepat
	pen.setpos(-68, 95)

	# pindahkan love dibawah text
	pen.down()

	# atur warna text menjadi hijau terang
	pen.color('lightgreen')

	# mari kita isi dengan kalimat yang anda ingin 
	pen.write("I Love You Siapa Nih ??", font=(
	"Verdana", 12, "bold"))


# menggambar hati
heart()

# menulis pesan
txt()

# Sembunyikan package turtle
pen.ht()
