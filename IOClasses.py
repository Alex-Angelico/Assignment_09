#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_list: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """
        # TODone modify method to accept a list of file names.
        file_name_CD, file_name_tracklists = file_list
        
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            # TODone add code to save track data to file
            with open(file_name_tracklists, 'w') as file:
                for disc in lst_Inventory:
                    if disc.cd_tracks == []:
                        pass
                    else:
                        disc_ref = str(disc.cd_id) + ','
                        file.write(disc_ref)
                        strTrackList = ''
                        for track in disc.cd_tracks:
                            try:
                                strTrack = track.get_track_record()[:-1] + ','
                                strTrackList += strTrack
                            except(AttributeError): # this error handling prevents empty track entries from being written to the file
                                pass
                        strTrackList = strTrackList[:-1] + '\n'
                        file.write(strTrackList)                
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_list: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """
        lst_Inventory = []
        # TODone modify method to accept a list of file names
        file_name_CD, file_name_tracklists = file_list
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    cd_data = line.strip().split(',')
                    row = DC.CD(cd_data[0], cd_data[1], cd_data[2])
                    lst_Inventory.append(row)
                    
            # TODone add code to load track data
            with open(file_name_tracklists, 'r') as file:
                for line in file:
                    tracklist_data = line.strip().split(',')
                    tracklist_data[0] = int(tracklist_data[0])
                    for row in lst_Inventory:
                        if tracklist_data[0] == row.cd_id:
                            track_data_group = []
                            track_data_count = 0
                            for track_data in tracklist_data[1:]:
                                track_data_count += 1
                                track_data_group.append(track_data)
                                if track_data_count == 3:
                                    track = DC.Track(track_data_group[0],track_data_group[1],track_data_group[2])
                                    row.add_track(track)
                                    track_data_group = []
                                    track_data_count = 0
                                else:
                                    pass
                        else:
                            pass
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """
        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """
        trknum = input('Enter Position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trknum, trkTitle, trkLength
        
