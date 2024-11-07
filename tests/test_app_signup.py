from playwright.sync_api import Page, expect

def test_attempt_signup_with_no_fields(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/signup")

    page.click("text='Submit'")

    assert page.url == f"http://{test_web_address}/signup"

def test_attempt_signup_with_invalid_email(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/signup")
    
    page.fill("input[name='name']", "Robert")
    page.fill("input[name='email']", "email")
    page.fill("input[name='password']", "ilovemywife")
    page.fill("input[name='mobile_number']", "1234567890")

    page.click("text=submit")

    assert page.url == f"http://{test_web_address}/signup"

def test_attempt_signup_with_invalid_password(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name='name']", "Robert")
    page.fill("input[name='email']", "rob@ert.com")
    page.fill("input[name='password']", "bob")
    page.fill("input[name='mobile_number']", "1234567890")

    page.click("text='Submit'")

    error_message = page.locator(".error-message")
    expect(error_message).to_have_text("Password must be at least 8 characters long.")

def test_attempt_signup_with_invalid_number(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/signup")
    
    page.fill("input[name='name']", "Robert")
    page.fill("input[name='email']", "rob@ert.com")
    page.fill("input[name='password']", "ilovemywife")
    page.fill("input[name='mobile_number']", "phone")

    page.click("text=submit")

    assert page.url == f"http://{test_web_address}/signup"

def test_attempt_correct_signup(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/signup")
    
    page.fill("input[name='name']", "Robert")
    page.fill("input[name='email']", "rob@ert.com")
    page.fill("input[name='password']", "ilovemywife")
    page.fill("input[name='mobile_number']", "1234567890")

    page.click("text=Submit")

    signup_success_heading = page.get_by_role("heading", name="Signup Successful!")
    expect(signup_success_heading).to_be_visible()

    page.click("text='Go to Login'")

    page.fill("input[name='email']", "rob@ert.com")
    page.fill("input[name='password']", "ilovemywife")
    page.click("text=Submit")

    assert page.url == f"http://{test_web_address}/logged/1"