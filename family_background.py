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
        <title>Family background</title>
        <link rel="stylesheet" type="text/css" href="familybackground.css">
    </head>
    <body>
      <div class="hi">
      <form>
        <input type="submit" class="button" name="goback" value="Go back!" onclick="history.go(-1)">
        </form>
        <fieldset style="border-color: purple">
        <legend><i><b>FAMILY BACKGROUND :</b></i></legend>
        <form method="post" action="family_background.py">
            <!--colon cancer-->
            Rectal bleeding or blood in your stool:
            <select name="r_bleeding">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Persistent abdominal discomfort, such as cramps, gas or pain:
            <select name="gas">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            A feeling that your bowel doesn't empty completely:
            <select name="b_empty">
              <option value="no" >No</option>
              <option value="yes">Yes</option>
            </select><br>
            Diarrhea or constipation or a change in the consistency of your stool, that lasts longer than four weeks:
            <select name="diarrhea">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Unexplained weight loss:
            <select name="cw_loss">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            <!--Prostate cancer-->
            Frequent urination:
            <select name="f_urination">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Weak or interrupted urine flow or the need to strain to empty the bladder:
            <select name="w_flow">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Blood in the urine:
            <select name="b_urine">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Blood in the seminal fluid:
            <select name="bs_fluid">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            New onset of erectile dysfunction:
            <select name="e_dys">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            <!--Ovarian cancer-->
            Abdominal bloating or swelling:
            <select name="a_bloat">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Quickly feeling full when eating:
            <select name="q_full">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Discomfort in the pelvis area:
            <select name="d_pelvis">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Changes in menstruation:
            <select name="c_menstruation">
              <option value="no">No</option>
              <option value="yes">Yes</option>
            </select><br>
            Tiredness or low energy:
            <select name="l_energy">
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


def familyback():
    def colon():
        cn = 0
        r_empty = form.getvalue("r_bleeding")
        if r_empty == 'yes':
            cn = cn + 1
        gas = form.getvalue("gas")
        if gas == 'yes':
            cn = cn + 1
        b_empty = form.getvalue("b_empty")
        if b_empty == 'yes':
            cn = cn + 1
        diarrhea = form.getvalue("diarrhea")
        if diarrhea == 'yes':
            cn = cn + 1
        cw_loss = form.getvalue("cw_loss")
        if cw_loss == 'yes':
            cn = cn + 1
        return cn

    def prostate():
        pros = 0
        f_urination = form.getvalue("f_urination")
        if f_urination == 'yes':
            pros = pros + 1
        w_flow = form.getvalue("w_flow")
        if w_flow == 'yes':
            pros = pros + 1
        b_urine = form.getvalue("b_urine")
        if b_urine == 'yes':
            pros = pros + 1
        bs_fluid = form.getvalue("bs_fluid")
        if bs_fluid == 'yes':
            pros = pros + 1
        e_dys = form.getvalue("e_dys")
        if e_dys == 'yes':
            pros = pros + 1
        return pros

    def ovarian():
        ova = 0
        a_bloat = form.getvalue("a_bloat")
        if a_bloat == 'yes':
            ova = ova + 1
        q_full = form.getvalue("q_full")
        if q_full == 'yes':
            ova = ova + 1
        d_pelvis = form.getvalue("d_pelvis")
        if d_pelvis == 'yes':
            ova = ova + 1
        c_menstruation = form.getvalue("c_menstruation")
        if c_menstruation == 'yes':
            ova = ova + 1
        l_energy = form.getvalue("l_energy")
        if l_energy == 'yes':
            ova = ova + 1
        return ova

    cn = colon()
    pros = prostate()
    ova = ovarian()

    if (cn > pros) and (cn > ova):
        print("These are the Symptoms of Colon Cancer")
    elif (pros > cn) and (pros > ova):
        print("These are the Symptoms of Prostate Cancer")
    elif (ova > cn) and (abd > pros):
        print("These are the Symptoms of Ovarian Cancer")
    elif (cn != 0 or pros != 0 or ova != 0) and ((cn == pros) or (ova == cn) or (pros == ova)):
        print("Mixed Possibilities,Please Consult a Doctor")


familyback()

print("""
 </div>
 </body>
</html>
""")
