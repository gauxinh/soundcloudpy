import httplib2
import requests


def call_api(url, authen, data, method):
    try:
        if method == "GET" or method == "POST" or method =="PUT" or method =='':
            response = requests.request(method,url,auth=(authen),data=data)
            print(response.status_code)
            if response.status_code >= 200 and response.status_code < 300:
                status='OK'
            elif response.status_code >= 400 and response.status_code < 500:
                status='Erreur de paramètre'
            elif response.status_code >= 500:
                status='Erreur de serveur'
            else:
                status='Erreur inconnu'
            print('Le status est '+status)
            print(response.headers)
            if not response.content:
                print('Pas de contenu dans la réponse')
            else:
                print(response.content)
        else:
            print('Méthode non autorisée')
            exit()
    except ConnectionError:
        print('Erreur de connexion est survenue'+response.reason)

    except TimeoutError:
        print('Connexion timeout')
    return response


def main():
    #url = 'https://sts.cdiscount.com/users/httpIssue.svc/?realm=https://wsvc.cdiscount.com/MarketplaceAPIService.svc'
    authen=('***','***')
    headers=('')
    data=('')
    method='GET'

    call_api(url,authen,data,method)

if __name__ == '__main__':
    main()