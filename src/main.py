from textnode import TextNode, TextType

def main():
    bill = TextNode("Wibble Wobble", TextType.NORMAL)
    bill_link = TextNode("Click here", TextType.CODE , "www.weewoo.com")
    
    print(bill)
    print(bill_link)


main()