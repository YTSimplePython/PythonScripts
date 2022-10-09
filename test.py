#Docstring the following function:

def create_buttons(self):
        
        # Create a start button
        self.start_button = tk.Button(
            self.window, text='Start', command=self.run)
        # Create a stop button
        self.stop_button = tk.Button(
            self.window, text='Stop', command=self.window.destroy)
        # Create a reset button
        self.reset_button = tk.Button(
            self.window, text='Reset', command=self.reset)
        # Create a speed slider
        self.speed_slider = tk.Scale(self.window, from_=1, to=100, orient=tk.HORIZONTAL,
                                     label='Speed', command=self.change_speed)
        self.speed_slider.set(self.speed)

        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()
        self.speed_slider.pack()

# An elaborate, high quality docstring for the above function: in the followin format:
# """

#         <text>

#         Parameters
#         ----------
#         ....

#         Returns
#         -------
#         ....
# """

def
