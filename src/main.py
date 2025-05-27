from GUI.gui import GUI

# Main function that puts everything together and runs the program
def main():
    gui = GUI()
    gui.menu_handler()

    while True:
        # enforce a minimum window size
        if gui.winfo_width() < 676:
            gui.geometry(f"676x{gui.winfo_height()}")
        if gui.winfo_height() < 676:
            gui.geometry(f"{gui.winfo_width()}x676")

        gui.canvas.delete("all")  # clear canvas

        gui.draw_path() # draw solved path

        # draw start/end points
        gui.maze.draw_square(gui.canvas, *gui.start_point, "#2025FF")
        gui.maze.draw_square(gui.canvas, *gui.end_point,   "#992528")

        gui.maze.draw_walls(gui.canvas) # draw maze walls

        gui.update()
        gui.update_idletasks()

if __name__ == "__main__":
    main()
