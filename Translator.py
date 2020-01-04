{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from googletrans import Translator\n",
    "win=tk.Tk()\n",
    "win.title(\"Translator\")\n",
    "win.geometry(\"250x150\")\n",
    "def translation():\n",
    "    word=entry.get()\n",
    "    translator=Translator(service_urls=['translate.google.com'])\n",
    "    translation1=translator.translate(word,dest=\"gu\")\n",
    "    label1=tk.Label(win,text=\"translated to gujarati : %s \"%translation1.text,bg=\"yellow\")\n",
    "    label1.grid(row=2,column=0)\n",
    "label=tk.Label(win,text=\"Enter Word : \")\n",
    "label.grid(row=0,column=0,sticky=\"W\")\n",
    "entry=tk.Entry(win)\n",
    "entry.grid(row=1,column=0)\n",
    "button=tk.Button(win,text=\"Translate\",command=translation)\n",
    "button.grid(row=1,column=2)\n",
    "win.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
