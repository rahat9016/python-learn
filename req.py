import requests

API_BASE_URL = 'https://api.kirjaswappi.fi/api/v1'


def authenticate():
    body ={
    'username': "user",
    'password': "mak12345"
    }
    try:
        response = requests.post(url=f'{API_BASE_URL}/authenticate', json=body)
        response.raise_for_status()
        return response.json().get('jwtToken')
            
    except requests.RequestException as e:
        print(f'Error during the authentication: {e}')
        return None


def get_users(token):
    print(token)
    try:
        response = requests.get(url=f'{API_BASE_URL}/users', headers={'Authorization': f'Bearer {token}'})
        response.raise_for_status()
        return response.json()
            
    except requests.RequestException as e:
        print(f'Fetching Error: {e}')
        return None

def delete_user(id, token):
    try:
        response = requests.delete(url=f'{API_BASE_URL}/users/{id}', headers={'Authorization': f'Bearer {token}'})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error deleting user {id}: {e}')
        return None
    


def main():
    jwt = authenticate()
    if not jwt:
        print('Failed JWT')
        return None
    elif jwt:
        users = get_users(jwt)
        if not users:
            print('Does not exit users')
            return None
    
        for user in users:
            user_id = user['id']
            if user_id:
                    delete_user(jwt, user_id)
            else:
                print(f'Invalid user data: {user}')
        
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')