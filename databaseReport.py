import sqlite3

def asCash(i):
    o = '${:,.2f}'.format(i)
    return o

def main ():
    dbCon = sqlite3.connect('medical.db')
    dbCur = dbCon.cursor()

# 4b run simple full table selects
    
    for table in ('surgery', 'doctor', 'patient'):
        dbCur.execute(f"select * from {table}")
        rows = dbCur.fetchall()

        for row in rows:
           print(row)
        print()

# 4c simple union of two tables with formated output
    
    dbCur.execute("""Select patientFN, patientLN, doctorFN, doctorLN
    from patient, doctor
    where patient.doctorID = doctor.doctorID
    order by patientLN,patientFN,doctorLN,doctorFN""")
    rows = dbCur.fetchall()

    for row in rows:
        p = row[0] + " " + row[1]
        d = row[2] + " " + row[3]
        print(f"Patient Name: {p.ljust(20)}  Doctor Name: {d}")
    print()

# 4d three table union, formated output
    
    dbCur.execute("""Select patientFN, patientLN, doctorFN, doctorLN, surgeryDesc
    from patient, surgery, doctor
    where surgery.doctorID = doctor.doctorID
    and surgery.patientID = patient.patientID
    order by surgeryDesc""")
    rows = dbCur.fetchall()

    for row in rows:
        p = row[0] + " " + row[1]
        d = row[2] + " " + row[3]
        s = row[4]
        print(f"Patient Name: {p.ljust(20)} Surgery: {s.ljust(10)} Doctor Name: {d}")
    print()

# two table union with a calculated value

    dbCur.execute("""Select surgeryDesc, sum(surgerycost) Cost
    from surgery
    group by surgeryDesc""")
    rows = dbCur.fetchall()

    t = 0.0
    for row in rows:
        s = row[0]
        c = float(row[1])
        t += c

        print (f"Surgery: {s.ljust(9)} Cost: {asCash(c).rjust(18)}")

    print(f"\n                  Total: {asCash(t).rjust(18)}")

main()
