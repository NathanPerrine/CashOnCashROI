class Rental_Prop:
    def __init__(self, name):
        self.name = name
        self.box1 = None
        self.box2 = None
        self.box3 = None
        self.box4 = None


    def __str__(self):
        return self.name
    def __repr__(self):
        return f"<Rental_Prop | {self.name}"

# Income
class Box1:
    def __init__(self, rental, laundry, storage, misc = 0):
        self.rental     = rental
        self.laundry    = laundry
        self.storage    = storage
        self.misc       = misc
        self.total      = 0
    
    def get_total(self):
        self.total = self.rental + self.laundry + self.storage + self.misc
    
    def __str__(self):
        return f"Box 1 total = {self.total}"
    def __repr__(self):
        return f"<Box1 | {self.rental} {self.laundry} {self.storage} {self.misc} {self.total}>"

# Expenses
class Box2:
    def __init__(self, tax, insurance, hoa, lawn, snow, vacancy, repairs, capex, propmanagement, mortgage):
        self.tax            = tax
        self.insurance      = insurance
        self.hoa            = hoa
        self.lawn           = lawn
        self.snow           = snow
        self.vacancy        = vacancy
        self.repairs        = repairs
        self.capex          = capex
        self.propmanagement = propmanagement
        self.mortgage       = mortgage
        self.util           = None
        self.total          = 0

    def get_total(self):
        self.total = self.tax + self.insurance + self.hoa + self.lawn + self.snow + self.vacancy + self.repairs + self.capex + self.propmanagement + self.mortgage
        self.total += self.util.total

class Utils:
    # Utilities
    def __init__(self, electric = 0, water = 0, sewer = 0, garbage = 0, gas = 0):
        self.electric   = electric
        self.water      = water
        self.sewer      = sewer
        self.garbage    = garbage
        self.gas        = gas
        self.total      = 0

    def get_total(self):
        self.total = self.electric + self.water + self.sewer + self.garbage + self.gas

#Cash Flow
class Box3:
    def __init__(self, income, expenses):
        self.income     = income
        self.expenses   = expenses
        self.total = 0

    def get_total(self):
        self.total = self.income - self.expenses

#Cash on Cash ROI
class Box4:
    def __init__(self, downpayment, closingcosts, rehabbudget, misc):
        self.downpayment    = downpayment
        self.closingcosts   = closingcosts
        self.rehabbudget    = rehabbudget
        self.misc           = misc
        self.totalinvest    = 0
        self.annualcash     = 0
        self.returnoninvest = 0

    def get_total_investment(self):
        self.totalinvest = self.downpayment + self.closingcosts + self.rehabbudget + self.misc
    
    def annual_cash_flow(self, monthly):
        self.annualcash = monthly * 12

    def roi(self):
        self.returnoninvest = (self.annualcash / self.totalinvest) * 100

#Income
def income(prop):
    print(f"Let's get the income sorted out for {prop}")
    print("Please only enter numbers when asked for money.")
    rent = int(input("How much do you charge for rent for the property? $"))
    
    #Laundry
    cont = input("Do you charge for laundry? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you charge for laundry? (y/n) ").lower()
    if cont == 'y':
        laundry = int(input("How much do you charge for laundry? $"))
    else: laundry = 0
    
    #Storage
    cont = input("Do you charge for storage? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you charge for storage? (y/n) ").lower()
    if cont == 'y':
        storage = int(input("How much do you charge for storage? $"))
    else: storage = 0
        
    #Misc
    cont = input("Do you have any miscellaneous fees? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you have any miscellaneous fees? (y/n) ").lower()
    if cont == 'y':
        misc = int(input("What is the total for your miscellaneous fees? $"))
    else: misc = 0

    #Create Box1
    prop.box1 = Box1(rent, laundry, storage, misc)
    prop.box1.get_total()

