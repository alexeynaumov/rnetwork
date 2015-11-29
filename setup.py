from distutils.core import setup

setup(name="rnetwork",
      version = "1.1.1",
      author = "Alexey Naumov",
      author_email = "rocketbuzzz@gmail.com",           
      description = "The rnetwork package makes network programming and debugging easy.",
      packages =  ["rnetwork", "dbg", "dbg/tcp", "dbg/tcp/client", "dbg/tcp/server", "dbg/tcp/tcpdebugger"],
      scripts = ["dbg/tcp/tdbg"]
     )
