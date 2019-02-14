from flask import Flask, jsonify
from quora import Quora

app = Flask (__name__)

@app.route ('/', methods=['GET'])
def index_route () :
    return jsonify({
		'author' : 'Tapasweni Pathak',
		'author_url' : 'http://tapaswenipathak.github.io/',
		'base_url' : 'api-quora.herokuapp.com',
	    	'project_name' : 'Quora API',
		'project_url' : 'http://github.com/tapaswenipathak/quora-api'
	})


@app.route ('/quora/userstats/<username>', methods=['GET'])
def userstats_route (sunsign) :
	result = dict (Quora.getUserStats (username))
	return jsonify (answers=result['answers'],
			questions=result['questions'],
			shares=result['shares'],
                        spaces=result['spaces'],
                        posts=result['posts'],
                        blogs=result['blogs'],
                        followers=result['followers'],
                        following=result['following'])

@app.route ('/quora/questionstats/<question>', methods=['GET'])
def questionstats_route (sunsign) :
	result = dict (Quora.getQuestionStats (question))
	return jsonify (followers=result['followers'],
			asked=result['asked'],
			merged_questions=result['merged_questions'],
                        views=result['views'])

@app.route ('/quora/answer/<question>/<username>', methods=['GET'])
def answer_route (sunsign) :
	result = dict (Quora.getAnswer (question, username))
	return jsonify (answer_text=result['answer'])

@app.route ('/quora/answerstats/<question>/<username>', methods=['GET'])
def answerstats_route (question, username) :
	result = dict (Quora.getAnswerStats (question, username))
	return jsonify (views=result['views'],
			upvotes=result['upvotes'])

@app.route ('/quora/blogstats/<blogname>', methods=['GET'])
def blogstats_route (blogname) :
	result = dict (Quora.getBlogStats (blogname))
	return jsonify (description=result['description'],
			view=result['view'],
                        followers=result['followers'])

@app.route ('/quora/userprofile/<username>', methods=['GET'])
def userprofile_route (blogname) :
	result = dict (Quora.getUserProfile (username))
	return jsonify (credential=result['credential'],
			top_writer=result['top_writer'],
                        knows_about=result['knows_about'])

if __name__ == "__main__":
	app.run()
