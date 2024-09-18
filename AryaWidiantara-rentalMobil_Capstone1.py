#===================================== work header & user id ===============================================
print('======================================================================================')
print('================================= ADIOS RENTAL MOBIL =================================')
print('======================== Jl. Kebon Kacang 20 Jakarta Selatan =========================') #alamat palsu
print('============================= 087730204009 / 0217465772 ==============================') #no palsu
print('======================================================================================')
print(' ')
print('''Notes Test (User ID) : ketik ADMIN/admin untuk masuk ke Program Administrator, 
ketik Nama Anda untuk masuk ke Program Customer''')
print(' ')
user_id = input('Masukkan ID User Anda : ').upper() 
#ketik ADMIN/admin untuk masuk ke program administrator, ketik nama untuk masuk ke program customer
#bisa menggunakan password, tapi agar mudah diakses jadi dihapuskan

print(' ')

#========================================== loading & intro =================================================
#loading screen & intro

def loading_screen():
    print('Tekan ENTER untuk kembali ke menu utama...')
    input()
    return

def loading_screen_next():
    print(' ')
    print('Silahkan tekan ENTER untuk melanjutkan...')
    input()
    return   

def intro():
    print(f'[ Welcome {user_id} - Adios Rental Mobil] ')
    print(' ')
    print('Tekan ENTER untuk masuk ke dalam program...')
    input()
    return

def dashboard():
    print(f'================================= Adios Rental Mobil =================================')
    print(f'{user_id}\'s dashboard')
    return

intro()

#list
data_mobil = [
    {
        'Plat Nomor': 'B6324WFG',
        'Merk': 'HONDA',
        'Model': 'SUV',
        'Tahun': 2006,
        'Status': 'ON RENT',
        'Driver': 'SELF DRIVE',
        'Customer' : 'RENDI',
        'Price (Rp)' : 550000
    },
    {
        'Plat Nomor': 'B2223SRG',
        'Merk': 'ALPHARD',
        'Model': 'MPV',
        'Tahun': 2007,
        'Status': 'AVAIL',
        'Driver': 'N/A',
        'Customer' : 'N/A',
        'Price (Rp)' : 1750000
    },
    {
        'Plat Nomor': 'B1234FFA',
        'Merk': 'BMW',
        'Model': 'SEDAN',
        'Tahun': 2002,
        'Status': 'AVAIL',
        'Driver': 'N/A',
        'Customer' : 'N/A',
        'Price (Rp)' : 1500000
    },
    {
        'Plat Nomor': 'B777UTK',
        'Merk': 'ALPHARD',
        'Model': 'MPV',
        'Tahun': 2010,
        'Status': 'ON RENT',
        'Driver': 'WITH DRIVER',
        'Customer' : 'FAISAL',
        'Price (Rp)' : 1750000
    },
    {
        'Plat Nomor': 'B889OTP',
        'Merk': 'TOYOTA',
        'Model': 'SUV',
        'Tahun': 2013,
        'Status': 'AVAIL',
        'Driver': 'N/A',
        'Customer' : 'N/A',
        'Price (Rp)' : 550000
    },
]
#============================================== CRUD =================================================

#===============================================READ==================================================
#menampilkan tabel data mobil
def report_data_mobil_table():
    #header tabel
    headers = data_mobil[0].keys()
    header_str = " ".join(f"{header:<20}" for header in headers)
    print('=' * len(header_str))
    print(header_str)
    print('-' * len(header_str))

    #menampilkan data
    for item in data_mobil:
        row_str = " ".join(f"{item[header]:<20}" for header in headers)
        print(row_str)
    print('=' * len(header_str))
    loading_screen_next()

#choices dalam menampilkan data
def report_data_mobil():
    print(' ')
    if not data_mobil:
        print('Laporan Data Mobil Rental:')
        print('=' * 21)
        print('-' * 21)
        print('Tidak ada data mobil.')
        print('=' * 21)
    else:
        print('Laporan Data Mobil Rental:')
        report_data_mobil_table()

