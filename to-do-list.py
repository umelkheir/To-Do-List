import flask
import datetime
app = flask.Flask("to_do_list")


class ToDo():
# Created properities and methods for the to do list.
    def __init__(self, name, description, due_date,):
        self.name = name
        self.description = description
        # used the datetime module to get me the date and I had to replace the "T" so it can match with the html input datetime-local
        self.due_date = datetime.datetime.strptime(due_date.replace("T", " "),"%Y-%m-%d %H:%M")

    def list_due_date(self):
        # time delta calculates the time we declared minus the current time now 
        time_delta = self.due_date - datetime.datetime.now()  
        if time_delta.days > 0:
            # this code tells the user how many days are remaining when it does the calculation on the previous code
            return f"{time_delta.days}  days remaining"
        elif time_delta.days == 0:
            return "Due today"
        else:
            return "Overdue"
        


## Used routes and functions to define the routes and get the different html files in the folder.
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_notes():
    notes_file = open("note.txt")
    content = notes_file.read()
    notes_file.close()
    lists = content.split("\n") 
    return lists

@app.route("/")
def login_page():
    return get_html("login") 



@app.route("/index")
def home_page():
    return get_html("index")

@app.route("/notes")
def note_page():
    html_page = get_html("notes")
    lists = get_notes()
    the_lists = []
    
    for  index, value in enumerate (lists):
        #using append to add list to the end the list
        if list(value):
        
            the_lists.append(f"<li class={'no-li' if 'Overdue' in value else ''} id ='list-" + str(index) + "'>" + str(value) + "</li>") 
    return html_page.replace("$$LISTNAMES$$", "".join(the_lists))

@app.route("/add")
def write_note():
    name = flask.request.args.get("a")
    description = flask.request.args.get("d")
    due = flask.request.args.get("due")
    todo = ToDo(name=name, description=description, due_date=due)
    with open("note.txt", "a") as file_text:
        file_text.write(f"{todo.name}   {todo.description}   {todo.due_date} {todo.list_due_date()}\n" )
    html_page = get_html("index")
    names = get_notes()
    the_values = ""
    for name in names:
            the_values += "<p>" + name + "</p>"
    return html_page.replace("$$LISTNAMES$$", the_values)

@app.route("/search")
def search():
    html_page = get_html("notes")
    query = flask.request.args.get("q")
    notes = get_notes()
    result = ""
    for note in notes:
        if note.lower().find(query.lower()) != -1:
            result += "<p>" + note + "</p>"
    if result == "":
        result += "<p> No such notes </p>"
    return html_page.replace("$$LISTNAMES$$", result)
