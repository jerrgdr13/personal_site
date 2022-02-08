from distutils.log import debug
from readline import append_history_file
from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)