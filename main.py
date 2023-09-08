from blog import create_app

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5500)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