#Expenses
def expenses(prop):
    print("Ok! Now for the fun part, expenses. Everything is per month")
    print("Again, numbers only when asked for money.")

    tax = int(input("How much do you pay in tax? $"))
    ins = int(input("How much do you pay in insurance? $"))

    #Utilities
    cont = input("Do you pay utilities? (y/n)").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you pay utilities? (y/n)").lower()
    if cont == 'y':
        #Get utility payments
        elec    = int(input("How much do you pay for electric? $"))
        water   = int(input("How much do you pay for water? $"))
        sewer   = int(input("How much do you pay for sewer? $"))
        garbage = int(input("How much do you pay for garbage? $"))
        gas     = int(input("How much do you pay for gas? $"))
        new_util = Utils(elec, water, sewer, garbage, gas)
    else:
        new_util = Utils()

    #HOA
    cont = input("Do you have any Home Owners Assiciation fees? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you have any Home Owners Assiciation fees? (y/n) ").lower()
    if cont == 'y':
        hoa = int(input("What is the total for your Home Owners Assiciation fees? $"))
    else: hoa = 0

    #Lawn
    cont = input("Do you have any Lawn care fees? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you have any Lawn care fees? (y/n) ").lower()
    if cont == 'y':
        lawn = int(input("What is the total for your Lawn care fees? $"))
    else: lawn = 0

    #Snow
    cont = input("Do you have any Snow Removal fees? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you have any Snow Removal fees? (y/n) ").lower()
    if cont == 'y':
        snow = int(input("What is the total for your Snow Removal fees? $"))
    else: snow = 0

    #Vacancy
    cont = input("Do you want to add any vacancy expenses? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Do you want to add any vacancy expenses? (y/n) ").lower()
    if cont == 'y':
        print(f"A safe vacancy expense would about 5% of your rental income, which currently is {prop.box1.total * 0.05}")
        vacancy = int(input("What is the total for your vacancy expenses? $"))
    else: vacancy = 0

    #repairs
    cont = input("Would you like to set aside a repair savings? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Would you like to set aside a repair savings? (y/n) ").lower()
    if cont == 'y':
        repair = int(input("How much would you like to set aside for repairs? $"))
    else: repair = 0

    #Capex
    cont = input("Would you like to set aside a Capital Expenditure savings? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Would you like to set aside a Capital Expenditure savings? (y/n) ").lower()
    if cont == 'y':
        capex = int(input("How much would you like to set aside for Capital Expenditure savings? $"))
    else: capex = 0

    #Property management
    cont = input("Are you paying for a property management company? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Are you paying for a property management company? (y/n) ").lower()
    if cont == 'y':
        pm = int(input("How much are you paying for the Property Management Company? $"))
    else: pm = 0

    #Mortgage
    cont = input("Are you paying a mortgage on this property? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Are you paying a mortgage on this property? (y/n) ").lower()
    if cont == 'y':
        mortgage = int(input("How much is the mortgage payment for this property? $"))
    else: mortgage = 0

    print("Well done, lets add all this up.")
    prop.box2 = Box2(tax, ins, hoa, lawn, snow, vacancy, repair, capex, pm, mortgage)
    prop.box2.util = new_util
    prop.box2.util.get_total()
    prop.box2.get_total()

#Cash Flow
def cashflow(prop):
    print("Let's analyze the cash flow for box 3.")
    print('...')
    inc = prop.box1.total
    exp = prop.box2.total
    prop.box3 = Box3(inc, exp)
    prop.box3.get_total()

    print(f"Your cash flow (income - expenses) for {prop.name} is: ${prop.box3.total}")

#Cash on Cash ROI
def cashROI(prop):
    print("Time to determine the Cash on Cash ROI for this property.")
    dpayment = int(input("What was the down payment for the house? $"))
    ccosts   = int(input("What were the closing costs? $"))
    rehab    = int(input("What was the rehab budget? $"))
    misc     = int(input("Any other misc. costs? $"))

    prop.box4 = Box4(dpayment, ccosts, rehab, misc)
    prop.box4.get_total_investment()
    prop.box4.annual_cash_flow(prop.box3.total)
    prop.box4.roi()

    print(f"Your Cash on Cash Return on Investment for this property currently is {prop.box4.returnoninvest}%")

