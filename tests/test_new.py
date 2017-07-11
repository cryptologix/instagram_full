#test 1

def test_1(app):
    app.open_home_page()
    app.session.login("silenkovinst","qweQWE123!@#")
    app.like.put_hashtag_name("#магнит")
    app.like.open_first_image()
    app.like.start_like(500)