#filter data untuk admin program
def filter_data(filter_type, filter_value):
    filtered_data = []
    for mobil in data_mobil:
        if filter_type == 'Status' and filter_value == mobil['Status']:
            filtered_data.append(mobil)
        elif filter_type == 'Model' and filter_value == mobil['Model']:
            filtered_data.append(mobil)
        elif filter_type == 'Customer' and filter_value == mobil['Customer']:
            filtered_data.append(mobil)

    #hasil      
    print("Laporan Data Mobil Rental:")
    headers = data_mobil[0].keys()
    header_str = " ".join(f"{header:<20}" for header in headers)
    print('=' * len(header_str))
    print(header_str)
    print('-' * len(header_str))
    
    if filtered_data:
        for mobil in filtered_data:
            row_str = " ".join(f"{mobil[header]:<20}" for header in headers)
            print(row_str)
    else:
        print("Tidak ada data yang sesuai dengan filter yang diberikan.")
    print('=' * len(header_str))
    loading_screen_next()

#filtering data untuk customer program
def filter_data_cust(filter_type, filter_value, additional_filter_type=None, additional_filter_value=None):
    filtered_data = []
    for mobil in data_mobil:
        if filter_type == 'Status' and filter_value == mobil['Status']:
            if additional_filter_type is None or (additional_filter_type in mobil and mobil[additional_filter_type] == additional_filter_value):
                filtered_data.append(mobil)
        elif filter_type == 'Model' and filter_value == mobil['Model']:
            if additional_filter_type is None or (additional_filter_type in mobil and mobil[additional_filter_type] == additional_filter_value):
                filtered_data.append(mobil)
        elif filter_type == 'Customer' and filter_value == mobil['Customer']:
            if additional_filter_type is None or (additional_filter_type in mobil and mobil[additional_filter_type] == additional_filter_value):
                filtered_data.append(mobil)

    #hasil      
    print("Laporan Data Mobil Rental:")
    #header tabel
    desired_headers = ['Plat Nomor', 'Merk', 'Model', 'Tahun', 'Status', 'Price (Rp)']
    header_str = " ".join(f"{header:<20}" for header in desired_headers)
    print('=' * len(header_str))
    print(header_str)
    print('-' * len(header_str))

    #menampilkan data
    if filtered_data:
        for mobil in filtered_data:
            row_str = " ".join(f"{mobil[header]:<20}" for header in desired_headers)
            print(row_str)
    else:
        print("Tidak ada data yang sesuai dengan filter yang diberikan.")
    print('=' * len(header_str))
    loading_screen_next()

#menu read data untuk admin
def report_data_mobil_menu():
    while True:
        print(' ')
        dashboard()
        column_width = 50

        #header
        header = f"{'=' * column_width}"
        title = "Laporan Data Mobil Rental:"
        separator = '-' * column_width

        #menampilkan menu read
        print(header)
        print(f"{title.center(column_width)}")
        print(separator)
        print(f"{'1. Tampilkan Semua Data Mobil Rental'.ljust(column_width)}")
        print(f"{'2. Cari Data Mobil yang Available'.ljust(column_width)}")
        print(f"{'3. Cari Data Mobil berdasarkan Nama Customer'.ljust(column_width)}")
        print(f"{'4. Cari Data Mobil berdasarkan Model Mobil'.ljust(column_width)}")
        print(f"{'5. Kembali ke Menu Utama'.ljust(column_width)}")
        print(header)

        choice = input("Pilih opsi [1-5]: ").strip()
        
        if choice == '1':
                print('Mencari Data Mobil Rental...')
                report_data_mobil()  
        elif choice == '2':
                print('Mencari Data Mobil Rental yang Available...')
                filter_data('Status','AVAIL')    
        elif choice == '3':
                nama_cust = input('Masukkan Nama Customer : ').upper()
                filter_data('Customer', nama_cust)   
        elif choice == '4':
                model_input = input('Masukkan Model Mobil (SUV,MPV,SEDAN): ').upper()
                filter_data('Model',model_input)        
        elif choice == '5':
                print('Kembali ke Menu Utama...')
                print(' ')
                break
        else:
                print("Opsi tidak valid. Silakan pilih [1-5].")
    
#menu read data untuk customer
def report_data_mobil_cust():
    while True:
        print(' ')
        dashboard()
        column_width = 40

        #header
        header = f"{'=' * column_width}"
        title = "Data Mobil Rental Terbaru :"
        separator = '-' * column_width

        #menampilkan menu read
        print(header)
        print(f"{title.center(column_width)}")
        print(separator)
        print(f"{'1. Cari Data Mobil yang Available'.ljust(column_width)}")
        print(f"{'2. Cari Data Mobil berdasarkan Model yang Available'.ljust(column_width)}")
        print(f"{'3. Kembali ke Menu Utama'.ljust(column_width)}")
        print(header)

        choice = input("Pilih opsi [1-3]: ").strip()
            
        if choice == '1':
            print('Mencari Data Mobil Rental yang Available...')
            filter_data_cust('Status','AVAIL')
        elif choice == '2':
            model_input = input('Masukkan Model Mobil yang ingin di cari (SUV,MPV,SEDAN): ').upper()
            print('Mencari Data Mobil Rental yang Available...')
            filter_data_cust('Model', model_input, 'Status', 'AVAIL')
        elif choice == '3':
            print('Kembali ke Menu Utama...')
            print(' ')
            break
        else:
            print('Opsi tidak valid. Silakan pilih [1-3].')

