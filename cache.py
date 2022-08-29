from cmath import log
import math


class Cache:

    wordn  :int 
    setn   :int 
    waysn  :int 
    dimb   :int 
    offb   :int 
    indexb :int  
    tag    :int 

    
    blocks :list
    indexes :list
    tags :list


    def __init__(self, word_n, set_n, ways_n, addresses) -> None:

        self.wordn = word_n
        self.setn = set_n
        self.waysn = ways_n

        self.dimb = self.__dimension(self.wordn)
        self.offb = self.__offset_block(self.wordn)
        self.indexb = self.__index_bits(self.setn)
        self.tag = self.__tag()

        
        self.blocks(addresses)
        self.indexes()
        self.tags()
        pass

    def __dimension(self, word_n):
        return word_n * 4 
    
    def __offset_block(self, word_n):
        return int(math.log(self.__dimension(word_n), 2))
    
    def __index_bits(self, set):
        return int(math.log(set, 2))
    
    def __tag(self):
        return 32-self.offb-self.indexb

    def blocks(self, addresses: list):
        self.blocks = [address//self.dimb for address in addresses]
    
    def indexes(self):
        self.indexes = [block%self.setn for block in self.blocks ]

    def  tags(self):
        self.tags = [block//self.setn for block in self.blocks ]


    def retrieve_table(self, addrs, padding_space):

        print(
                f"  ".join(f"{el:>{padding_space}}" for el in addrs)+"\n\n"
                    +f"  ".join(f"{el:>{padding_space}}" for el in self.blocks)+"\n"
                    +f"  ".join(f"{el:>{padding_space}}" for el in self.indexes)+"\n"
                    +f"  ".join(f"{el:>{padding_space}}" for el in self.tags)
                    )
