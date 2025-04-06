import time

import pytest
from Pages.LoginPage import Login_page
from apirequests import api_requests
from Pages.BooksPage import Books_page
from Utils.Random_userandpass_generator import generate_random_password, generate_random_username
from  conftest import SingletonDriverinstance,driver


@pytest.fixture(scope="session")
def create_user_fixture():
    # Generate random username and password
    username, password = generate_random_username(), generate_random_password()
    # Create user via API
    api_requests.create_user(username, password)
    return username, password




#@pytest.mark.usefixtures("driver")
def test_login_via_web(driver, create_user_fixture):
    username, password = create_user_fixture
    driver.get('https://demoqa.com/login')
    # Initialize Login Page
    login = Login_page(driver)
    login.scroll_in_the_login()
    login.login(username, password)

@pytest.mark.usefixtures("driver")
def test_validate_userName(driver, create_user_fixture):
    actual_username = create_user_fixture[0]
    books = Books_page(driver)
    books.validate_userName(actual_username)

@pytest.mark.usefixtures("driver")
def test_compare_books_via_ui_and_api(driver):
    driver.get('https://demoqa.com/books')
    time.sleep(4)
    print('HiEPam')
    books = Books_page(driver)
    books.scroll_by_pixels()
    time.sleep(8)
    Books_from_ui=books.get_ui_books_and_details()
    Books_from_api=api_requests.get_books()
    print(f"TheBooks_from_ui are{Books_from_ui},Books_from_api are {Books_from_api} ")
    for i in range (len(Books_from_ui)):
        print(Books_from_ui[i]["author"],Books_from_api["books"][i]["author"],"Im in books validation")
        assert Books_from_ui[i]["author"]==Books_from_api["books"][i]["author"],f"The assertion failed for author:{Books_from_ui[i]["author"]}{Books_from_api["books"][i]["author"]}"
        assert Books_from_ui[i]["title"]==Books_from_api["books"][i]["title"],f"The assertion failed for title:{Books_from_ui[i]["title"]}{Books_from_api["books"][i]["title"]}"
        assert Books_from_ui[i]["publisher"]==Books_from_api["books"][i]["publisher"],f"The assertion failed for publisher:{Books_from_ui[i]["publisher"]}{Books_from_api["books"][i]["publisher"]}"






