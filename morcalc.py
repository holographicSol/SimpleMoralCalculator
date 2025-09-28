# these are the actual factors that determine weather crime has really been committed

""" user defined """
# a crime that is deadly. this is categorically tha amoral crime.
deadly_sin = False
# a legal crime. the most moral crime of the two, depending on why you committed it, which of in combination with
# a deadly sin is of course certainly amoral+.
legal_crime = False
# input garbage...
garbage = False

x = input("Have you commited a legal crime? (y/n/garbage?): ")
if x.lower() == 'y':
    legal_crime = True
else:
    garbage = True

x = input("Have you commited a deadly sin? (y/n/garbage): ")
if x.lower() == 'y':
    deadly_sin = True
else:
    garbage = True

print()

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
                                              ' What is a legal crime anyway unless it has any moral standing, which'
                                              ' at the very least is to maintain order, you would be better to'
                                              ' understand this for the betterment of you own society, so that you may'
                                              ' be legitimate in your cause.')
    if garbage is True:
        print('However, you also entered garbage. Perhaps you have much to learn and you may be falling somewhat,'
              'depending on what you did and why.')

if deadly_sin is True and legal_crime is False:
    crime_severity = 2
    print('Deadly Sin: ' + str(deadly_sin) + '. Not a legal crime but is a deadly sin, perhaps at least you will get'
                                             ' away with your dirty deed no matter how many lives you have devastated as'
                                             ' a consequence of your deadly sin, as far as the legal system is'
                                             ' concerned (perhaps there is a problem here with the legal system).'
                                             ' A deadly sin what can I say, how many people do you cause to suffer'
                                             ' while facing no legal recourse whatsoever and how long will it last?')
    if garbage is True:
        print('Deadly sin and you entered input garbage? You are falling into a deadly trap of your own making.')

if legal_crime is True and deadly_sin is True:
    crime_severity = 3
    print('Legal Crime & Deadly Sin: ' + str(deadly_sin) + '. Is a legal crime AND is deadly sin, there is no'
                                                           ' helping you, perhaps you should pray and apologize'
                                                           ' sincerely? Seeing as one or more deadly sins may have been'
                                                           'the motives for your legal crimes.'
                                                           ' You broke the law and with a deadly sin as your motive'
                                                           ' , but for some reason you were at least honest about it all.'
                                                           ' Still, you better start praying soon, before its too late.')
    if garbage is True:
        print('Breaking the law and commiting deadly sin while also entering input garbage? All motives are known and'
              ' are deducible, fallen one.')

if crime_committed is False:
    crime_severity = 4
    print('Crime Committed: ' + str(crime_committed) + '. You appear to have not commited any legal crime nor any'
                                                       ' deadly sin. Perhaps you cannot be trusted here to tell the'
                                                       ' truth. What legal crime and or deadly sin are you hiding'
                                                       ' from us all and as of so far, are getting away with?'
                                                       ' The worst of the worst, guilty of all or one of all of the '
                                                       ' above and you lied about it.'
                                                       ' You are crime severity MAX. Are you trying to further hurt'
                                                       ' and or compromise people from your position of deceit?')
    if garbage is True:
        print('Input garbage with no ounce of truth. Do you still see your seat in the skies above?')

print()
print('Crime Severity: ' + str(crime_severity) + '/' + str(max_crime_severity) )
print()
input()