#===============================================CREATE==================================================
#create data mobil
def tambah_data_mobil():
    print(' ')
    dashboard()
    column_width = 30
    
    #header
    header = f"{'=' * column_width}"
    title = "Menambah Data Mobil Rental"
    separator = '-' * column_width

    #menampilkan menu
    print(header)
    print(f"{title.center(column_width)}")
    print(separator)
    while True:
        plat_nomor = input(f"{'1. Masukkan Plat nomor mobil : '.ljust(column_width)}").strip().upper()
    
        #check duplikat
        if any(mobil['Plat Nomor'] == plat_nomor for mobil in data_mobil):
            print("Plat nomor sudah ada. Silakan masukkan plat nomor yang berbeda.")
            print(' ')
            continue  
        break  
    
    merk = input(f"{'2. Masukkan Merk mobil:'.ljust(column_width)}").upper()
    model = input(f"{'3. Masukkan Model mobil:'.ljust(column_width)}").upper()
    while True:
        try:
            tahun = int(input(f"{'4. Masukkan Tahun mobil:'.ljust(column_width)}"))
            break  # Jika berhasil, keluar dari loop
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk tahun mobil.")
            print(' ')

    status = input(f"{'5. Masukkan Status mobil (ON RENT / AVAIL):'.ljust(column_width)}").upper()
    driver = input(f"{'6. Masukkan Metode Driving (SELF DRIVE / WITH DRIVER) <ENTER to skip>:'.ljust(column_width)}").upper()
    if driver == "":
        driver = "N/A"
    customer = input(f"{'7. Masukkan Nama Customer <ENTER to skip>:'.ljust(column_width)}").upper()
    if customer == "":
        customer = "N/A"
    while True:
        try:
            price = int(input(f"{'8. Masukkan Harga Rental perhari:'.ljust(column_width)}"))
            break  # Jika berhasil, keluar dari loop
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk harga rental.")
            print(' ')
    print(header)
    
    databaru = {
        'Plat Nomor' : plat_nomor,
        'Merk' : merk,
        'Model' : model,
        'Tahun' : tahun,
        'Status' : status,
        'Driver' : driver,
        'Customer' : customer,
        'Price (Rp)' : price
        }
    
    print(header)
    print("Data yang akan ditambahkan:")
    for key, value in databaru.items():
        print(f"{key}: {value}")
    print(header)
    
    #crosschecking
    while True:
        crosscheck = input('Apakah data yang anda masukkan sudah benar(Y/N) :').upper()
        if crosscheck == 'Y':
            data_mobil.append(databaru)
            print('---- Data Mobil Rental telah berhasil ditambahkan ----')
            print(' ')
            input()
            report_data_mobil_table()
            print(' ')
            loop_input = input('Apakah mau menambah data mobil lagi (Y/N) : ').upper()
            if loop_input == 'Y':
                tambah_data_mobil()
            elif loop_input == 'N':
                break
            else:
                print("Pilihan tidak valid. Harap masukkan Y/N.")
            break
        elif crosscheck == 'N':
            print('Penambahan Data dibatalkan...')
            break
        else:
            print("Pilihan tidak valid. Harap masukkan Y/N.")
            
#menu tambah data 
def tambah_data_mobil_menu():
    while True:
        print(' ')
        dashboard()
        column_width = 30

        #header
        header = f"{'=' * column_width}"
        title = "Menambah Data Mobil Rental"
        separator = '-' * column_width

        #menampilkan menu
        print(header)
        print(f"{title.center(column_width)}")
        print(separator)
        print(f"{'1. Input Data Mobil'.ljust(column_width)}")
        print(f"{'2. Kembali ke Menu Utama'.ljust(column_width)}")
        print(header)

        choice = input("Pilih opsi [1-2]: ").strip()
            
        if choice == '1':
            print("Memilih Input Data Mobil...")
            tambah_data_mobil()
        elif choice == '2':
            print("Kembali ke Menu Utama...")
            break
        else:
            print("Opsi tidak valid. Silakan pilih [1-2].")

