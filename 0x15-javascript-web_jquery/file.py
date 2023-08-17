def create_files():
    for i in range(3, 10):
        jsfiles = f"{i}-main.html"
        htmlfiles = f"{i}-script.js"

        with open(jsfiles, 'w') as file:
            file.write("")

        with open(htmlfiles, 'w') as file:
            file.write("")

    for i in range(100, 104):
        jsfiles = f"{i}-main.html"
        htmlfiles = f"{i}-script.js"

        with open(jsfiles, 'w') as file:
            file.write("")

        with open(htmlfiles, 'w') as file:
            file.write("")

if __name__ == "__main__":
    create_files()
