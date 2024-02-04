travelLogs = [
  {
    "country": "USA",
    "visits": 7,
    "cities": ["Washington","New York","Nevada"]
  },
  {
    "country":"Italy",
    "visits": 3,
    "cities":["Sicily","Venice","Rome","Milan"]
  }
]

def addNewCountry(countryVisited, timeVisited,citiesVisited):
  newCountry = {}
  newCountry["country"] = countryVisited
  newCountry["visits"] = timeVisited
  newCountry["cities"] = citiesVisited
  travelLogs.append(newCountry)

addNewCountry("Germany", 2,["Frankfurt","Berlin","Munich","Hamburg"])

print(travelLogs)