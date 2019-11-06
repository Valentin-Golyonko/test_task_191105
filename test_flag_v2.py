from flag_v2 import inner_circle


def test_flag():
    """
    >>> inner_circle('2')
    ############
    #          #
    #          #
    #   ****   #
    #   *oo*   #
    #   *oo*   #
    #   ****   #
    #          #
    #          #
    ############


    >>> inner_circle('3')
    ################
    #              #
    #      **      #
    #    ******    #
    #    *oooo*    #
    #   **oooo**   #
    #   **oooo**   #
    #    *oooo*    #
    #    ******    #
    #      **      #
    #              #
    ################

    >>> inner_circle('4')
    ####################
    #                  #
    #                  #
    #        **        #
    #      ******      #
    #     **oooo**     #
    #     *oooooo*     #
    #    **oooooo**    #
    #    **oooooo**    #
    #     *oooooo*     #
    #     **oooo**     #
    #      ******      #
    #        **        #
    #                  #
    #                  #
    ####################


    >>> inner_circle('5')
    ########################
    #                      #
    #                      #
    #          **          #
    #        ******        #
    #       *oooooo*       #
    #      *oooooooo*      #
    #      *oooooooo*      #
    #     **oooooooo**     #
    #     **oooooooo**     #
    #      *oooooooo*      #
    #      *oooooooo*      #
    #       *oooooo*       #
    #        ******        #
    #          **          #
    #                      #
    #                      #
    ########################

    >>> inner_circle('6')
    ############################
    #                          #
    #                          #
    #                          #
    #            **            #
    #         ********         #
    #        **oooooo**        #
    #       **oooooooo**       #
    #       *oooooooooo*       #
    #       *oooooooooo*       #
    #      **oooooooooo**      #
    #      **oooooooooo**      #
    #       *oooooooooo*       #
    #       *oooooooooo*       #
    #       **oooooooo**       #
    #        **oooooo**        #
    #         ********         #
    #            **            #
    #                          #
    #                          #
    #                          #
    ############################

    >>> inner_circle('7')
    ################################
    #                              #
    #                              #
    #                              #
    #              **              #
    #           ********           #
    #          **oooooo**          #
    #         *oooooooooo*         #
    #        **oooooooooo**        #
    #        *oooooooooooo*        #
    #        *oooooooooooo*        #
    #       **oooooooooooo**       #
    #       **oooooooooooo**       #
    #        *oooooooooooo*        #
    #        *oooooooooooo*        #
    #        **oooooooooo**        #
    #         *oooooooooo*         #
    #          **oooooo**          #
    #           ********           #
    #              **              #
    #                              #
    #                              #
    #                              #
    ################################

    >>> inner_circle('8')
    ####################################
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    #                **                #
    #             ********             #
    #           **oooooooo**           #
    #          **oooooooooo**          #
    #          *oooooooooooo*          #
    #         *oooooooooooooo*         #
    #         *oooooooooooooo*         #
    #         *oooooooooooooo*         #
    #        **oooooooooooooo**        #
    #        **oooooooooooooo**        #
    #         *oooooooooooooo*         #
    #         *oooooooooooooo*         #
    #         *oooooooooooooo*         #
    #          *oooooooooooo*          #
    #          **oooooooooo**          #
    #           **oooooooo**           #
    #             ********             #
    #                **                #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################

    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
