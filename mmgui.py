import tkinter as tk
def mmenu():
    mpcs = False
    def strtgm():
        nonlocal mpcs
        mpcs = True
        mwindow.destroy()

    def quitgm():
        nonlocal mpcs
        mpcs = False
        mwindow.destroy()
        
    

    mwindow = tk.Tk()

    mwindow.title("Little Miss Witch -MMenu")
    mwindow.geometry("720x360")

    mheader = tk.Frame(mwindow, bg="black", height=69)
    mbody = tk.Frame(mwindow, bg="black")
    mfooter = tk.Frame(mwindow, bg="black", height=30)

    mheader.pack(fill="x")
    mheader.pack_propagate(False)

    mbody.pack(fill="both", expand=True)

    mfooter.pack(fill="x")
    mfooter.pack_propagate(False)

    tk.Label(
        mheader,
        text="""======================
Little Miss Witch
======================""",
        fg="green",
        bg="black",
        font=("Arial", 18)
    ).pack(expand=True)

    tk.Label(
        mfooter,
        text="Version 0.1",
        fg="white",
        bg="black",
    ).pack(side="left", padx=10)

    tk.Label(
        mfooter,
        text="DevPreview",
        fg="white",
        bg="black",
    ).pack(side="right", padx=10)

    tk.Button(mbody, text="Start Game", command=strtgm, bg="grey", fg="lightgrey").pack(pady=45)
    tk.Button(mbody, text="Quit Game", command=quitgm, bg="grey", fg="lightgrey").pack(pady=15)

    tk.mainloop()

    return mpcs

