from flag_v3 import Flag3


def test_jp_flag():
    """
    >>> Flag3(2).print_flag()
    ########
    #      #
    #  **  #
    #  **  #
    #      #
    ########
    <BLANKLINE>

    >>> Flag3(4).print_flag()
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

    >>> Flag3(6).print_flag()
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

    >>> Flag3(8).print_flag()
    ##########################
    #                        #
    #                        #
    #                        #
    #                        #
    #          ****          #
    #         *oooo*         #
    #        *oooooo*        #
    #        *oooooo*        #
    #        *oooooo*        #
    #        *oooooo*        #
    #         *oooo*         #
    #          ****          #
    #                        #
    #                        #
    #                        #
    #                        #
    ##########################
    <BLANKLINE>

    >>> Flag3(10).print_flag()
    ################################
    #                              #
    #                              #
    #                              #
    #                              #
    #                              #
    #             ****             #
    #            *oooo*            #
    #           *oooooo*           #
    #          *oooooooo*          #
    #          *oooooooo*          #
    #          *oooooooo*          #
    #          *oooooooo*          #
    #           *oooooo*           #
    #            *oooo*            #
    #             ****             #
    #                              #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    <BLANKLINE>

    >>> Flag3(3).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3('w').print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3(None).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3('').print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3(-1).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3([]).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3([0]).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    >>> Flag3(2.0).print_flag()
    Traceback (most recent call last):
        ...
    argparse.ArgumentError: The input Number must be positive integer even number!

    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
