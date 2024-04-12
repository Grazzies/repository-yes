Meme_dict = {"LOL" : "tanggapan terhadap sesuatu yang lucu",
            "CRINGE" : "sesuatu yang aneh atau memalukan",
            "ROFL" :  "tanggapan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"}
            
word = input("ketik kata yang tidak mengerti (menggunakan huruf kapital semua):")

if word in Meme_dict.keys():
    print("makna katanya adalah", Meme_dict[word])
else:
    print("kata tidak ditemukan")

