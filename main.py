import requests

def get_breaking_bad_quotes(num_quotes):
    url = f"https://api.breakingbadquotes.xyz/v1/quotes/{num_quotes}"
    response = requests.get(url)

    if response.status_code == 200:
        quotes = response.json()
        for i, quote_info in enumerate(quotes):
            quote = quote_info['quote']
            author = quote_info['author']
            print(f"{i + 1}. Breaking Bad Quote: {quote} - {author}")
    else:
        print(f"Error: {response.status_code}")

num_quotes = int(input("Kaç alıntı istersiniz? "))

get_breaking_bad_quotes(num_quotes)



