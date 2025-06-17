from textnode import TextNode

def main():
    bill = TextNode("Wibble Wobble", "normal")
    bill_link = TextNode("Click here", "code")
    
    bill.__repr__()
    print(bill_link)


main()