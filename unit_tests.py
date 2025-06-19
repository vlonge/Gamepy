import unittest
from app import app, db, Character, Gender
from flask import url_for
from random import randint

class TestCharacterPage(unittest.TestCase):

    def setUp(self):
        # Configure the app for testing
        app.config['TESTING'] = True
        # Use an in-memory SQLite database for tests
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        # Create the test client
        self.app = app.test_client()
        # Push the application context and create all tables
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        # Cleanup the database and remove the app context
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_home_unfilled(self):
        # Test that the home route ("/") returns a 200 OK status code.
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

        # Optionally, check for expected content in the rendered template.
        self.assertIn(b"App Pages", response.data)
        self.assertIn(b"Characters", response.data)

    def test_home_filled(self):
        # get character page url
        char_url = ""
        with app.app_context():
            char_url = url_for("/character")
        url = bytes(char_url, "utf-8")

        # Test that the home route ("/") returns a 200 OK status code.
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

        # Optionally, check for expected content in the rendered template.
        self.assertIn(b"App Pages", response.data)
        self.assertIn(b"Characters", response.data)
        self.assertIn(url, response.data)

    def test_character_page(self): 
        # Test that the home route ("/") returns a 200 OK status code.
        response = self.app.get("/character")
        self.assertEqual(response.status_code, 200)
        # Optionally, check for expected content in the rendered template.
        self.assertIn(b"Character", response.data)

    def test_add_character(self):
        # Test posting a new todo item using the "/add" route.
        name = "Crimson Chin"
        default_gender = Gender.THEY
        
        response = self.app.post("/character/add", data={"name": name},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verify that the new todo has been added to the database.
        char = Character.query.filter_by(name=name).first()
        self.assertIsNotNone(char)
        self.assertEqual(char.gender, default_gender)
        self.assertEqual(char.name, name)

    def test_change_gender(self):
        # Manually add a todo item to update.
        name = "Trixie Tang"
        init_gender = Gender(randint(0,3))
        changed_gender = Gender((init_gender.value+1)%4)
        
        char = Character(name=name, gender=init_gender) 
        db.session.add(char)
        db.session.commit()
        char_id = char.id

        # Toggle its 'complete' value by accessing the update route.
        response = self.app.get(f"/character/update/{char_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Use Session.get() instead of Query.get()
        updated_char = db.session.get(Character, char_id)
        self.assertEqual(updated_char.gender, changed_gender)
        self.assertEqual(char.name, name)

    def test_delete_todo(self):
        # Manually add a todo item to delete.
        char = Character(name="character for deletion", gender=Gender.OTHER)
        db.session.add(char)
        db.session.commit()
        char_id = char.id

        # Delete the todo using the delete route.
        response = self.app.get(f"/character/delete/{char_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Use Session.get() instead of Query.get()
        deleted_char = db.session.get(Character, char_id)
        self.assertIsNone(deleted_char)

    # def test_failure(self):
    #     # Simulate a failure case
    #     self.assertFalse(True, "This test should fail.")

if __name__ == "__main__":
    unittest.main()