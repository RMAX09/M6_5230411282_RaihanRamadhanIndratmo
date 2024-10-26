class Order:
    def __init__(self):
        self.daftarPesanan = []
        self.statusPesanan = ["Menunggu", "Diproses", "Dikirim", "Selesai"]

    def inputBarang(self):
        daftarBarang = []
        while True:
            print("\n--- Input Barang ---")
            nama = input("Nama barang: ")
            try:
                harga = float(input("Harga barang: "))
                jumlah = int(input("Jumlah barang: "))

                item = {
                    'nama': nama,
                    'harga': harga,
                    'jumlah': jumlah,
                    'total': harga * jumlah
                }
                daftarBarang.append(item)

                tambah = input("\nInput barang lain? (y/t): ").lower()
                if tambah != 'y':
                    break
            except ValueError:
                print("Error: Input harga dan jumlah harus angka!")
                continue

        return daftarBarang

    def buatPesanan(self):
        print("\nInput Pesanan Baru")
        try:
            idPesanan = int(input("ID Pesanan: "))
            if self.cariPesanan(idPesanan):
                print("Error: ID sudah digunakan!")
                return

            namaPemesan = input("Nama Pemesan: ")
            print("\nInput barang pesanan:")
            barang = self.inputBarang()

            totalBayar = sum(item['total'] for item in barang)

            dataPesanan = {
                'id': idPesanan,
                'pemesan': namaPemesan,
                'barang': barang,
                'totalBayar': totalBayar,
                'status': self.statusPesanan[0]
            }
            self.daftarPesanan.append(dataPesanan)
            print("\nPesanan berhasil dicatat!")
        except ValueError:
            print("Error: ID harus angka!")

    def nampilkanPesanan(self):
        if not self.daftarPesanan:
            print("\nBelum ada pesanan!")
            return

        print("\nDaftar Pesanan:")
        for pesanan in self.daftarPesanan:
            print("=" * 60)
            print(f"ID Pesanan   : {pesanan['id']}")
            print(f"Pemesan      : {pesanan['pemesan']}")
            print(f"Status       : {pesanan['status']}")
            print("\nRincian Barang:")
            print("-" * 60)
            print(f"{'Nama Barang':<25} {'Harga':<12} {'Jumlah':<8} {'Total':<12}")
            print("-" * 60)
            for item in pesanan['barang']:
                print(
                    f"{item['nama']:<25} Rp {item['harga']:<10.0f} {item['jumlah']:<8} Rp {item['total']:.0f}")
            print("-" * 60)
            print(f"Total Pembayaran: Rp {pesanan['totalBayar']:.0f}")
            print("=" * 60)

    def ubahStatus(self, idPesanan, statusBaru):
        pesanan = self.cariPesanan(idPesanan)
        if pesanan:
            pesanan['status'] = statusBaru
            return True
        return False

    def cariPesanan(self, idPesanan):
        for pesanan in self.daftarPesanan:
            if pesanan['id'] == idPesanan:
                return pesanan
        return None