def displayInfo(prop):
    print(f"AThis is the total breakdown of {prop.name}.")

    dash = '-' * 30
    #Dislpay Box 1 - Income
    print(dash)
    print("{:^20}{:<20}".format('Box 1 - Income', '$$$$'))
    print(dash)
    print("{:<20} ${:<20}".format("Rental", prop.box1.rental))
    print("{:<20} ${:<20}".format("Laundry", prop.box1.laundry))
    print("{:<20} ${:<20}".format("Storage", prop.box1.storage))
    print("{:<20} ${:<20}".format("Miscellaneous", prop.box1.misc))
    print("{:<20} ${:<20}".format("Grand Total", prop.box1.total))
    print(dash)

    #Display Box 2 - Expenses
    print(dash)
    print("{:^20}{:<20}".format('Box 2 - Expenses', '$$$$'))
    print(dash)
    print("{:<20} ${:<20}".format("Tax", prop.box2.tax))
    print("{:<20} ${:<20}".format("Insurance", prop.box2.insurance))
    print("{:<20} ${:<20}".format("HOA", prop.box2.hoa))
    print("{:<20} ${:<20}".format("Lawn", prop.box2.lawn))
    print("{:<20} ${:<20}".format("Snow", prop.box2.snow))
    print("{:<20} ${:<20}".format("Vacancy", prop.box2.vacancy))
    print("{:<20} ${:<20}".format("Repairs", prop.box2.repairs))
    print("{:<20} ${:<20}".format("CapEx", prop.box2.capex))
    print("{:<20} ${:<20}".format("Property Management", prop.box2.propmanagement))
    print("{:<20} ${:<20}".format("Mortgage", prop.box2.mortgage))
    print("{:<20} ${:<20}".format("Utilities", prop.box2.util.total))
    print("{:<20} ${:<20}".format("Grand Total", prop.box2.total))
    print(dash)

    #Display Box 3 - Cash Flow
    print(dash)
    print("{:^20}{:<20}".format('Box 3 - Cash Flow', '$$$$'))
    print(dash)
    print("{:<20} {:<20}".format("Income", f"${prop.box3.income}"))
    print("{:<20} {:<20}".format("Expenses", f"${prop.box3.expenses}"))
    print("{:<20} {:<20}".format("Total", f"${prop.box3.total}"))

    #Display Box 4 - CoC ROI
    print(dash)
    print("{:^20}{:<20}".format('Box 4 - Cash ROI', '$$$$'))
    print(dash)
    print("{:<20} ${:<20,.2f}".format("Down Payment", prop.box4.downpayment))
    print("{:<20} ${:<20,.2f}".format("Closing Costs", prop.box4.closingcosts))
    print("{:<20} ${:<20,.2f}".format("Rehab Budget", prop.box4.rehabbudget))
    print("{:<20} ${:<20,.2f}".format("Miscellaneous", prop.box4.misc))
    print("{:<20} ${:<20,.2f}".format("Total Invested", prop.box4.totalinvest))
    print("{:<20} ${:<20,.2f}".format("Annual Cash", prop.box4.annualcash))
    print("{:<20} %{:<20,.2f}".format("ROI", prop.box4.returnoninvest))

