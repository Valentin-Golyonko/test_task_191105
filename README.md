# Japanese flag

# v3 (latest)
OOP and simple circle formula with 3 'if' to determine circle borders (with outer circle radius correction coefficient).
- <code>python3 flag_v3.py</code>
- <code>python3 test_flag_v3.py -v</code>

# v2
Uses NumPy and <a href="https://stackoverflow.com/questions/39073973/how-to-generate-a-matrix-with-circle-of-ones-in-numpy-scipy/39074620">How to generate a matrix with circle of ones in numpy/scipy</a>
- <code>python3 flag_v2.py</code>
- <code>python3 test_flag_v2.py -v</code>

Version 2 is just for fun! <br>
- console line spacing must be < 0.8;
- violated the condition of height and width of the rectangle.

# v1
The fist idea was - it's a rhomb! Algorithm implements 4 border-circle lines.
- <code>python3 flag.py</code>
- <code>python3 test_flag.py -v</code>


<details><summary><b>Task (CLICK ME)</b></summary>
<p>
    
The purpose of the task is to implement a function that will accept a single input parameter N and output a string with an ASCII art of the japanese flag.

Here is an example of flags for various values of N:

    N = 2                           N = 6
    ########                        ####################
    #      #                        #                  #
    #  **  #                        #                  #
    #  **  #                        #                  #
    #      #                        #        **        #
    ########                        #       *oo*       #
                                    #      *oooo*      #
    N = 4                           #      *oooo*      #
    ##############                  #       *oo*       #
    #            #                  #        **        #
    #            #                  #                  #
    #     **     #                  #                  #
    #    *oo*    #                  #                  #
    #    *oo*    #                  ####################
    #     **     #
    #            #
    #            #
    ##############
    

    

The following is a list of requirements for the function:

- The input N shall be an integer even number
- The width of the inner area of the rectangle (excluding border) shall be 3 * N
- The height of the inner area of the rectangle (excluding border) shall be 2 * N
- The vertical distance between the circle and the border of the rectangle shall be N/2
- The horizontal distance between the circle and the border of the rectangle shall be N
- `#` symbol shall be used for rectangle border, `*` symbol shall be used for the circle border, `o` symbol shall be used for inner circle area
- The function shall return a string and use `\n` as line separators
- The function shall accept a single parameter N
- If the parameter is not a valid even integer number the `ArgumentError` exception shall be thrown
- The result of the task shall be provided a single python file named `flag.py` with a function named `flag` defined in it
</p>
</details>
