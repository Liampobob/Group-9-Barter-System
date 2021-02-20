from django.http import HttpResponse, JsonResponse, HttpRequest
from SPARQLWrapper import SPARQLWrapper as Sparql
from SPARQLWrapper import JSON as SPARQL_JSON
from database_queries import PREFIXES, Select_Queries, Insert_Queries

endpoint = "http://localhost:7205/repositories/barter"

def send_insert_query(request):
	return

def send_select_query(request):
	# takes in a GET request. required parameters: 'query_type', 'endpoint'. currently only handles 'open_jobs'
	if request.method != 'GET' : return JsonResponse( { 'status_code' : 405, 'result' : "SELECT queries must use GET requests" } )
	query_type = request.content_params['query_type']
	query_template = Select_Queries(query_type)
	query_string = PREFIXES +  query_template.format( str(request.content_params['worker_id']) )
	query_object = Sparql(request.content_params['endpoint'])
	query_object.setQuery(query_string)
	query_object.setReturnFormat(SPARQL_JSON)
	try:
		result_in = query_object.query().convert()
		result_bindings = result_in["results"]["bindings"]
		return JsonResponse( { 'status_code' : 200, 'result' : result_bindings } )
	except Exception as e:
		return JsonResponse( { 'status_code' : 500, 'result' : e } )
