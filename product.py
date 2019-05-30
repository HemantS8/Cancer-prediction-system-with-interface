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
        <title>Pollution</title>
        <link rel="stylesheet" type="text/css" href="product.css">
    </head>
    <body>
      <div class="hi">
      <form>
        <input type="submit" class="button" name="goback" value="Go back!" onclick="history.go(-1)">
        </form>
        <fieldset style="border-color: purple">
        <legend><i><b>PRODUCT :</b></i></legend>
         <!-- Oral cancer due to tobacco-->
        <form action="product.py" method="post">
            Are you having mouth pain:          
            <select name="m_pain">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            A lip or mouth sore that doesn't heal:
            <select name="sore">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Difficult or painful swallowing:
            <select name="swallow">
              <option value="no" name="swallow">No</option>
              <option value="yes" name="swallow">Yes</option>
            </select><br>
            A growth or lump inside your mouth:
            <select>
              <option value="no" name="lump">No</option>
              <option value="yes" name="lump">Yes</option>
            </select><br>
            A white or reddish patch on the inside of your mouth:
            <select>
              <option value="no" name="patch">No</option>
              <option value="yes" name="patch">Yes</option>
            </select><br>
            <!-- Lung cancer due to smoking-->
            A cough that does not go away or gets worse
            <select name="cough">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Coughing up blood or rust-colored sputum:
            <select name="blood_sputum">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Chest pain that is often worse with deep breathing, coughing, or laughing:
            <select name="c_pain">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Feeling tired or weak:
            <select name="weak">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Weight loss and loss of appetite:
            <select name="w_loss">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            <!-- Liver cancer due to alcohol-->
            Abdominal swelling:
            <select  name="a_swelling">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Nausea and vomiting:
            <select name="vomit">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            White, chalky stools:
            <select name="stool">
              <option value="no">No</option>
              <option value="yes">Yes</option>            
            </select><br>
            <br>
             <input type="submit" class="button1" name="submit" value="submit">
            </form>
      </fieldset>
    </div>
<div class="hi">
 """)
def product():
    def oral():
        o = 0
        mp = form.getvalue("m_pain")
        if mp == 'yes':
            o = o + 1
        sr = form.getvalue("sore")
        if sr == 'yes':
            o = o + 1
        sw = form.getvalue("swallow")
        if sw == 'yes':
            o = o + 1
        lump = form.getvalue("lump")
        if lump == 'yes':
            o = o + 1
        pch = form.getvalue("patch")
        if pch == 'yes':
            o = o + 1
        return o

    def lung():
        lg = 0
        ch = form.getvalue("cough")
        if ch == 'yes':
            lg = lg + 1
        bs = form.getvalue("blood_sputum")
        if bs == 'yes':
            lg = lg + 1
        c_pain = form.getvalue("c_pain")
        if c_pain == 'yes':
            lg = lg + 1
        weak = form.getvalue("weak")
        if weak == 'yes':
            lg = lg + 1
        w_loss = form.getvalue("w_loss")
        if w_loss == 'yes':
            lg = lg + 1
        return lg

    def abdominal():
        abd = 0
        asw = form.getvalue("a_swell")
        if asw == 'yes':
            abd = abd + 1
        vomit = form.getvalue("vomit")
        if vomit == 'yes':
            abd = abd + 1
        tatti = form.getvalue("stool")
        if tatti == 'yes':
            abd = abd + 1
        return abd

    o = oral()
    lg = lung()
    abd = abdominal()

    if (o > lg) and (o > abd):
        print("These are the Symptoms of Oral Cancer")
    elif (lg > o) and (lg > abd):
        print("These are the Symptoms of Lung Cancer")
    elif (abd > lg) and (abd > o):
        print("These are the Symptoms of Liver Cancer")
    elif (o != 0 or lg != 0 or abd != 0) and ((o == abd) or (o == lg) or (abd == lg)):
        print("Mixed Possibilities,Please Consult a Doctor")

product()

print("""
  </body>
</html>

""")
