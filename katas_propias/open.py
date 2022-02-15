def main():
  print("hola mundo")
  try:
     open('config.txt')
  except FileNotFoundError:
    print("Couldn't find the config.txt file!")



if __name__ == '__main__':
    main()