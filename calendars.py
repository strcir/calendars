#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Provides functions to convert between several different calendars
that I have used at some point or other and to report the current date in each calendar."""

__author__ = "Strahinja Ciric"

from math import *
import datetime

greg_monthnames = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
lc_monthnames = {0: "UGAS Day", 1: "Unifex", 2: "Bifex", 3: "Trifex", 4: "Quadrifex", 5: "Quintafex", 6: "Hexafex", 7: "Septafex", 8: "Octafex", 9: "Nonafex", 10: "Decafex", 11: "Solafex", 12: "Lunafex", 13: "Foryfex"}
he_monthnames = {1: u"Ūnus", 2: "Duo", 3: u"Trēs", 4: "Quattuor", 5: u"Quīnque", 6: "Sext", 7: "Interval", 8: "Septem", 9: u"Octō", 10: "Novem", 11: "Decem", 12: u"Ūndecim", 13: u"Duodēcim", 14: u"Leapday"}
he_monthabbrev = {1: "U", 2: "DU", 3: "T", 4: "Q", 5: "QQ", 6: "S", 7: "I", 8: "SM", 9: "O", 10: "N", 11: "D", 12: "UD", 13: "DD", 14: "L"}
he_monthnum = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "I", 8: "7", 9: "8", 10: "9", 11: "10", 12: "11", 13: "12", 14: "L"}
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
    DAYS_IN_FIXED_MONTH = 28
    MONTHS_IN_FIXED_YEAR = 13
    fixed_date[0] = dayinyear % DAYS_IN_FIXED_MONTH
    fixed_date[1] = (dayinyear - 1) / DAYS_IN_FIXED_MONTH + 1
    if fixed_date[0] == 0:
        fixed_date[0] = DAYS_IN_FIXED_MONTH
    MONTH_OF_FIXED_LEAPDAY = 6
    if leapyear(date[2]) and fixed_date[1] > MONTH_OF_FIXED_LEAPDAY:
        fixed_date[0] -= 1
        if fixed_date[0] == 0:
            fixed_date[1] -= 1
            if fixed_date[1] == MONTH_OF_FIXED_LEAPDAY:
                fixed_date[0] = DAYS_IN_FIXED_MONTH + 1
            else:
                fixed_date[0] = DAYS_IN_FIXED_MONTH
    if fixed_date[1] == (MONTHS_IN_FIXED_YEAR + 1):
        fixed_date[1] = MONTHS_IN_FIXED_YEAR
        fixed_date[0] = DAYS_IN_FIXED_MONTH + 1
    return fixed_date

def fixed_weekday(fixed_date):
    """Find, for any given date in the International Fixed calendar, which day of the week it is.
    
    Parameters
    ----------
    fixed_date : [int, int, int]
        A list of day (of the month), month, and year in the International Fixed calendar.

    Returns
    -------
    int
        The number of the day of the week, starting with Sunday as 0.
    """
    date = fixed_date[0]
    DAYS_IN_FIXED_MONTH = 28
    DAYS_IN_WEEK = 7
    day = ((date - 1) % DAYS_IN_WEEK)
    if date > DAYS_IN_FIXED_MONTH:
        day = 7 #Year Day
    return day

def greg_to_slav(date):
    """Convert a date in the Gregorian calendar to a date in the early medieval Slavic calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the early medieval Slavic calendar.
    """
    slav_date = [0,0,0]
    slav_date[0] = date[0] #Historically inaccurate; months seem to have started with the new moon.
    MONTHS_IN_YEAR = 12
    MONTHS_BETWEEN_GREG_AND_SLAV_NEW_YEAR = 2
    slav_date[1] = (date[1] - MONTHS_BETWEEN_GREG_AND_SLAV_NEW_YEAR) % MONTHS_IN_YEAR
    if (slav_date[1] == 0):
        slav_date[1] = MONTHS_IN_YEAR
    SLAVIC_YEAR_ZERO = -5508 #Approx. the Byzantine Anno Mundi; the original Slavic calendar was probably lunar, not solar
    slav_date[2] = date[2] - SLAVIC_YEAR_ZERO
    if (slav_date[1] > (MONTHS_IN_YEAR - MONTHS_BETWEEN_GREG_AND_SLAV_NEW_YEAR)):
        slav_date[2] -= 1
    if (slav_date[2] > SLAVIC_YEAR_ZERO):
        slav_date[2] += 1
    return slav_date

def days_since_1Jan2000(date):
    """Find, for any given date in the Gregorian calendar, how many days it is since 1 January 2000.

    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    int
        The number of days since 1 January 2000: 1 Jan is 0, 2 Jan is 1, ..., and days before are negative.
    """
    years_since = date[2] - 2000
    if years_since < -2000:
        years_since += 1
    DAYS_IN_YEAR = 365
    if (years_since > 0):
        leapdays_since = years_since / 4 - years_since / 100 + years_since / 400 #This intentionally excludes the leapday in 2000.
        if (leapyear(date[2])):
            leapdays_since -= 1
        days_since = (years_since * DAYS_IN_YEAR) + leapdays_since + greg_dayinyear(date)
    elif (years_since == 0):
        days_since = greg_dayinyear(date) - 1
    else:
        years_since = -(years_since)
        leapdays_since = years_since / 4 - years_since / 100 + years_since / 400
        if (leapyear(date[2])):
            leapdays_since -= 1
        dayfromend = DAYS_IN_YEAR - greg_dayinyear(date)
        if (leapyear(date[2])):
            dayfromend += 1
        days_since = -((years_since - 1) * DAYS_IN_YEAR) - leapdays_since - dayfromend - 1
    return days_since

def ageindays(date):
    """Find, for any given date in the Gregorian calendar, how many days old I was on that date.

    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    int
        My age in days on that date.
    """
    DAYS_LIVED_BEFORE_2000 = 2396
    return DAYS_LIVED_BEFORE_2000 + days_since_1Jan2000(date)

def foryfex(year):
    """Determine whether a year of the Ugas I calendar is a Foryfex year.

    Parameters
    ----------
    year : int
        A year in the Ugas I calendar.

    Returns
    -------
    bool
        True if and only if the year is a Foryfex year.
    """
    INTERVAL_BETWEEN_FORYFEX_YEARS = 125
    if (year % INTERVAL_BETWEEN_FORYFEX_YEARS == 0):
        return True
    return False

def greg_to_ugas(date):
    """Convert a date in the Gregorian calendar to a date in the fictional Ugas I calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the fictional Ugas I calendar.
    """
    ugas_date = [0,0,0]
    days_since_25Jan1776 = days_since_1Jan2000(date) + 81790
    LENGTH_OF_FORYFEX_CYCLE = 45655
    INTERVAL_BETWEEN_FORYFEX_YEARS = 125
    DAYS_IN_YEAR = 365
    DAYS_IN_UGAS_MONTH = 30
    MONTHS_IN_UGAS_YEAR = 13
    foryfexen = (days_since_25Jan1776 - 1) / LENGTH_OF_FORYFEX_CYCLE
    dayincycle = (days_since_25Jan1776 % LENGTH_OF_FORYFEX_CYCLE)
    if (dayincycle == 0):
        dayincycle = LENGTH_OF_FORYFEX_CYCLE
    ugas_date[2] = (dayincycle - 1) / DAYS_IN_YEAR + 1
    if (ugas_date[2] == (INTERVAL_BETWEEN_FORYFEX_YEARS + 1)):
        ugas_date[2] = INTERVAL_BETWEEN_FORYFEX_YEARS
    ugas_date[2] += ((foryfexen - 1) * INTERVAL_BETWEEN_FORYFEX_YEARS)
    if foryfex(ugas_date[2]):
        dayinyear = dayincycle - LENGTH_OF_FORYFEX_CYCLE + DAYS_IN_YEAR + DAYS_IN_UGAS_MONTH
        ugas_date[1] = (dayinyear - 1) / DAYS_IN_UGAS_MONTH + 1
        ugas_date[0] = dayinyear - (DAYS_IN_UGAS_MONTH * (ugas_date[1] - 1))
        ugas_date[1] = ugas_date[1] % (MONTHS_IN_UGAS_YEAR + 1)
    else:
        dayinyear = (dayincycle % DAYS_IN_YEAR)
        if (dayinyear == 0):
            dayinyear = DAYS_IN_YEAR
        ugas_date[1] = (dayinyear - 1) / DAYS_IN_UGAS_MONTH + 1
        ugas_date[0] = dayinyear - (DAYS_IN_UGAS_MONTH * (ugas_date[1] - 1))
        ugas_date[1] = ugas_date[1] % MONTHS_IN_UGAS_YEAR
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
    """Determine whether a year of the Light Council calendar is a Foryfex year.

    Parameters
    ----------
    year : int
        A year in the Light Council calendar.

    Returns
    -------
    bool
        True if and only if the year is a Foryfex year.
    """
    INTERVAL_BETWEEN_FORYFEX_YEARS = 30
    if (year % INTERVAL_BETWEEN_FORYFEX_YEARS == 0):
        return True
    return False

def greg_to_lc(date):
    """Convert a date in the Gregorian calendar to a date in the fictional Light Council calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the fictional Light Council calendar.
    """
    lc_date = [0,0,0]
    days_since_30Jan1971 = days_since_1Jan2000(date) + 10563
    LENGTH_OF_FORYFEX_CYCLE = 10980
    INTERVAL_BETWEEN_FORYFEX_YEARS = 30
    DAYS_IN_YEAR = 365
    DAYS_IN_LC_MONTH = 30
    MONTHS_IN_LC_YEAR = 13
    foryfexen = (days_since_30Jan1971 - 1) / LENGTH_OF_FORYFEX_CYCLE
    dayincycle = (days_since_30Jan1971 % LENGTH_OF_FORYFEX_CYCLE)
    if (dayincycle == 0):
        dayincycle = LENGTH_OF_FORYFEX_CYCLE
    lc_date[2] = (dayincycle - 1) / DAYS_IN_YEAR + 1
    if (lc_date[2] == (INTERVAL_BETWEEN_FORYFEX_YEARS + 1)):
        lc_date[2] = INTERVAL_BETWEEN_FORYFEX_YEARS
    lc_date[2] += (foryfexen * INTERVAL_BETWEEN_FORYFEX_YEARS)
    if lc_foryfex(lc_date[2]):
        dayinyear = dayincycle - LENGTH_OF_FORYFEX_CYCLE + DAYS_IN_YEAR + DAYS_IN_LC_MONTH
        lc_date[1] = (dayinyear - 1) / DAYS_IN_LC_MONTH + 1
        lc_date[0] = dayinyear - (DAYS_IN_LC_MONTH * (lc_date[1] - 1))
        lc_date[1] = lc_date[1] % (MONTHS_IN_LC_YEAR + 1)
    else:
        dayinyear = (dayincycle % DAYS_IN_YEAR)
        if (dayinyear == 0):
            dayinyear = DAYS_IN_YEAR
        lc_date[1] = (dayinyear - 1) / DAYS_IN_LC_MONTH + 1
        lc_date[0] = dayinyear - (DAYS_IN_LC_MONTH * (lc_date[1] - 1))
        lc_date[1] = lc_date[1] % MONTHS_IN_LC_YEAR
    return lc_date

def greg_to_he(date):
    """Convert a date in the Gregorian calendar to a date in the Historical Era calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the Historical Era calendar.
    """
    HE_YEAR_ZERO = -3100
    he_date = [0,0,date[2] - HE_YEAR_ZERO]
    if he_date[2] < (-HE_YEAR_ZERO + 1): #if the date is BC
        he_date[2] += 1
    MONTHS_BETWEEN_GREG_AND_HE_NEW_YEAR = 3
    DATE_OF_HE_NEW_YEAR = 21
    if ((date[1] < MONTHS_BETWEEN_GREG_AND_HE_NEW_YEAR) or ((date[1] == MONTHS_BETWEEN_GREG_AND_HE_NEW_YEAR) and (date[0] < DATE_OF_HE_NEW_YEAR))):
        he_date[2] -= 1
    dayinyear = greg_dayinyear(date)
    DAYS_BETWEEN_GREG_AND_HE_NEW_YEAR = 80
    DAYS_IN_YEAR = 365
    if leapyear(date[2]):
        if (dayinyear < (DAYS_BETWEEN_GREG_AND_HE_NEW_YEAR + 1)):
            dayinyear += (DAYS_IN_YEAR + 1)
        dayinyear -= DAYS_BETWEEN_GREG_AND_HE_NEW_YEAR
    else:
        if (dayinyear < DAYS_BETWEEN_GREG_AND_HE_NEW_YEAR):
            dayinyear += DAYS_IN_YEAR
        dayinyear -= (DAYS_BETWEEN_GREG_AND_HE_NEW_YEAR - 1)
    DAYS_IN_HE_MONTH = 30
    if (dayinyear < 186):
        he_date[1] = (dayinyear - 1) / DAYS_IN_HE_MONTH + 1
        he_date[0] = (dayinyear % DAYS_IN_HE_MONTH)
    else:
        he_date[1] = (dayinyear - 186) / DAYS_IN_HE_MONTH + 8
        he_date[0] = ((dayinyear - 185) % DAYS_IN_HE_MONTH)
    if he_date[0] == 0:
        he_date[0] = DAYS_IN_HE_MONTH
    return he_date

def greg_to_zavar(date):
    """Convert a date in the Gregorian calendar to a date in the (Zavaric) Holocene Era calendar.
    
    Parameters
    ----------
    date : [int, int, int]
        A list of day (of the month), month, and year in the Gregorian calendar.

    Returns
    -------
    [int, int, int]
        A list of day (of the month), month, and year in the (Zavaric) Holocene Era Era calendar.
    """
    ZAVAR_YEAR_ZERO = -9750 #-9600 in the original »Newly “Revised Calendar”«, but always considered subject to revision
    zavar_date = [0,0,date[2] - ZAVAR_YEAR_ZERO]
    if zavar_date[2] < (-ZAVAR_YEAR_ZERO + 1): #if the date is BC
        zavar_date[2] += 1
    MONTHS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR = 3
    DATE_OF_ZAVAR_NEW_YEAR = 21
    if ((date[1] < MONTHS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR) or ((date[1] == MONTHS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR) and (date[0] < DATE_OF_ZAVAR_NEW_YEAR))):
        zavar_date[2] -= 1
    dayinyear = greg_dayinyear(date)
    DAYS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR = 80
    DAYS_IN_YEAR = 365
    if leapyear(date[2]):
        if (dayinyear < (DAYS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR + 1)):
            dayinyear += (DAYS_IN_YEAR + 1)
        dayinyear -= (DAYS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR + 1)
    else:
        if (dayinyear < DAYS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR):
            dayinyear += DAYS_IN_YEAR
        dayinyear -= DAYS_BETWEEN_GREG_AND_ZAVAR_NEW_YEAR
    zavar_date[0] = dayinyear
    return zavar_date

def report(a="other"):
    """Takes a date in the proleptic Gregorian calendar and prints its equivalent in various other systems.
    
    Parameters
    ----------
    a : [int, int, int] or str, optional
        Either a list of day (of the month), month, and year in the Gregorian calendar, or the string "now" to use the current date.
        If this parameter is not supplied, the program will request input.
    """
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
    
    he_date = greg_to_he(date) #Officially called the »Revised Calendar« or »Logical Solar Calendar«
    print u"The Historical Era calendar date is {} {} {}.".format(he_date[0], he_monthnames[he_date[1]], he_date[2])
    print u"     (Fell Year convention {}{}’{}, Defieristic convention ’{}|{}|{}.)".format(
        he_monthabbrev[he_date[1]], he_date[0], str(he_date[2]%100).zfill(2), str(he_date[2]%100).zfill(2), he_monthnum[he_date[1]], he_date[0])

    zavar_date = greg_to_zavar(date)
    print u"The (Zavaric) Holocene Era calendar date is Day {}, {}±50.".format(zavar_date[0], zavar_date[2])

report("now")
