from customtkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database
import config

class TimelineFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, fg_color="transparent")

        timeline_title_label = CTkLabel(master=self,
                                         text="Stock Bar Chart",
                                         font=("Roboto", 40, "bold"))
        timeline_title_label.place(x=26, y=88)

        self.figure = Figure(figsize=(0.8, 0.4), dpi=120, facecolor=config.background)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor(config.background)

        # Placeholder for empty graph
        self.ax.set_title("Stock Bar Chart")
        self.ax.set_xlabel("Product Names")
        self.ax.set_ylabel("Quantities")
        self.ax.bar([], [], color=config.secondary)

        self.ax.tick_params(axis='x', colors=config.text)
        self.ax.tick_params(axis='y', colors=config.text)
        self.ax.spines['top'].set_color(config.background)
        self.ax.spines['right'].set_color(config.background)
        self.ax.spines['left'].set_color(config.text)
        self.ax.spines['bottom'].set_color(config.text)

        # Embed Matplotlib Figure in Tkinter via Canvas
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.place(x=0, y=195, width=1100, height=580)

        # Load data for the bar graph
        self.refresh_bar_graph()

    def refresh_bar_graph(self):
        self.ax.clear()

        data = database.fetch_inventory_data()

        product_names = [row[1] for row in data]
        quantities = [row[3] for row in data]

        shortened_names = [name[:10] + "..." if len(name) > 10 else name for name in product_names]

        self.ax.bar(shortened_names, quantities, color=config.secondary)
        self.ax.set_title("Stock Bar Chart")
        self.ax.set_xlabel("Product Names")
        self.ax.set_ylabel("Quantities")

        self.ax.tick_params(axis='x', rotation=18)
        self.figure.subplots_adjust(left=0.08, right=0.98, top=0.92, bottom=0.15)

        # Redraw the canvas
        self.canvas.draw()