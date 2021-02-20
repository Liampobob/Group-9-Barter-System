# borrowed code from https://github.com/rob-metalinkage/django-rdf-io/blob/master/rdf_io/models.py
from django.db import models
from django.utils.encoding import iri_to_uri, uri_to_iri


from rdflib import Graph, namespace, XSD
from rdflib.term import URIRef, Literal


# Create your models here.

class Prefix():
	def __init__(self, pref, url):
		self.pref = pref + ":"
		self.url = url
		if url[-1] != "/" and url[-1] != "#":
			self.url = url + "#"
		self.query_prefix = None
		return

	def get_query_prefix(self):
		if self.query_prefix is None:
			self.query_prefix = "PREFIX " + self.pref + " <" + self.url + "> "
		return self.query_prefix

class RDFClass():
	def __init__(self, prefixes, id):
		self.prefixes = prefixes
		self.id = id
		self.uri = prefixes["class"].pref + self.__class__.__name__ + str(id)
		return



class User(RDFClass):
	def __init__(self, id, name, username, password, camp, prefixes):
		RDFClass.__init__(self, prefixes, id)
		self.id = id
		self.name = name
		self.username = username
		self.password = password
		self.in_camp = camp
		self.attached_picture = None
		self.location = None
		self.primary_language = None
		self.spoken_language = []
		send_insert_query()
		return

	def set_location(self, lat, long):
		loc = Location(self, lat, long)
		if self.location is None: send_insert_query()
		else: send_update_query()
		self.location = loc
		return

	def set_primary_language(self, language):
		if self.primary_language is None:
			send_insert_query()
		else:
			send_update_query()
			self.remove_spoken_language(self.primary_language)
		self.primary_language = language
		self.add_spoken_language(language)
		return

	def add_spoken_language(self, language):
		if language not in self.spoken_language:
			self.spoken_language.append(language)
			send_insert_query()

	def remove_spoken_language(self, language):
		if language in self.spoken_language:
			self.spoken_language.remove(language)
			send_delete_query()


class Location(RDFClass):
	def __init__(self, parent, lat, long):
		RDFClass.__init__(self, parent.prefixes, self.id)
		self.parent_uri = parent.uri
		self.prefixes = parent.prefixes
		self.id = parent.id
		self.uri = prefixes["class"].pref + str(self.id)
		self.latitude = lat
		self.longitude = long
		send_insert_query()
