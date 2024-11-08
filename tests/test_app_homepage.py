from playwright.sync_api import Page, expect

def test_check_homepage_is_empty(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/")

    title = page.locator("h2")
    expect(title).to_have_text("Latest Available Stays")

    listings = page.locator("div.new-listings").all()
    assert len(listings) == 0

def test_check_homepage_is_populated(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    page.goto(f"http://{test_web_address}/")

    title = page.locator("h2")
    expect(title).to_have_text("Latest Available Stays")

    listings = page.locator("div.new-listings").all()
    assert len(listings) == 5

def test_check_homepage_cant_see_viewing_when_not_logged_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    page.goto(f"http://{test_web_address}/")

    buttons = page.locator("a.space-button").all()
    popup_message = page.locator(".popup")

    expect(popup_message).not_to_be_visible()
    buttons[0].click()
    expect(popup_message).to_be_visible()

def test_check_logged_in_homepage_has_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    db_connection.execute("INSERT INTO users (email, hashed_password) VALUES ('test@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f')")

    page.goto(f"http://{test_web_address}/login")

    page.fill("input[name='email']", "test@gmail.com")
    page.fill("input[name='password']", "12345678")
    page.click("text=Submit")

    title = page.locator("h2")
    expect(title).to_have_text("Latest Available Stays")

    listings = page.locator("div.new-listings").all()
    assert len(listings) == 5

def test_check_logged_in_homepage_can_access_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    db_connection.execute("INSERT INTO users (email, hashed_password) VALUES ('test@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f')")

    page.goto(f"http://{test_web_address}/login")

    page.fill("input[name='email']", "test@gmail.com")
    page.fill("input[name='password']", "12345678")
    page.click("text=Submit")

    listings = page.locator("a.read-more").all()
    listings[1].click()

    assert True