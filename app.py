from application import app
# if the file is being run directly, and not imported, then start the application. 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