#===============================================UPDATE==================================================
#update data mobil
def ubah_data_mobil():
    print(' ')
    dashboard()
    column_width = 30
    
    #header
    header = f"{'=' * column_width}"
    title = "Merubah Data Mobil Rental"
    separator = '-' * column_width

    print(header)
    print(f"{title.center(column_width)}")
    print(separator)
    #update data
    while True:
        plat_nomor = input(f"{'Masukkan Plat nomor mobil : '.ljust(column_width)}").strip().upper()
    
        #check duplikat
        if any(mobil['Plat Nomor'] == plat_nomor for mobil in data_mobil):
            print(' ')
            break  
        else:
            print("Plat nomor tidak ada. Silakan masukkan plat nomor yang sesuai.")
            break  

    for mobil in data_mobil:
        if mobil['Plat Nomor'] == plat_nomor:
            print(header)
            print("Masukkan data baru untuk mobil dengan plat nomor", plat_nomor)
            merk_baru = input('Masukkan merk baru mobil: ').upper()
            model_baru = input('Masukkan model baru mobil: ').upper()
            while True:
                try:
                    tahun_baru = int(input('Masukkan tahun baru mobil: '))
                    break  
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk harga rental.")
                    print(' ')
            status_baru = input('Masukkan status mobil sekarang (ON RENT / AVAIL): ').upper()
            customer_baru = input('Masukkan Nama Customer sekarang <ENTER to skip>: ').upper()
            if customer_baru== "":
                customer_baru = "N/A"
            driver_baru = input('Masukkan metode driving sekarang (SELF DRIVE / WITH DRIVER) <ENTER to skip>: ').upper()
            if driver_baru == "":
                driver_baru = "N/A"
            while True:
                try:
                    price_baru = int(input('Masukkan Harga Rental perhari sekarang:'))
                    break  
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk harga rental.")
                    print(' ')

            #tampilkan data sebelum konfirmasi
            print(header)
            print(f"Data Baru untuk Plat Nomor {plat_nomor}:")
            print(f"Merk: {merk_baru}")
            print(f"Model: {model_baru}")
            print(f"Tahun: {tahun_baru}")
            print(f"Status: {status_baru}")
            print(f"Customer: {customer_baru}")
            print(f"Driver: {driver_baru}")
            print(f"Harga: {price_baru} (Rp)")

        #crosscheck
            while True:
                crosscheck = input('\nApakah Anda yakin ingin mengubah data ini? (Y/N): ').strip().upper()
                if crosscheck == 'Y':
                # Lakukan perubahan
                    mobil.update({
                    'Merk': merk_baru,
                    'Model': model_baru,
                    'Tahun': tahun_baru,
                    'Status': status_baru,
                    'Customer': customer_baru,
                    'Driver': driver_baru,
                    'Price (Rp)': price_baru
                    })
                    print(' ')
                    print('---- Data Mobil Rental telah berhasil dirubah ----')
                    loading_screen_next()
                    break
                elif crosscheck == 'N':
                    print('Perubahan Data dibatalkan...')
                    break
                else:
                    print("Pilihan tidak valid. Harap masukkan Y/N.")
            
            report_data_mobil()
            
    
