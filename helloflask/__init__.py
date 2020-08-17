from flask import Flask, g, Response, make_response

app = Flask(__name__)
# app.debug = True
# app.config['SERVER_NAME'] = 'localhost:5000'

@app.before_request
def before_request():
    g.str = "한글"
    print("before_request")

@app.before_first_request
def before_first_request():
    print ("before_first_request")

@app.after_request
def after_request(aa):
    print("after_request")
    return(aa)

@app.teardown_request
def teardown_request(exception):
    return("teardown_request")

# @app.teardown_appcontext
# def teardown_appcontext(exception):
#     print("teardown_appcontext")

@app.route("/")
def helloworld():
    # return "Hello Flask World!" + getattr(g, 'str', '111')
    custom_res = Response("helloflask Response", 200, {'test':'ttt'})
    return make_response(custom_res)

@app.route("/shindalsoo", host="local1.com")
def shindalsoo1():
    return("local1.com이다")
@app.route("/shindalsoo", host="local2.com")
def shindalsoo2():
    return("local2.com이다")

@app.route('/shindalsoo', redirect_to='/xxx')
def shindalsoo3():
    return("local2.com이다")

@app.route('/xxx')
def xxx():
    return("xxx")

# @app.route('/test/<tid>')
# def test3(tid):
#     print("tid is",tid)
#     def application(environ1, start_response1):
#         body = 'tid is %s' % tid
#         headers = [ ('Content-Type', 'text/plain'),
#                     ('Content-Length', str(len(body)))]
#         start_response1('200 OK', headers)
#         return [body]
#     return make_response(application)

@app.route('/test/<tid>')
def test_tid(tid):
    return("/test %s" % tid)

@app.route('/test/<tid>/<bid>')
def test_tid_bid(tid,bid):
    return("/test tid is %s, bid is %s" % (tid, bid))

# @app.route('/test/<tid>/<bid>')
# def test5(tid,bid):
#     print("tid is",tid)
#     def application(environ1, start_response1):
#         body = 'bid is %s' % bid
#         headers = [ ('Content-Type', 'text/plain'),
#                     ('Content-Length', str(len(body)))]
#         start_response1('200 OK', headers)
#         return [body]
#     return make_response(application)

@app.route("/test_wsgi")
def wsgi_test():
    def application(environ1, start_response1):
        body = 'The request method waw %s' % environ1['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'),
                    ('Content-Length', str(len(body)))]
        start_response1('200 OK', headers)
        return [body]
    return make_response(application)


