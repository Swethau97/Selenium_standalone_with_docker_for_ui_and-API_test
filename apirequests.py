import requests
from Utils.Logger import initialize_logger

logger=initialize_logger()
class api_requests:
    @staticmethod
    def create_user(username,password):
        url='https://demoqa.com/Account/v1/User'
        headers={
            'Content-Type':'application/json',
            'Accept': 'application/json'
        }
        body={
"userName": username,
"password": password
}
        response=requests.post(url,json=body,headers=headers)
        print("Response Status Code:", response.status_code,username,password)
        print("Response Body:", response.json())
        if response.status_code !=201:
            logger.error(f"Request failed:{response.text} ")
            raise Exception(f"Request failed [To create user] {response.status_code}")
        logger.info(f"The request is successful {response.status_code} and the user is successfully created")
        return response.json()

    @staticmethod
    def get_books():
        response=requests.get('https://demoqa.com/BookStore/v1/Books')
        if response.status_code != 200:
            logger.error(f"Request failed:{response.text} ")
            raise Exception(f"Request failed [To get the books {response.status_code}")
        logger.info(f"The request is successful {response.status_code} and the user is successfully created")
        print(response.json(),"from api")
        return response.json()