#update data nama customer, driver , status
def ubah_data_customer():
    print(' ')
    dashboard()
    column_width = 30
    
    #header
    header = f"{'=' * column_width}"
    title = "Merubah Data Mobil Rental"
    separator = '-' * column_width

    print(header)
    print(f"{title.center(column_width)}")
    print(separator)
    #update data
    while True:
        plat_nomor = input(f"{'Masukkan Plat nomor mobil : '.ljust(column_width)}").strip().upper()
    
        #check duplikat
        if any(mobil['Plat Nomor'] == plat_nomor for mobil in data_mobil):
            print(' ')
            break  
        else:
            print("Plat nomor tidak ada. Silakan masukkan plat nomor yang sesuai.")
            break   

    for mobil in data_mobil:
        if mobil['Plat Nomor'] == plat_nomor:    
            print("Masukkan data baru untuk mobil dengan plat nomor", plat_nomor)
            status_baru = input('Masukkan status mobil sekarang (ON RENT / AVAIL): ').upper()
            customer_baru = input('Masukkan Nama Customer sekarang <ENTER to skip>: ').upper()
            if customer_baru== "":
                customer_baru = "N/A"
            driver_baru = input('Masukkan metode driving sekarang (SELF DRIVE / WITH DRIVER) <ENTER to skip>: ').upper()
            if driver_baru == "":
                driver_baru = "N/A"

            #tampilkan data sebelum konfirmasi
            print(f'Plat Nomor: {plat_nomor} ini akan diakses')
            print('\nData yang akan diubah:')
            print(f'Merk: {mobil["Merk"]}')
            print(f'Model: {mobil["Model"]}')
            print(f'Tahun: {mobil["Tahun"]}')
            print(f'Status: {status_baru}')
            print(f'Customer: {customer_baru}')
            print(f'Driver: {driver_baru}')
            print(f'Harga (Rp): {mobil["Price (Rp)"]}')

            #crosscheck
            while True:
                crosscheck = input('\nApakah Anda yakin ingin mengubah data ini? [Y/N]: ').strip().upper()
                if crosscheck == 'Y':
                # Lakukan perubahan
                    mobil['Status'] = status_baru
                    mobil['Customer'] = customer_baru
                    mobil['Driver'] = driver_baru
                    print(' ')
                    print('---- Data Mobil Rental telah berhasil dirubah ----')
                    loading_screen_next()
                    break
                elif crosscheck == 'N':
                    print('Perubahan Data dibatalkan...')
                    break
                else:
                    print("Pilihan tidak valid. Harap masukkan [Y/N].")

            report_data_mobil()

#menu update data
def ubah_data_mobil_menu():
    while True:
        print(' ')
        dashboard()
        column_width = 50

        # Format header
        header = f"{'=' * column_width}"
        title = "Merubah Data Mobil Rental"
        separator = '-' * column_width

        # Menampilkan menu
        print(header)
        print(f"{title.center(column_width)}")
        print(separator)
        print(f"{'1. Merubah Overall Data Mobil'.ljust(column_width)}")
        print(f"{'2. Merubah Data Customer dan Status Mobil'.ljust(column_width)}")
        print(f"{'3. Kembali ke Menu Utama'.ljust(column_width)}")
        print(header)

        choice = input("Pilih opsi [1-3]: ").strip()
            
        if choice == '1':
            print('Merubah Data Mobil...')
            ubah_data_mobil()
        elif choice == '2':
            print('Merubah Data Customer...')
            ubah_data_customer()
        elif choice == '3':
            print('Kembali ke Menu Utama...')
            print(' ')
            break
        else:
            print('Opsi tidak valid. Silakan pilih [1-3].')

#================================================DELETE=================================================
#delete data mobil
def hapus_data_mobil(): 
    print(' ')
    dashboard()
    column_width = 30

    #header
    header = f"{'=' * column_width}"
    title = "Menambah Data Mobil Rental"
    separator = '-' * column_width

    print(header)
    print(f"{title.center(column_width)}")
    print(separator)
    
    while True:
        plat_nomor = input(f"{'Masukkan Plat nomor mobil : '.ljust(column_width)}").strip().upper()
    
        #check duplikat
        if any(mobil['Plat Nomor'] == plat_nomor for mobil in data_mobil):
            print(' ')
            break  
        else:
            print("Plat nomor tidak ada. Silakan masukkan plat nomor yang sesuai.")
            break   

    for mobil in data_mobil:
        if mobil['Plat Nomor'] == plat_nomor:
            while True:
                print(' ')
                #infodata
                print(f"Data mobil yang akan dihapus:")
                print(f"Plat Nomor : {mobil['Plat Nomor']}")
                print(f"Merk       : {mobil['Merk']}")
                print(f"Model      : {mobil['Model']}")
                print(f"Tahun      : {mobil['Tahun']}")
                print(f"Status     : {mobil['Status']}")
                print(f"Driver     : {mobil['Driver']}")
                print(f"Customer   : {mobil['Customer']}")
                print(f"Price (Rp) : {mobil['Price (Rp)']}")
                print(' ')
                
                #crosscheck
                crosscheck = input('Apakah Anda yakin ingin menghapus data ini? (Y/N): ').strip().upper()
                if crosscheck == 'Y':
                    data_mobil.remove(mobil)
                    print(' ')
                    print('---- Data Mobil Rental telah berhasil dihapus ----')
                    print(' ')
                    print("Data mobil setelah penghapusan:")
                    report_data_mobil()
                    break
                elif crosscheck == 'N':
                    print('Penghapusan data dibatalkan.')
                    break
                else:
                    print('Pilihan tidak valid. Harap masukkan [Y/N].')
            break
           
        
                       
    
