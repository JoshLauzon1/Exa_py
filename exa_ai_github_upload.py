from exa_py import Exa
exa = Exa('') #put exa key in here

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=[''], #put any website link in here
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()