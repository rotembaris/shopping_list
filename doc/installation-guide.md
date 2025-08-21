# Installation and Configuration Guide

This Guide assumes you know nothing about VSCode, Git, Github, or Python. It will walk you through the steps to set up your development environment. It will be simple as possible while installing all you need to easily start.

In this guide, you will learn how to set up the following tools:
- Git
- GitHub
- Python
- Visual Studio Code (VSCode) - including installing the required and recommended extensions.

While trying to keep the instructions simple as possible, this guide adds some extra notes to expand your base knowledge. Those notes will be marked with `💡`. It is recommended to read them, but don't worry if you don't fully understand or remember them.

> 🤖 **Hackaton Note:** 
> During the Hackathon, the IT guy 🪛 will be available to help you with any issues you may encounter. Don't hesitate to ask for help if you get stuck or have questions about the installation process.

## Installing Git

Git is a version control system that allows you to track changes in your code and collaborate with others. It is a must-know tool for any developer.

>💡**Fun Fact:** Did you know Git was invented by Linus Torvalds, the creator of Linux, in just a few weeks during 2005? He built it because no existing version control system met the needs of the Linux kernel project!
 
First you need to download git from the [official Git website](https://git-scm.com/downloads). 

>❗Choose the version that matches your operating system (Windows, macOS, or Linux).

After downloading, run the installer and follow the instructions. Keep the default settings except for the following steps:
- **Select Components**: 
    - [Recommended] Uncheck `Windows Explorer integration`. 
        > 💡You just don't need it in your context menu.
    - Check `Add a Git Bash Profile to Windows Terminal`. 
        > 💡This will allow you to use Git Bash in Windows Terminal, which is a convenient feature.
- **Choose the default editor used by Git**: 
    - Select `Visual Studio Code` from the list.
        > 💡This will set VSCode as your default text editor for Git.
- **Adjusting the name of the initial branch in new repositories**: 
    - Select `Override the default branch name for new repositories`,  and keep the default value `main`.
        > 💡This is a modern convention, replacing the older `master` branch name.

✅ Congratulations! You have successfully installed Git. To verify the installation, open a terminal (or Git Bash) and run the following command:

```shell
git --version
``` 
If Git is installed correctly, you should see the version number displayed in the terminal. For example:

```shell
git version 2.51.0.windows.1
```

> 💡**Tip:** Git is a very powerful tool and can be overwhelming for beginners. But in fact, the basic concept and use of it is very simple and there are countless tutorials on the internet so you are not alone. To start fast and easy:
1. AI Chats are your friend. Use the Github Copilot integration on VSCode or any other AI chat to ask questions and get help.
2. Use the [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) to quickly find the commands you need.
3. Use [Learn Git Branching](https://learngitbranching.js.org/) to practice Git commands in a fun and interactive way.
4. Don't bother too much on using Git commands in the terminal. VSCode has very intuitive Git integration that allows you to perform most Git operations easily through the UI. It also has great extensions for viewing the commit tree.

> 😫 **Encouragement:** You installed Git! now there is really nothing you can't do!


## Register to GitHub

Github is a web-based platform that allows you to host and manage your Git repositories. It is widely used, especially in the Open Source community, for collaboration and sharing code with others.

First, you need to create a GitHub account. Go to the [GitHub website](https://github.com/) and click on the "Sign up" button. Follow the instructions to create your account.

When you are done, sign in to your new account. You will use it later.

✅ Congratulations! You have successfully created a GitHub account. 

> 🤖 **Hackathon Note:** Now it is the time to ask the Hackathon IT guy 🪛 to invite you to the Hackathon repository 🤗!


## Installing Python

Python is a programming language that is widely used for various applications. It is known for its simplicity and readability, making it a great choice for beginners.

> 💡**Fun Fact:** Python was created by Guido van Rossum and first released in 1991. It was named after the British comedy group Monty Python, not after the snake!

> 💡**Another Fun Fact 🤗:** Python is interpreted programming language, which means that the computer does not compile the whole code before running it, but rather executes it line by line.

First, you need to download Python from the [official Python website](https://www.python.org/downloads/).

> ❗Choose the version that matches your operating system (Windows, macOS, or Linux). It is recommended to use the latest stable version.

After downloading, run the installer and follow the instructions. Make sure to check the box that says `Add Python to PATH`/`Add Python to environment variables` before clicking "Install Now". 

> 💡**Note:** Adding Python to PATH will allow you to run Python from the command line without specifying the full path to the Python executable.

## Installing Visual Studio Code (VSCode)
Visual Studio Code (VSCode) is a powerful and popular code editor that supports many programming languages, including Python. It has a rich ecosystem of extensions that can enhance your development experience.

> 💡**Fun Fact:** VSCode was developed by Microsoft and first released in 2015. It has quickly become one of the most popular code editors in the world, thanks to its flexibility and extensibility. 

> 💡**We Love Fun Facts ❣️:** VSCode was the first IDE to support an AI-Chat integration, which allows you to get AI-powered code suggestions and assistance directly in the editor. Although it wasn't the first to introduce the agent mode, it still has one of the best generative AI integration.

> 💡**Term**: IDE stands for Integrated Development Environment, which is a software application that provides comprehensive facilities to programmers for software development. It typically includes a code editor, debugger, and build automation tools.

First, you need to download VSCode from the [official VSCode website](https://code.visualstudio.com/Download).

> ❗Choose the version that matches your operating system (Windows, macOS, or Linux) - But you already know that, right? 😉

After downloading, run the installer and follow the instructions. Keep the default settings except for the following steps:
- **Select Additional Tasks**: 
    - Check `Add "Open with Code" action to the Windows Explorer file context menu`.
    - Check `Add "Open with Code" action to the Windows Explorer directory context menu`.
    > 💡This will allow you to open files and folders in VSCode directly from the context menu in Windows Explorer.

After the installation is complete, Check the box that says `Launch Visual Studio Code` and click `Finish`.

✅ Congratulations! You have successfully installed Visual Studio Code. You are now ready to start coding! 🤗