def updateInfo(prop):
    print("What section would you like to update?")
    print("1. Box 1 - Income\n2. Box 2 - Expenses\n3. Box 3 - Cash Flow\n4. Box 4 - CoC ROI")
    update = int(input("Please enter either 1, 2, 3, or 4 "))
    while update not in {1, 2, 3, 4}:
        update = int(input("Please enter either 1, 2, 3, or 4 "))

    #User wants to update the Income Box
    if update == 1:
        print("What would you like to update?")
        print("1. Rental\n2. Laundry\n3. Storage\n4. Misc\n5. All")
        update = int(input("Please enter either 1, 2, 3, 4 or 5 "))
        while update not in {1, 2, 3, 4, 5}:
            update = int(input("Please enter either 1, 2, 3, 4 or 5 "))
        if update == 5:
            income(prop)
        elif update == 1:
            new_rental = int(input("Please enter the new rental: $"))
            prop.box1.rental = new_rental
        elif update == 2:
            new_laundry = int(input("Please enter the new laundry: $"))
            prop.box1.laundry = new_laundry
        elif update == 3:
            new_storage = int(input("Please enter the new storage: $"))
            prop.box1.storage = new_storage
        elif update == 4:
            new_misc = int(input("Please enter the new misc: $"))
            prop.box1.misc = new_misc

    #Box 2 - Expenses
    if update == 2:
        print("What would you like to update?")
        print("1. Tax\n2. Insurance\n3. HOA\n4. Lawn\n5. Snow\n6. Vacancy\n7. Repairs\n8. CapEx\n9. Property Management\n10. Mortgage\n11. Util\n12 All")
        update = int(input("Please enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12 "))
        while update not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
            update = int(input("Please enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12 "))
        if update == 12:
            expenses(prop)
        elif update == 1:
            new_tax = int(input("Please enter the new tax: $"))
            prop.box2.tax = new_tax
        elif update == 2:
            new_insurance = int(input("Please enter the new insurance: $"))
            prop.box2.insurance = new_insurance
        elif update == 3:
            new_hoa = int(input("Please enter the new hoa: $"))
            prop.box2.hoa = new_hoa
        elif update == 4:
            new_lawn = int(input("Please enter the new lawn: $"))
            prop.box2.lawn = new_lawn
        elif update == 5:
            new_snow = int(input("Please enter the new snow: $"))
            prop.box2.snow = new_snow
        elif update == 6:
            new_vacancy = int(input("Please enter the new vacancy: $"))
            prop.box2.vacancy = new_vacancy
        elif update == 7:
            new_repairs = int(input("Please enter the new repairs: $"))
            prop.box2.repairs = new_repairs
        elif update == 8:
            new_capex = int(input("Please enter the new capex: $"))
            prop.box2.capex = new_capex
        elif update == 9:
            new_propmanagement = int(input("Please enter the new propmanagement: $"))
            prop.box2.propmanagement = new_propmanagement
        elif update == 10:
            new_mortgage = int(input("Please enter the new mortgage: $"))
            prop.box2.mortgage = new_mortgage
        elif update == 11:
            new_electric = int(input("Please enter the new electric: $"))
            new_water = int(input("Please enter the new water: $"))
            new_sewer = int(input("Please enter the new sewer: $"))
            new_garbage = int(input("Please enter the new garbage: $"))
            new_gas = int(input("Please enter the new gas: $"))
            new_util = Utils(new_electric, new_water, new_sewer, new_garbage, new_gas)
            new_util.get_total()
            prop.box2.util = new_util
    #Box 3 - Cash Flow
    if update == 3:
        print("Box 3 will be updated automatically if you update either Box 1 or Box 2.")

    #Box 4 - CoC ROI
    if update == 4:
        print("What would you like to update?")
        print("1. Down Payment\n2. Closing Costs\n3. Rehab Budget\n4. Misc\n5. All")
        update = int(input("Please enter either 1, 2, 3, 4 or 5 "))
        while update not in {1, 2, 3, 4, 5}:
            update = int(input("Please enter either 1, 2, 3, 4 or 5 "))
        if update == 5:
            cashROI(prop)
        elif update == 1:
            new_downpayment = int(input("Please enter the new downpayment: $"))
            prop.box2.downpayment = new_downpayment
        elif update == 2:
            new_closingcosts = int(input("Please enter the new closing costs: $"))
            prop.box2.closingcosts = new_closingcosts
        elif update == 3:
            new_rehabbudget = int(input("Please enter the new rehab budget: $"))
            prop.box2.rehabbudget = new_rehabbudget
        elif update == 4:
            new_misc = int(input("Please enter the new misc: $"))
            prop.box2.misc = new_misc

    #Update everything
    prop.box1.get_total()
    prop.box2.get_total()
    prop.box3.income = prop.box1.total
    prop.box3.exp = prop.box2.total
    prop.box3.get_total()
    prop.box4.get_total_investment()
    prop.box4.annual_cash_flow(prop.box3.total)
    prop.box4.roi()

def mainCalc():
    print("Welcome to Bobs Blackjack er... Cash on Cash ROI Calculator!")
    
    cont = input("Would you like to add a new rental property to analyze? (y/n) ").lower()
    while cont not in {'y', 'n'}:
        cont = input("Would you like to add a new rental property to analyze? (y/n) ").lower()
        
    
    if cont == 'y':
        uinput = input("What is the name of your new rental property? ")
        new_prop = Rental_Prop(uinput)

        #Box 1 - Income
        income(new_prop)

        #Box2
        expenses(new_prop)

        #Box3
        cashflow(new_prop)

        #Box4
        cashROI(new_prop)

        #Display information neatly
        displayInfo(new_prop)

        #Ask if they want to update
        cont = input(f"Are you happy with the ROI of {new_prop.box4.returnoninvest}%? Or would you like to update some numbers? ('y', 'n') ").lower()
        while cont not in {'y', 'n'}:
            cont = input(f"Are you happy with the ROI of {new_prop.box4.returnoninvest}%? Or would you like to update some numbers? ('y', 'n') ").lower()

        while cont == 'y':
            updateInfo(new_prop)
            displayInfo(new_prop)
            cont = input("Are you happy with the new numbers? ('y', 'n') ")
            while cont not in {'y', 'n'}:
                cont = input("Are you happy with the new numbers? ('y', 'n') ")
            #happy with the new numbers
            if cont == 'y':
                break


    print("Thanks for coming to Bobs Cash Calc!")

mainCalc()