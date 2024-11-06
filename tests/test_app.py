from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
#def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    #page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    #p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    #expect(p_tag).to_have_text("This is the homepage.")

# unfinished, to be worked on after implementing show-spaces
#def test_create_space(db_connection, page, test_web_address):
    #db_connection.seed("seeds/makersbnb.sql")
    #page.goto(f"http://{test_web_address}/list-space")
    ##page.fill("input[name=spacename]", "Test Space")
   # page.fill("input[name=price]", "50")
    #page.fill("input[name=description]", "This is a test description.")
    #page.click("text='Upload Space'")

def test_show_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    page.goto(f"http://{test_web_address}/home/1")
    
    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Cosy Apartment in the Heart of the City")