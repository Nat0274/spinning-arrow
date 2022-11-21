def on_forever():
    def on_screen_up():
       
        basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
        """)
        basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        """)
        basic.show_leds("""
                . . # . .
                . . # # .
                # # # # #
                . . # # .
                . . # . .
                """)
        basic.show_leds("""
                . . # . .
                . . # . .
                # # # # #
                . # # # .
                . . # . .
                """)
        basic.show_leds("""
                . . # . .
                . # # . .
                # # # # #
                . # # . .
                . . # . .
                """)
        basic.show_leds("""
                        . . # . .
                        . # # # .
                        # # # # #
                        . . # . .
                        . . # . .
                        """)
        basic.show_leds("""
                        . . # . .
                        . . # # .
                        # # # # #
                        . . # # .
                        . . # . .
                        """)
        basic.show_leds("""
                        . . # . .
                        . . # . .
                        # # # # #
                        . # # # .
                        . . # . .
                        """)
        basic.show_leds("""
                        . . # . .
                        . # # . .
                        # # # # #
                        . # # . .
                        . . # . .
                        """)        
    input.on_screen_up(on_screen_up) 
forever(on_forever)
