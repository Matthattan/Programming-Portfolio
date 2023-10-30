from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.co.uk/PlayStation-Card-Wallet-Download-Code/dp/B00GUXZTOI/ref=zg_bs_c_videogames_sccl_1/262-0977284-3341907?pd_rd_w=mXhec&content-id=amzn1.sym.3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_p=3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_r=KXG045BTZSHV4H57394J&pd_rd_wg=YKAaE&pd_rd_r=8ee4f873-a028-404d-89f7-878a7ef33377&pd_rd_i=B00GUXZTOI&th=1"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

# Due to botting, parsing actual website is no longer possible
prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)