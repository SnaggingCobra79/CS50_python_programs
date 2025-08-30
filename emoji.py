import emoji

def main():
    code = input("Input: ")
    print(emoji.emojize(code, language="alias"))
main()
