class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(self.nama, "mulai berlari!")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        self.skor += jumlah
        print(self.nama, "mengumpulkan", jumlah, "koin")

    def tabrak_rintangan(self):
        self.is_running = False
        print("Game Over! Karakter", self.nama, "menabrak rintangan.")

    def info_player(self):
        print("Nama:", self.nama)
        print("Skor:", self.skor)
        print("Jumlah koin:", self.koin)
        print("Status berlari:", self.is_running)


# Pengujian objek
player1 = KarakterSurfer("Jake")

player1.berlari()
player1.ambil_koin(10)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()
