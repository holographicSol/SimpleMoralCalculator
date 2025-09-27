# these are the actual factors that determine weather crime has really been committed

""" user defined """
# acting on deadly can permanently devastate someone's or some peoples lives but may not be a legal crime even if
# that crime does in fact devastate someone's or multiple peoples lives (permanently or not).
# this value is truly variable.
deadly_sin = True
# legal is a crime.
# this value is truly variable.
legal_crime = True

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
getting_away_with_something = False

# test: deadly sin true/false and legal_crime true false. if either are true then crime has been committed.
if clean_record is True or clean_record is False:
    getting_away_with_something = True

if getting_away_with_something:
    if deadly_sin is True or legal_crime is True:
        crime_committed = True

if deadly_sin is True and legal_crime is False:
    print('Deadly Sin: ' + str(deadly_sin) + '. Not a legal crime but is a deadly sin, perhaps at least you will get'
                                             ' away with your dirty deed no matter how many lives you have devastated as'
                                             ' a consequence of your deadly sin as far as the legal system is'
                                             ' concerned.')

if legal_crime is True and deadly_sin is False:
    print('Legal Crime: ' + str(deadly_sin) + '. Is a legal crime but is not a deadly sin. Maybe someone commited a'
                                              ' deadly sin that effected you to commit a legal crime?')

if legal_crime is True and deadly_sin is True:
    print('Legal Crime & Deadly Sin: ' + str(deadly_sin) + '. Is a legal crime AND is deadly sin, there is no'
                                                           ' helping you, perhaps you should pray and apologize'
                                                           ' sincerely? Seeing as one or more deadly sins may be your'
                                                           ' motive.')

if crime_committed is False:
    print('Crime Committed: ' + str(crime_committed) + '. You appear to have not commited any legal crime nor any'
                                                       ' deadly sin. Perhaps you cannot be trusted here to tell the'
                                                       ' truth.')
