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
        <link rel="stylesheet" type="text/css" href="pollution.css">
    </head>
    <body>
      <div class="hi">
      <form>
        <input type="submit" class="button" name="goback" value="Go back!" onclick="history.go(-1)">
        </form>
        <fieldset style="border-color: purple">
        <legend><i><b>POLLUTION :</b></i></legend>
        <form action="pollution.py" method="post">
            <!-- Lung cancer due to air pollution -->
            A cough that does not go away or gets worse
            <select name="a_cough">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Coughing up blood or rust-colored sputum:
            <select name="a_blood">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Chest pain that is often worse with deep breathing, coughing, or laughing:
            <select name="a_pain">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Feeling tired or weak:
            <select name="a_tired">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Weight loss and loss of appetite:
            <select name="aw_loss">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            <!-- Leukemia cancer due to soil pollution -->
            Bone pain and tenderness:
            <select name="b_pain">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Bleeding easily and bruising easily:
            <select name="bleeding">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Red spots on the skin:
            <select name="r_spot">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Painless, swollen lymph nodes:
            <select name="s_lymph">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Frequent infections:
            <select name="f_infection">
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


def pollution():
    def aplung():
        ap = 0
        a_cough = form.getvalue("a_cough")
        if a_cough == 'yes':
            ap = ap + 1
        a_blood = form.getvalue("a_blood")
        if a_blood == 'yes':
            ap = ap + 1
        a_pain = form.getvalue("a_pain")
        if a_pain == 'yes':
            ap = ap + 1
        a_tired = form.getvalue("a_tired")
        if a_tired == 'yes':
            ap = ap + 1
        aw_loss = form.getvalue("aw_loss")
        if aw_loss == 'yes':
            ap = ap + 1
        return ap

    def leukemia():
        lk = 0
        b_pain = form.getvalue("b_pain")
        if b_pain == 'yes':
            lk = lk + 1
        bleeding = form.getvalue("bleeding")
        if bleeding == 'yes':
            lk = lk + 1
        r_spot = form.getvalue("r_spot")
        if r_spot == 'yes':
            lk = lk + 1
        s_lymph = form.getvalue("s_lymph")
        if s_lymph == 'yes':
            lk = lk + 1
        f_infection = form.getvalue("f_infection")
        if f_infection == 'yes':
            lk = lk + 1
        return lk

    ap = aplung()
    lk = leukemia()
    if ap > lk:
        print("These are the Symptoms of Lung Cancer")
    elif lk > ap:
        print("These are the Symptoms of Leukemia Cancer")
    elif (ap != 0 or lk != 0) and ap == lk:
        print("Mixed Possibilities,Please Consult a Doctor")


pollution()
print(""" 
  </div>
 </body>
</html>
""")
