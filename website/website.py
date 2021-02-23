from flask import Flask, send_from_directory
import os

TEMPLATE_DIR = os.path.abspath('/Desktop/433Website/')

app = Flask(__name__, static_folder='')

@app.route('/')
def home():
	root_dir = os.path.dirname(os.getcwd()) + '/433Website'
	return send_from_directory(root_dir, 'testWebsite.html')

@app.route('/voteCount')
def voteCount():
	root_dir = os.path.dirname(os.getcwd()) + '/433Website'
	return send_from_directory(root_dir, 'voteCount.html')

@app.route('/signIn')
def signIn():
	root_dir = os.path.dirname(os.getcwd()) + '/433Website'
	return send_from_directory(root_dir, 'signIn.html')

@app.route('/end')
def end():
	root_dir = os.path.dirname(os.getcwd()) + '/433Website'
	return send_from_directory(root_dir, 'end.html')

@app.route('/castVote')
def castVote():
	root_dir = os.path.dirname(os.getcwd()) + '/433Website'
	return send_from_directory(root_dir, 'castVote.html')

if __name__ == "__main__":
	app.run(port=5006,debug=True)