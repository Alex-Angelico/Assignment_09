#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODone add code as required
        cdcount = 0
        searchcount = 0
        for cd in table:
            cdcount += 1
            if cd_idx == cd.cd_id:
                searchcount += 1
                return cd
            elif (cdcount == len(table)) and searchcount == 0:
                raise Exception('CD / Album index not in inventory.')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd

        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the track gets added to

        Raises:
            Exception: raised in case position is not an integer

        Returns:
            None: DESCRIPTION

        """

        # TODone add code as required
        track_number, track_title, track_length = track_info
        try:
            track_number = int(track_number)
        except:
            raise Exception('Track number must be an Integer!')
        newTrack = DC.Track(track_number, track_title, track_length)
        cd.add_track(newTrack)
        
    @staticmethod
    def rmv_track(track_number: int, cd: DC.CD) -> None:
        """removes a track with track_number from cd
        
        Args:
            track_number (int): Integer corresponding to Track.t_number to be deleted from cd.cd_tracks
            cd (DC.CD): cd object the track gets removed from
            
        Raises:
            Exception: raised in case position is not an integer
            
        Returns:
            None
        
        """
        try:
            track_number = int(track_number)
        except:
            raise Exception('Track number must be an Integer!')
        cd.rmv_track(track_number)