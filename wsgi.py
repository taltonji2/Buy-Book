import src
handler = src.create_app()


if __name__ == '__main__':
    print("== Running in debug mode ==")
    src.create_app().run(host='0.0.0.0', port=5000, debug=True)