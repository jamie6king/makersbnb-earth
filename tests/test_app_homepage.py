from playwright.sync_api import Page, expect

def test_check_homepage_empty(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/")

    listings_title = page.locator("h2")
    expect(listings_title).to_have_text("Latest Available Stays")

    listings = page.locator("div.new-listings")
    expect(listings).not_to_be_visible()

def test_check_homepage_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    page.goto(f"http://{test_web_address}/")

    listings_title = page.locator("h2")
    expect(listings_title).to_have_text("Latest Available Stays")

    listings = page.locator("div.new-listings").all()
    assert len(listings) == 6
