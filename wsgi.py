from src import create_app

handler = create_app()

if __name__ == '__main__':
    handler.run(host='0.0.0.0', port=5000, debug=True)