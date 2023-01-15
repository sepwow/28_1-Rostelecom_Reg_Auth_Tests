import os

from dotenv import load_dotenv

load_dotenv()

name = os.getenv('name')
surname = os.getenv('surname')
mail = os.getenv('mail')
phone = os.getenv('phone')
password = os.getenv('password')
