'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
app = Flask(__name__)


class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    
    School('mb',     '1.Muttukadu Beach'  , 12.806030245781262, 80.24285937299557),
    School('kb',     '2.Kovalam Beach'    ,12.790013135344275, 80.25412378616241),
    School('ub',     '3.Uthandi beach'    ,12.871713645684556, 80.2507926197579),
    School('mbrm',     '4.Mahabalipuram'    ,12.622529944552687, 80.19435802677405),
    School('dc',     '5.Dakshin Chitra'    ,12.871713645684556, 80.2507926197579),
    School('acl',    '6.Anna Centenary Library'   ,13.017271379142114, 80.23992531457709),
    School('vgp',    '7.VGP Kingdom'   ,12.91441967383443, 80.25051327271278),
    School('mgm',    '8.MGM Dizee World'   ,12.826171688531627, 80.24419107307018),
    School('ql',    '9.Queensland'   ,13.030108649944667, 80.02760267159891),
    School('mjl',    '10.Mayajaal'   ,12.848063267643113, 80.23995164419287),
    School('aazp',    '11.Arignar Anna Zoological Park'   ,12.879525301586247, 80.08190087270661),
    School('cb',    '12.Crocodile Bank'   ,12.743068809332774, 80.2401470015645),
    School('tp',    '13.Thiruvalluvar Park'   ,12.97548307025423, 80.1993262437392),
    School('vnp',    '14.Vivekananda Nagar Park'   ,13.127023429293967, 80.14284799934575),


  )
schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('index1.html', schools=schools)


@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)

app.run(host='localhost', debug=True)