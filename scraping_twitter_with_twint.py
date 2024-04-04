import twint
# Configure
def scraping_twitter(keyword,lokasi_penympanan):
    c = twint.Config()
    c.Search = keyword
    c.Lang = "id"
    c.Since = "2022-01-01 21:09:18" #"2022-01-01 21:09:18"
    c.Until = "2022-10-04 21:09:18" #"2022-10-04 21:09:18"
    c.Store_csv = True
    c.Output = lokasi_penympanan
# Run
    twint.run.Search(c)
    
# Import json Python module
import json
 
# Open the sample JSON file
# Using the open() function
file = open("Scraping produk wardah.json", 'r')
 
# Convert the JSON data into Python object
# Here it is a dictionary
json_data = json.load(file)
 
file.close()

for data in json_data:
    print(data["Nama Kategori"])
    nama_kategori = data["Nama Kategori"]
    nama_file = data["Nama Kategori"]+".csv"
    scraping_twitter(nama_kategori,nama_file)
