def get_from_list(glist: [], step: float, remain: float):
    """ use the enumerate function to return individual items in each subtitle """
    return [ i for idx, i in enumerate(glist) if idx%step==remain ]

@dataclass(slots=False)
class sub:
    """ The subtitle object takes in a source file's path, 's_path', and returns the subtitle index, timestamp, and content1,2,3, etc """
    s_path: str       # this is the path of the subtitle file
    step: int         # this is the number of rows to jump from index n to index n+1
    
    def s_list(cls):
        """ store the raw string in the form of a list """
        return Path(cls.s_path).read_text(encoding='utf-8').split('\n')
    
    def s_idx(cls):
        """ return the list of subtitle index """
        return get_from_list(cls.s_list(), cls.step, 0)
    def s_time(cls):
        """ return the list of subtitle index """
        return get_from_list(cls.s_list(), cls.step, 1)
    