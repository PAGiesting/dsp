# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


## Typing

It may sound silly, but make sure you know how to type.  Take this [typing test](http://www.typingtest.com/). You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

## Terminal Editor

You will need to use a terminal text editor at times.  You will **always need to use a terminal editor on the cloud** (e.g. Amazon Web Services).  This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

There are 3 widely used terminal editors.  Here's a [discussion comparing **nano**, **vim**, and **emacs**](http://askubuntu.com/questions/804/comparizon-between-text-editors-in-ubuntu-vim-vs-emacs-vs-nano).  
 * [nano](http://staffwww.fullcoll.edu/sedwards/Nano/IntroToNano.html) - this is the simplest to use 
 * [vim](http://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/) - is the default on many systems and you might find yourself in it even if you did not intend to
 * [emacs](http://ocean.stanford.edu/research/quick_emacs.html) - oldest editor, has steep learning curve, powerful, has lots of extensible options
 
Note:  Both Emacs and vim have built-in interactive tutorials that you can try.

You should know how to do the following tasks, *at the minimum*, on **nano** and **vim**:  
1.  open a file  
2.  edit a file  
3.  save a file  
4.  exit a file   

Here's a basic list of commands:  

|   |terminal editor | open a file    |  edit a file |  save a file       |  exit a file   |  
|---|----------------|----------------|--------------|--------------------|----------------|
| 1 | nano           | nano filen.py  | [just type]  | ctrl + o, enter    | ctrl + x       |
| 2 | vim, vi        | vim filen.py   | [just type]  | esc :w, enter      | esc :q, enter  |
| 3 | emacs          | emacs filen.py | [just type]  | ctrl-x, xtrl-s     | ctrl-x, ctrl-c |
 

---

## Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * [Emacs](http://ocean.stanford.edu/research/quick_emacs.html)
 * [vim](http://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/)
 * [Sublime Text 3](https://www.sublimetext.com/)
 * [Atom](https://atom.io/)
 * [Spyder](https://www.spyder-ide.org/)
 * [PyCharm](https://www.jetbrains.com/pycharm/)
 * [Rodeo](http://blog.yhat.com/posts/introducing-rodeo.html)

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter notebooks, but this does not remove the need for proficiency in an editor or IDE.

#### Comments for editors:
Pine was my first email client, so I am very familiar with nano.
I went through the vim tutorial, overcoming decades of terror.
I downloaded VSCode during my prework for the other bootcamp I was thinking of taking, and have also practiced a bit in Spyder.
I use Kate on Linux as my default editor.
