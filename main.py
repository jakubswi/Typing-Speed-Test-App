from tkinter import *
import time
from random import choice


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("1200x200")
        self.test_started = False
        self.text_list = [
            "The quick brown fox jumps over the lazy dog. A quick movement of the enemy will jeopardize six gunboats. Pack my box with five dozen liquor jugs. Jackdaws love my big sphinx of quartz.",
            "The five boxing wizards jump quickly. How razorback-jumping frogs can level six piqued gymnasts! The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog.",
            "Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sphinx of black quartz, judge my vow. The five boxing wizards jump quickly. Jack quietly moved up front and seized the big ball of wax.",
            "The quick brown fox jumps over the lazy dog. Bright vixens jump; dozy fowl quack. A wizard’s job is to vex chumps quickly in fog. Watch Jeopardy!, Alex Trebek’s fun TV quiz game.",
            "Pack my box with five dozen liquor jugs. Amazingly few discotheques provide jukeboxes. The quick brown fox jumps over the lazy dog. Why shouldn't a quixotic Kazakh vampire jog barefoot?"
        ]
        self.test_text = choice(self.text_list)
        self.setup_gui()

    def setup_gui(self):
        self.text_label = Label(self.root, text="Type this sentence:")
        self.text_label.pack()

        self.test_sentence_label = Label(self.root, text=self.test_text)
        self.test_sentence_label.pack()

        self.start_button = Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack()

        self.entry_label = Label(self.root, text="Type here:")
        self.entry_label.pack()

        self.entry = Entry(self.root, width=200)
        self.entry.pack(padx=10, pady=10)
        self.entry.pack()

        self.timer_label = Label(self.root, text="Time: 0 s")
        self.timer_label.pack()

        self.result_label = Label(self.root, text="")
        self.result_label.pack()

    def start_test(self):
        if not self.test_started:
            self.start_button.config(state=DISABLED)
            self.test_started = True
            self.start_time = time.time()
            self.root.after(1000, self.update_timer)
            self.entry.bind("<KeyRelease>", self.check_input)

    def update_timer(self):
        if self.test_started:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text="Time: {:.1f} s".format(elapsed_time))
            self.root.after(100, self.update_timer)

    def check_input(self, event):
        if self.entry.get() == self.test_text:
            elapsed_time = time.time() - self.start_time
            self.result_label.config(
                text="Test completed in {:.1f} seconds. Your typing speed is {:.2f} characters per second.".format(
                    elapsed_time, len(self.test_text) / elapsed_time))
            self.entry.unbind("<KeyRelease>")
            self.test_text = choice(self.text_list)
            self.test_sentence_label.configure(text=self.test_text)
            self.entry.delete(0, END)
            self.test_started = False
            self.start_button.config(state=NORMAL)


if __name__ == "__main__":
    root = Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
