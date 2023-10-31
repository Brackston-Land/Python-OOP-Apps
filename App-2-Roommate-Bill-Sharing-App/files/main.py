import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    """
    Creates a roommate person who lives in the apartment and pays a share to the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_roommate):
        weight = self.days_in_house / (self.days_in_house + other_roommate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Create a pdf file that contains data about the roommates such as
    their names, their due amount and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):

        roommate1_pay = str(round(roommate1.pays(bill=bill, other_roommate=roommate2), 2))
        roommate2_pay = str(round(roommate2.pays(bill=bill, other_roommate=roommate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name='house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Bill', border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        # Insert name and due amount of the first roommate
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate1_pay, border=0, ln=1)

        # Insert name and due amount of the second roommate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)

amount = float(input('Hey user, enter the bill amount '))
period = input('What is the bill period? E.g. December 2020 ')

name1 = input('What is your name? ' )
days_in_house1 = int(input(f'What many days did {name1} stay in the house during the bill period? ' ))

name2 = input('What is the name of the other roommate? ' )
days_in_house2 = int(input(f'What many days did {name2} stay in the house during the bill period? ' ))

the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1)
roommate2 = Roommate(name2, days_in_house2)

print()

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf",)
pdf_report.generate(roommate1, roommate2, bill=the_bill)