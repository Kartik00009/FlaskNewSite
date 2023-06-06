from website import create_app
from newsapi import NewsApiClient

app = create_app()
newsapi = NewsApiClient(api_key='bfb1f9bdc8354843b030c42346272995')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
