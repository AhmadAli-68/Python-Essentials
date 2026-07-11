def main():
  try:
    a = int(input('Enter a number: '))
    print(a)
    return

  except Exception as e:
    print(e)
    return

  finally:
    print('I am inside finally.')

main()

#? Ab finally... agr error araha hai, tb bhi execute hoga.... agr error nai araha tb bhi execute hoga. But WHY??

#* Why?... because finally is used in functions... jb function execute hoga... to finally chale ga hi chale ga.... agr hum finally use nai krty... to yeh 'I am inside finally' print nai hoga.