class Delivery:
    def __init__(self):
        self.daftarPengiriman = []
        self.statusPengiriman = ["Persiapan",
                                 "Dalam Perjalanan", "Sampai Tujuan"]

    def prosesPengiriman(self, sistemPesanan):
        print("\nInput Pengiriman Baru")
        try:
            idPesanan = int(input("ID Pesanan: "))
            pesanan = sistemPesanan.cariPesanan(idPesanan)

            if pesanan is None:
                print("Pesanan tidak ditemukan!")
                return

            if pesanan['status'] != "Menunggu":
                print("Pesanan sudah diproses!")
                return

            namaPenerima = pesanan['pemesan']
            catatan = input("Catatan pengiriman: ")
            tglKirim = input("Tanggal kirim (DD/MM/YYYY): ")
            alamatTujuan = input("Alamat tujuan: ")

            dataPengiriman = {
                'id': idPesanan,
                'penerima': namaPenerima,
                'barang': pesanan['barang'],
                'totalBayar': pesanan['totalBayar'],
                'catatan': catatan,
                'tanggal': tglKirim,
                'alamat': alamatTujuan,
                'status': self.statusPengiriman[0]
            }
            self.daftarPengiriman.append(dataPengiriman)
            sistemPesanan.ubahStatus(idPesanan, "Diproses")
            print("Pengiriman berhasil diproses!")
        except ValueError:
            print("Error: ID harus angka!")

    def perbaruiStatus(self):
        if not self.daftarPengiriman:
            print("\nBelum ada data pengiriman!")
            return

        try:
            idPengiriman = int(input("ID Pengiriman: "))
            pengiriman = self.cariPengiriman(idPengiriman)

            if pengiriman is None:
                print("Data pengiriman tidak ditemukan!")
                return

            print("\nStatus saat ini:", pengiriman['status'])
            print("Pilihan status:")
            for idx, status in enumerate(self.statusPengiriman):
                print(f"{idx + 1}. {status}")

            pilih = int(input("Pilih status (1-3): ")) - 1
            if 0 <= pilih < len(self.statusPengiriman):
                pengiriman['status'] = self.statusPengiriman[pilih]
                print("Status berhasil diperbarui!")
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Error: Input harus angka!")

    def cariPengiriman(self, idPengiriman):
        for pengiriman in self.daftarPengiriman:
            if pengiriman['id'] == idPengiriman:
                return pengiriman
        return None

    def nampilkanPengiriman(self):
        if not self.daftarPengiriman:
            print("\nBelum ada data pengiriman!")
            return

        print("\nDaftar Pengiriman:")
        for pengiriman in self.daftarPengiriman:
            print("=" * 60)
            print(f"ID Pengiriman  : {pengiriman['id']}")
            print(f"Penerima       : {pengiriman['penerima']}")
            print(f"Tanggal Kirim  : {pengiriman['tanggal']}")
            print(f"Alamat         : {pengiriman['alamat']}")
            print(f"Status         : {pengiriman['status']}")
            print(f"Catatan        : {pengiriman['catatan']}")
            print("\nRincian Barang:")
            print("-" * 60)
            print(f"{'Nama Barang':<25} {'Harga':<12} {'Jumlah':<8} {'Total':<12}")
            print("-" * 60)
            for item in pengiriman['barang']:
                print(
                    f"{item['nama']:<25} Rp {item['harga']:<10.0f} {item['jumlah']:<8} Rp {item['total']:.0f}")
            print("-" * 60)
            print(f"Total Pembayaran: Rp {pengiriman['totalBayar']:.0f}")
            print("=" * 60)


def menuUtama():
    print("\n=== SIHA-RIR | HANTOE KURIR | ORDER CEPAT, KIRIM CEPAT, TINGGAL SATSET ===")
    print("1. Menu Pesanan")
    print("2. Menu Pengiriman")
    print("3. Keluar")
    return input("Pilih menu (1-2), 3 Keluar : ")


def menuPesanan():
    print("\n=== MENU PESANAN ===")
    print("1. Buat Pesanan")
    print("2. Lihat Pesanan")
    print("3. Kembali")
    return input("Pilih menu (1-2), 3 Keluar : ")


def menuPengiriman():
    print("\n=== MENU PENGIRIMAN ===")
    print("1. Input Pengiriman")
    print("2. Lihat Pengiriman")
    print("3. Update Status")
    print("4. Kembali")
    return input("Pilih menu (1-3), 4 Keluar : ")


def main():
    sistemPesanan = Order()
    sistemPengiriman = Delivery()

    while True:
        pilihan = menuUtama()

        if pilihan == "1":
            while True:
                subPilihan = menuPesanan()
                if subPilihan == "1":
                    sistemPesanan.buatPesanan()
                elif subPilihan == "2":
                    sistemPesanan.nampilkanPesanan()
                elif subPilihan == "3":
                    break
                else:
                    print("Menu tidak valid!")

        elif pilihan == "2":
            while True:
                subPilihan = menuPengiriman()
                if subPilihan == "1":
                    sistemPengiriman.prosesPengiriman(sistemPesanan)
                elif subPilihan == "2":
                    sistemPengiriman.nampilkanPengiriman()
                elif subPilihan == "3":
                    sistemPengiriman.perbaruiStatus()
                elif subPilihan == "4":
                    break
                else:
                    print("Menu tidak valid!")

        elif pilihan == "3":
            print("\nSIHANTOE | SATSET SOLUTION!")
            break
        else:
            print("Menu Ga Valid!")


if __name__ == "__main__":
    main()
