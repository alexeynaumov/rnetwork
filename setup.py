from distutils.core import setup

setup(name="rnetwork",
      version = "1.0.1",
      author = "Alexei Naumov",
      author_email = "alexei.naumov@yahoo.com",           
      description = "The rnetwork package makes network programming and debugging easy.",
      packages =  ["rnetwork", "dbg/tcp/tcpdebugger"],
      scripts = ["dbg/dbg"]
     )
