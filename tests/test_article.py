import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
 '''
 Test Class to test the behaviour of the Article class
 '''

def setUp(self):
 '''
 Set up method that will run before every Test
 '''
 self.new_article = Article(1234,'wired',"Apple Walks a Privacy Tightrope to Spot Child Abuse in iCloud","With a new capability to search for illegal material not just in the cloud but on user devices, the company may have opened up a new front in the encryption wars.","https://www.wired.com/story/apple-csam-detection-icloud-photos-encryption-privacy/",'general',': "https://i1.wp.com/electrek.co/wp-content/uploads/sites/3/2021/08/mow-joe-electric-mower.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1',"https://i1.wp.com/electrek.co/wp-content/uploads/sites/3/2021/08/mow-joe-electric-mower.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1")

def test_instance(self):
 self.assertTrue(isinstance(self.new_article,Article))

