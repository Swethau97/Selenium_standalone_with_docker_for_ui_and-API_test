from BasePages.Basemethods import BaseMethods
from selenium.webdriver.common.by import By


class Books_page(BaseMethods):
    USERNAME = (By.ID, "userName-value")
    BOOKS_TABLE=(By.CLASS_NAME,"rt-tr-group")


    def __init__(self, driver):
        super().__init__(driver)


    def validate_userName(self, actual_userName, timeout=15):
        return_element = self.find_element(self.USERNAME, timeout)
        expected_userName = return_element.text
        print("asser usernames",actual_userName,expected_userName)
        assert expected_userName == actual_userName, (
            f"Expected username '{expected_userName}' does not match actual username '{actual_userName}'"
        )

    def get_ui_books_and_details(self):
        books = self.find_elements(self.BOOKS_TABLE)  # Locate all rows in the table
        book_details = []

        for i in range(1, len(books)-1):  # XPath uses 1-based indexing
            try:
                title_element = self.find_element(
                    (By.XPATH, f"(//div[@class='rt-tr-group'][{i}]//div[@class='rt-td'][2]//a)"))
                author_element = self.find_element(
                    (By.XPATH, f"(//div[@class='rt-tr-group'][{i}]//div[@class='rt-td'][3])"))
                publisher_element = self.find_element(
                    (By.XPATH, f"(//div[@class='rt-tr-group'][{i}]//div[@class='rt-td'][4])"))

                # Extract text content, falling back to an empty string if not found
                title_text = title_element.text if title_element else ""
                author_text = author_element.text if author_element else ""
                publisher_text = publisher_element.text if publisher_element else ""

                # Log or use the extracted data as needed
                print(f"Title: {title_text}, Author: {author_text}, Publisher: {publisher_text}")

            except Exception as e:
                # Handle any errors, e.g., element not found
                print(f"Error processing book at index {i}: {e}")

            # Append book details to the list
            book_details.append({
                "title": title_text,
                "author": author_text,
                "publisher": publisher_text
            })

        print(book_details)
        return book_details

    def scroll_in_the_books_page(self):
        self.scroll_by_pixels()



