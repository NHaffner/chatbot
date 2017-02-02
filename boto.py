"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request, datetime
import json

curse_words = ["shit","baby girl","cunt","knob","bellend","fuck"]
hello_list = ["hello","hi","how are you","hey","hii","heyy","how are you?"]
time_list = ["what is the time","time"]


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    robot_answer = evaluate_robot(user_message)
    return json.dumps(robot_answer)

def evaluate_robot(msg):

    if msg.find("gilad") != -1:
        result = {"animation": "inlove", "msg": "is that you?"}
        return result

    if msg.find("?") != -1:
        result = {"animation":"ok", "msg":"good question!"}
        return result

    if any(x in msg for x in curse_words):
        result = {"animation": "crying", "msg": "please dont use that word"}
        return result

    if any(x in msg for x in hello_list):
        result = {"animation": "excited", "msg": "Hey! Whatsup?! x"}
        return result

    if any(x in msg for x in time_list):
        result ={"animation": "giggling","msg":str(datetime.datetime.now())}
        return result

    else:
        result = {"animation": "no", "msg": "i dont understand..."}
        return result



@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7001)

if __name__ == '__main__':
    main()
