#CSci 127 Teaching Staff
#November 16th, 2024
#A template for a program that computes LIRR transit fares.
#Modified by:  Jayden Shofolahan

def computeFare(zone, ticketType):
  fare = 0
     

  if zone == 1 and ticketType == "peak" or zone == 4 and ticketType == "off-peak":
    fare = fare + 8.75
  elif zone == 1 and ticketType == "off-peak":
    fare = fare + 6.25 
  elif (zone == 2 or zone == 3) and ticketType == "peak":
    fare = fare + 10.25 
  elif (zone == 2 or zone == 3) and ticketType == "off-peak":
    fare = fare + 7.50 
  elif zone == 4 and ticketType == "peak":
    fare = fare + 12.00 
  elif zone == 5 and ticketType == "peak":
    fare = fare + 13.50 
  elif zone == 6 and ticketType == "peak":
    fare = fare + 13.50 
  elif zone == 7 and ticketType == "peak":
    fare = fare + 13.50 
  elif zone == 5 and ticketType == "off-peak":
    fare = fare + 9.75 
  elif zone == 6 and ticketType == "off-peak":
    fare = fare + 9.75
  elif zone == 7 and ticketType == "off-peak":
    fare = fare + 9.75 
  else:
    fare = fare - 1 
  


  return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
