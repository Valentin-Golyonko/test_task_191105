from flag import flag


def test_jp_flag():
    """
    >>> print(flag('2'))
    ########
    #      #
    #  **  #
    #  **  #
    #      #
    ########
    <BLANKLINE>

    >>> print(flag('4'))
    ##############
    #            #
    #            #
    #     **     #
    #    *oo*    #
    #    *oo*    #
    #     **     #
    #            #
    #            #
    ##############
    <BLANKLINE>

    >>> print(flag('6'))
    ####################
    #                  #
    #                  #
    #                  #
    #        **        #
    #       *oo*       #
    #      *oooo*      #
    #      *oooo*      #
    #       *oo*       #
    #        **        #
    #                  #
    #                  #
    #                  #
    ####################
    <BLANKLINE>

    >>> print(flag('8'))
    ##########################
    #                        #
    #                        #
    #                        #
    #                        #
    #           **           #
    #          *oo*          #
    #         *oooo*         #
    #        *oooooo*        #
    #        *oooooo*        #
    #         *oooo*         #
    #          *oo*          #
    #           **           #
    #                        #
    #                        #
    #                        #
    #                        #
    ##########################
    <BLANKLINE>

    >>> print(flag('10'))
    ################################
    #                              #
    #                              #
    #                              #
    #                              #
    #                              #
    #              **              #
    #             *oo*             #
    #            *oooo*            #
    #           *oooooo*           #
    #          *oooooooo*          #
    #          *oooooooo*          #
    #           *oooooo*           #
    #            *oooo*            #
    #             *oo*             #
    #              **              #
    #                              #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    <BLANKLINE>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
