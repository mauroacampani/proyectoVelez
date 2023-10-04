import requests

import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def generate_request(url, params={}):
    response = requests.get(url, params=params , headers=headers)

    if response.status_code == 200:
        return response.json()



def get_username(params={}):
    
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/arg.copa_lpf/teams/21/roster?region=ar&lang=es', params)
    player = {}

    if response:
        
        arquero = jugador(response, 'Arquero')

        player['arquero'] = arquero

        defensor = jugador(response, 'Defensor')

        player['defensa'] = defensor
        
        medio = jugador(response, 'Mediocampista')

        player['medio'] = medio

        atacante = jugador(response, 'Atacante')

        player['ataque'] = atacante


        return player

    return ''

def jugador(response, posicion):

        resultado = list()

        equipos = response['athletes']
        
        for n in equipos:
            
            if n['position']['displayName'] == posicion:
                
                tablaProsiciones = {}
            
                tablaProsiciones['nombre'] = n['fullName']
                valor = n.__contains__('jersey')
                if valor:
                    
                    tablaProsiciones['dorsal'] = n['jersey']

                # tablaProsiciones['nac'] = n['jersey']

                tablaProsiciones['edad'] = n['age']
                #tablaProsiciones['altura'] = n['displayHeight']
                tablaProsiciones['pos'] = n['position']['abbreviation']
                #tablaProsiciones['peso'] = n['displayWeight']
                tablaProsiciones['nac'] = n['citizenship']
                resultado.append(tablaProsiciones)
                
        return resultado
    
    


