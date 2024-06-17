import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://fuatanshori.com/masuk/')

    def test_login_gagal(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email') 
        password_field = driver.find_element(By.NAME, 'password')
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('passwordsalah') 
        password_field.send_keys(Keys.RETURN)
        self.assertIn('https://fuatanshori.com/masuk/', driver.current_url)
        error_message = driver.find_element(By.CLASS_NAME, 'danger')
        self.assertEqual(error_message.text, 'Email Atau Password Salah')
        
    def test_login_berhasil(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('mysqladmin')
        password_field.send_keys(Keys.RETURN)
        self.assertIn('https://fuatanshori.com/', driver.current_url)
        
        
        
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
     
        
class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://fuatanshori.com/daftar/')
        

    def test_register_gagal_password_berbeda(self):
        driver = self.driver
        nama_lengkap_field = driver.find_element(By.NAME,'full_name')
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password1')
        password_confirmation_field = driver.find_element(By.NAME, 'password2')
        
        nama_lengkap_field.send_keys('admin')
        email_field.send_keys('admin@gmail.com')
        password_field.send_keys('mysqladmin')
        password_confirmation_field.send_keys('mysqladminn')
        password_field.send_keys(Keys.RETURN)
        error_message = driver.find_element(By.CLASS_NAME, 'danger')
        self.assertEqual(error_message.text, 'Password berbeda')
        
    # --
    def test_register_berhasil(self):
        driver = self.driver
        nama_lengkap_field = driver.find_element(By.NAME,'full_name')
        email_field = driver.find_element(By.NAME, 'email') 
        password_field = driver.find_element(By.NAME, 'password1')
        password_confirmation_field = driver.find_element(By.NAME, 'password2')
        
        data_nama_lengkap='admin1234'
        data_email= 'admin1235@gmail.com'
        data_password = 'mysqladmin'
        data_password_confirmation = 'mysqladmin'
        
        nama_lengkap_field.send_keys(data_nama_lengkap)
        email_field.send_keys(data_email)
        password_field.send_keys(data_password) 
        password_confirmation_field.send_keys(data_password_confirmation)
        password_field.send_keys(Keys.RETURN)
        self.assertIn(f'https://fuatanshori.com/masuk/?command=verification&email={data_email}', driver.current_url)  # Asumsikan tetap di halaman login
        
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        

class TambahMapel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://fuatanshori.com/masuk/')

    # --
    def test_tambah_mapel_sukses(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('mysqladmin')
        password_field.send_keys(Keys.RETURN)
        
        driver.get("https://fuatanshori.com/admin/mapel/matapelajaran/add/")
        nama_mapel_field = driver.find_element(By.NAME, 'nama_mapel')
        mini_description_field = driver.find_element(By.NAME, 'mini_description')
        save_field = driver.find_element(By.NAME, '_save')
       
        data_mapel ="Bahasa I"
        nama_mapel_field.send_keys(data_mapel)
        mini_description_field.send_keys("ini deskripsi")
        save_field.send_keys(Keys.RETURN)
        success_message = driver.find_element(By.CLASS_NAME, 'success')
        self.assertEqual(success_message.text,f'Matapelajaran “{data_mapel}” berhasil ditambahkan.')
        
       
    def test_tambah_mapel_gagal_input_nama_mapel(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('mysqladmin') 
        password_field.send_keys(Keys.RETURN)
        
        driver.get("https://fuatanshori.com/admin/mapel/matapelajaran/add/")
        nama_mapel_field = driver.find_element(By.NAME, 'nama_mapel')
        mini_description_field = driver.find_element(By.NAME, 'mini_description')
        save_field = driver.find_element(By.NAME, '_save')
        nama_mapel_field.send_keys("")
        mini_description_field.send_keys("ini deskripsi")
        save_field.send_keys(Keys.RETURN)
        errorlist_message = driver.find_element(By.CSS_SELECTOR, 'ul.errorlist li')
        self.assertEqual(errorlist_message.text,"Bidang ini tidak boleh kosong.")
    
        
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

class TambahModul(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://fuatanshori.com/masuk/')

    def test_tambah_modul_sukses(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('mysqladmin')
        password_field.send_keys(Keys.RETURN)
        
        driver.get("https://fuatanshori.com/admin/modul/modul/add/")
        nama_modul_field = driver.find_element(By.NAME, 'nama_modul')  
        mata_pelajaran_field = driver.find_element(By.NAME, 'mata_pelajaran')  
        mini_description_field = driver.find_element(By.NAME, 'mini_description')  
        modul_field = driver.find_element(By.NAME, 'modul')  
        
        
        data_nama_modul ="Pertemuan 1"
        nama_modul_field.send_keys(data_nama_modul)
        mini_description_field.send_keys("pertemuan pertama bab 1")
        mata_pelajaran_field.send_keys(Keys.ARROW_DOWN)
        modul_field.send_keys('D:\\PY\\file.pdf')
        save_field = driver.find_element(By.NAME, '_save')  
        save_field.send_keys(Keys.RETURN)

        success_message = driver.find_element(By.CLASS_NAME, 'success')
        self.assertEqual(success_message.text,f'Modul “{data_nama_modul}” berhasil ditambahkan.')
   
    def test_tambah_modul_gagal_upload_modul(self):
        driver = self.driver
        email_field = driver.find_element(By.NAME, 'email')  
        password_field = driver.find_element(By.NAME, 'password')  
        
        email_field.send_keys('muhammadalghifari602@gmail.com')
        password_field.send_keys('mysqladmin')
        password_field.send_keys(Keys.RETURN)
        
        driver.get("https://fuatanshori.com/admin/modul/modul/add/")
        nama_modul_field = driver.find_element(By.NAME, 'nama_modul')
        mata_pelajaran_field = driver.find_element(By.NAME, 'mata_pelajaran') 
        mini_description_field = driver.find_element(By.NAME, 'mini_description') 
        modul_field = driver.find_element(By.NAME, 'modul') 
        
        
        data_nama_modul ="Pertemuan 1"
        nama_modul_field.send_keys(data_nama_modul)
        mini_description_field.send_keys("pertemuan pertama bab 1")
        mata_pelajaran_field.send_keys(Keys.ARROW_DOWN)
        modul_field.send_keys('D:\\PY\\file.docx')
        save_field = driver.find_element(By.NAME, '_save')
        save_field.send_keys(Keys.RETURN)

        errorlist_message = driver.find_element(By.CSS_SELECTOR, 'ul.errorlist li')

        self.assertEqual(errorlist_message.text,f'Ekstensi berkas “docx” tidak diizinkan. Ekstensi diizinkan adalah: pdf.')
        
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

        
        
if __name__ == "__main__":
    unittest.main()
