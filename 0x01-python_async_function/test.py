import asyncio
import time

async def brewcoffee():
     print('stwart Brewcoffee()')
     await asyncio.sleep(3)
     print('End brewcoffee')
     return "Coffee Ready"

async def toastBagel():
     print("start toastBagel()")
     await asyncio.sleep(2)
     print("End of toastBagel()")
     return "Bagel Toasted"

def main():
     start_time = time.time()

     result_coffee = brewcoffee()
     result_Bagel = toastBagel()

     end_time = time.time()
     elaspes = end_time - start_time

     print(f"Result of brewcoffee: {result_coffee}")
     print(f"Result of brewcoffee: {result_Bagel}")
     print(f"Total of brewcoffee: {elaspes}")

if __name__ == "__main__":
     main()
