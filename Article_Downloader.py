import pdfkit
import requests
import os

def is_url_valid(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def download_article_as_pdf(url, output_path="output.pdf"):
    try:
        pdfkit.from_url(url, output_path)
        print(f"Your article is successfully downloaded to {output_path}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    URL = input("Provide article URL: ")
    if is_url_valid(URL):
        download_article_as_pdf(URL)
    else:
        print("Enter a valid working URL")
