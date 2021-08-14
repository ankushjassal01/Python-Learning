# functions
def album_options():
    """
    :return: print options for user to choose from
    """
    return """CHOOSE OPTIONS:
            1. 1 TO ADD NEW ALBUM DETAILS 
            2. 2 TO CHANGE EXISTING ALBUM DETAILS (ALBUM/ARTIST/YEAR ONLY)
            3. 3 TO ADD/REMOVE/UPDATE SONGS IN DEFINED ALBUM
            4. 4 TO CHECK THE YOUR ALBUM DETAILS
            5. 5 TO REMOVE THE WHOLE ALBUM DETAILS
            6. 0 TO TERMINATE THE ALBUM PROGRAM """

def change_options():
    return """PLEASE CHOOSE VALUE TO CHANGE:'
                        1.ALBUM
                        2.ARTIST
                        3.YEAR
                        4. O TO QUIT CHANGES AND SEE MAIN CHOICES
                      """


def song_options():
    return """CHOOSE:
                            1.ADD SONG NAME
                            2.UPDATE SONG NAME
                            3.REMOVE SONG NAME
                            4.O TO QUIT CHANGES AND SEE MAIN CHOICES"""


def years(prompt: str) -> int:
    """
    Get the int year input from stdin

    func will continue looping until stdin have correct `int` year value
    if incorrect value then stdout will print message to terminal/console

    :param prompt: a text message for user stdout display user to add value in terminal
    :return: the `int` value of year
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric() and len(temp) == 4:
            return int(temp)
        else :  # we can remove else and write code like line 35
            print('-----that is not a year.. type again-----')
        # print('-----that is not a year.. type again-----') this is not indent at if block level so if if false then print work ..
        # if if works then return terminate the while loop
        # return will terminate the while loop so no need to write the break


# FOR DEBUGGING ONLY
# Album_list = [('KUSH', 'SNOOP', 2000, ['KUSH']), ('8 MILES', 'EMINEM', 2000, ['8 MILES']),('KAMIKAZI', 'EMINEM', 2017, ['RIVER'])]
Album_list = []
tup = () # TO ADD THE VALUES IN THE ALBUM AFTER FIRST CREATION
while True:
    if Album_list == []:
        print('CURRENTLY NO ALBUM ADDED IN ALBUM LIST DATABASE PLEASE ADD THE DATA IN ALBUM LIST: ')
        album_name = input('TYPE THE ALBUM NAME: ')
        Artist = input('TYPE THE ARTIST NAME: ')
        year = years('TYPE THE YEAR OF ALBUM: ')
        songs = input('TYPE THE SONG NAME: ')
        Album_list = [(album_name.upper(), Artist.upper(), year, [songs.upper()])]
        print('NEW ALBUM CREATED IN ALBUM LIST.PLEASE CHECK IT BELOW: ')
    elif Album_list != []:
        print('*************ALBUM LIST*************')
        print(Album_list)
        print(album_options())
        again = input()

        # TO TERMINATE THE ALBUM PROGRAM
        if again == '0':
            print('THANK YOU FOR YOUR INPUT :)')
            break

        # TO ADD NEW ALBUM DETAILS
        if again == '1':
            print('*************ADD NEW ALBUM*************')
            tup = list(tup)  # MAKE EMPTY TUPLE A LIST
            tup.clear()
            album_name1 = input('TYPE THE ALBUM NAME: ')  # USER INPUT
            tup.append(album_name1.upper())  # ADD THE ALBUM NAME IN TUP LIST
            Artist1 = input('TYPE THE ARTIST NAME: ')  # USER INPUT
            tup.append(Artist1.upper())  # ADD THE ARTIST NAME IN TUP LIST
            year1 = years('TYPE THE YEAR OF ALBUM: ')  # USER INPUT # year function used
            tup.append(year1)  # ADD YEAR(INT ONLY) IN TUP LIST
            songs1 = input('TYPE THE SONG OR SONGS NAME: ')  # USER INPUT
            tup.append([songs1.upper()])  # ADD THE LIST OF SONGS IN TUP LIST
            # CHANGED THE LIST TUP TO TUPLE TUP TO HAVE DATA INTEGRITY IN LIST OF TUPLES
            tup = tuple(tup)
            Album_list.append(tup)  # ADD THE TUP TUPLE IN THE ALBUM LIST
            print(Album_list)

        # TO CHANGE EXISTING ALBUM DETAILS (ALBUM/ARTIST/YEAR ONLY)
        if again == '2':
            if Album_list == []:
                print('CURRENTLY NO ALBUM ADDED IN ALBUM LIST DATABASE PLEASE SELECT FRIST OPTION TO ADD THE DATA IN ALBUM LIST')
                break
            else:
                print('*************CHANGE THE ALBUM DETAILS*************')
                choice2 = input('WRITE THE ALBUM/ARTIST NAME YOU WANT CHANGE: ')  # USER INPUT
                # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
                for index, album_details in enumerate(Album_list):
                    if choice2.upper() in album_details:
                        print('YOUR INPUT GIVE ALBUM DETAILS:{}'.format(Album_list[index]))
                        user_choices2 = None
                        while user_choices2 != '0':
                            print(change_options()) # function printed
                            user_choices2 = input()  # USER INPUT
                            # CHANGE TUPLE ALBUM TO LIST ALBUM - DATA TYPE CHANGE
                            Album_list[index] = list(Album_list[index])
                            if user_choices2 == '0':
                                print('PLEASE SELECT FROM BELOW CHOICES AGAIN')
                                break
                            # TO CHANGE ALBUM NAME
                            elif user_choices2 == '1':
                                album_name2 = input('TYPE THE ALBUM NAME: ')  # USER INPUT
                                Album_list[index][0] = album_name2.upper()
                                print("{} ALBUM REPLACED/UPDATED IN ALBUM/ARTIST'S ALBUM: {}".format(album_name2.upper(),Album_list[index]))

                            # TO CHANGE ARTIST NAME
                            elif user_choices2 == '2':
                                Artist2 = input('TYPE THE ARTIST NAME: ')  # USER INPUT
                                Album_list[index][1] = Artist2.upper()
                                print("{} ARTIST REPLACED/UPDATED IN ALBUM/ARTIST'S ALBUM: {}".format(Artist2.upper(),Album_list[index]))

                            # TO CHANGE YEAR VALUE
                            elif user_choices2 == '3':
                                year2 = years('TYPE THE YEAR OF ALBUM: ')  # USER INPUT  # year() used
                                Album_list[index][2] = year2
                                print("{} YEAR REPLACED/UPDATED IN ALBUM/ARTIST'S ALBUM: {}".format(year2,Album_list[index]))
                            elif user_choices2 not in ('0123'):
                                print("YOU HAVE GIVEN WRONG CHOICE. {} NOT EQUAL TO 0/1/2/3".format(user_choices2.upper()))

                            # CHANGED THE LIST TO TUPLE TO HAVE DATA INTEGRITY IN LIST OF TUPLES
                            Album_list[index] = tuple(Album_list[index])
                            print()
                            print('CHANGED ALBUM DETAILS ARE : {}'.format(Album_list[index]))
                            print()  # for space in output
                            print("""TO CHANGE AGAIN CHOOSE OPTIONS FROM BELOW OR ""PRESS 0 IF NOTHING TO DO""""")
                        break  # to come out of if condition and avoid going to condition else
                else:
                    print('{} IS NOT EXIST IN ALBUM LIST'.format(choice2.upper()))
                    print('PLEASE SELECT FROM BELOW CHOICES AGAIN:')
                    break

        # TO ADD/REMOVE/UPDATE SONGS IN DEFINED ALBUM
        if again == '3':
            if Album_list == []:
                print('CURRENTLY NO ALBUM ADDED IN ALBUM LIST DATABASE PLEASE SELECT FRIST OPTION TO ADD THE DATA IN ALBUM LIST')
                break
            else:
                print('*************ADD/UPDATE/REMOVE THE SONG IN ALBUM*************')
                choice3 = input("WRITE THE ALBUM/ARTIST'S NAME: ")  # USER INPUT
                # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
                for index, album_details in enumerate(Album_list):
                    # CHECK IF THE USER INPUT EXISTS IN ALBUM DETAILS
                    if choice3.upper() in album_details:
                        print("'{}' ALBUM/ARTIST'S ALBUM HAVE THESE DETAILS '{}'".format(choice3.upper(), album_details))
                        user_choices3 = None
                        while user_choices3 != '0':
                            print(song_options()) # function printed
                            user_choices3 = input()  # USER CHOICES

                            # TO ADD THE SONG IN THE SONG LIST OF ALBUM(TUPLE)
                            if user_choices3 == '1':
                                print('*************ADDING SONG*************')
                                # USER INPUT TO ADD THE SONG
                                add_song = input('PLEASE WRITE THE SONG YOU WANT TO ADD: ')
                                # CONDITION TO CHECK IF USER INPUT EXIST IN ALBUM OR NOT
                                if add_song.upper() not in album_details[3]:
                                    # IF ABOVE CONDITION TRUE THEN ADD THAT SONG IN SONG LIST(INDEXING OF TUPLE)
                                    album_details[3].append(add_song.upper())
                                    # INDEXING TO GET THE SONG ALBUM NAME
                                    print("'{}' IS SUCCESSFULLY ADDED IN '{}' ALBUM /ARTIST'S ALBUM".format(add_song.upper(),
                                                                                                            album_details[0]))
                                else:
                                    # IF USER INPUT EXISTS THEN PRINT MESSAGE  # INDEXING TO GET THE SONG ALBUM NAME
                                    print("'{}' SONG ALREADY EXISTS IN THE '{}' ALBUM /ARTIST'S ALBUM".format(add_song.upper(),
                                                                                                              album_details[0]))
                                print(album_details)
                                print('')
                            # TO UPDATE THE SONG IN SONG LIST IN ALBUM(TUPLE)
                            elif user_choices3 == '2':
                                print('*************Update SONG*************')
                                print("LIST OF SONGS IN ALBUM/ARTIST'S ALBUM:'{}' ".format(choice3.upper()))
                                # LIST OF SONGS
                                print(album_details[3])
                                # USER INPUT
                                replaced_song = input('PLEASE WRITE THE SONG YOU WANT TO REPLACE: ')
                                # CHECK IF USER INPUT IN SONGS LIST (INDEXING OF TUPLE)
                                if replaced_song.upper() in album_details[3]:
                                    # TO GET THE INDEX VALUES AND RESPECTIVE SONG IN ALBUM LIST(LIST UNPACKING)
                                    for song_index, song in enumerate(album_details[3]):
                                        # USER INPUT
                                        update_song = input('PLEASE PUT THE SONG NAME FOR REPLACED SONG: ')
                                        # ITEM ASSIGNMENT IN LIST
                                        album_details[3][song_index] = update_song.upper()
                                        # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                                        print("""'{}' IS REPLACED/UPDATED BY '{}' IN '{}' ALBUM/ARTIST'S ALBUM""".
                                              format(replaced_song.upper(), update_song.upper(), album_details[0]))
                                        break

                                else:
                                    # IF USER INPUT NOT EXISTS THEN PRINT MESSAGE #  # INDEXING TO GET THE SONG ALBUM NAME
                                    print(
                                        "'{}' SONG NOT EXISTS IN '{}' ALBUM/ARTIST'S ALBUM,PLEASE ADD IT OR CHECK SONG AGAIN".format(
                                            replaced_song.upper(), album_details[0]))
                                print(album_details)
                                print('')
                            # TO REMOVE THE SONG IN SONG LIST IN ALBUM(TUPLE)
                            elif user_choices3 == '3':
                                print('*************REMOVING SONG*************')
                                print("LIST OF SONGS IN '{}' ALBUM/ARTIST'S ALBUM".format(choice3.upper()))
                                # LIST OF SONGS FOR USER READABILITY
                                print(album_details[3])
                                # input from user
                                remove_song = input('please write the song you want to Remove: ')
                                # CONDITION TO CHECK IF SONG EXITS IN SONG LIST (INDEXING ON ALBUM)
                                if remove_song.upper() in album_details[3]:
                                    # USED REMOVED METHOD OS LIST TO REMOVE THE SONG FROM LIST
                                    album_details[3].remove(remove_song.upper())
                                    # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                                    print("'{}' SONG SUCCESSFULLY REMOVED FROM '{}' ALBUM/ARTIST'S ALBUM".format(
                                        remove_song.upper(), album_details[0]))
                                else:
                                    # INDEXING TO GET THE SONG ALBUM NAME IN BELOW PRINT
                                    print(
                                        """'{}' SONG NOT EXISTS IN '{}' ALBUM/ARTIST'S ALBUM, PLEASE ADD IT OR CHECK SONG AGAIN WHICH YOU WANT TO REMOVE'""".
                                            format(remove_song.upper(), album_details[0]))
                                print(album_details)
                                print('')
                            # to come out of while loop
                            elif user_choices3 == '0':
                                break
                            elif user_choices3 not in ('0123'):
                                print("YOU HAVE GIVEN WRONG CHOICE. {} NOT EQUAL TO 0/1/2/3".format(user_choices3.upper()))
                        print('')
                        break  # to come out of if condition and avoid going to condition else
                else:
                    print("'{}' ALBUM/ARTIST'S ALBUM IS NOT EXIST IN ALBUM LIST".format(choice3.upper()))
                    break
        # 4 TO CHECK THE YOUR ALBUM DETAILS
        if again == '4':
            if Album_list == []:
                print('CURRENTLY NO ALBUM ADDED IN ALBUM LIST DATABASE PLEASE SELECT FRIST OPTION TO ADD THE DATA IN ALBUM LIST')
                break
            else:
                print('*************ALBUM DETAILS*************')
                # USER INPUT
                choice4 = input("PLEASE WRITE THE ALBUM/ARTIST/SONG YOU WANT TO CHECK IF ONLY YEAR THEN TYPE 'YEAR' TEXT: ")
                choice4_int = None
                if choice4.upper() =='YEAR':
                    choice4_int = int(input('PLEASE WRITE THE YEAR FOR WHICH YOU WANT TO CHECK ALBUM RECORD: '))
                choice4_bool = False
                # TO GET THE INDEX VALUES AND TUPLES IN ALBUM LIST
                for index, album_details4 in enumerate(Album_list):
                    # CHECK IF USER INPUT EXISTS IN ALBUM TUPLES
                    if choice4.upper() in album_details4:
                        print("""{} ALBUM/ARTIST DETAILS IS : {}""".format(choice4, album_details4))
                        choice4_bool = True
                        print()
                    elif choice4_int in album_details4:
                        print("""{} YEAR HAVE THESE ALBUMS DETAILS: {}""".format(choice4_int, album_details4))
                        choice4_bool = True
                        print()
                else:
                    print()
                    if choice4_bool != True and choice4.upper() != 'YEAR':
                        print('{} ALBUM/ARTIST DONT EXIST IN ALBUM_LIST'.format(choice4.upper()))
                        print()
                    elif choice4_bool != True and choice4_int != None :
                        print('{} YEAR DONT HAVE ANY ALBUM IN ALBUM_LIST'.format(choice4_int))
                        print()
        # TO REMOVE THE WHOLE ALBUM DETAILS
        if again == '5':
            if Album_list == []:
                print('CURRENTLY NO ALBUM ADDED IN ALBUM LIST DATABASE PLEASE SELECT FRIST OPTION TO ADD THE DATA IN ALBUM LIST')
                break
            else:
                print('*************REMOVE WHOLE ALBUM DETAILS FROM ALBUM LIST*************')
                # USER INPUT
                choice5 = input("PLEASE WROTE THE ALBUM/ARTIST/SONG YOU WANT TO REMOVE OR ONLY YEAR THEN TYPE 'YEAR' TEXT: : ")
                print()
                choice5_int = None
                if choice5.upper() == 'YEAR':
                    choice5_int = int(input('PLEASE WRITE THE YEAR FOR WHICH YOU WANT TO REMOVE ALBUM RECORD: '))
                    print()
                choice5_bool = False
                for index in range(len(Album_list) - 1, -1, -1):
                    if choice5.upper() in Album_list[index]:
                        # removing the whole tuple from list
                        cache_add = Album_list.pop(index)
                        choice5_bool = True
                        print("REMOVING '{}'from '{}' ALBUM/ ARTIST's/SONG's ALBUM".format(cache_add, choice5.upper()))
                        print()
                        # confirmation for  user to remove or not
                        while True:
                            confirmation_check = input('ARE YOU SURE YOU WANT TO REMOVE IT, IF YES THEN TYPE - Y , IF NOT THEN N : ')
                            print()

                            if confirmation_check.upper() == 'N':
                                Album_list.insert(index, cache_add)
                                print('YOUR ALBUM LIST IS UNCHANGED AS YOU DONT WANT TO REMOVE THE ALBUM FROM ALBUM LIST')
                                print()
                                break
                            elif confirmation_check.upper() not in 'N Y':
                                print("YOU HAVE GIVEN WRONG CONFRIMATION '{}' IS NOT 'Y'/'N'".format(confirmation_check.upper()))
                            else:
                                print('YOUR CHOICE {} IS SUCCESSFULLY REMOVING {} FROM ALBUM LIST'.format(choice5.upper(),cache_add))
                                print()
                                break
                        print('YOUR REMAINING ALBUM LIST IS:')
                        print(Album_list)
                    # for integer removal like year
                    # condition is to check if loop item should check this if condition or not.if first if already worked then it wont work
                    # if choice5_bool != True # this is making below to run for only one time
                    #for index in range(len(Album_list) - 1, -1, -1):
                    else:
                        if choice5_int in Album_list[index]:
                            cache_add = Album_list.pop(index)
                            choice5_bool = True
                            print("REMOVING '{}' FROM YEAR :'{}'S ALUBMS".format(cache_add, choice5_int))
                            # confirmation for  user to remove or not
                            while True:
                                confirmation_check = input('ARE YOU SURE YOU WANT TO REMOVE IT, IF YES THEN TYPE - Y , IF NOT THEN N : ')
                                if confirmation_check.upper() == 'N':
                                    Album_list.insert(index, cache_add)
                                    print('YOUR ALBUM LIST IS UNCHANGED AS YOU DONT WANT TO REMOVE THE ALBUM FROM ALBUM LIST')
                                    print()
                                    break
                                elif confirmation_check.upper() not in 'N Y':
                                    print("YOU HAVE GIVEN WRONG CONFRIMATION '{}' IS NOT 'Y'/'N'".format(confirmation_check.upper()))
                                else:
                                    print("YOUR CHOICE OF YEAR:'{}' IS SUCCESSFULLY REMOVING '{}' FROM ALBUM LIST".format(choice5_int, cache_add))
                                    print('YOUR REMAINING ALBUM LIST IS:')
                                    print(Album_list)
                                    print()
                                    break
                            print('YOUR REMAINING ALBUM LIST IS:')
                            print(Album_list)
                else:
                    if choice5_bool != True and choice5.upper() != 'YEAR':
                        print("'{}' IS NOT IN ALBUM LIST PLEASE CHECK AGAIN".format(choice5.upper()))
                        print()
                    if choice5_bool != True and choice5_int != None:
                        print("'{}' YEAR DONT HAVE ANY ALBUM IN ALBUM_LIST".format(choice5_int))
                        print()
        if again not in '012345':
            print("YOU HAVE SELECTED WRONG OPTION.'{}' NOT LISTED IN BELOW LIST. PLEASE SELECT CORRECT OPTION:".format(again))