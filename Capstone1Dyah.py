# Nama : Dyah Ayu Daratika
# CAPSTONE PROJECT MODULE 1 - DATA KARYAWAN PERUSAHAAN 
# Poin Penilaian : Penjelasan, Create, Read, Update, Delete, Integrasi sistem dan efisiensi kode 
# Upload video ke youtube, dan file python project ke Github


ListKaryawan = [
    {
        'No' : '1', 
        'Nama' : 'Dyah Ayu Daratika', 
        'Gender' : 'Perempuan', 
        'Umur' : 29, 
        'Posisi' : 'Business Development',
        'Alamat' : 'Jalan Gilimanuk No.2, Jakarta Barat'
    },
    {
        'No' : '2', 
        'Nama' : 'Irwansyah Ramadhani', 
        'Gender' : 'Laki-Laki', 
        'Umur' : 28, 
        'Posisi' : 'Head of Finance',
        'Alamat' : 'Jalan Semut Kecil No.169, Jakarta Timur'
    },
    {
        'No' : '3', 
        'Nama' : 'Vannesa Nathania', 
        'Gender' : 'Perempuan', 
        'Umur' : 20, 
        'Posisi' : 'Data Engineer',
        'Alamat' : 'Jalan Bawang No.77, Bekasi'
    },
    {
        'No' : '4', 
        'Nama' : 'Renny Rachmatya', 
        'Gender' : 'Perempuan', 
        'Umur' : 26, 
        'Posisi' : 'Data Analyst Staff',
        'Alamat' : 'Jalan Tomar No.89'
    }
]

# Pilihan Table Data Karyawan 

def DataKaryawan():
    if ListKaryawan == []:
        print()
        print('''
    -----Tidak Ditemukan Data Karyawan---''')

    else:
        print('''
    -----Report Data Karyawan-----

    -----Data Karyawan PT Maju Terus Bersama Indonesia-----\n\n
No. \t| Nama \t\t\t| Gender \t| Umur \t| Posisi \t\t| Alamat''')
        for idx, item in enumerate(ListKaryawan):
            print(f"{item['No']} \t| {item['Nama']} \t| {item['Gender']} \t| {item['Umur']} \t| {item['Posisi']} \t| {item['Alamat']}")

# Pilihan Menu No. 1.1 - Report Data Karyawan       
def MenuDataKaryawan():
    print('''    
    Menu Report Data Karyawan:
    1. Report Data Karyawan 
    2. Cari Data Karyawan
    3. Kembali ke Menu Utama\n''')
    
    InputMenuReport = input(''' Silahkan Pilih Menu diatas (1-3) : ''')
    if InputMenuReport == '1':
        DataKaryawan()
    elif InputMenuReport == '2':
        CariData()
    elif InputMenuReport == '3':
        print('''
        -----Kembali ke Menu Utama-----''')
        MenuUtama()
    else:
        print()
        print('-----Anda Masukkan Pilihan yang Salah-----\n\tSilahkan masukkan pilihan Menu yang Benar (1-5) :')
        MenuDataKaryawan()

# Pilihan No.1.2 Cari Data Karyawan 

def CariData(): 
    DataKaryawan()
    InputNo = int(input('''
    ----- Cari Data Karyawan
    
    Masukkan No. Karyawan yang Anda Cari: ''' ))


    for i in range(len(ListKaryawan)):
        if InputNo == ListKaryawan[i]['No']:
            print(f'''
    Data Karyawan Ditemukan dengan No.: {InputNo}''')
            print('''
    ----------Data Karyawan PT Maju Terus Bersama Indonesia-----------
    No. \t| Nama \t\t| Gender \t| Umur \t| Posisi \t| Alamat''')
            print(f"{ListKaryawan[i]['No']} \t| {ListKaryawan[i]['Nama']} \t| {ListKaryawan[i]['Gender']} \t| {ListKaryawan[i]['Umur']} \t| {ListKaryawan[i]['Posisi']} \t| {ListKaryawan[i]['Alamat']}")
        if InputNo != ListKaryawan[i]['No']:
            print('''
    \t-----Data Karyawan Tidak Dapat Ditemukan-----''')
        MenuDataKaryawan()       

# Menu Create Data Karyawan 

def InputData():
    NoKaryawan = int(input('\t1. Masukkan No. Karyawan:'))
    for i in range(len(ListKaryawan)):
        if NoKaryawan == ListKaryawan[i]['No']:
            print('''
            -----Data Sudah Ada di Database, Tidak Perlu Anda Tambahkan-----\n
            -----Silahkan Masukkan Data yang Lain-----''')
            print()
            TambahData()
        
        else:
            NamaKaryawan = input('2. Nama Karyawan: ')
            GenderKaryawan = input('3. Gender Karyawan (Perempuan/Laki-Laki): ')
            UmurKaryawan = input('4. Umur Karyawan (tahun): ')
            PosisiKaryawan = input('5. Posisi Karyawan: ')
            AlamatKaryawan = input('6. Alamat Karyawan: ')
            break
    
    Notifikasi = input('''
    -----Apakah Anda Yakin untuk Simpan Data Karyawan (Yes/No)?''')
    if Notifikasi == 'Yes':
            ListKaryawan.append({
            'No' : NoKaryawan, 
            'Nama' : NamaKaryawan, 
            'Gender' : GenderKaryawan, 
            'Umur' : UmurKaryawan, 
            'Posisi' : PosisiKaryawan,
            'Alamat' : AlamatKaryawan
         })
            print('''
    -----Data Karyawan "Berhasil" Ditambahkan-----''')
    
    elif Notifikasi == 'No':
            print('''
    -----Data Karyawan Tidak Ditambahkan-----''')

    else:
            print()
            print('''
    ---Pilihan yang Anda Masukkan Salah---
                
    ---Silahkan Masukkan Kembali Pilihan Anda: ''')
    DataKaryawan()


