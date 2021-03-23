from django.http import HttpResponse, JsonResponse, HttpRequest
import db_methods

endpoint = "http://localhost:7205/repositories/barter"

def test_send_select_query():
	params = {
		'endpoint' : endpoint,
		'query_type' : 'open_jobs',
		'worker_id' : 199
	}
	req = HttpRequest()
	req.method = 'GET'
	req.content_params = params
	db_methods.send_select_query(req)

test_send_select_query()
