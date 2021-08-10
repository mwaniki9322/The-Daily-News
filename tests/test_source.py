import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
 '''
 Test Class to test the behaviour of the Movie class
 '''

def setUp(self):
 '''
 Set up method that will run before every Test
 '''
 self.new_source = Source(1234,'wired',"Apple Walks a Privacy Tightrope to Spot Child Abuse in iCloud","With a new capability to search for illegal material not just in the cloud but on user devices, the company may have opened up a new front in the encryption wars.","https://www.wired.com/story/apple-csam-detection-icloud-photos-encryption-privacy/",'general','en','us')

def test_instance(self):
 self.assertTrue(isinstance(self.new_source,Source))

 