#menu delete data
def hapus_data_mobil_menu():
    while True:
        print(' ')
        dashboard()
        column_width = 30

        #header
        header = f"{'=' * column_width}"
        title = "Menghapus Data Mobil Rental"
        separator = '-' * column_width

        #menampilkan menu
        print(header)
        print(f"{title.center(column_width)}")
        print(separator)
        print(f"{'1. Delete Data Mobil'.ljust(column_width)}")
        print(f"{'2. Kembali ke Menu Utama'.ljust(column_width)}")
        print(header)

        choice = input("Pilih opsi [1-2]: ").strip()
            
        if choice == '1':
            print("Memilih Data Mobil untuk di hapus...")
            print(' ')
            hapus_data_mobil()
        elif choice == '2':
            print("Kembali ke Menu Utama...")
            print(' ')
            break
        else:
            print("Opsi tidak valid. Silakan pilih [1-2].")


#================================================MAIN MENU=================================================
#main menu untuk admin
def print_menu_admin():
    #list main menu
    menu_options = [
        (1, 'Report Data Mobil'),
        (2, 'Menambahkan Data Mobil'),
        (3, 'Merubah Data Mobil'),
        (4, 'Menghapus Data Mobil'),
        (5, 'Exit')
    ]

    #spacing
    col1_width = 5
    col2_width = 25

    #print tabel
    print("=" * (col1_width + col2_width + 3))
    print(f"{'No':<{col1_width}} | {'Menu':<{col2_width}}")
    print("-" * (col1_width + col2_width + 3))

    #print menu
    for option, menu in menu_options:
        print(f"{option:<{col1_width}} | {menu:<{col2_width}}")
    
    print("=" * (col1_width + col2_width + 3))

#main menu untuk customer
def print_menu_customer():
    #list main menu
    menu_options = [
        (1, 'Data Rental Mobil Hari ini'),
        (2, 'Pemesanan & Customer Service'),
        (3, 'Exit')
    ]

    #spacing
    col1_width = 5
    col2_width = 25

    #print tabel
    print("=" * (col1_width + col2_width + 3))
    print(f"{'No':<{col1_width}} | {'Menu':<{col2_width}}")
    print("-" * (col1_width + col2_width + 3))

    #print menu
    for option, menu in menu_options:
        print(f"{option:<{col1_width}} | {menu:<{col2_width}}")
    
    print("=" * (col1_width + col2_width + 3))

#main menu loop untuk admin
def main_admin():
    while True:
        print(' ')
        dashboard()
        print_menu_admin()
      
        try:
            pilihan = int(input("Silahkan pilih menu [1-5] : "))
        except ValueError:
            print("Input tidak valid. Masukkan angka antara [1-5].")
            loading_screen_next()
            continue
        
        if pilihan == 1:
            report_data_mobil_menu()
        elif pilihan == 2:
            tambah_data_mobil_menu()
        elif pilihan == 3:
            ubah_data_mobil_menu()
        elif pilihan == 4:
            hapus_data_mobil_menu()
        elif pilihan == 5:
            print(' ')
            print("Keluar dari program...")
            print(f"Thank you {user_id}, Adios!")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu antara [1-5].")
            print(' ')

#main menu loop untuk customer
def main_customer():
    while True:
        print(' ')
        dashboard()
        print_menu_customer()
      
        try:
            pilihan = int(input("Silahkan pilih menu [1-3] : "))
        except ValueError:
            print("Input tidak valid. Masukkan angka antara [1-3].")
            loading_screen()
            continue
        
        if pilihan == 1:
            report_data_mobil_cust()
        elif pilihan == 2:
            print(' ')
            print('Hubungi 087730204009 / 0217465772 atau langsung datang ke Lokasi kami di Jl. Kebon Kacang 20 Jakarta Selatan')
            print(' ')
            loading_screen()

        elif pilihan == 3:
            print(' ')
            print("Keluar dari program...")
            print(f"Thank you {user_id}, Adios!")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu antara [1-3].")
            print(' ')

#call main menu
if user_id == 'ADMIN':
    main_admin()
else:
    main_customer()
    



#patch 9/17:
#read   :done
#create :done
#update :done
#delete :done

#check overall code : done