def resultados(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/21/schedule?region=ar&lang=es&season=2023', params)
    
    resultado = list()

    i = 1
    if response:

        fixture = response['events']
        
        for c in fixture:
            if c['id'] != '625787':
                for e in c['competitions']:
                    fecha = e['date']
                    dia = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime('%A')
                    fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m-%Y")
                    
                
                    tablaProsiciones = {}
                    tablaProsiciones['dia'] = dia
                    tablaProsiciones['fecha'] = fecha1
                    tablaProsiciones['equipo1'] = e['competitors'][0]['team']['displayName']
                    tablaProsiciones['equipo2'] = e['competitors'][1]['team']['displayName']
                    tablaProsiciones['logo1'] = e['competitors'][0]['team']['logos'][0]
                    tablaProsiciones['logo2'] = e['competitors'][1]['team']['logos'][0]
                    tablaProsiciones['score1'] = e['competitors'][0]['score']['value']
                    tablaProsiciones['score2'] = e['competitors'][1]['score']['value']
                    

                    resultado.append(tablaProsiciones)
                        
                     
         
        return resultado
    
    return ''


def resultadosLib(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/21/schedule?region=ar&lang=es&season=2023', params)
    
    resultado = list()

    if response:

        fixture = response['events']
        
        for c in fixture:
            
            if c['seasonType']['id'] == "5" or c['seasonType']['id'] == "6":
                
                for e in c['competitions']:
                    fecha = e['date']
                    dia = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime('%A')
                    fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m-%Y")
                    
                    tablaProsiciones = {}
                    tablaProsiciones['dia'] = dia
                    tablaProsiciones['fecha'] = fecha1
                    
                    tablaProsiciones['equipo1'] = e['competitors'][0]['team']['displayName']
                    tablaProsiciones['equipo2'] = e['competitors'][1]['team']['displayName']
                    tablaProsiciones['logo1'] = e['competitors'][0]['team']['logos'][0]
                    tablaProsiciones['logo2'] = e['competitors'][1]['team']['logos'][0]
                    tablaProsiciones['score1'] = e['competitors'][0]['score']['value']
                    tablaProsiciones['score2'] = e['competitors'][1]['score']['value']
                    tablaProsiciones['condicion'] = e['leg']['displayValue']
                    tablaProsiciones['estadio'] = e['venue']['fullName']
                        

                    resultado.append(tablaProsiciones)
                    
         
        return resultado
    return ''


def calendario(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/all/teams/21/schedule?region=ar&lang=es&fixture=true', params)
    
    resultado = list()

    i = 1
    if response:

        fixture = response['events']
        
        for c in fixture:
            calendario = {}
            calendario['liga'] = c['league']['abbreviation']
            for e in c['competitions']:
                
                fecha = e['date']
                    
                fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m")
                       
                
                calendario['fecha'] = fecha1
                calendario['equipo1'] = e['competitors'][0]['team']['displayName']
                calendario['equipo2'] = e['competitors'][1]['team']['displayName']
                calendario['logo1'] = e['competitors'][0]['team']['logos'][0]
                calendario['logo2'] = e['competitors'][1]['team']['logos'][0]
                

                resultado.append(calendario)
                        
                        
         
        return resultado
    
    return ''



  
def tabla(params={}):
    #COPA DE LA LIGA ARGENTINA
    response = generate_request('https://site.web.api.espn.com/apis/v2/sports/soccer/arg.copa_lpf/standings?region=ar&lang=es&contentorigin=deportes&season=2023&sort=rank%3Aasc', params)
    
    #LIGA ARGENTINA
    #response = generate_request('https://site.web.api.espn.com/apis/v2/sports/soccer/ARG.1/standings?region=ar&lang=es&contentorigin=deportes&season=2023&sort=rank%3Aasc', params)
    if response:
        
        fixture = response['children']
        
        i = 1
        datos = list() 
        for t in fixture:
        
            
            for s in t['standings']['entries']:
               
                tablaProsiciones = {}
                tablaProsiciones['puesto'] = i
                tablaProsiciones['logo'] = s['team']['logos']
                tablaProsiciones['name'] = s['team']['name']
                tablaProsiciones['pj'] = s['stats'][0]
                tablaProsiciones['g'] = s['stats'][7]
                tablaProsiciones['e'] = s['stats'][6]
                tablaProsiciones['p'] = s['stats'][1]
                tablaProsiciones['gf'] = s['stats'][5]
                tablaProsiciones['gc'] = s['stats'][4]
                tablaProsiciones['dif'] = s['stats'][2]
                tablaProsiciones['pts'] = s['stats'][3]
                
                
                datos.append(tablaProsiciones)

                i +=1

                    
            return datos
    
    return ''

def tablaLibertadores(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/v2/sports/soccer/conmebol.libertadores/standings?region=ar&lang=es&contentorigin=deportes&season=2023&sort=rank%3Aasc', params)
                                
    if response:
        
        fixture = response['children']
        i = 1
        datos = list() 
        for t in fixture:
        
            if t['id'] == "3":
                
                for s in t['standings']['entries']:
            
                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['logo'] = s['team']['logos']
                    tablaProsiciones['name'] = s['team']['name']
                    tablaProsiciones['pj'] = s['stats'][3]
                    tablaProsiciones['g'] = s['stats'][0]
                    tablaProsiciones['e'] = s['stats'][2]
                    tablaProsiciones['p'] = s['stats'][1]
                    tablaProsiciones['gf'] = s['stats'][4]
                    tablaProsiciones['gc'] = s['stats'][5]
                    tablaProsiciones['dif'] = s['stats'][9]
                    tablaProsiciones['pts'] = s['stats'][6]

                    datos.append(tablaProsiciones)

                    i +=1

                    
                return datos
    
    return ''

def goles(params={}):
    #PARA CAMBIAR LOS GOLEADORES DE LA LIGA DESPUES DE soccer/ARG.1 PARA LA COPA DE LA LIGA arg.copa_lpf
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/arg.copa_lpf/teams/21/statistics?region=ar&lang=es&contentorigin=deportes&level=1', params)
    
    if response:
        
        fixture = response['results']['stats']
        i = 1
        datos = list()
        asist = list()
        est = {}

        for t in fixture:
            
            if t['name'] == 'goalsLeaders':
                for s in t['leaders']:
                    

                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['name'] = s['athlete']['displayName']
                    tablaProsiciones['pj'] = s['athlete']['statistics'][0]
                    tablaProsiciones['g'] = s['athlete']['statistics'][1]

                    datos.append(tablaProsiciones)
                    i +=1
                    if i == 11:
                        break

                

                est['goles'] = datos
            else:
                i = 1
                for s in t['leaders']:
                    

                    tablaProsiciones = {}
                    tablaProsiciones['puesto'] = i
                    tablaProsiciones['name'] = s['athlete']['displayName']
                    tablaProsiciones['pj'] = s['athlete']['statistics'][0]
                    tablaProsiciones['a'] = s['athlete']['statistics'][2]

                    asist.append(tablaProsiciones)
                    i +=1
                    if i == 11:
                        break
                
                est['asist'] = asist

        return est
         
        
    return ''


def tarjetas(params={}):
    response = generate_request('https://site.web.api.espn.com/apis/site/v2/sports/soccer/arg.copa_lpf/teams/21/statistics?region=ar&lang=es&contentorigin=deportes&level=2', params)
    
    if response:
        
        fixture = response['results']['stats']
        i = 1
        datos = list()

        for t in fixture:
            
                

            tablaProsiciones = {}
            tablaProsiciones['puesto'] = i
            tablaProsiciones['name'] = t['displayName']
            tablaProsiciones['pj'] = t['statistics'][0]
            tablaProsiciones['tr'] = t['statistics'][1]
            tablaProsiciones['ta'] = t['statistics'][2]
            datos.append(tablaProsiciones)
            i +=1
            if i == 11:
                break
        
        return datos
         
        
    return ''