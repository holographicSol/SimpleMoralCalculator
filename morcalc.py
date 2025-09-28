# these are the actual factors that determine weather crime has really been committed

""" user defined """
# acting on deadly can permanently devastate someone's or some peoples lives but may not be a legal crime even if
# that crime does in fact devastate someone's or multiple peoples lives (permanently or not).
# this value is truly variable.
deadly_sin = False
# legal is a crime.
# this value is truly variable.
legal_crime = False

""" computer defined """
# crime commited is determined by weather or not someone acted out of deadly sin and or commited a legal crime.
# this value is set by the computer.
crime_committed = False

# these are factors that do not actually matter in determining weather or not a crime has been committed.

# basically meaningless and has no actual bearing on weather or not lives have been devastated by a deadly sin
# (permanently or not). This value does not need to change because it makes no difference to weather or not a crime has
# been committed.
clean_record = False

# speaks for itself weather a legal crime has been committed and or lives have been devastated by a deadly sin
# (permanently or not). This value does not need to change because it makes no difference to weather or not a crime has
# been committed.
getting_away_with_crime_or_crime_is_known_to_be_committed = False

# Clean record? Makes no difference. What crimes have you committed?
# this is always true.
if clean_record is True or clean_record is False:
    getting_away_with_crime_or_crime_is_known_to_be_committed = True

# What will it be? Legal crime? Deadly sin? Both?
if getting_away_with_crime_or_crime_is_known_to_be_committed:
    if deadly_sin is True or legal_crime is True:
        crime_committed = True

crime_severity = 0
max_crime_severity = 4

if legal_crime is True and deadly_sin is False:
    crime_severity = 1
    print('Legal Crime: ' + str(deadly_sin) + '. Is a legal crime but is not a deadly sin. Maybe someone commited a'
                                              ' deadly sin that effected you to commit a legal crime?'
                                              ' What is a legal crime anyway unless it it has any moral standing which'
                                              ' at the very least is to maintain order, you would be better to'
                                              ' understand this for the betterment of you own society.')

if deadly_sin is True and legal_crime is False:
    crime_severity = 2
    print('Deadly Sin: ' + str(deadly_sin) + '. Not a legal crime but is a deadly sin, perhaps at least you will get'
                                             ' away with your dirty deed no matter how many lives you have devastated as'
                                             ' a consequence of your deadly sin as far as the legal system is'
                                             ' concerned (perhaps there is a problem here with the legal system).'
                                             ' A deadly sin what can I say, how many people do you cause to suffer'
                                             ' while facing no legal recourse?')

if legal_crime is True and deadly_sin is True:
    crime_severity = 3
    print('Legal Crime & Deadly Sin: ' + str(deadly_sin) + '. Is a legal crime AND is deadly sin, there is no'
                                                           ' helping you, perhaps you should pray and apologize'
                                                           ' sincerely? Seeing as one or more deadly sins may be your'
                                                           ' motive.'
                                                           ' Well you broke the law and for reasons of deadly sin, but'
                                                           ' for some reason you were at least honest about it all.')

if crime_committed is False:
    crime_severity = 4
    print('Crime Committed: ' + str(crime_committed) + '. You appear to have not commited any legal crime nor any'
                                                       ' deadly sin. Perhaps you cannot be trusted here to tell the'
                                                       ' truth. What legal crime and or deadly sin are you hiding'
                                                       ' from us all and as of so far, are getting away with?'
                                                       ' The worst of the worst, guilty of all or one of the above and'
                                                       ' lied about it.')

print('Crime Severity: ' + str(crime_severity) + '/' + str(max_crime_severity) )
