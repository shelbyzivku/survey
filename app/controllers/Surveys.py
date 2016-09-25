from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        self.load_model('Survey')
   
    def index(self):
        print self.models['Survey'].get_surveys()
        if not 'counter' in session:
            session['counter'] = 0
        return self.load_view('index.html')

    def process(self):
        # print 'error got to process'

        session['counter'] += 1

        data = {
            'name': request.form['name'],
            'language': request.form['lang'],
            'comment': request.form['comment']

        }

        # print data

        self.models['Survey'].add_survey(data)
        # session['name'] = request.form['name']
        # session['comment'] = request.form['comment']
        # session['lang'] = request.form['lang']
        return redirect('/result')

    def result(self):
        data = self.models['Survey'].get_surveys()
        return self.load_view('result.html', surveys=data, counter=session['counter'])