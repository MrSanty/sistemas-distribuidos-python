import os


def comeBack( root ):
  root.destroy()
  # command to restart the app
  if os.getcwd().endswith('client'):
    os.system('python index.py')
  elif os.getcwd().endswith('client/helpers'):
    os.system('python ../index.py')
  else:
    os.system('python proyecto/client/index.py')