def TambahData():
    while True:
        TambahDataKaryawan = input('''
        -----Menu Tambah Data Karyawan-----
        -----Menu:
             1. Tambah Data Karyawan 
             2. Kembali ke Menu Utama 

        Silahkan pilih Sub Menu Create Data (1 - 2): ''')

        if TambahDataKaryawan == '1':
            print('''
                ---Silahkan Masukkan Data Karyawan yang Ingin Anda Tambahkan---
                
                Masukkan Informasi Karyawan: ''')
            InputData()
            
        elif TambahDataKaryawan == '2':
            print('''
                ---Anda akan Kembali ke Menu Utama---''')
        else:
            print('''
                ---Pilihan yang Anda Masukkan Salah---
                
                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
            TambahData()

# Menu Update Data Karyawan

def UpdateData():
    while True:
        UpdateDataKaryawan = input('''
        -----Menu Update Data Karyawan----
        
        -----Menu: 
             1. Update Data Karyawan:
             2. Kembali ke Menu Utama
             
        Silahkan Pilih Sub Menu Update Data Karyawan (1 - 2): ''')

        if UpdateDataKaryawan == '1':
            DataKaryawan()
            NoKaryawan = int(input('\t| Masukkan No. Karyawan: '))
            for i in range(len(ListKaryawan)):
                if NoKaryawan == ListKaryawan[i]['No']:
                        print('''
                    ----Data Karyawan Ditemukan''')
                        Condition = input('''
                    -----Pilih 'Yes' jika ingin update data-----
                    -----Pilih 'No' jika anda batal update data-----''')
                        print()
                        if Condition == 'Yes':
                            print('''
                    -----Lanjutkan Update Data-----''')
                            Informasi = input('''
                    -----Pilih Informasi yang Mau Anda Update: 
                         1. No. Karyawan
                         2. Nama Karyawan
                         3. Gender Karyawan
                         4. Umur Karyawan
                         5. Posisi Karyawan
                         6. Alamat Karyawan
                    
                    -----Masukkan Pilihan Anda (1 - 5): ''')
                                
                            if Informasi == '1':
                                NoNewKaryawan = int(input('''
                    -----Masukkan No. Karyawan Baru: -----'''))
                                ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)?''')
                                if ConditionInformation == 'Yes': 
                                    ListKaryawan[i]['No.'] = NoNewKaryawan
                                    print('''
                        -----Data Karyawan "Berhasil" di-Update-----''')
                                    DataKaryawan()
                                elif ConditionInformation == 'No':
                                    print('''
                        -----Update Data Karyawan "Cancel"''')
                                    UpdateData()
                                else:
                                    print()
                                    print('''
                                ---Pilihan yang Anda Masukkan Salah---
                
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break

                        elif Informasi == '2':
                            NamaNewKaryawan = input('''
                    -----Masukkan Nama Karyawan yang Baru: ''')
                            ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)? ''')
                            if ConditionInformation == 'Yes':
                                ListKaryawan[i]['nama'] = NamaNewKaryawan
                                print('''
                    -----Data Karyawan "Berhasil" di-Update-----''')
                                DataKaryawan()  

                            elif ConditionInformation == 'No': 
                                print('''
                        -----Update Data Karyawan "Cancel"''')
                                UpdateData()
                            
                            else:
                                print()
                                print('''
                                ---Pilihan yang Anda Masukkan Salah---
                
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break

                        elif Informasi == '3':
                            GenderNewKaryawan = input('''
                    -----Masukkan Gender Karyawan yang Baru: ''')
                            ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)? ''')
                            if ConditionInformation == 'Yes':
                                ListKaryawan[i]['nama'] = GenderNewKaryawan
                                print('''
                    -----Data Karyawan "Berhasil" di-Update-----''')
                                DataKaryawan()        

                            elif ConditionInformation == 'No':
                                print('''
                        -----Update Data Karyawan "Cancel"''')
                                UpdateData()
                            
                            else:
                                print()
                                print('''
                                ---Pilihan yang Anda Masukkan Salah---
                    
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break
                            
                        elif Informasi == '4':
                            UmurNewKaryawan = input('''
                    -----Masukkan Umur Karyawan yang Baru: ''')
                            ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)? ''')
                            if ConditionInformation == 'Yes':
                                ListKaryawan[i]['nama'] = UmurNewKaryawan
                                print('''
                    -----Data Karyawan "Berhasil" di-Update-----''')
                                DataKaryawan()        

                            elif ConditionInformation == 'No':
                                print('''
                        -----Update Data Karyawan "Cancel"''')
                                UpdateData()
                            
                            else:
                                print()
                                print('''
                                ---Pilihan yang Anda Masukkan Salah---
                    
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break

                        elif Informasi == '5':
                            PosisiNewKaryawan = input('''
                    -----Masukkan Posisi Karyawan yang Baru: ''')
                            ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)? ''')
                            if ConditionInformation == 'Yes':
                                ListKaryawan[i]['nama'] = PosisiNewKaryawan
                                print('''
                    -----Data Karyawan "Berhasil" di-Update-----''')
                                DataKaryawan()        

                            elif ConditionInformation == 'No':
                                print('''
                        -----Update Data Karyawan "Cancel"''')
                                UpdateData()
                            
                            else:
                                print()
                                print('''
                                ---Pilihan yang Anda Masukkan Salah---
                    
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break

                        elif Informasi == '6':
                            AlamatNewKaryawan = input('''
                    -----Masukkan Alamat Karyawan yang Baru: ''')
                            ConditionInformation = input('''
                        -----Apakah Anda Yakin untuk Update Data Karyawan (Yes/No)? ''')
                            if ConditionInformation == 'Yes':
                                ListKaryawan[i]['nama'] = AlamatNewKaryawan
                                print('''
                    -----Data Karyawan "Berhasil" di-Update-----''')
                                DataKaryawan()        

                            elif ConditionInformation == 'No':
                                print('''
                        -----Update Data Karyawan "Cancel"''')
                                UpdateData()
                            
                            else:
                                print()
                                print('''
                                ---Pilihan yang Anda Masukkan Salah---
                    
                                ---Silahkan Masukkan Kembali Pilihan Anda: ''')
                                break

        elif UpdateDataKaryawan == '2':
            print('''
            ---Anda akan Kembali ke Menu Utama---''')
            MenuUtama()

        else:
            print('''
            ---Pilihan yang Anda Masukkan Salah---
                
            ---Silahkan Masukkan Kembali Pilihan Anda: ''')
            UpdateData()

# Delete Data Karyawan 

def DeleteDataKaryawan():

    DataKaryawan()

    while True:
        DeleteDataKaryawan = input('''
    -----Menu "Delete" Data Karyawan-----
    
    -----Menu:
         1. Delete Data Karyawan
         2. Kembali ke Menu Utama
         
    -----Silahkan pilih Sub Menu Delete Data Karyawan (1 - 2): ''')

        if DeleteDataKaryawan == '1':
            NoKaryawan = int(input('''
    -----Masukkan No. Karyawan yang ingin di-delete: '''))
            for i in range(len(ListKaryawan)):
                if NoKaryawan == ListKaryawan[i]['No']:
                    print('''
        -----Data Karyawan Ditemukan-----''')
                    DeleteCondition = input('''
        -----Apakah Anda Yakin untuk Deleter Data Karyawan ini (Yes/No)? ''')
                    if DeleteCondition == 'Yes':
                        NoKaryawan == ListKaryawan[i]['No']
                        del ListKaryawan[i]
                        print(f'''
        -----Data Karyawan No.: {NoKaryawan} "Berhasil" di-delete-----''')
                        break

                    elif DeleteCondition == 'No':
                        print('''
        -----Data Karyawan Tidak di-delete-----''')
                        break

                    else:
                        print('''
        -----Anda Memasukkan Pilihan yang Salah-----\n\tSilahkan masukkan pilihan Menu yang Benar (Yes/No: ''')
       
        elif DeleteDataKaryawan == '2':
            print('''
        -----Anda akan Kembali ke Menu Utama---''')
            MenuUtama()
        
        else:
            print()
            print('''
        -----Anda Memasukkan Pilihan yang Salah-----\n\tSilahkan masukkan pilihan Menu yang Benar (1 - 2): ''')
        DeleteDataKaryawan()

def MenuUtama():
    PilihanMenu = input('''
    ----------Data Karyawan PT Maju Terus Bersama Indonesia-----------

    Selamat Datang di PT MTBI

    Pilihan Menu:
        1. Report Data Karyawan 
        2. Menambah Data Karyawan 
        3. Update Data Karyawan 
        4. Menghapus Data Karyawan 
        5. Exit Program
    
    Silahkan pilih Menu diatas (1-5) : ''')
    
    while True:
        if PilihanMenu == '1':
            MenuDataKaryawan()  
        elif PilihanMenu == '2':
            TambahData()
        elif PilihanMenu == '3':
            UpdateData()
        elif PilihanMenu == '4':
            DeleteDataKaryawan()
        elif PilihanMenu == '5':
            print('''
    -----Terima Kasih-----''')
            quit()
        else:
            print()
            print('-----Anda Memasukkan Pilihan yang Salah-----\n\tSilahkan masukkan pilihan Menu yang Benar (1-5) :')
            MenuUtama()

print(MenuUtama())


