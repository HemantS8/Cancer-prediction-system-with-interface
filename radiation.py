#!C:\Users\Hemant\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html")
print()
import cgi

form = cgi.FieldStorage()
print("""


  <!DOCTYPE html>
  <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Radiation</title>
        <link rel="stylesheet" type="text/css" href="radiation.css">
    </head>
    <body>
      <div class="hi">
      <form>
        <input type="submit" class="button" name="goback" value="Go back!" onclick="history.go(-1)">
        </form>
        <fieldset style="border-color: purple">
        <legend><i><b>RADIATION :</b></i></legend>
            <!-- Brain cancer-->
            <form method="post" action="radiation.py">
            Severe headaches:
            <select name="headache">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Sleep problems:
            <select name="sleep">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Memory problems:
            <select name="memory">
              <option value="no" >No</option>
              <option value="yes">Yes</option>
            </select><br>
            Seizures(Muscle jerking or twitching):
            <select name="seizures">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Problems balancing or walking:
            <select name="balance">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            <!--Skin cancer-->
            New moles:
            <select name="newmole">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Moles that increases in size:
            <select name="molesize">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            A spot that changes colour from brown to black or is varied:
            <select name="molecolor">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            A spot that becomes raised or develops a lump within it:
            <select name="molelump">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Moles that itch or tingle:
            <select name="moleitch">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
             <br>
             <input type="submit" class="button1" name="submit" value="submit">
            </form>
      </fieldset>
      </div>
    <div = "hi">

""")

def radiation():
    def brain():
        td = 0
        headache = form.getvalue("headache")
        if headache == 'yes':
            td = td + 1
        sleep = form.getvalue("sleep")
        if sleep == 'yes':
            td = td + 1
        memory = form.getvalue("memory")
        if memory == 'yes':
            td = td + 1
        seizures = form.getvalue("seizures")
        if seizures == 'yes':
            td = td + 1
        balance = form.getvalue("balance")
        if balance == 'yes':
            td = td + 1

        return td

    def skin():
        sk = 0
        newmole = form.getvalue("newmole")
        if newmole == 'yes':
            sk = sk + 1
        molesize = form.getvalue("molesize")
        if molesize == 'yes':
            sk = sk + 1
        molecolor = form.getvalue("molecolor")
        if molecolor == 'yes':
            sk = sk + 1
        molelump = form.getvalue("molelump")
        if molelump == 'yes':
            sk = sk + 1
        moleitch = form.getvalue("moleitch")
        if moleitch == 'yes':
            sk = sk + 1
        return sk

    td = brain()
    sk = skin()
    if td > sk:
        print("These are the Symptoms of Brain Cancer")
    elif sk > td:
        print("These are the Symptoms of Skin Cancer")
    elif (td != 0 or sk != 0) and td == sk:
        print("Mixed Possibilities,Please Consult a Doctor")


radiation()

print("""
</div>
</body>
</html>

""")
