import requests
from dotenv  import load_dotenv
load_dotenv()

key=os.environ['BOOKBOTCLUBAPI']
H={"api_key":key}
url="https://api.airtable.com/v0/appB7YoaWh3su8mAO/BookClubBot?maxRecords=999&view=Grid%20view"
r=requests.get(url,params=H)
books_dict=r.json()
print(books_dict)

