#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Provides functions to convert between several different calendars
that are of interest to me and to report the current date in each calendar."""

__author__ = "Strahinja Ciric"

from math import *
import datetime

greg_monthnames = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
lc_monthnames = {0: "UGAS Day", 1: "Unifex", 2: "Bifex", 3: "Trifex", 4: "Quadrifex", 5: "Quintafex", 6: "Hexafex", 7: "Septafex", 8: "Octafex", 9: "Nonafex", 10: "Decafex", 11: "Solafex", 12: "Lunafex", 13: "Foryfex"}
defier_monthnames = {1: u"Ūnus", 2: "Duo", 3: u"Trēs", 4: "Quattuor", 5: u"Quīnque", 6: "Sext", 7: "Interval", 8: "Septem", 9: u"Octō", 10: "Novem", 11: "Decem", 12: u"Ūndecim", 13: u"Duodēcim", 14: u"Leapday"}
defier_monthabbrev = {1: "U", 2: "DU", 3: "T", 4: "Q", 5: "QQ", 6: "S", 7: "I", 8: "SM", 9: "O", 10: "N", 11: "D", 12: "UD", 13: "DD", 14: "L"}
defier_monthnum = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "I", 8: "7", 9: "8", 10: "9", 11: "10", 12: "11", 13: "12", 14: "L"}
fixed_monthnames = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "Sol", 8: "July", 9: "August", 10: "September", 11: "October", 12: "November", 13: "December"}
positivist_monthnames = {1: "Moses", 2: "Homer", 3: "Aristotle", 4: "Archimedes", 5: "Caesar", 6: "Saint Paul", 7: "Charlemagne", 8: "Dante", 9: "Gutenberg", 10: "Shakespeare", 11: "Descartes", 12: "Frederick", 13: "Bichat"}
slav_monthnames = {1: u"Berzĭnĭ", 2: u"Květĭnĭ", 3: u"Travĭnĭ", 4: u"Čĭrvĭnĭ", 5: u"Lipĭnĭ", 6: u"Sĭrpĭnĭ", 7: u"Versĭnĭ", 8: u"Rjuıĭnĭ", 9: u"Listopadŭ", 10: u"Grudĭnĭ", 11: u"Prosinĭcĭ", 12: u"Sěčĭnĭ", 13: u"Ljutĭnĭ"}
fr_monthnames = {1: u"Vendémiaire", 2: u"Brumaire", 3: u"Frimaire", 4: u"Nivôse", 5: u"Pluviôse", 6: u"Ventôse", 7: u"Germinal", 8: u"Floréal", 9: u"Prairial", 10: u"Messidor", 11: u"Thermidor", 12: u"Fructidor"}

greg_daynames = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
fixed_daynames = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Year Day"}
slav_daynames = {0: u"Nedělja", 1: u"Ponedělŭkŭ", 2: u"Vŭtorŭkŭ", 3: u"Serda", 4: u"Četvĭrtŭkŭ", 5: u"Pętŭkŭ", 6: u"Sǫbota"}
fr_daynames = {1: "Primidi", 2: "Duodi", 3: "Tridi", 4: "Quartidi", 5: "Quintidi", 6: "Sextidi", 7: "Septidi", 8: "Octidi", 9: "Nonidi", 10: u"Décadi"}

def leapyear(year):
    """Determine whether a year of the Gregorian calendar is a leap year.

    Parameters
    ----------
    year : int
        A year in the Gregorian calendar.

    Returns
    -------
    bool
        True if and only if the year is a leap year.
    """
    leap = True
    if (not(year % 4 == 0)):
        leap = False
    elif (not(year % 100 == 0)):
        leap = True
    elif (not(year % 400 == 0)):
        leap = False
    return leap

def greg_dayinyear(date):
    """Find, for any given date in the Gregorian calendar, which day in the year it is out of 365.

    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    int
        The day in the year (out of 365) that the date represents.
    """
    greg_monthlengths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    i = 1
    total = 0
    while i < date[1]:
        total = total + greg_monthlengths[i]
        i += 1
    total = total + date[0]
    DAYS_BEFORE_LEAPDAY = 59
    if ((leapyear(date[2])) and (total > DAYS_BEFORE_LEAPDAY) and (date[1] != 2)):
        total += 1
    return total

def greg_weekday(date):
    """Find, for any given date in the Gregorian calendar, which day of the week it is.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    int
        The number of the day of the week, starting with Sunday as 0.
    """
    month = date[1]
    year = date[2]
    DAYS_IN_WEEK = 7
    MONTHS_IN_YEAR = 12
    if (month < 3):
        month += MONTHS_IN_YEAR
        year -= 1
    day = date[0] + 2*month + (3*(month + 1) / 5) + year + (year / 4) - (year / 100) + (year / 400) + 1
    day = (day % DAYS_IN_WEEK)
    return day

def greg_to_positivist(date):
    """Convert a date in the Gregorian calendar to a date in the Positivist calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the Positivist calendar.
    """
    POSITIVIST_YEAR_ZERO = 1788
    positivist_date = [0,0,date[2] - POSITIVIST_YEAR_ZERO]
    if positivist_date[2] < (-POSITIVIST_YEAR_ZERO + 1): #if the date is BC
        positivist_date[2] += 1
    dayinyear = greg_dayinyear(date)
    DAYS_IN_POSITIVIST_MONTH = 28
    MONTHS_IN_POSITIVIST_YEAR = 13
    positivist_date[0] = dayinyear % DAYS_IN_POSITIVIST_MONTH
    positivist_date[1] = (dayinyear - 1) / DAYS_IN_POSITIVIST_MONTH + 1
    if positivist_date[0] == 0:
        positivist_date[0] = DAYS_IN_POSITIVIST_MONTH
    if positivist_date[1] == (MONTHS_IN_POSITIVIST_YEAR + 1):
        positivist_date[1] = MONTHS_IN_POSITIVIST_YEAR
        positivist_date[0] += DAYS_IN_POSITIVIST_MONTH
    return positivist_date

def positivist_weekday(positivist_date):
    """Find, for any given date in the Positivist calendar, which day of the week it is.
    
    Parameters
    ----------
    positivist_date : [int, int, int]
        A list of day (of the month), month, and year in the Positivist calendar.

    Returns
    -------
    int
        The number of the day of the week, starting with Sunday as 0.
    """
    date = positivist_date[0]
    DAYS_IN_POSITIVIST_MONTH = 28
    DAYS_IN_WEEK = 7
    day = (date % DAYS_IN_WEEK)
    if date > DAYS_IN_POSITIVIST_MONTH:
        day = 7 #Year Day
    return day

def greg_to_fixed(date):
    """Convert a date in the Gregorian calendar to a date in the International Fixed calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the International Fixed calendar.
    """
    fixed_date = [0,0,date[2]]
    dayinyear = greg_dayinyear(date)
    fixed_date[0] = dayinyear % 28
    fixed_date[1] = (dayinyear - 1) / 28 + 1
    if fixed_date[0] == 0:
        fixed_date[0] = 28
    if leapyear(date[2]) and fixed_date[1] > 6:
        fixed_date[0] -= 1
        if fixed_date[0] == 0:
            fixed_date[1] -= 1
            if fixed_date[1] == 6:
                fixed_date[0] = 29
            else:
                fixed_date[0] = 28
    if fixed_date[1] == 14:
        fixed_date[1] = 13
        fixed_date[0] = 29
    return fixed_date

def fixed_weekday(fixed_date):
    date = fixed_date[0]
    day = ((date - 1) % 7)
    if date > 28:
        day = 7
    return day

def greg_to_slav(date):
    slav_date = [0,0,0]
    slav_date[0] = date[0] #Definitely wrong; months seem to have started with the new moon.
    slav_date[1] = (date[1] - 2) % 12
    if (slav_date[1] == 0):
        slav_date[1] = 12
    slav_date[2] = date[2] + 5508 #Approx. the Byzantine Anno Mundi; the actual Slavic calendar was probably lunar, not solar
    if (slav_date[1] > 10):
        slav_date[2] -= 1
    if (slav_date[2] < 5508):
        slav_date[2] += 1
    return slav_date

def days_since_1Jan2000(date): #i.e. 1 Jan is 0, 2 Jan is 1, ...
    years_since = date[2] - 2000
    if years_since < -2000:
        years_since += 1
    if (years_since > 0):
        leapdays_since = years_since / 4 - years_since / 100 + years_since / 400 #This intentionally excludes the leapday in 2000.
        if (leapyear(date[2])):
            leapdays_since -= 1
        days_since = (years_since * 365) + leapdays_since + greg_dayinyear(date)
    elif (years_since == 0):
        days_since = greg_dayinyear(date) - 1
    else:
        years_since = -(years_since)
        leapdays_since = years_since / 4 - years_since / 100 + years_since / 400
        if (leapyear(date[2])):
            leapdays_since -= 1
        dayfromend = 365 - greg_dayinyear(date)
        if (leapyear(date[2])):
            dayfromend += 1
        days_since = -((years_since - 1) * 365) - leapdays_since - dayfromend - 1
    return days_since

def ageindays(date):
    return 2396 + days_since_1Jan2000(date)

def foryfex(year):
    if (year % 125 == 0):
        return True
    return False

def greg_to_ugas(date):
    ugas_date = [0,0,0]
    days_since_25Jan1776 = days_since_1Jan2000(date) + 81790
    foryfexen = (days_since_25Jan1776 - 1) / 45655
    dayincycle = (days_since_25Jan1776 % 45655)
    if (dayincycle == 0):
        dayincycle = 45655
    ugas_date[2] = (dayincycle - 1) / 365 + 1
    if (ugas_date[2] == 126):
        ugas_date[2] = 125
    ugas_date[2] += ((foryfexen - 1) * 125)
    if foryfex(ugas_date[2]):
        dayinyear = dayincycle - 45260
        ugas_date[1] = (dayinyear - 1) / 30 + 1
        ugas_date[0] = dayinyear - (30 * (ugas_date[1] - 1))
        ugas_date[1] = ugas_date[1] % 14
    else:
        dayinyear = (dayincycle % 365)
        if (dayinyear == 0):
            dayinyear = 365
        ugas_date[1] = (dayinyear - 1) / 30 + 1
        ugas_date[0] = dayinyear - (30 * (ugas_date[1] - 1))
        ugas_date[1] = ugas_date[1] % 13
    return ugas_date

##greg_monthlengths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
##greg_leapmonthlengths = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
##i = 2000
##while i < 2016:
##    j = 1
##    while j <= 12:
##        k = 1
##        if leapyear(i):
##            while k <= greg_leapmonthlengths[j]:
##                ugas_date = greg_to_ugas([k,j,i])
##                print "The Ugas I calendar date is {} {} {}.".format(ugas_date[0], lc_monthnames[ugas_date[1]], ugas_date[2])
##                k += 1
##        else:
##            while k <= greg_monthlengths[j]:
##                ugas_date = greg_to_ugas([k,j,i])
##                print "The Ugas I calendar date is {} {} {}.".format(ugas_date[0], lc_monthnames[ugas_date[1]], ugas_date[2])
##                k += 1
##        j += 1
##    i += 1

def lc_foryfex(year):
    if (year % 30 == 0):
        return True
    return False

def greg_to_lc(date):
    lc_date = [0,0,0]
    days_since_30Jan1971 = days_since_1Jan2000(date) + 10563
    foryfexen = (days_since_30Jan1971 - 1) / 10980
    dayincycle = (days_since_30Jan1971 % 10980)
    if (dayincycle == 0):
        dayincycle = 10980
    lc_date[2] = (dayincycle - 1) / 365 + 1
    if (lc_date[2] == 31):
        lc_date[2] = 30
    lc_date[2] += (foryfexen * 30)
    if lc_foryfex(lc_date[2]):
        dayinyear = dayincycle - 10585
        lc_date[1] = (dayinyear - 1) / 30 + 1
        lc_date[0] = dayinyear - (30 * (lc_date[1] - 1))
        lc_date[1] = lc_date[1] % 14
    else:
        dayinyear = (dayincycle % 365)
        if (dayinyear == 0):
            dayinyear = 365
        lc_date[1] = (dayinyear - 1) / 30 + 1
        lc_date[0] = dayinyear - (30 * (lc_date[1] - 1))
        lc_date[1] = lc_date[1] % 13
    return lc_date

def greg_to_defier(date):
    defier_date = [0,0,date[2] + 3100]
    if defier_date[2] < 3101:
        defier_date[2] += 1
    if ((date[1] < 3) or ((date[1] == 3) and (date[0] < 21))):
        defier_date[2] -= 1
    dayinyear = greg_dayinyear(date)
    if leapyear(date[2]):
        if (dayinyear < 81):
            dayinyear += 366
        dayinyear -= 80
    else:
        if (dayinyear < 80):
            dayinyear += 365
        dayinyear -= 79
    if (dayinyear < 186):
        defier_date[1] = (dayinyear - 1) / 30 + 1
        defier_date[0] = (dayinyear % 30)
    else:
        defier_date[1] = (dayinyear - 186) / 30 + 8
        defier_date[0] = ((dayinyear - 185) % 30)
    if defier_date[0] == 0:
        defier_date[0] = 30
    return defier_date

def greg_to_zavar(date):
    zavar_date = [0,0,date[2] + 9750] #9600 in the original »Newly “Revised Calendar”«, but always considered subject to revision
    if zavar_date[2] < 9751: #9601 originally
        zavar_date[2] += 1
    if ((date[1] < 3) or ((date[1] == 3) and (date[0] < 21))):
        zavar_date[2] -= 1    
    dayinyear = greg_dayinyear(date)
    if leapyear(date[2]):
        if (dayinyear < 81):
            dayinyear += 366
        dayinyear -= 81
    else:
        if (dayinyear < 80):
            dayinyear += 365
        dayinyear -= 80
    zavar_date[0] = dayinyear
    return zavar_date

def report(a="other"): #Input should be proleptic Gregorian
    if (a == "now"):
        now = datetime.datetime.now()
        year = int("%d" % now.year)
        month = int("%d" % now.month)
        date = int("%d" % now.day)
    elif (isinstance(a, list)):
        year = a[2]
        month = a[1]
        date = a[0]
    else:
        year = input("Input year (negative for BC): ")
        month = input("Input number of month: ")
        date = input("Input date: ")
    
    date = [date, month, year]

    print "You have lived for {} days.".format(ageindays(date))
    
    greg_day = greg_weekday(date)
    print "The Gregorian calendar date is {}, {} {} {}.".format(greg_daynames[greg_day], date[0], greg_monthnames[date[1]], date[2])
    print u"     (Early conventions {}-{}-’{}, {} {} ’{}.)".format(
        date[1], date[0], str(date[2]%100).zfill(2), greg_monthnames[date[1]], date[0], str(date[2]%100).zfill(2))

    positivist_date = greg_to_positivist(date)
    positivist_day = positivist_weekday(positivist_date)
    print u"The Positivist calendar date is {}, {} {} {}.".format(fixed_daynames[positivist_day], positivist_date[0], positivist_monthnames[positivist_date[1]], positivist_date[2])

    fixed_date = greg_to_fixed(date)
    fixed_day = fixed_weekday(fixed_date)
    print u"The International Fixed calendar date is {}, {} {} {}.".format(fixed_daynames[fixed_day], fixed_date[0], fixed_monthnames[fixed_date[1]], fixed_date[2])

    slav_date = greg_to_slav(date)
    print u"The Slavic calendar date is {}, {} {} {}.".format(slav_daynames[greg_day], slav_date[0], slav_monthnames[slav_date[1]], slav_date[2])
    
    ugas_date = greg_to_ugas(date)
    print "The Ugas I calendar date is {} {} {}.".format(ugas_date[0], lc_monthnames[ugas_date[1]], ugas_date[2])

    lc_date = greg_to_lc(date)
    if lc_date[1] > 0:
        print "The Light Council calendar date is {} {} {}.".format(lc_date[0], lc_monthnames[lc_date[1]], lc_date[2])
    else:
        intercalarydays = {1: "Air", 2: "Fire", 3: "Water", 4: "Earth", 5: "Light"}
        print "The Light Council calendar date is {} {}.".format(intercalarydays[lc_date[0]], lc_date[2])
    
    defier_date = greg_to_defier(date) #Officially called the »Revised Calendar« or »Logical Solar Calendar«
    print u"The Historical Era calendar date is {} {} {}.".format(defier_date[0], defier_monthnames[defier_date[1]], defier_date[2])
    print u"     (Wretched convention {}{}’{}, Defieristic convention ’{}|{}|{}.)".format(
        defier_monthabbrev[defier_date[1]], defier_date[0], str(defier_date[2]%100).zfill(2), str(defier_date[2]%100).zfill(2), defier_monthnum[defier_date[1]], defier_date[0])

    zavar_date = greg_to_zavar(date)
    print u"The (Zavaric) Holocene Era calendar date is Day {}, {}±50.".format(zavar_date[0], zavar_date[2])

report("now")
