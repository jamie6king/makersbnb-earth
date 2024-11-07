from playwright.sync_api import Page, expect

def test_attempt_incorrect_login(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/login")
    
    page.fill("input[name='email']", "incorrect@gmail.com")
    page.fill("input[name='password']", "wrongpassw0rd")

    page.click("text=Submit")

    error_message = page.locator(".error-message")
    expect(error_message).to_have_text("Invalid email or password!")

def test_attempt_correct_login(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    
    db_connection.execute("INSERT INTO users (email, hashed_password) VALUES ('test@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f')")

    page.goto(f"http://{test_web_address}/login")

    page.fill("input[name='email']", "test@gmail.com")
    page.fill("input[name='password']", "12345678")
    page.click("text=Submit")

    assert page.url == f"http://{test_web_address}/logged/1"