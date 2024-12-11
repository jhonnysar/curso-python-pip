import utils
import read_csv
import charts

def run():
  data=read_csv.read_csv('data.csv')
  country=input('Type Country => ')

  datos = utils.population_by_country(data,country)
  if len(datos)>0:
    year,population = utils.get_population(datos[0])
    print (year)
    print (population)
    charts.generate_bar_chart(country,year,population)
  
  data=list(filter(lambda item: 'America' in item['Continent'],data))
  countries,percentages = utils.get_world_percentages(data)
  charts.generate_pie_chart(countries,percentages)

if __name__ == '__main__':
  run()