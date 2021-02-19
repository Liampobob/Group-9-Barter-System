PREFIXES = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX barc: <https://www.barter.ie/database/classes#>
PREFIX barp: <https://www.barter.ie/database/predicates#>
PREFIX bard: <https://www.barter.ie/database/data#>"""

Select_Queries = {
	'open_jobs' : """SELECT ?jobID ?jobTitle ?jobDate WHERE {{ ?job barp:id ?jobID ; barp:title ?jobTitle ; barp:datePosted ?jobDate ; barp:postedBy ?client ; barp:status 'open' ; barp:skillTag ?skill . ?worker barp:id ?id ; barp:inCamp ?camp ; barp:skillTag ?skill . FILTER(?id = {}) ?client barp:inCamp ?camp . }}"""
}

Insert_Queries = {
	'new_user' : {
		'base_query' : "INSERT DATA {{ bard:user{1} a barc:{0} ; barp:id {1} ; barp:name '{2}' ; barp:username '{3}' ; barp:password '{4}' ; barp:inCamp bard:{5} {6}. }}",
		'primaryLanguage' : " barp:primaryLanguage '{}' ",
		'spokenLanguage' : " barp:spokenLanguage '{}' ",
		'skillTag' : " barp:skillTag '{}' ",
		'attachedPicture' : " barp:attachedPicture {}"
	},
	'new_location' : "INSERT DATA {{ bard:user{0} barp:location bard:loc{0} . bard:loc{0} a barc:Location ; barp:longitude {1} ; barp:latitude {2} . }}",
	'new_work_history' : {
		'base_query' : "INSERT DATA {{ bard:user{0} barp:hasHistory bard:hist{0}_{1} . bard:hist{0}_{1} a barc:WorkHistory ; barp:skillTag {2} {3} . }}",
		'title' : " barp:title '{}' ",
		'description' : " barp:description '{}' ",
		'startDate' : " barp:startDate '{}' ",
		'endDate' : " barp:startDate '{}' " }
}
