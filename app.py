from app.__init__ import create_app

# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=5000, debug=True)