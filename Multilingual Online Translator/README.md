https://hyperskill.org/projects/99
# About
Everyone’s familiar with online translators. They giving us a handy way to translate on the go. In this project, you’re about to write an app that translates the words you type and gives you many usage examples based on the context.
# Learning outcomes
You will learn to work with loops and conditions, pip and packages. You’ll be talking to the web with requests and handle the data with BeautifulSoup libraries.
# 4/7 Description
Good! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will add the ability to translate from/to any language in the list.

The maximum number of languages our translator can support is 13. They are:
-ul
+ Arabic
+ German
+ English
+ Spanish
+ French
+ Hebrew
+ Japanese
+ Dutch
+ Polish
+ Portuguese
+ Romanian
+ Russian
+ Turkish


# 5/7 Description
You’ve done a great job! There is just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better.

This stage is meant to teach you how to work with files.

First, you’re going to add another cool feature to the project. Think how great it would be if you could translate to all the languages at once and save it for later!

Here's what you’ll do:
-ul
+ Add the ability to translate to all languages at once
+ Save results to the file on your computer
To make the first feature possible, there’s a way to expand the existing language list with zero, which will mean the translation to all languages listed below.

Since you will get a long output with all these translations coming one after another, it’s better to save it to the file on your computer so that you can read it later. You can name this file as the word in the input.
# 6/7 Description
There’s a faster way to translate a word without being asked by the program every time. To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.

At this stage, you should add command-line argument handling in your code. This is possible via Python sys package.

You'll see some significant changes in the usability of the app!

 # 7/7 Description
 
 Okay, it seems like your program translates as expected. However, there’s a problem you should always keep in mind: something can break your program.

Up to this stage, you were thinking about things that should be in your code. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? That can break your program.

All these situations are called exceptions because you didn’t expect them to happen, and now you have to handle them.
