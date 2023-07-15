import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent=''
)

search_term = input("Search : ")

page = wiki_wiki.page(search_term)

if page.exists():
    print("Article title :", page.title)
    print("Article summary : ")
    print(page.summary)
    print("Article Links:", page.fullurl)
else:
    print("Page not found.")
