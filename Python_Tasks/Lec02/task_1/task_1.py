# Program to let the user choose the browser and open a choosen website form url module
import url

url.print_browesers()
browser = int(input())
url.print_urls()
website = int(input())

url.open(browser, website)
