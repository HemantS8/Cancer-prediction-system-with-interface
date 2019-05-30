#!C:\Users\Hemant Sharma\AppData\Local\Programs\Python\Python36-32\python.exe
print("Content-Type: text/html")
print()
import cgi

form = cgi.FieldStorage()


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
        print(o)
    elif (lg > o) and (lg > abd):
        print(lg)
    elif (abd > lg) and (abd > o):
        print(abd)
    elif (abd == lg) or (o == lg) or (abd == o):
        print("equal")


product()


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
        print(td)
    elif sk > td:
        print(sk)


radiation()


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
        print(ap)
    elif lk > ap:
        print(lk)


pollution()


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
        print(cn)
    elif (pros > cn) and (pros > ova):
        print(pros)
    elif (ova > cn) and (abd > pros):
        print(ova)


familyback()
