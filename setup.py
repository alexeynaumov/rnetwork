from distutils.core import setup

setup(name="rnetwork",
      version = "1.1.1",
      author = "Alexey Naumov",
      author_email = "rocketbuzzz@gmail.com",           
      description = "",
      packages =  ["rnetwork", "ndbg", "ndbg/tcp", "ndbg/tcp/client", "ndbg/tcp/server", "ndbg/udp"],
      package_data = {
          'ndbg/tcp/client': [
              'icons/*',
          ],
          'ndbg/tcp/server': [
              'icons/*',
          ],
      },
      scripts = ["ndbg/tcp/tdbgc", "ndbg/tcp/tdbgs"]
     )
